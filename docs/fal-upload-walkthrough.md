# Del MP4 local a una referencia para fal

Guía de trabajo revisada el 26 de septiembre de 2026. Los comandos se ejecutan en un terminal, desde la raíz del repositorio. Requieren Python y `uv`; el agente puede comprobar su instalación antes de empezar.

## Cuatro cosas distintas

1. **Archivo local:** el MP4 que exportas de Blender o el PNG de tu logo.
2. **Archivo subido:** fal almacena ese archivo y devuelve una URL que el modelo puede leer.
3. **Petición de generación:** envías el prompt, los ajustes y las URLs al modelo.
4. **Resultado:** recuperas la petición por su ID y descargas el vídeo generado.

Subir un archivo no ejecuta el modelo. Una ruta como `renders/hero.mp4` solo existe en tu ordenador: no sustituye a una URL en `video_urls`.

## Preparar los archivos

Para el primer plano, prepara `inputs/hero.mp4` y `inputs/logo.png` dentro de tu proyecto. Estos nombres son una convención del tutorial: copia tus archivos reales a esas rutas o cambia los argumentos de los comandos.

Reproduce el vídeo completo antes de subirlo. Comprueba duración, resolución y tamaño con el agente. Revisa los límites vigentes en la [API del modelo](https://fal.ai/models/bytedance/seedance-2.0/fast/reference-to-video/api), especialmente si vas a combinar dos vídeos. Conserva el original cuando recortes o redimensiones.

## Cuenta y clave

Crea o usa tu propia cuenta de fal y una clave de API desde su panel. Estar conectado en el navegador no proporciona automáticamente una clave al terminal. La generación requiere saldo y debe ajustarse a tu presupuesto.

El helper incluido permite introducir la clave en un prompt oculto. No necesitas pegarla en la conversación con el agente ni escribirla dentro de un script. Para una grabación, haz la configuración de la cuenta fuera de cámara.

## Comprobar la selección sin subir

```sh
uv run --with fal-client python skills/xu-fal/scripts/fal_upload.py \
  --manifest run/uploads.json inputs/hero.mp4 inputs/logo.png
```

Resultado esperado: `local-only plan`, dos archivos con tamaño y hash, y `network_calls: 0`. Esta operación todavía no crea el manifiesto de subidas.

## Subir y guardar las URLs

```sh
uv run --with fal-client python skills/xu-fal/scripts/fal_upload.py \
  --manifest run/uploads.json --upload --prompt-key \
  inputs/hero.mp4 inputs/logo.png
```

Introduce la clave cuando la pida el terminal. El helper utiliza `SyncClient.upload_file` del SDK oficial y guarda cada subida en `run/uploads.json`. El resultado esperado es `storage_uploaded` y una URL por archivo. Consulta la [referencia oficial del cliente](https://fal-ai.github.io/fal/client/fal_client.html).

Si repites el comando, reutiliza el recibo de un archivo cuyo contenido no ha cambiado. Esto no comprueba que la URL siga disponible: verifica su acceso antes de generar. Usa `--refresh` solo cuando necesites volver a subirlo, por ejemplo si la URL ha caducado.

No publiques claves. Los recibos contienen rutas locales y URLs de medios: revísalos antes de incluirlos en un repositorio público.

## Asignar cada URL al papel correcto

Este fragmento ilustra la parte de referencias de la petición; **no es una petición ejecutable completa**:

```json
{
  "video_urls": ["URL_DEL_MP4_DE_BLENDER"],
  "image_urls": ["URL_DEL_LOGO"]
}
```

El primer elemento de `video_urls` es `@Video1`; el primero de `image_urls` es `@Image1`. Los nombres del archivo y el orden de subida no determinan esa numeración: la determina el orden dentro de cada lista de la petición.

Para el segundo plano:

```json
{
  "video_urls": ["URL_DE_LA_NUEVA_ACCION", "URL_DEL_EXTRACTO_DEL_HERO_APROBADO"],
  "image_urls": ["URL_DEL_LOGO"]
}
```

Aquí `@Video1` dirige la nueva acción y cámara; `@Video2` aporta la apariencia aprobada; `@Image1` conserva la marca. El prompt debe decirlo explícitamente. Sustituye los marcadores por URLs reales y revisa las entradas antes de enviar. La [documentación del modelo](https://fal.ai/models/bytedance/seedance-2.0/fast/reference-to-video/api) define estos campos.

## ¿Por qué no aparece en Assets?

El helper de subida guarda el archivo en almacenamiento y obtiene una URL. En nuestra prueba, eso no bastó para que apareciera en la biblioteca visual de Assets; fue necesaria una operación de registro aparte. El recibo distingue `storage_uploaded` de `assets_library_verified`.

Para llamar al modelo por API, usa la URL devuelta. No añadas el registro en Assets como requisito de esta ruta. Si prefieres organizar los archivos en la web de fal, consulta el [procedimiento de Assets y diagnóstico](../skills/xu-fal/references/uploads.md) y verifica después la biblioteca visual.

## Enviar una vez y recuperar el mismo trabajo

Antes de enviar, guarda la petición completa: endpoint, prompt, URLs en orden, duración, resolución, relación de aspecto y audio. Comprueba el precio actual y decide el gasto máximo.

El SDK permite enviar a la cola y obtener un ID. Guarda ese ID inmediatamente junto a la petición. Consulta el estado y recupera el resultado de **ese mismo ID**. Si se corta la conexión, revisa el historial de fal antes de volver a enviar: una desconexión no demuestra que el trabajo haya fallado.

Descarga el vídeo devuelto por tu petición a tu proyecto; reproduce el archivo completo y comprueba el movimiento y la identidad del sujeto. Ese archivo descargado es el que usarás en la web. La clave de fal no tiene que formar parte de la página publicada.

## Si algo falla

| Síntoma | Comprobación |
| --- | --- |
| No existe el archivo | Carpeta actual y ruta exacta del MP4/PNG |
| Falta la credencial | Clave propia mediante el prompt oculto o `FAL_KEY` |
| El modelo rechaza la referencia | Formato, tamaño, resolución y duración combinada frente al esquema actual |
| Se copia la cámara equivocada | Orden de `video_urls` y papel de cada referencia en el prompt |
| No aparece en Assets | Distinguir almacenamiento de registro en la biblioteca |
| Se pierde la conexión | Recuperar el ID existente antes de cualquier reenvío |

Esta guía documenta el helper existente y la API consultada. No se ha ejecutado una nueva subida ni una generación pagada para validar esta edición del tutorial.
