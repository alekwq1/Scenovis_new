const DICT = {
  pl: {
    formSending:"Wysyłanie...",
    formPreview:"To podgląd lokalny. Wysyłka formularza zadziała dopiero po publikacji na Netlify z włączoną obsługą formularzy.",
    formFailure:"Nie udało się wysłać. Spróbuj ponownie lub napisz do nas bezpośrednio.",
    formSuccess:"Dziękujemy! Twoje zapytanie zostało wysłane. Skontaktujemy się z Tobą.",
    privacyNote:"Projekt do uzupełnienia i sprawdzenia przed publikacją.",
    privacyTitle:"Polityka prywatności",
    privacyLink:"Polityka prywatności",
    sendInquiry:"Wyślij zapytanie",
    formDisclaimer:"Dane wykorzystamy tylko do odpowiedzi na zapytanie. <a class=\"privacy-open\" href=\"privacy.html\">Polityka prywatności</a>.",
    messagePlaceholder:"W kilku słowach napisz, o co chodzi...",
    messageLabel:"Wiadomość <span class=\"optional\">(opcjonalnie)</span>",
    contactPlaceholder:"np. +48 500 000 000 lub kontakt@firma.pl",
    contactLabel:"Telefon lub e-mail <span class=\"required\">*</span>",
    formIntro:"Telefon lub e-mail — to wystarczy. Odeślemy odpowiedź albo oddzwonimy.",
    formTitle:"Zostaw kontakt.",
    videoSoonTitle:'Tu pojawi się Twój film 3D',videoSoonText:'Miejsce na wideo produktu lub interaktywny model.',
    eventPolandTitle:'Planujesz wydarzenie w Polsce?',eventPolandText:'Pomożemy zorganizować je na miejscu — również gdy Twój zespół działa za granicą. Uzgodnimy zakres, skoordynujemy dostawców i przygotujemy obsługę. Rozmawiamy po polsku i angielsku.',eventPolandAction:'Porozmawiajmy o wydarzeniu',optEvent:'Organizacja całego wydarzenia',
    skip:'Przejdź do treści',navServices:'Oferta',navExamples:'Przykłady',navApproach:'Jak pracujemy',navAbout:'O nas',navContact:'Kontakt',
    heroEyebrow:'PREZENTACJE PRODUKTÓW • MULTIMEDIA • EXPO',heroTitle:'Pokaż, jak działa <em>Twój produkt.</em>',heroText:'Interaktywne prezentacje 3D, obsługa targów i organizacja wydarzeń. Wybierz jedną usługę lub powierz nam przygotowanie całości.',ctaTalk:'Porozmawiajmy o projekcie',ctaExplore:'Zobacz ofertę',heroFooter:'Gdańsk · Projekty w Polsce i za granicą · PL / EN',artTitle:'Technologia, którą można zrozumieć.',artText:'Prezentacje, które przyciągają uwagę i wyjaśniają produkt.',conceptLabel:'KONCEPCJA AI · NIE REALIZACJA KLIENTA',
    rail1:'INTERAKTYWNE 3D',rail2:'EKRANY I MULTIMEDIA',rail3:'HOSTESSY I PERSONEL',rail4:'ORGANIZACJA WYDARZEŃ',
    servicesIndex:'OFERTA',servicesTitle:'Od pojedynczej usługi <br>do całego wydarzenia.',servicesLead:'Od modelu 3D i obsługi stoiska po organizację całego wydarzenia. Ustalamy zakres dopasowany do Twojego celu, terminu i budżetu.',service1Title:'Prezentacje produktów 3D',service1Desc:'Modele techniczne, przekroje, animacje i interaktywne prezentacje pokazujące, jak działa produkt.',service2Title:'Ekrany i multimedia',service2Desc:'Ekrany dotykowe, konfiguracja stanowisk i przygotowanie treści do działania na miejscu.',service3Title:'Hostessy i obsługa prezentacji',service3Desc:'Personel do powitania gości, wsparcia stanowiska i prowadzenia pokazów na wydarzeniu.',service4Title:'Organizacja wydarzeń',service4Desc:'Miejsce, harmonogram, dostawcy, technika i obsługa na miejscu. Organizujemy całe wydarzenie lub wybraną część, zgodnie z ustalonym zakresem.',serviceAction:'Zapytaj o usługę',servicesFoot:'Masz już stoisko, ekran lub model? Zamów tylko potrzebną usługę albo połącz kilka — dopasujemy się do Ciebie.',servicesFootAction:'Ustalmy zakres ↗',
    examplesIndex:'PRZYKŁADY ZASTOSOWAŃ',examplesTitle:'Złożony produkt.<br><em>Prosta prezentacja.</em>',examplesLead:'Pokazujemy, jak działa produkt i co kryje się w środku. Gotowa prezentacja może też służyć po targach — w sprzedaży, showroomie i online.',caseTag1:'KONCEPCJA AI / EXPO',caseTag2:'KONCEPCJA AI / PRODUKT 3D',case1Title:'Stoisko, które pokazuje więcej.',case1Desc:'Duży ekran przyciąga uwagę, a interaktywna prezentacja pomaga zagłębić się w szczegóły produktu.',case2Title:'Pokaż to, czego nie widać.',case2Desc:'Przekroje, widoki rozłożone i animacje pomagają wyjaśnić budowę i działanie urządzenia.',conceptDisclaimer:'Powyższe ilustracje są koncepcjami przygotowanymi z użyciem AI, a nie zrealizowanymi projektami klientów Scenovis.',
    flexIndex:'ELASTYCZNY ZAKRES',flexTitle:'Tyle wsparcia,<br><em>ile potrzebujesz.</em>',flexLead:'Nie wciskamy każdemu tego samego pakietu. Możesz zamówić wyłącznie personel, prezentację 3D albo połączyć kilka elementów w jedno rozwiązanie.',flexAction:'Opowiedz, czego potrzebujesz',flex1Title:'Jedna usługa',flex1Desc:'Np. hostessa lub obsługa prezentacji na targach',flex2Title:'Kilka elementów',flex2Desc:'Np. aplikacja 3D, ekran dotykowy i wsparcie techniczne',flex3Title:'Kompleksowo',flex3Desc:'Koncepcja ekspozycji, multimedia, partnerzy i koordynacja',
    reuseIndex:'WARTOŚĆ PO WYDARZENIU',reuseTitle:'Targi się kończą.<br><em>Prezentacja zostaje.</em>',reuseDesc:'Model i materiały przygotowane na wydarzenie mogą później pracować dla Twojego zespołu sprzedaży, na stronie internetowej lub w showroomie.',reuse1:'TARGI',reuse2:'SPRZEDAŻ',reuse3:'SHOWROOM',reuse4:'WWW',
    stepsIndex:'JAK PRACUJEMY',stepsTitle:'Prosty proces.<br><em>Jasne ustalenia.</em>',stepsLead:'Od pierwszego kontaktu wiesz, co obejmuje projekt, kto za co odpowiada i na kiedy wszystko będzie gotowe.',step1Title:'Krótka rozmowa',step1Desc:'Poznajemy produkt lub wydarzenie, termin i cel. Możesz zacząć od jednego zdania.',step2Title:'Zakres i wycena',step2Desc:'Dobieramy usługi, wykonawców i harmonogram. Przed rozpoczęciem wiesz, za co płacisz.',step3Title:'Realizacja i wsparcie',step3Desc:'Przygotowujemy materiały lub personel i koordynujemy uzgodniony zakres.',
    aboutIndex:'O NAS',aboutTitle:'Dwie osoby.<br><em>Jedno podejście.</em>',aboutLead:'Technologia i organizacja w jednym miejscu. Wiesz, z kim rozmawiasz i kto prowadzi Twój projekt.',aleksRole:'INTERAKTYWNE 3D I TECHNOLOGIA',aleksDesc:'Pomagam pokazać, jak działa Twój produkt — za pomocą modeli 3D, wizualizacji i interaktywnych prezentacji. Korzystam przy tym z doświadczenia w BIM i pracy z dokumentacją techniczną.',lizaRole:'ORGANIZACJA WYDARZEŃ',lizaDesc:'Pomagam zorganizować całe wydarzenie lub wybraną część. Koordynuję przygotowania, dostawców i obsługę na miejscu — od pierwszych ustaleń do zakończenia wydarzenia.',lizaPhotoNote:'MIEJSCE NA ZDJĘCIE LIZY',teamNote:'W zależności od zakresu projektu współpracujemy z dobranymi specjalistami od techniki, zabudowy i obsługi wydarzeń.',
    contactIndex:'KONTAKT',contactTitle:'Masz pomysł?<br><em>Porozmawiajmy.</em>',contactLead:'Zostaw numer telefonu lub e-mail albo napisz do nas bezpośrednio. Ustalimy szczegóły w rozmowie.',contactDirect:'WYBIERZ NAJWYGODNIEJSZY SPOSÓB',waSub:'Szybka wiadomość do Scenovis',phoneSub:'Zadzwoń i opowiedz o projekcie',emailSub:'Wyślij opis lub materiały',contactExtra:'Współpraca po polsku i angielsku.',formEyebrow:'SZYBKIE ZAPYTANIE',nameLabel:'Imię <span class="optional">(opcjonalnie)</span>',serviceLabel:'Czego potrzebujesz?',namePlaceholder:'Jak mamy się zwracać?',optNotSure:'Jeszcze nie wiem / potrzebuję porady',opt3d:'Prezentacja 3D produktu',optAv:'Ekran lub multimedia',optPeople:'Hostessy / obsługa prezentacji',optExpo:'Obsługa stoiska targowego',optOther:'Inny temat',chipPricing:'Proszę o wycenę',chipCall:'Proszę o kontakt',chipEvent:'Mam wydarzenie',sendWa:'Wyślij przez WhatsApp',sendEmail:'Przygotuj e-mail',footerText:'Interaktywne 3D · Targi · Organizacja wydarzeń',errContact:'Podaj numer telefonu (min. 7 cyfr) albo poprawny adres e-mail.',messagePricing:'Proszę o orientacyjną wycenę.',messageCall:'Proszę o kontakt w sprawie możliwej współpracy.',messageEvent:'Planuję wydarzenie i potrzebuję wsparcia.',waHello:'Dzień dobry, kontaktuję się przez stronę Scenovis.',fName:'Imię',fContact:'Kontakt',fService:'Temat',fMessage:'Wiadomość',fNoMsg:'Proszę o kontakt i ustalenie szczegółów.',mailSubject:'Zapytanie ze strony Scenovis',contactTitleMeta:'Scenovis — prezentacje 3D i organizacja wydarzeń',contactDescMeta:'Interaktywne prezentacje 3D, multimedia, obsługa targów i organizacja całych wydarzeń. Wsparcie na miejscu w Polsce. Współpraca PL / EN.'
  },
  en: {
    formSending:"Sending...",
    formPreview:"This is a local preview. Form submissions work after the site is deployed to Netlify and form detection is enabled.",
    formFailure:"Could not send your enquiry. Please try again or contact us directly.",
    formSuccess:"Thank you! Your enquiry has been submitted. We will be in touch.",
    privacyNote:"Draft. Please complete and verify before publication.",
    privacyTitle:"Privacy policy",
    privacyLink:"Privacy policy",
    sendInquiry:"Send enquiry",
    formDisclaimer:"We use your details only to reply to your enquiry. <a class=\"privacy-open\" href=\"privacy.html\">Privacy policy</a>.",
    messagePlaceholder:"Tell us briefly what you need...",
    messageLabel:"Message <span class=\"optional\">(optional)</span>",
    contactPlaceholder:"e.g. +48 500 000 000 or hello@company.com",
    contactLabel:"Phone or email <span class=\"required\">*</span>",
    formIntro:"A phone number or email is enough. We will reply or call you back.",
    formTitle:"Leave your contact.",
    videoSoonTitle:'Your 3D video goes here',videoSoonText:'Space for product footage or an interactive model.',
    eventPolandTitle:'Planning an event in Poland?',eventPolandText:'We help organise it locally, even if your team is based abroad. We agree on the scope, coordinate suppliers and arrange on-site support. We speak Polish and English.',eventPolandAction:'Let’s discuss your event',optEvent:'Complete event organisation',
    skip:'Skip to content',navServices:'Services',navExamples:'Examples',navApproach:'Our process',navAbout:'About us',navContact:'Contact',
    heroEyebrow:'PRODUCT PRESENTATIONS • MULTIMEDIA • EXPO',heroTitle:'Show how <em>your product works.</em>',heroText:'Interactive 3D presentations, trade fair support and event organisation. Choose one service or let us organise the whole event.',ctaTalk:'Let’s discuss your project',ctaExplore:'Explore services',heroFooter:'Gdańsk · Projects in Poland and internationally · PL / EN',artTitle:'Technology made clear.',artText:'Presentations that attract attention and explain your product.',conceptLabel:'AI CONCEPT · NOT A CLIENT PROJECT',
    rail1:'INTERACTIVE 3D',rail2:'SCREENS & MULTIMEDIA',rail3:'HOSTESSES & EVENT STAFF',rail4:'EVENT ORGANISATION',
    servicesIndex:'SERVICES',servicesTitle:'From a single service <br>to a complete event.',servicesLead:'From a 3D model and booth support to a complete event. We agree on the scope to fit your goals, schedule and budget.',service1Title:'Interactive product 3D',service1Desc:'Technical models, cutaways, animations and interactive experiences that explain how products work.',service2Title:'Screens and multimedia',service2Desc:'Touchscreens, display setups and multimedia prepared and tested for your event.',service3Title:'Hostesses and presenters',service3Desc:'Staff to welcome visitors, support your booth and help demonstrate your products.',service4Title:'Event organisation',service4Desc:'Venue, schedule, suppliers, equipment and on-site staff. We organise the whole event or selected parts, based on the agreed scope.',serviceAction:'Ask about this service',servicesFoot:'Already have a booth, screen or model? Choose a single service or combine several — we will adapt to your needs.',servicesFootAction:'Discuss the scope ↗',
    examplesIndex:'WHAT WE CAN SHOW',examplesTitle:'Complex product.<br><em>Clear presentation.</em>',examplesLead:'Show how your product works and what is inside. Reuse the presentation after the event — in sales meetings, showrooms and online.',caseTag1:'AI CONCEPT / EXPO',caseTag2:'AI CONCEPT / 3D PRODUCT',case1Title:'A booth that shows more.',case1Desc:'A large display attracts attention while an interactive presentation lets visitors explore product details.',case2Title:'Show what is hidden.',case2Desc:'Cutaways, exploded views and animations help explain how a machine is built and how it operates.',conceptDisclaimer:'Images above are AI-assisted concepts, not completed Scenovis client projects.',
    flexIndex:'FLEXIBLE SCOPE',flexTitle:'Exactly the support<br><em>you need.</em>',flexLead:'No one-size-fits-all packages. Order event staff only, a 3D presentation, or combine several services into one project.',flexAction:'Tell us what you need',flex1Title:'One service',flex1Desc:'For example, a hostess or product presenter at your booth',flex2Title:'Several services',flex2Desc:'For example, a 3D app, touchscreen and technical support',flex3Title:'Full coordination',flex3Desc:'Exhibition concept, multimedia, partners and delivery',
    reuseIndex:'VALUE BEYOND THE EVENT',reuseTitle:'The event ends.<br><em>Your presentation stays.</em>',reuseDesc:'A model built for an event can continue supporting your sales team, website or showroom long after the exhibition.',reuse1:'EXPO',reuse2:'SALES',reuse3:'SHOWROOM',reuse4:'WEB',
    stepsIndex:'HOW WE WORK',stepsTitle:'Simple process.<br><em>Clear expectations.</em>',stepsLead:'From the first conversation, you know the project scope, responsibilities and delivery timeline.',step1Title:'Quick discussion',step1Desc:'We learn about your product or event, timing and goals. One sentence is enough to start.',step2Title:'Scope and quote',step2Desc:'We agree on services, partners and a timeline. You know what is included before we start.',step3Title:'Delivery and support',step3Desc:'We prepare the presentation or staff and coordinate the agreed scope.',
    aboutIndex:'ABOUT US',aboutTitle:'Two people.<br><em>One approach.</em>',aboutLead:'Technology and organisation under one roof. You know who you are speaking to and who leads your project.',aleksRole:'INTERACTIVE 3D & TECHNOLOGY',aleksDesc:'I help you show how your product works through 3D models, visualisations and interactive presentations. I draw on my experience with BIM and technical documentation.',lizaRole:'EVENT COORDINATION',lizaDesc:'I help organise the whole event or selected parts. I coordinate preparations, suppliers and on-site staff, from the first discussion to the end of the event.',lizaPhotoNote:'LIZA PHOTO COMING SOON',teamNote:'Depending on the project, we work with trusted specialists in AV, booth construction and event staffing.',
    contactIndex:'CONTACT',contactTitle:'Have an idea?<br><em>Let’s talk.</em>',contactLead:'Leave your phone number or email, or contact us directly. We will discuss the details together.',contactDirect:'CHOOSE WHAT WORKS FOR YOU',waSub:'Send Scenovis a quick message',phoneSub:'Call to discuss your project',emailSub:'Send your brief or files',contactExtra:'We work in Polish and English.',formEyebrow:'QUICK ENQUIRY',nameLabel:'Name <span class="optional">(optional)</span>',serviceLabel:'What do you need?',namePlaceholder:'What should we call you?',optNotSure:'Not sure yet / need advice',opt3d:'3D product presentation',optAv:'Screen or multimedia',optPeople:'Hostesses / presentation staff',optExpo:'Trade fair booth support',optOther:'Something else',chipPricing:'Please send a quote',chipCall:'Please contact me',chipEvent:'I have an event',sendWa:'Send via WhatsApp',sendEmail:'Prepare an email',footerText:'Interactive 3D · Trade fairs · Event organisation',errContact:'Enter a valid email address or a phone number with at least 7 digits.',messagePricing:'Please send me an estimated quote.',messageCall:'Please contact me to discuss a possible project.',messageEvent:'I am planning an event and need support.',waHello:'Hello, I am contacting you through the Scenovis website.',fName:'Name',fContact:'Contact',fService:'Topic',fMessage:'Message',fNoMsg:'Please contact me to discuss the details.',mailSubject:'Scenovis website enquiry',contactTitleMeta:'Scenovis — 3D presentations and event organisation',contactDescMeta:'Interactive 3D presentations, multimedia, trade fair support and complete event organisation. Local support in Poland. We work in Polish and English.'
  },
};
let lang = 'pl';
const $ = id => document.getElementById(id);
function setLang(next) {
  if(!Object.hasOwn(DICT,next)) next='pl';
  lang=next;
  const tr=DICT[next];
  document.documentElement.lang=next;
  document.title=tr.contactTitleMeta;
  document.querySelector('meta[name="description"]').content=tr.contactDescMeta;
  document.querySelectorAll('[data-i18n]').forEach(el=>{const k=el.dataset.i18n;if(tr[k]!==undefined)el.textContent=tr[k]});
  document.querySelectorAll('[data-i18n-html]').forEach(el=>{const k=el.dataset.i18nHtml;if(tr[k]!==undefined)el.innerHTML=tr[k]});
  document.querySelectorAll('[data-placeholder]').forEach(el=>{const k=el.dataset.placeholder;if(tr[k]!==undefined)el.placeholder=tr[k]});
  document.querySelectorAll('[data-lang]').forEach(el=>el.setAttribute('aria-pressed',el.dataset.lang===next?'true':'false'));
  document.querySelectorAll('[data-chip]').forEach(el=>el.classList.remove('active'));
  $('menu-toggle').setAttribute('aria-label',next==='pl'?'Otwórz lub zamknij menu':'Toggle navigation');
  $('nav').setAttribute('aria-label',next==='pl'?'Nawigacja główna':'Main navigation');
  $('form-error').textContent='';
  document.querySelectorAll('[data-privacy-lang]').forEach(el=>{el.hidden=el.dataset.privacyLang!==next});
  const url=new URL(window.location.href);url.searchParams.set('lang',next);try{window.history.replaceState(null,'',url)}catch{}
  try{window.localStorage.setItem('scenovis_lang',next)}catch{}
  const headerMessage=next==='en'?'Hello! I would like to discuss a Scenovis project.':'Dzień dobry! Chcę porozmawiać o projekcie ze Scenovis.';
  $('whatsapp-header').href='https://wa.me/48666895060?text='+encodeURIComponent(headerMessage);
  $('wa-contact').href=$('whatsapp-header').href;
}
function validContact(s) {
  const v=s.trim();const email=/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(v);
  const phone=/^[+\d\s().-]+$/.test(v)&&v.replace(/\D/g,'').length>=7&&v.replace(/\D/g,'').length<=15;
  return email||phone;
}
function validateEnquiry(){
  const input=$('contact-value'), error=$('form-error');
  error.textContent='';error.classList.remove('success');input.classList.remove('invalid');input.removeAttribute('aria-invalid');
  if(!validContact(input.value)){
    error.textContent=DICT[lang].errContact;
    input.classList.add('invalid');input.setAttribute('aria-invalid','true');input.focus();return false;
  }
  return true;
}
async function submitEnquiry(event){
  event.preventDefault();
  if(!validateEnquiry())return;
  const error=$('form-error');const button=$('send-inquiry');const label=button.querySelector('span');
  // A local HTML preview or test server has no Netlify Forms endpoint.
  if(!['http:','https:'].includes(location.protocol)||['localhost','127.0.0.1'].includes(location.hostname)){
    error.textContent=DICT[lang].formPreview;return;
  }
  const form=$('inquiry');const contact=$('contact-value').value.trim();
  $('netlify-reply').value=contact.includes('@')?contact:'';
  const payload=new URLSearchParams(new FormData(form));
  button.disabled=true;label.textContent=DICT[lang].formSending;
  try{
    const response=await fetch('/',{method:'POST',headers:{'Content-Type':'application/x-www-form-urlencoded'},body:payload.toString()});
    if(!response.ok) throw new Error('Form submission: HTTP '+response.status);
    error.textContent=DICT[lang].formSuccess;error.classList.add('success');
    form.reset();$('service-topic').value='';$('netlify-reply').value='';
  }catch(err){
    error.textContent=DICT[lang].formFailure;
  }finally{
    button.disabled=false;label.textContent=DICT[lang].sendInquiry;
  }
}
window.addEventListener('DOMContentLoaded',()=>{
  const queryLang=new URLSearchParams(window.location.search).get('lang');
  let saved='pl';try{saved=window.localStorage.getItem('scenovis_lang')||'pl'}catch{}
  setLang(queryLang||saved);
  document.querySelectorAll('[data-lang]').forEach(btn=>btn.addEventListener('click',()=>setLang(btn.dataset.lang)));
  document.querySelectorAll('[data-service]').forEach(btn=>btn.addEventListener('click',()=>{ $('service-topic').value=btn.dataset.service; navigateSection('contact'); }));
  $('inquiry').addEventListener('submit',submitEnquiry);
  document.addEventListener('click',e=>{const a=e.target.closest('a.privacy-open');if(a){e.preventDefault();$('privacy-modal').showModal()}});
  $('privacy-close').addEventListener('click',()=>$('privacy-modal').close());
  $('privacy-modal').addEventListener('click',e=>{if(e.target===$('privacy-modal'))$('privacy-modal').close()});
  $('contact-value').addEventListener('input',()=>{$('form-error').textContent='';$('contact-value').classList.remove('invalid');$('contact-value').removeAttribute('aria-invalid')});
  const menu=$('menu-toggle');const nav=$('nav');menu.addEventListener('click',()=>{const expanded=menu.getAttribute('aria-expanded')==='true';menu.setAttribute('aria-expanded',String(!expanded));nav.classList.toggle('open',!expanded)});
  document.querySelectorAll('#nav a').forEach(a=>a.addEventListener('click',()=>{nav.classList.remove('open');menu.setAttribute('aria-expanded','false')}));
  document.addEventListener('keydown',e=>{if(e.key==='Escape'&&nav.classList.contains('open')){nav.classList.remove('open');menu.setAttribute('aria-expanded','false');menu.focus()}});
  // Update a tiny reading indicator and highlight the nearest menu section.
  // No mandatory scroll snap: longer sections and forms stay fully reachable.
  const sectLinks=new Map([...document.querySelectorAll('#nav a')].map(a=>[a.getAttribute('href').substring(1),a]));
  const order=['services','about','contact'];
  const progress=$('scroll-progress').querySelector('span');
  let frame=false;
  const updateScrollUI=()=>{
    frame=false;
    const max=Math.max(1,document.documentElement.scrollHeight-window.innerHeight);
    progress.style.transform='scaleX('+Math.min(1,Math.max(0,window.scrollY/max))+')';
    let active=null;
    const limit=window.scrollY+document.querySelector('.site-header').offsetHeight+Math.min(170,innerHeight*.24);
    for(const id of order){if($(id)&&$(id).offsetTop<=limit) active=id;}
    sectLinks.forEach((a,id)=>{a.classList.toggle('current',id===active);if(id===active)a.setAttribute('aria-current','location');else a.removeAttribute('aria-current')});
  };
  const queueScrollUI=()=>{if(!frame){frame=true;window.requestAnimationFrame(updateScrollUI)}};
  window.addEventListener('scroll',queueScrollUI,{passive:true});
  window.addEventListener('resize',queueScrollUI,{passive:true});
  updateScrollUI();
  $('year').textContent=String(new Date().getFullYear());
});

