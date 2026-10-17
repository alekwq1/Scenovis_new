/* SCENOVIS — interaktywny model 3D (Three.js r170, pliki lokalne, bez CDN).
   Ładowany dopiero po kliknięciu „Uruchom model 3D” (import() z site.js).
   Model: /assets/3d/scenovis-mikroskop.glb (eksport z Blendera, projekt demonstracyjny).
   Widok rozłożony: przesunięcia części z /assets/3d/scenovis-mikroskop.json (policzone w Blenderze). */
import * as THREE from './vendor/three-0.170.0/three.module.min.js';
import { GLTFLoader } from './vendor/three-0.170.0/GLTFLoader.js';
import { OrbitControls } from './vendor/three-0.170.0/OrbitControls.js';
import { RoomEnvironment } from './vendor/three-0.170.0/RoomEnvironment.js';

const MODEL = '/assets/3d/scenovis-mikroskop.glb';
const META = '/assets/3d/scenovis-mikroskop.json';

export async function start(host, T, onProgress) {
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const canvas = document.createElement('canvas');
  canvas.className = 'viewer-canvas';
  canvas.setAttribute('aria-label', T.canvas_label);
  canvas.tabIndex = 0;
  host.appendChild(canvas);

  const renderer = new THREE.WebGLRenderer({ canvas, antialias: true, alpha: true, powerPreference: 'high-performance' });
  renderer.setPixelRatio(Math.min(devicePixelRatio || 1, 2));
  renderer.outputColorSpace = THREE.SRGBColorSpace;
  renderer.toneMapping = THREE.AgXToneMapping;
  renderer.toneMappingExposure = 1.05;
  renderer.shadowMap.enabled = true;
  renderer.shadowMap.type = THREE.PCFSoftShadowMap;

  const scene = new THREE.Scene();
  const pmrem = new THREE.PMREMGenerator(renderer);
  scene.environment = pmrem.fromScene(new RoomEnvironment(), 0.04).texture;
  scene.environmentIntensity = 0.75;

  const key = new THREE.DirectionalLight(0xfff3e6, 2.2);
  key.position.set(-0.6, 1.2, 0.9); key.castShadow = true;
  key.shadow.mapSize.set(1024, 1024); key.shadow.bias = -0.0004; key.shadow.radius = 4;
  const rim = new THREE.DirectionalLight(0xffb28e, 0.9); rim.position.set(0.8, 0.6, -0.9);
  scene.add(key, rim, new THREE.HemisphereLight(0xdfe6ea, 0x1a1f20, 0.35));

  const camera = new THREE.PerspectiveCamera(32, 1, 0.01, 20);
  const controls = new OrbitControls(camera, canvas);
  controls.enableDamping = true; controls.dampingFactor = 0.08;
  controls.enablePan = false; controls.minDistance = 0.32; controls.maxDistance = 2.2;
  controls.minPolarAngle = 0.25; controls.maxPolarAngle = Math.PI / 2 + 0.05;
  controls.autoRotate = !reduce; controls.autoRotateSpeed = 0.8;

  const [gltf, meta] = await Promise.all([
    new GLTFLoader().loadAsync(MODEL, e => { if (e.total && onProgress) onProgress(e.loaded / e.total); }),
    fetch(META).then(r => r.json()).catch(() => ({ explode: {} }))
  ]);
  const model = gltf.scene;
  model.traverse(o => { if (o.isMesh) { o.castShadow = true; o.receiveShadow = true; } });
  scene.add(model);

  // Wyśrodkowanie i kadr
  const box = new THREE.Box3().setFromObject(model);
  const size = box.getSize(new THREE.Vector3()), center = box.getCenter(new THREE.Vector3());
  model.position.sub(new THREE.Vector3(center.x, box.min.y, center.z));
  const target = new THREE.Vector3(0, size.y * 0.5, 0);
  controls.target.copy(target);
  const home = { pos: new THREE.Vector3(size.y * 1.35, size.y * 0.95, size.y * 1.95), target: target.clone() };
  camera.position.copy(home.pos);

  // Cień na podłodze
  const ground = new THREE.Mesh(new THREE.PlaneGeometry(3, 3), new THREE.ShadowMaterial({ opacity: 0.32 }));
  ground.rotation.x = -Math.PI / 2; ground.receiveShadow = true; scene.add(ground);
  key.target.position.copy(target); scene.add(key.target);

  // Widok rozłożony: przesunięcia z Blendera (już w osiach glTF)
  const parts = [];
  for (const [name, d] of Object.entries(meta.explode || {})) {
    const node = model.getObjectByName(name);
    if (node) parts.push({ node, rest: node.position.clone(), delta: new THREE.Vector3(...d) });
  }
  let explode = 0, explodeTarget = 0;
  function applyExplode() {
    const e = explode < 0.5 ? 4 * explode ** 3 : 1 - (-2 * explode + 2) ** 3 / 2;
    for (const p of parts) p.node.position.copy(p.rest).addScaledVector(p.delta, e);
  }

  // Punkty z opisami
  const layer = document.createElement('div'); layer.className = 'viewer-hotspots'; host.appendChild(layer);
  const card = document.createElement('div'); card.className = 'viewer-card'; card.hidden = true;
  card.setAttribute('role', 'status'); card.setAttribute('aria-live', 'polite'); host.appendChild(card);
  const spots = (T.hotspots || []).map((h, i) => {
    const node = model.getObjectByName(h.node);
    if (!node) return null;
    const b = document.createElement('button');
    b.type = 'button'; b.className = 'viewer-spot'; b.textContent = String(i + 1);
    b.setAttribute('aria-label', h.title);
    b.addEventListener('click', () => {
      const open = b.classList.toggle('is-on');
      spots.forEach(s => s && s.btn !== b && s.btn.classList.remove('is-on'));
      card.hidden = !open;
      if (open) { card.innerHTML = ''; const t = document.createElement('strong'); t.textContent = h.title; const p = document.createElement('p'); p.textContent = h.text; card.append(t, p); controls.autoRotate = false; }
    });
    layer.appendChild(b);
    return { btn: b, node };
  }).filter(Boolean);
  const tmp = new THREE.Vector3(), bb = new THREE.Box3();
  function placeSpots() {
    const w = canvas.clientWidth, h = canvas.clientHeight;
    for (const s of spots) {
      bb.setFromObject(s.node).getCenter(tmp); tmp.project(camera);
      const vis = tmp.z < 1;
      s.btn.style.transform = `translate(${(tmp.x * 0.5 + 0.5) * w}px, ${(-tmp.y * 0.5 + 0.5) * h}px)`;
      s.btn.hidden = !vis;
    }
  }

  // Pasek narzędzi
  const bar = document.createElement('div'); bar.className = 'viewer-bar';
  const bExplode = button(T.explode, () => {
    explodeTarget = explodeTarget ? 0 : 1; bExplode.textContent = explodeTarget ? T.assemble : T.explode;
    bExplode.setAttribute('aria-pressed', String(!!explodeTarget));
    if (reduce) { explode = explodeTarget; applyExplode(); }
    track('viewer_explode', { state: explodeTarget ? 'open' : 'closed' });
  });
  bExplode.setAttribute('aria-pressed', 'false');
  const bReset = button(T.reset, () => { tween = { t0: performance.now(), from: camera.position.clone(), to: home.pos.clone() }; controls.autoRotate = !reduce; });
  const hint = document.createElement('span'); hint.className = 'viewer-hint'; hint.textContent = T.hint;
  bar.append(bExplode, bReset, hint); host.appendChild(bar);
  function button(label, fn) { const b = document.createElement('button'); b.type = 'button'; b.className = 'viewer-btn'; b.textContent = label; b.addEventListener('click', fn); return b; }
  function track(ev, p) { if (window.scenovisTrack) window.scenovisTrack(ev, p); }
  canvas.addEventListener('pointerdown', () => { controls.autoRotate = false; });

  let tween = null;
  function resize() {
    const w = host.clientWidth, h = host.clientHeight;
    renderer.setSize(w, h, false); camera.aspect = w / h; camera.updateProjectionMatrix();
  }
  new ResizeObserver(resize).observe(host); resize();

  // Render tylko gdy sekcja jest widoczna
  let visible = true;
  new IntersectionObserver(es => { visible = es[0].isIntersecting; if (visible) loop(); }).observe(host);
  let last = performance.now(), running = false;
  function loop() {
    if (running) return; running = true;
    requestAnimationFrame(function frame(now) {
      const dt = Math.min(0.05, (now - last) / 1000); last = now;
      if (explode !== explodeTarget) {
        explode += Math.sign(explodeTarget - explode) * dt / 0.9;
        explode = Math.max(0, Math.min(1, explode)); applyExplode();
      }
      if (tween) {
        const u = Math.min(1, (now - tween.t0) / 700), e = u * u * (3 - 2 * u);
        camera.position.lerpVectors(tween.from, tween.to, e); controls.target.lerp(home.target, e);
        if (u >= 1) tween = null;
      }
      controls.update(dt); renderer.render(scene, camera); placeSpots();
      if (visible) requestAnimationFrame(frame); else running = false;
    });
  }
  loop();
  track('viewer_ready');
  return { renderer };
}
