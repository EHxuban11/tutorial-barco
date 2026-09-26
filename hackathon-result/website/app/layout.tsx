import "./globals.css";
import "./embat-presentation.css";
import type { Metadata } from "next";
import { PresentationNav } from "@/components/PresentationNav";
import { PresentationBrand } from "@/components/PresentationBrand";
import { BoatTransition } from "@/components/BoatTransition";
export const metadata: Metadata = { title: "Elkano — the boat presentation", description: "The HackSpain boat presentation: Blender, Seedance and scroll-driven storytelling.", icons: { icon: "/images/elkano-head.png" } };
export default function RootLayout({children}:{children:React.ReactNode}) {
  return <html lang="es"><body className="antialiased bg-surface min-h-screen">{children}<BoatTransition/><footer className="presentation-footer on-film"><PresentationBrand/></footer><PresentationNav/></body></html>;
}
