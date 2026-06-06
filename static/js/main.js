/* ─────────────────────────────────────────────────────────────
   Three.js animated particle network background — subtle.
   Falls back gracefully if Three.js fails to load.
   ───────────────────────────────────────────────────────────── */

(function () {
  if (typeof THREE === "undefined") return;

  const canvas = document.getElementById("bg-canvas");
  if (!canvas) return;

  const renderer = new THREE.WebGLRenderer({
    canvas,
    alpha: true,
    antialias: true,
  });
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
  renderer.setSize(window.innerWidth, window.innerHeight);

  const scene = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(
    60,
    window.innerWidth / window.innerHeight,
    0.1,
    2000
  );
  camera.position.z = 600;

  /* Particles */
  const PARTICLE_COUNT = 220;
  const positions = new Float32Array(PARTICLE_COUNT * 3);
  const velocities = new Float32Array(PARTICLE_COUNT * 3);

  for (let i = 0; i < PARTICLE_COUNT; i++) {
    positions[i * 3 + 0] = (Math.random() - 0.5) * 1600;
    positions[i * 3 + 1] = (Math.random() - 0.5) * 1000;
    positions[i * 3 + 2] = (Math.random() - 0.5) * 800;
    velocities[i * 3 + 0] = (Math.random() - 0.5) * 0.3;
    velocities[i * 3 + 1] = (Math.random() - 0.5) * 0.3;
    velocities[i * 3 + 2] = (Math.random() - 0.5) * 0.2;
  }

  const particleGeo = new THREE.BufferGeometry();
  particleGeo.setAttribute(
    "position",
    new THREE.BufferAttribute(positions, 3)
  );

  const particleMat = new THREE.PointsMaterial({
    color: 0x4f8cff,
    size: 2.2,
    transparent: true,
    opacity: 0.85,
    sizeAttenuation: true,
  });

  const points = new THREE.Points(particleGeo, particleMat);
  scene.add(points);

  /* Connection lines */
  const MAX_LINES = PARTICLE_COUNT * 4;
  const linePositions = new Float32Array(MAX_LINES * 6);
  const lineGeo = new THREE.BufferGeometry();
  lineGeo.setAttribute(
    "position",
    new THREE.BufferAttribute(linePositions, 3).setUsage(THREE.DynamicDrawUsage)
  );
  const lineMat = new THREE.LineBasicMaterial({
    color: 0xd4af37,
    transparent: true,
    opacity: 0.18,
  });
  const lines = new THREE.LineSegments(lineGeo, lineMat);
  scene.add(lines);

  /* Pointer parallax */
  let pointerX = 0;
  let pointerY = 0;
  window.addEventListener("pointermove", (e) => {
    pointerX = (e.clientX / window.innerWidth - 0.5) * 60;
    pointerY = (e.clientY / window.innerHeight - 0.5) * 60;
  });

  /* Resize */
  window.addEventListener("resize", () => {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
  });

  /* Render loop */
  const tmp = new THREE.Vector3();
  const tmp2 = new THREE.Vector3();
  const LINK_DIST_SQ = 130 * 130;

  function tick() {
    const pos = particleGeo.attributes.position.array;

    for (let i = 0; i < PARTICLE_COUNT; i++) {
      pos[i * 3 + 0] += velocities[i * 3 + 0];
      pos[i * 3 + 1] += velocities[i * 3 + 1];
      pos[i * 3 + 2] += velocities[i * 3 + 2];

      if (pos[i * 3 + 0] > 800 || pos[i * 3 + 0] < -800) velocities[i * 3 + 0] *= -1;
      if (pos[i * 3 + 1] > 500 || pos[i * 3 + 1] < -500) velocities[i * 3 + 1] *= -1;
      if (pos[i * 3 + 2] > 400 || pos[i * 3 + 2] < -400) velocities[i * 3 + 2] *= -1;
    }
    particleGeo.attributes.position.needsUpdate = true;

    /* Build lines for nearby pairs */
    let lineIndex = 0;
    for (let a = 0; a < PARTICLE_COUNT && lineIndex < MAX_LINES; a++) {
      tmp.set(pos[a * 3], pos[a * 3 + 1], pos[a * 3 + 2]);
      for (let b = a + 1; b < PARTICLE_COUNT && lineIndex < MAX_LINES; b++) {
        tmp2.set(pos[b * 3], pos[b * 3 + 1], pos[b * 3 + 2]);
        const dx = tmp.x - tmp2.x;
        const dy = tmp.y - tmp2.y;
        const dz = tmp.z - tmp2.z;
        const distSq = dx * dx + dy * dy + dz * dz;
        if (distSq < LINK_DIST_SQ) {
          linePositions[lineIndex * 6 + 0] = tmp.x;
          linePositions[lineIndex * 6 + 1] = tmp.y;
          linePositions[lineIndex * 6 + 2] = tmp.z;
          linePositions[lineIndex * 6 + 3] = tmp2.x;
          linePositions[lineIndex * 6 + 4] = tmp2.y;
          linePositions[lineIndex * 6 + 5] = tmp2.z;
          lineIndex++;
        }
      }
    }
    lineGeo.setDrawRange(0, lineIndex * 2);
    lineGeo.attributes.position.needsUpdate = true;

    /* Camera parallax */
    camera.position.x += (pointerX - camera.position.x) * 0.04;
    camera.position.y += (-pointerY - camera.position.y) * 0.04;
    camera.lookAt(scene.position);

    renderer.render(scene, camera);
    requestAnimationFrame(tick);
  }

  tick();
})();

/* Reveal sections on scroll */
(function () {
  if (!("IntersectionObserver" in window)) return;
  const els = document.querySelectorAll(".kpi-card, .work-card, .timeline__item, .stack-group, .contact-card");
  els.forEach((el) => {
    el.style.opacity = "0";
    el.style.transform = "translateY(18px)";
    el.style.transition = "opacity 480ms ease, transform 540ms cubic-bezier(.2,.7,.2,1)";
  });
  const io = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.style.opacity = "1";
        entry.target.style.transform = "translateY(0)";
        io.unobserve(entry.target);
      }
    });
  }, { threshold: 0.08 });
  els.forEach((el) => io.observe(el));
})();