window.addEventListener('DOMContentLoaded',()=>{
 const reduced=matchMedia('(prefers-reduced-motion: reduce)');
 const header=document.querySelector('.site-header');
 const hero=document.querySelector('.hero-art');
 const fine=matchMedia('(hover: hover) and (pointer: fine)');
 const revealElements=[...document.querySelectorAll('.section-heading,.service-card,.case-card,.step,.team-member,.about-note,.contact-left,.form-panel')];
 let observer;
 function revealSection(target){target?.querySelectorAll('.motion-item').forEach(el=>{el.classList.add('in-view');observer?.unobserve(el)})}
 if(!reduced.matches&&'IntersectionObserver' in window){
  observer=new IntersectionObserver(entries=>entries.forEach(entry=>{if(entry.isIntersecting){entry.target.classList.add('in-view');observer.unobserve(entry.target)}}),{threshold:.06,rootMargin:'0px 0px -16px 0px'});
  revealElements.forEach(el=>{const siblings=[...el.parentElement.children];el.style.setProperty('--delay',Math.min(siblings.indexOf(el),3)*75+'ms');el.classList.add('motion-item');observer.observe(el)});
  document.querySelectorAll('.hero-copy>*').forEach((el,i)=>el.animate([{opacity:0,transform:'translateY(20px)'},{opacity:1,transform:'translateY(0)'}],{duration:700,delay:i*85,easing:'cubic-bezier(.19,1,.22,1)',fill:'backwards'}));
 }
 document.querySelectorAll('a[href^="#"]').forEach(a=>a.addEventListener('click',e=>{
  if(e.button!==0||e.metaKey||e.ctrlKey||e.shiftKey||e.altKey)return;
  const id=a.hash.slice(1);if(!document.getElementById(id))return;
  e.preventDefault();navigateSection(id);
 }));
 document.querySelectorAll('[data-service]').forEach(a=>a.addEventListener('click',()=>revealSection(document.getElementById('contact'))));
 document.addEventListener('focusin',e=>e.target.closest('.motion-item')?.classList.add('in-view'));
 if(location.hash)revealSection(document.getElementById(location.hash.slice(1)));
 const measureHeader=()=>document.documentElement.style.setProperty('--header-offset',(header.getBoundingClientRect().height+12)+'px');
 if('ResizeObserver' in window)new ResizeObserver(measureHeader).observe(header);measureHeader();
 let scrollFrame=false;
 function updateAtmosphere(){scrollFrame=false;header.classList.toggle('is-scrolled',scrollY>12);if(!reduced.matches&&fine.matches){const rect=hero.getBoundingClientRect();if(rect.bottom>0&&rect.top<innerHeight)hero.style.setProperty('--hero-shift',Math.max(-10,Math.min(10,scrollY*.025))+'px')}}
 addEventListener('scroll',()=>{if(!scrollFrame){scrollFrame=true;requestAnimationFrame(updateAtmosphere)}},{passive:true});updateAtmosphere();
 hero.addEventListener('pointermove',e=>{if(reduced.matches||!fine.matches)return;const r=hero.getBoundingClientRect();hero.style.setProperty('--ry',((e.clientX-r.left)/r.width-.5)*3+'deg');hero.style.setProperty('--rx',-((e.clientY-r.top)/r.height-.5)*3+'deg')});
 hero.addEventListener('pointerleave',()=>{hero.style.setProperty('--rx','0deg');hero.style.setProperty('--ry','0deg')});
 document.querySelectorAll('.service-card').forEach(card=>card.addEventListener('pointermove',e=>{if(reduced.matches||!fine.matches)return;const r=card.getBoundingClientRect();card.style.setProperty('--mx',e.clientX-r.left+'px');card.style.setProperty('--my',e.clientY-r.top+'px')}));
 reduced.addEventListener('change',()=>{if(reduced.matches){revealElements.forEach(el=>el.classList.add('in-view'));observer?.disconnect();document.querySelectorAll('.hero-copy>*').forEach(el=>el.getAnimations().forEach(a=>a.finish()));hero.style.setProperty('--hero-shift','0px')}});
});

