# Inicio para el despliegue de modelos fast.ai en Render

Este repositorio puede utilizarse como punto de partida para desplegar modelos fast.ai en Render.

La aplicación de ejemplo descrita aquí está en https://fastai-v3.onrender.com. ¡Pruébala con imágenes de osos!.

Puedes probar tus cambios localmente instalando Docker y usando el siguiente comando:

```
docker build -t fastai-v3 . && docker run --rm -it -p 5000:5000 fastai-v3
```

La guía para el despliegue de producción en Render está en https://course.fast.ai/deployment_render.html.

Por favor, utilice el hilo del foro fast.ai de Render para preguntas y soporte.






# Starter for deploying [fast.ai](https://www.fast.ai) models on [Render](https://render.com)

This repo can be used as a starting point to deploy [fast.ai](https://github.com/fastai/fastai) models on Render.

The sample app described here is up at https://fastai-v3.onrender.com. Test it out with bear images!

You can test your changes locally by installing Docker and using the following command:

```
docker build -t fastai-v3 . && docker run --rm -it -p 5000:5000 fastai-v3
```

The guide for production deployment to Render is at https://course.fast.ai/deployment_render.html.

Please use [Render's fast.ai forum thread](https://forums.fast.ai/t/deployment-platform-render/33953) for questions and support.
