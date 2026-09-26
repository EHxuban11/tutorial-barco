# Slides-only Elkano presentation

Adapted from `amarkosmarkos/Elkano_Embat`, branch `xubranch`, commit recorded in [../provenance.json](../provenance.json).

```sh
npm ci
npm run dev       # http://localhost:4323/intro/?present=1
npm run build     # static export in out/
npm run preview   # serve the static export on 4323
```

The build prepares videos from `../videos/`. No API keys, database, raw financial data or platform server are needed. Tested with Node 24.19.0 and npm 11.17.0.

Scene order and selected clips: `lib/presentation.ts`. Playback: `components/Escena.tsx`. Stars/constellations: `components/SkyStory.tsx`. Navigation: `components/PresentationNav.tsx`.

Use a wide, preferably 16:9 presentation viewport. The original cover crop can clip constellation/score content on tall screens; the archive preserves that limitation. A new tutorial site should explicitly adapt the overlay for narrow screens.

The 12-slide narrative is retained. Platform routes, data loaders, Convex, demo-video mode and platform links are removed. Financial claims in the retained slides are historical hackathon content, not new tutorial calculations.

This package does not deploy over the original site. The original production presentation remains at https://elkano-embat-deck.vercel.app/intro/?present=1 .
