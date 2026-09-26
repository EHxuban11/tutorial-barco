# Prompts originales del barco

Selección de los mensajes que Xuban escribió a Astra durante HackSpain (18 y 19 de septiembre de 2026) y que dieron forma al barco, a los vídeos y a la escena de las estrellas. Van en orden cronológico, con la hora.

Es una selección editada: se han corregido erratas y se han quitado palabrotas, rutas locales, mensajes de estado ("¿cómo va?") y todo lo que no tenía que ver con el barco (la plataforma financiera, el póster, la logística del equipo). El sentido de cada mensaje no se ha cambiado. Los prompts de generación exactos que se enviaron a Seedance están en [fal-prompts.md](fal-prompts.md).

## 1. El barco en Blender

**18 sep, 22:35**
> Can you read this conversation? Basically I want the boat to be made in Blender on this MacBook. The goal is that at the end I want a website where, when I scroll, it moves the frames of the video generated in Blender. Let's focus 100% on Blender. Make the boat with the flag of Embat kind of move in Blender. Thank you.

**22:39**
> We might need to use the Blender MCP? I may not have that set up.

*Al final no hizo falta: Astra ejecutó Python dentro de Blender desde la terminal.*

**23:17** *(con una imagen de referencia de la nao)*
> Could it look like Elcano's boat (Juan Sebastián Elcano)? Also the flag: could this be the waving flag of the boat? Focus on the boat more than the water.

**23:24**
> I see a white flag, not the Embat logo. Also, for now, forget about the ocean, don't change it anymore.

**23:52**
> ¿Y hay alguna manera de hacer que el barco esté mejor renderizado?

**19 sep, 00:21** *(con el logo de Embat)*
> ¿Puedes poner este logo en todas las velas y renderizar de nuevo? Que se vea desde el frente del barco. Y quítale el fondo al logo, porque la vela es beige y el logo tiene fondo blanco, y el fondo blanco sobra.

**00:59**
> ¿Puedes mejorar el agua para que sea un poco más como la de One Piece, o agua más normal o mejor hecha, sin esos hilos?

**00:59**
> Te doy libertad creativa ahora para que mejores todo en general.

**01:04**
> Una cosa: el barco más o menos tiene que ser el de Elcano, creo que se llama Victoria. La forma debería ser esa, aunque te dejo jugar un poco con el color.

## 2. Del render de Blender al vídeo fotorrealista

**12:51**
> Construye la página web, por favor. Vamos a tener que empezar a hacer el vídeo, y a lo mejor se genera con ByteDance o lo que sea. Estoy un poco confuso, vamos a alinearnos primero. ¿Cómo lo ves? Crea el Next.js por ahora y nos alineamos.

**13:02**
> ¿Y ByteDance puede usar nuestro vídeo de Embat como entrada y hacer uno mucho más HD? ¿Eso existe? ¿Cómo va? El vídeo está bastante guapo, solo que hay que hacerlo HD.

**13:04**
> Yo probaría ahora simplemente a generar con Seedance el vídeo usando el vídeo de referencia, y ver si mantiene los logos.

**13:57**
> Vale, pero me esperaba algo más fotorrealista, la verdad.

**13:58**
> Lo que quiero es que se vea como una producción de Hollywood.

**14:01**
> Dale. ¿Y cómo podemos reducir costes un poco?

**14:11** *(al ver el vídeo 8, la primera prueba cinematográfica)*
> ¡El vídeo es increíble!

## 3. Todas las escenas

**14:21**
> Lo que haría es tener paciencia e ir escena a escena, haciendo poco a poco todas las de Blender, y confiar en el proceso. Al final pasamos todo por ByteDance, porque ya hemos demostrado que el modelo funciona muy bien. Primero hacemos la maqueta de la página en Next.js con todas las escenas sacadas de Blender. Escribe para Astra el prompt: la idea no es que lo haga todo de una vez, sino que esté al tanto y yo pueda iterar con él.

*Ese encargo es [PROMPT-astra.md](PROMPT-astra.md).*

**14:42**
> ¿Seedance puede renderizar ese vídeo aunque tenga cortes, o es mejor pasarle varios fragmentos? Busca en la documentación.

**14:44**
> Vale, pues hagamos fragmentos.

**15:21**
> ¿Y si en vez de vídeos le damos un PNG como entrada? Por ejemplo, para la parte donde se abre el cofre: abrir el cofre de manera más fluida dándole una imagen y diciéndole que lo abra.

**16:51**
> El cofre no funciona: debería ser un cofre pequeño en un barco grande, la cámara se acerca al cofre y, cuando se abre, hay papiros. Ahora mismo es un cofre gigante en un barco pequeño que se abre y no hay nada dentro. Y en el vídeo de la isla con ciudad, la gracia son los barquitos: que cada barquito sea una empresa, con barcos variados en tamaño y estado.

*El feedback completo es [FEEDBACK-videos-astra.md](FEEDBACK-videos-astra.md).*

**17:05**
> Renderízalo, pero dale libertad creativa a Seedance: no con el barco, sí con la caja, porque ahora se abre de forma muy tosca.

**17:08**
> El vídeo 8 como referencia, no.

**17:09**
> El vídeo 13 como referencia de todos. Si hay alguno anterior que no use el 13, re-renderízalo.

*Desde aquí, el vídeo 13 es la referencia de apariencia de todas las escenas.*

## 4. Ajustes finales

**17:59**
> ¿Por qué el vídeo de la escena 6 es tan malo comparado con los demás? ¿Tenemos alguno mejor? Desentona mucho la calidad.

**18:01**
> En la slide de las constelaciones, el vídeo de fondo ya tiene estrellas. Las estrellas que ponemos por encima las hizo mi compañero con una versión vieja del vídeo, y claro, ya no son las mismas.

**18:01**
> No me gusta el vídeo que has propuesto: tiene que ser como el actual, pero con más calidad. Supongo que simplemente hay que re-renderizarlo.

**18:07**
> Creo que el vídeo de la isla 1 no aporta nada realmente. Lo podemos quitar, mal que me pese.

**19:04**
> We need to radically improve slide 2. First, it's too fast, so make it slower. And the stars don't align anymore, so the animation doesn't make much sense. Could you align the stars?

**19:11**
> No, I want a rollback. The video already has stars, so adapt to those and create the constellations from them. Just adapt the previous animation to match the background video.

**19:15**
> Ahora molaría que el logo de Embat apareciera como el 78: las otras constelaciones desaparecen y sale el logo de Embat, dibujado como las otras constelaciones pero más grande, con un texto sobre un score unificado con el que tomar decisiones.
