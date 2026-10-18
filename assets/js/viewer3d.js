/* SCENOVIS — interaktywny model 3D (Three.js r170, pliki lokalne, bez CDN).
   Ładowany dopiero po kliknięciu „Uruchom model 3D” (import() z site.js).
   Model: /assets/3d/scenovis-mikroskop.glb (eksport z Blendera).
   Widok rozłożony: przesunięcia części z /assets/3d/scenovis-mikroskop.json (policzone w Blenderze).
   Animacje: wejście kamery, płynne zbliżenia do części (lot po łuku wokół celu),
   rozkładanie z opóźnieniem między częściami, podświetlenie wybranej części, zwiedzanie z opisami. */
import * as THREE from './vendor/three-0.170.0/three.module.min.js';
import { GLTFLoader } from './vendor/three-0.170.0/GLTFLoader.js';
import { OrbitControls } from './vendor/three-0.170.0/OrbitControls.js';
import { RoomEnvironment } from './vendor/three-0.170.0/RoomEnvironment.js';

const MODEL = '/assets/3d/scenovis-mikroskop.glb';
const META = '/assets/3d/scenovis-mikroskop.json';
const ACCENT = new THREE.Color(0xff9364);
const TOUR_MS = 5200;

const easeInOut = u => (u < 0.5 ? 4 * u * u * u : 1 - Math.pow(-2 * u + 2, 3) / 2);
const easeOut = u => 1 - Math.pow(1 - u, 3);

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
  controls.enablePan = false; controls.minDistance = 0.12; controls.maxDistance = 2.2;
  controls.minPolarAngle = 0.2; controls.maxPolarAngle = Math.PI / 2 + 0.05;
  controls.autoRotate = false; controls.autoRotateSpeed = 0.6;

  const [gltf, meta] = await Promise.all([
    new GLTFLoader().loadAsync(MODEL, e => { if (e.total && onProgress) onProgress(e.loaded / e.total); }),
    fetch(META).then(r => r.json()).catch(() => ({ explode: {} }))
  ]);
  const model = gltf.scene;
  // Materiały: eksport z Blendera zawiera niebieską emisję i przezroczystość z efektu podświetlenia w prezentacji.
  const ROUGH = { M_Paint_Lacquer_White: 0.32, M_Paint_Lacquer_Grey: 0.38, M_Plastic_Tech_Black: 0.5,
    M_Rubber_Grip: 0.85, M_Metal_Brushed_Steel: 0.32 };
  const fixed = new Set();
  const isGlass = m => m.transmission > 0 || /Glass/i.test(m.name || '');
  const isDecal = m => /Label|Specimen/i.test(m.name || '');
  model.traverse(o => {
    if (!o.isMesh) return;
    const mats = [].concat(o.material);
    o.castShadow = !mats.some(isGlass); o.receiveShadow = true;
    if (mats.some(isGlass)) o.renderOrder = 2;      // szkło rysowane po elementach nieprzezroczystych
    if (mats.some(isDecal)) o.renderOrder = 1;
    for (const m of mats) {
      if (fixed.has(m)) continue; fixed.add(m);
      m.emissive && m.emissive.setRGB(0, 0, 0);
      if (isGlass(m)) {
        // Szkło bez przebiegu transmission (migotało na cienkich, nakładających się ściankach szkiełka):
        // zwykła przezroczystość, tylko przednie ścianki, bez zapisu głębi.
        m.transmission = 0; m.thickness = 0;
        m.transparent = true; m.depthWrite = false; m.side = THREE.FrontSide;
        m.metalness = 0; m.roughness = 0.04;
        if (/Slide/i.test(m.name)) { m.color.setRGB(0.86, 0.93, 0.95); m.opacity = 0.22; }
        else { m.color.setRGB(0.12, 0.16, 0.2); m.opacity = 0.85; }
        m.envMapIntensity = 1.4;
      } else {
        m.transparent = false; m.opacity = 1; m.depthWrite = true;
      }
      if (isDecal(m)) {
        // napisy i preparat leżą tuż na powierzchni — przesunięcie głębi zapobiega migotaniu
        m.polygonOffset = true; m.polygonOffsetFactor = -2; m.polygonOffsetUnits = -2;
        if (m.map) m.alphaTest = 0.4;
      }
      if (ROUGH[m.name] !== undefined) m.roughness = ROUGH[m.name];
      m.needsUpdate = true;
    }
  });
  scene.add(model);

  // Wyśrodkowanie i kadr
  const box = new THREE.Box3().setFromObject(model);
  const size = box.getSize(new THREE.Vector3()), center = box.getCenter(new THREE.Vector3());
  model.position.sub(new THREE.Vector3(center.x, box.min.y, center.z));
  const H = size.y;
  const target = new THREE.Vector3(0, H * 0.5, 0);
  const home = { pos: new THREE.Vector3(H * 1.35, H * 0.95, H * 1.95), target: target.clone() };
  const exTarget = target.clone().add(new THREE.Vector3(0, H * 0.12, 0));

  // Cień na podłodze
  const ground = new THREE.Mesh(new THREE.PlaneGeometry(3, 3), new THREE.ShadowMaterial({ opacity: 0.32 }));
  ground.rotation.x = -Math.PI / 2; ground.receiveShadow = true; scene.add(ground);
  key.target.position.copy(target); scene.add(key.target);

  // ---------- kamera: lot po łuku wokół celu (bez przelatywania przez model) ----------
  let fly = null;
  const sph = new THREE.Spherical(), sA = new THREE.Spherical(), sB = new THREE.Spherical();
  const tmpV = new THREE.Vector3();
  function flyTo(pos, tgt, ms) {
    const from = camera.position.clone(), fromT = controls.target.clone();
    sA.setFromVector3(from.clone().sub(fromT));
    sB.setFromVector3(pos.clone().sub(tgt));
    let dTheta = sB.theta - sA.theta;
    if (dTheta > Math.PI) dTheta -= 2 * Math.PI;
    if (dTheta < -Math.PI) dTheta += 2 * Math.PI;
    const dur = reduce ? 0 : (ms || THREE.MathUtils.clamp(500 + 900 * Math.abs(dTheta) / Math.PI + 400 * Math.abs(Math.log(sB.radius / sA.radius)), 700, 1700));
    fly = { t0: performance.now(), dur, fromT, toT: tgt.clone(), r0: sA.radius, r1: sB.radius,
            th0: sA.theta, dTh: dTheta, ph0: sA.phi, ph1: sB.phi };
    if (!dur) stepFly(performance.now());
  }
  function stepFly(now) {
    const u = fly.dur ? Math.min(1, (now - fly.t0) / fly.dur) : 1, e = (fly.ease || easeInOut)(u);
    controls.target.lerpVectors(fly.fromT, fly.toT, e);
    // łuk: lekkie oddalenie w połowie lotu, gdy kamera obiega model
    const lift = Math.sin(Math.PI * e) * Math.min(0.35, Math.abs(fly.dTh) / Math.PI * 0.5);
    sph.set(THREE.MathUtils.lerp(fly.r0, fly.r1, e) * (1 + lift),
            THREE.MathUtils.lerp(fly.ph0, fly.ph1, e), fly.th0 + fly.dTh * e);
    camera.position.copy(controls.target).add(tmpV.setFromSpherical(sph));
    if (u >= 1) fly = null;
  }

  // ---------- widok rozłożony: przesunięcia z Blendera, części ruszają kolejno ----------
  const parts = [];
  for (const [name, d] of Object.entries(meta.explode || {})) {
    const node = model.getObjectByName(name);
    if (node) parts.push({ node, rest: node.position.clone(), delta: new THREE.Vector3(...d) });
  }
  // kolejność: od najdalej przesuwanych (efekt „otwierania” od zewnątrz)
  parts.sort((a, b) => b.delta.length() - a.delta.length());
  const STAGGER = 0.5; // część osi czasu przeznaczona na opóźnienia
  let explode = 0, explodeTarget = 0;
  function applyExplode() {
    const n = Math.max(1, parts.length - 1);
    parts.forEach((p, i) => {
      const order = explodeTarget ? i / n : (n - i) / n; // składanie w odwrotnej kolejności
      const u = THREE.MathUtils.clamp((explode - order * STAGGER) / (1 - STAGGER), 0, 1);
      const local = explodeTarget ? u : 1 - THREE.MathUtils.clamp(((1 - explode) - order * STAGGER) / (1 - STAGGER), 0, 1);
      p.node.position.copy(p.rest).addScaledVector(p.delta, easeInOut(local));
    });
  }

  // ---------- punkty z opisami, zbliżenia, podświetlenie ----------
  const layer = document.createElement('div'); layer.className = 'viewer-hotspots'; host.appendChild(layer);
  const card = document.createElement('div'); card.className = 'viewer-card'; card.hidden = true;
  card.setAttribute('role', 'status'); card.setAttribute('aria-live', 'polite'); host.appendChild(card);
  const spots = (T.hotspots || []).map((h, i) => {
    const node = model.getObjectByName(h.node);
    if (!node) return null;
    const b = document.createElement('button');
    b.type = 'button'; b.className = 'viewer-spot'; b.textContent = String(i + 1);
    b.setAttribute('aria-label', h.title);
    layer.appendChild(b);
    // własne kopie materiałów — podświetlenie tylko tej części
    const meshes = [];
    node.traverse(o => { if (o.isMesh) { o.material = [].concat(o.material).map(m => m.clone()); if (o.material.length === 1) o.material = o.material[0]; meshes.push(o); } });
    return { btn: b, node, h, meshes, glow: 0 };
  }).filter(Boolean);
  spots.forEach((s, i) => s.btn.addEventListener('click', () => {
    stopTour();
    if (active === i) clearFocus(); else focus(i);
  }));

  let active = -1;
  const bb = new THREE.Box3(), c3 = new THREE.Vector3(), s3 = new THREE.Vector3();
  function focus(i) {
    active = i; const s = spots[i];
    spots.forEach((x, k) => { x.btn.classList.toggle('is-on', k === i); x.btn.setAttribute('aria-pressed', String(k === i)); });
    bb.setFromObject(s.node); bb.getCenter(c3); bb.getSize(s3);
    const r = THREE.MathUtils.clamp(Math.max(s3.x, s3.y, s3.z) * 3.8, H * 0.5, H * 1.05) * (camera.aspect < 1 ? 1.25 : 1);
    // kierunek: z bieżącej strony kamery, ale z przyjemnym kątem z góry (15–35°)
    const dir = camera.position.clone().sub(controls.target); dir.y = 0;
    if (dir.lengthSq() < 1e-6) dir.set(1, 0, 1);
    dir.normalize();
    const elev = THREE.MathUtils.degToRad(s.h.elev !== undefined ? s.h.elev : 24);
    const pos = c3.clone().addScaledVector(dir, r * Math.cos(elev)).add(new THREE.Vector3(0, r * Math.sin(elev), 0));
    controls.autoRotate = false;
    flyTo(pos, c3.clone());
    showCard(i);
    track('viewer_focus', { part: s.h.node });
  }
  function clearFocus(goHome) {
    active = -1; card.hidden = true;
    spots.forEach(x => { x.btn.classList.remove('is-on'); x.btn.setAttribute('aria-pressed', 'false'); });
    if (goHome) flyHome();
  }
  function flyHome() {
    const t = explodeTarget ? exTarget : home.target;
    const dir = home.pos.clone().sub(home.target);
    flyTo(t.clone().add(dir.multiplyScalar(explodeTarget ? 1.4 : 1)), t.clone());
  }
  function showCard(i) {
    const s = spots[i];
    card.innerHTML = '';
    const head = document.createElement('div'); head.className = 'viewer-card-head';
    const num = document.createElement('span'); num.className = 'viewer-card-num'; num.textContent = `${i + 1} / ${spots.length}`;
    const close = document.createElement('button'); close.type = 'button'; close.className = 'viewer-card-close';
    close.setAttribute('aria-label', T.close); close.textContent = '×';
    close.addEventListener('click', () => { stopTour(); clearFocus(true); });
    head.append(num, close);
    const t = document.createElement('strong'); t.textContent = s.h.title;
    const p = document.createElement('p'); p.textContent = s.h.text;
    const nav = document.createElement('div'); nav.className = 'viewer-card-nav';
    const prev = document.createElement('button'); prev.type = 'button'; prev.textContent = '‹ ' + T.prev;
    const next = document.createElement('button'); next.type = 'button'; next.textContent = T.next + ' ›';
    prev.addEventListener('click', () => { stopTour(); focus((i - 1 + spots.length) % spots.length); });
    next.addEventListener('click', () => { stopTour(); focus((i + 1) % spots.length); });
    nav.append(prev, next);
    card.append(head, t, p, nav);
    card.hidden = false;
    card.classList.remove('is-in'); void card.offsetWidth; card.classList.add('is-in');
  }

  // ---------- zwiedzanie: kolejne zbliżenia z opisami ----------
  let tour = null;
  function startTour() {
    let i = active >= 0 ? (active + 1) % spots.length : 0;
    focus(i);
    tour = setInterval(() => { i = (i + 1) % spots.length; focus(i); }, TOUR_MS);
    bTour.textContent = T.tour_stop; bTour.setAttribute('aria-pressed', 'true');
    track('viewer_tour');
  }
  function stopTour() {
    if (!tour) return;
    clearInterval(tour); tour = null;
    bTour.textContent = T.tour; bTour.setAttribute('aria-pressed', 'false');
  }

  const proj = new THREE.Vector3();
  function placeSpots() {
    const w = canvas.clientWidth, h = canvas.clientHeight;
    for (const s of spots) {
      bb.setFromObject(s.node).getCenter(proj); proj.project(camera);
      const vis = proj.z < 1 && Math.abs(proj.x) < 1.05 && Math.abs(proj.y) < 1.05;
      s.btn.style.transform = `translate(${(proj.x * 0.5 + 0.5) * w}px, ${(-proj.y * 0.5 + 0.5) * h}px)`;
      s.btn.hidden = !vis;
    }
  }

  // ---------- pasek narzędzi ----------
  const bar = document.createElement('div'); bar.className = 'viewer-bar';
  const bTour = button(T.tour, () => { if (tour) { stopTour(); } else startTour(); });
  bTour.classList.add('viewer-btn--accent'); bTour.setAttribute('aria-pressed', 'false');
  const bExplode = button(T.explode, () => {
    explodeTarget = explodeTarget ? 0 : 1; bExplode.textContent = explodeTarget ? T.assemble : T.explode;
    bExplode.setAttribute('aria-pressed', String(!!explodeTarget));
    if (active < 0) flyHome();
    if (reduce) { explode = explodeTarget; applyExplode(); }
    track('viewer_explode', { state: explodeTarget ? 'open' : 'closed' });
  });
  bExplode.setAttribute('aria-pressed', 'false');
  const bReset = button(T.reset, () => { stopTour(); clearFocus(); flyHome(); controls.autoRotate = !reduce; });
  const hint = document.createElement('span'); hint.className = 'viewer-hint'; hint.textContent = T.hint;
  bar.append(bTour, bExplode, bReset, hint); host.appendChild(bar);
  function button(label, fn) { const b = document.createElement('button'); b.type = 'button'; b.className = 'viewer-btn'; b.textContent = label; b.addEventListener('click', fn); return b; }
  function track(ev, p) { if (window.scenovisTrack) window.scenovisTrack(ev, p); }
  canvas.addEventListener('pointerdown', () => { controls.autoRotate = false; fly = null; stopTour(); });
  canvas.addEventListener('wheel', () => { fly = null; stopTour(); }, { passive: true });
  host.addEventListener('keydown', e => { if (e.key === 'Escape' && active >= 0) { stopTour(); clearFocus(true); } });

  function resize() {
    const w = host.clientWidth, h = host.clientHeight;
    renderer.setSize(w, h, false); camera.aspect = w / h; camera.updateProjectionMatrix();
  }
  new ResizeObserver(resize).observe(host); resize();

  // ---------- wejście: kamera nadlatuje z daleka i z boku ----------
  controls.target.copy(home.target);
  if (reduce) {
    camera.position.copy(home.pos); controls.autoRotate = false;
  } else {
    const startDir = home.pos.clone().sub(home.target);
    sph.setFromVector3(startDir); sph.radius *= 1.9; sph.theta -= 1.1; sph.phi = Math.max(0.35, sph.phi - 0.35);
    camera.position.copy(home.target).add(tmpV.setFromSpherical(sph));
    flyTo(home.pos.clone(), home.target.clone(), 2000);
    fly.ease = easeOut;
    setTimeout(() => { if (!fly && active < 0 && !tour) controls.autoRotate = true; }, 2100);
  }
  canvas.classList.add('is-in');

  // Render tylko gdy sekcja jest widoczna
  let visible = true, offX = 0, offY = 0;
  new IntersectionObserver(es => { visible = es[0].isIntersecting; if (visible) loop(); }).observe(host);
  let last = performance.now(), running = false;
  function loop() {
    if (running) return; running = true;
    requestAnimationFrame(function frame(now) {
      const raw = (now - last) / 1000; last = now;
      const dt = Math.min(0.05, raw);
      if (explode !== explodeTarget) {
        // czas rzeczywisty (do 0,25 s na klatkę) — animacja trwa ~1,5 s także na wolnych urządzeniach
        explode += Math.sign(explodeTarget - explode) * Math.min(0.25, raw) / 1.5;
        explode = THREE.MathUtils.clamp(explode, 0, 1); applyExplode();
      }
      if (fly) stepFly(now);
      // przesunięcie kadru, gdy otwarty jest opis: część obok opisu (desktop) lub nad nim (telefon)
      const wide = camera.aspect >= 1, open = active >= 0;
      const wantX = open && wide ? -0.16 : 0, wantY = open && !wide ? 0.2 : 0;
      offX += (wantX - offX) * Math.min(1, dt * 4); offY += (wantY - offY) * Math.min(1, dt * 4);
      const vw = canvas.clientWidth || 1, vh = canvas.clientHeight || 1;
      if (Math.abs(offX) > 1e-4 || Math.abs(offY) > 1e-4) camera.setViewOffset(vw, vh, offX * vw, offY * vh, vw, vh);
      else if (camera.view) camera.clearViewOffset();
      // pulsujące podświetlenie wybranej części
      for (let k = 0; k < spots.length; k++) {
        const s = spots[k], want = k === active ? 0.014 + 0.008 * Math.sin(now / 320) : 0;
        if (Math.abs(s.glow - want) < 0.002 && want === 0) continue;
        s.glow += (want - s.glow) * Math.min(1, dt * 8);
        for (const m of s.meshes) for (const mat of [].concat(m.material)) if (mat.emissive) { mat.emissive.copy(ACCENT); mat.emissiveIntensity = s.glow; }
      }
      controls.update(dt); renderer.render(scene, camera); placeSpots();
      if (visible) requestAnimationFrame(frame); else running = false;
    });
  }
  loop();
  track('viewer_ready');
  return { renderer };
}
