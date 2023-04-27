## Hacer pruebas de estrés a la API con el modelo expuesto con al menos 50.000 requests durante 45 segundos. Para esto debes utilizar esta herramienta y presentar las métricas obtenidas
Para este paso usamos un archivo docker que ya viene configurado con wrk y asi poder evaluarestresar el api del modelo

antes de nada debemos tener el api dockerizada corriendo

docker build -t atraso_vuelo .  

docker run -p 8000:8000 atraso_vuelo

despues descargamos nuestra imagen wrk y evaluamos las cargas para la api

docker pull williamyeh/wrk

docker run --rm -v $(pwd)/script.lua:/data/script.lua --net=host williamyeh/wrk -t4 -c200 -d45s -s /data/script.lua http://localhost:8000/v1/prediction

como resultado obtuvimos:

Running 45s test @ http://localhost:8000/v1/prediction
  4 threads and 200 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     1.46s   309.13ms   2.00s    71.26%
    Req/Sec    21.25     24.38   232.00     90.89%
  2788 requests in 45.10s, 381.17KB read
  Socket errors: connect 0, read 0, write 0, timeout 613
Requests/sec:     61.82

¿Cómo podrías mejorar el performance de las pruebas de estres anteriores?

1. Aumentar el número de conexiones concurrentes: si el rendimiento actual es de 200 conexiones concurrentes, se podría intentar aumentar a 400, 600 o incluso más conexiones para ver cómo afecta el rendimiento. Sin embargo, hay que tener en cuenta que un mayor número de conexiones puede aumentar la carga del servidor y afectar su capacidad de respuesta.

2. Aumentar el tiempo de duración de la prueba: si la duración actual de la prueba es de 45 segundos, se podría aumentar a un tiempo mayor como 60 o 90 segundos para ver cómo afecta el rendimiento.

3. Optimizar el código del servidor: es posible que el código del servidor pueda ser optimizado para mejorar el rendimiento y reducir la latencia. Se pueden realizar mejoras en la implementación de algoritmos, en la gestión de memoria, en el uso de caché, entre otros.

4. Optimizar el entorno de ejecución: se pueden realizar mejoras en el entorno de ejecución del servidor, como ajustar la configuración del sistema operativo o del servidor web, mejorar la configuración del hardware, entre otros.

5. Realizar pruebas de estrés en diferentes momentos: puede ser útil realizar pruebas de estrés en diferentes momentos del día para ver cómo el rendimiento varía en diferentes condiciones de carga.
