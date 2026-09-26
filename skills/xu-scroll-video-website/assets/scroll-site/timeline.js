export const clamp = n => Math.min(1, Math.max(0, Number.isFinite(n) ? n : 0));
export function sectionProgress(top, height, viewport) {
  return clamp(-top / Math.max(1, height - viewport));
}
export function videoTime(progress, duration, start = 0, end = duration) {
  if (!Number.isFinite(duration) || duration <= 0) return 0;
  const last = Math.max(0, duration - 1 / 60);
  const first = Math.min(last, Math.max(0, Number.isFinite(start) ? start : 0));
  const stop = Math.min(last, Math.max(first, Number.isFinite(end) ? end : last));
  return first + clamp(progress) * (stop - first);
}
