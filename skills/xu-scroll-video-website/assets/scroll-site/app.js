import { scenes } from './scenes.js';
import { sectionProgress, videoTime } from './timeline.js';
const $ = id => document.getElementById(id);
const preference = matchMedia('(prefers-reduced-motion: reduce)');
let motion = !preference.matches, playing = false, active = 0, queued = false, previousTime = 0;
const records = scenes.map((config, index) => {
  const section = document.createElement('section');
  section.className = 'scene'; section.id = config.id || `scene-${index}`;
  section.style.setProperty('--screens', Math.max(2, config.screens || 3));
  const stage = document.createElement('div'); stage.className = 'stage';
  const video = document.createElement('video');
  video.muted = true; video.playsInline = true; video.preload = 'metadata';
  if (config.poster) video.poster = config.poster;
  const copy = document.createElement('div'); copy.className = 'copy';
  const title = document.createElement('h1'); title.textContent = config.title || '';
  const text = document.createElement('p'); text.textContent = config.text || '';
  copy.append(title, text);
  const status = document.createElement('p'); status.className = 'status'; status.textContent = 'Loading video…';
  stage.append(video, copy, status); section.append(stage); $('scenes').append(section);
  const record = { config, section, video, copy, status, wanted: null, progress: 0, failed: false };
  const flush = () => {
    if (record.wanted === null || !Number.isFinite(video.duration) || video.seeking) return;
    const target = record.wanted; record.wanted = null;
    if (Math.abs(target - video.currentTime) > 1 / 60) video.currentTime = target;
  };
  record.seek = time => { record.wanted = time; flush(); };
  video.addEventListener('loadedmetadata', schedule);
  video.addEventListener('loadeddata', () => { status.hidden = true; schedule(); });
  video.addEventListener('seeked', flush);
  video.addEventListener('error', () => { record.failed = true; status.hidden = false; status.textContent = 'This video could not be loaded.'; schedule(); });
  video.src = config.video;
  return record;
});
$('empty').hidden = records.length > 0;
document.querySelector('nav').hidden = !records.length;
function stop() { playing = false; $('play').textContent = 'Play'; $('play').setAttribute('aria-pressed', 'false'); }
function schedule() { if (!queued) { queued = true; requestAnimationFrame(render); } }
function render(now) {
  queued = false;
  const dt = Math.min(0.05, previousTime ? (now - previousTime) / 1000 : 0); previousTime = now;
  for (let i = 0; i < records.length; i++) {
    const r = records[i], box = r.section.getBoundingClientRect();
    r.progress = sectionProgress(box.top, box.height, innerHeight);
    if (box.top <= innerHeight / 2 && box.bottom >= innerHeight / 2) active = i;
    if (box.bottom > 0 && box.top < innerHeight) {
      r.seek(videoTime(motion ? r.progress : 0, r.video.duration, r.config.start, r.config.end));
    }
    const visible = r.progress >= (r.config.copyStart ?? 0) && r.progress <= (r.config.copyEnd ?? 1);
    r.copy.hidden = !visible;
  }
  const current = records[active]; if (!current) return;
  $('current').textContent = `${active + 1} / ${records.length} · ${current.config.title || ''}`;
  $('progress').value = current.progress;
  $('previous').disabled = active === 0; $('next').disabled = active === records.length - 1;
  $('play').disabled = !motion || current.failed || !Number.isFinite(current.video.duration);
  $('motion').hidden = motion;
  if (playing && !$('play').disabled) {
    const travel = current.section.offsetHeight - innerHeight;
    const seconds = Math.max(.1, videoTime(1, current.video.duration, current.config.start, current.config.end) - videoTime(0, current.video.duration, current.config.start, current.config.end));
    if (current.progress >= .999) stop();
    else { scrollTo({ top: scrollY + travel * dt / seconds, behavior: 'instant' }); schedule(); }
  }
}
function move(index) {
  stop(); const target = records[Math.max(0, Math.min(records.length - 1, index))];
  target?.section.scrollIntoView({ behavior: motion ? 'smooth' : 'instant', block: 'start' });
}
$('previous').onclick = () => move(active - 1);
$('next').onclick = () => move(active + 1);
$('play').onclick = () => { if (playing) stop(); else { playing = true; previousTime = 0; $('play').textContent = 'Pause'; $('play').setAttribute('aria-pressed', 'true'); schedule(); } };
$('motion').onclick = () => { motion = true; schedule(); };
preference.addEventListener('change', e => { motion = !e.matches; stop(); schedule(); });
addEventListener('scroll', schedule, { passive: true }); addEventListener('resize', schedule);
addEventListener('wheel', stop, { passive: true }); addEventListener('touchstart', stop, { passive: true });
addEventListener('keydown', e => {
  if (e.target.closest('button,a,input,textarea,select')) return;
  if (e.key === 'ArrowRight') { e.preventDefault(); move(active + 1); }
  else if (e.key === 'ArrowLeft') { e.preventDefault(); move(active - 1); }
  else if (['ArrowUp','ArrowDown','PageUp','PageDown','Home','End',' '].includes(e.key)) stop();
});
schedule();
