# Verified notes: Blender 5.2.2, September 2026

Blender 5.2.2 LTS worked on Apple Silicon with Cycles Metal: set the Cycles preferences' `compute_device_type='METAL'`, refresh devices, enable Metal devices, then set `scene.cycles.device='GPU'`. Detect available devices rather than assuming Metal.

Installed `ShaderNodeTexSky.sky_type` values were `SINGLE_SCATTERING`, `MULTIPLE_SCATTERING`, `PREETHAM`, `HOSEK_WILKIE`. Assigning the older `NISHITA` value failed. The density property was `aerosol_density`, not `dust_density`. Inspect `node.bl_rna.properties` in the installed version. `use_nodes` worked but emitted Blender 6.0 deprecation warnings.

## Geometry lessons

- Give loft sides and end caps consistent outward winding.
- Smooth cylinder caps made thin wheels look like balls. Keep caps flat and smooth only the cylinder sides.
- Subdivide door-outline segments before projecting them onto a curved shell; long straight segments disappear inside it.
- Tessellate and subdivide filled SVG outlines before mapping them over curved bodies. Preserve holes in letters. A tiny offset prevents z-fighting; a large offset makes painted logos look like badges.
- Check opposite-side logo orientation and parent logos to moving roots.
- Update the view layer before saving a new camera's world matrix for fixed-camera assertions.
- Saved viewport preferences may reopen differently on the user's machine. Verify the opened scene rather than promising an exact viewport.