// Single anchor-navigation path. Never intercept wheel/touch or force scroll snapping.
function navigateSection(id){
 const target=document.getElementById(id);if(!target)return;
 const nav=document.getElementById('nav'),menu=document.getElementById('menu-toggle');
 nav.classList.remove('open');menu.setAttribute('aria-expanded','false');
 target.querySelectorAll('.motion-item').forEach(el=>el.classList.add('in-view'));
 const header=document.querySelector('.site-header');
 const top=id==='top'?0:Math.max(0,target.getBoundingClientRect().top+scrollY-header.getBoundingClientRect().height-12);
 const url=new URL(location.href);url.hash=id;
 if(location.hash!==url.hash)history.pushState(null,'',url);
 window.scrollTo({top,behavior:matchMedia('(prefers-reduced-motion: reduce)').matches?'instant':'smooth'});
 const focusTarget=target.querySelector('h1,h2')||target;
 if(!focusTarget.hasAttribute('tabindex'))focusTarget.setAttribute('tabindex','-1');
 focusTarget.focus({preventScroll:true});
}

// Hero carousel: manual controls; no automatic motion while reading.
window.addEventListener('DOMContentLoaded',()=>{
 const slides=[...document.querySelectorAll('.hero-slide')],buttons=[...document.querySelectorAll('.hero-dot')];
 const title=document.getElementById('hero-media-title'),desc=document.getElementById('hero-media-desc');
 const copy={pl:[['Prezentacja produktu na targach','Duży ekran, interaktywne doświadczenie.'],['Zajrzyj do wnętrza produktu','Przekroje, detale i animacje techniczne.'],['Twój produkt w ruchu','Tutaj wstawimy gotowe wideo lub prezentację 3D.']],en:[['Product presentation at a trade fair','Large screens and interactive experiences.'],['Explore how a product works','Technical sections, details and animations.'],['Your product in motion','Your video or 3D presentation will appear here.']]};
 let current=0;function show(i){current=(i+slides.length)%slides.length;slides.forEach((s,n)=>s.classList.toggle('is-active',n===current));buttons.forEach((b,n)=>{b.classList.toggle('active',n===current);b.setAttribute('aria-pressed',String(n===current))});const lng=document.documentElement.lang==='en'?'en':'pl';[title.textContent,desc.textContent]=copy[lng][current]}
 buttons.forEach((b,i)=>b.addEventListener('click',()=>show(i)));document.querySelector('.hero-next')?.addEventListener('click',()=>show(current+1));document.querySelectorAll('[data-lang]').forEach(b=>b.addEventListener('click',()=>show(current)));show(0);
});
