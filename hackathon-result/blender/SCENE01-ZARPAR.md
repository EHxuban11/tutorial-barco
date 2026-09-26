# Escena 1: Zarpar, maqueta para aprobar

Fuente: `ELKANO-v6-ocean.blend`, conservada sin cambios.
Escena editable: `ELKANO-scene01-zarpar.blend`.
Constructor: `scene01_zarpar.py`, ejecutado sobre la fuente V6.

- 288 fotogramas, 24 fps, 12 segundos, sin cortes ni audio.
- Previsualización real a 800×450, Cycles/Metal, 8 muestras y denoise.
- Plano lateral con un ligero ángulo de proa para leer las velas.
- Entrada por la izquierda; final cerca del centro, ligeramente a la izquierda.
- Travelling suave de dos unidades; no hay zoom ni cambio de lente.
- Mismo barco, velas y bandera animadas del V6.
- Agua más tranquila; mayor extensión del mar para disimular el límite del detalle.
- Coordenadas de la espuma ligadas al barco móvil, no al origen fijo del mundo.

`encode_scene01.py` comprueba los 288 PNG, codifica H.264 CRF 23 con faststart
y GOP de 12 para facilitar el scrubbing, y decodifica todos los frames de salida.
Entrega `videos/9.mp4` y las copias `barco-largo-blender.mp4` y
`barco-largo.mp4` en `Elkano_Embat/apps/web/public/video/`.
No sustituye `barco.mp4`: la intro anterior permanece intacta.

Esto es una maqueta, no el acabado cinematográfico ni un render final HD.
Seedance queda para después de aprobar las escenas. No se ha consumido crédito.
