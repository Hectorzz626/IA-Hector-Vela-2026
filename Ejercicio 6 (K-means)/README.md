# Reporte: Ejercicio 1 — Separar los blobs y volver a elegir k

**1. Codo en la corrida original:**
Al observar la gráfica de inercia de la corrida original, el codo se marcaría en **$k = 4$**. En este punto, la caída drástica de la inercia se detiene y la curva comienza a aplanarse de manera casi horizontal.

**2. Silueta máxima en la corrida original:**
En los datos originales, el puntaje de la silueta alcanza su valor máximo también en **$k = 4$**.

**3. Valores utilizados para la modificación:**
Para lograr separar las cinco nubes a simple vista, se utilizaron los siguientes valores:
* **Nuevos centros (`blob_centers`):**
  * Centro 1: `[ 0.2, 2.3]`
  * Centro 2: `[-1.5, 2.3]`
  * Centro 3: `[-2.8, 1.8]`
  * Centro 4: `[-4.0, 3.0]`
  * Centro 5: `[-4.0, 0.5]`
* **Nuevos valores de desviación estándar (`blob_std`):** `[0.4, 0.3, 0.2, 0.2, 0.2]`

* **¿Por qué se usaron estos valores?**
En los datos originales, los tres centros de la izquierda compartían la coordenada $x = -2.8$, lo que causaba que la distancia entre ellos fuera muy pequeña (menor a $\sim 2(\sigma_i+\sigma_j)$), provocando que se fusionaran. Al mover dos de estos centros a la coordenada $x = -4.0$ y separarlos ampliamente en el eje $y$ (a $3.0$ y $0.5$), se garantiza una distancia lo suficientemente grande como para que los puntos no se superpongan. Además, se aumentó ligeramente la desviación estándar (de $0.1$ a $0.2$) para darle a esas nubes un volumen un poco más notorio, pero gracias a la nueva separación geográfica que establecimos, K-means puede distinguirlas perfectamente sin que se mezclen.

**4. ¿Por qué el codo "prefiere" $k=4$ en los datos de Géron si `make_blobs` usó 5 centros?**
El codo prefiere $k=4$ porque tres de los blobs del lado izquierdo están casi pegados al compartir la misma coordenada $x = -2.8$ y tener una desviación muy pequeña de $0.1$. Debido a esta enorme cercanía geométrica, el algoritmo de K-means no logra percibir la separación real y los trata como si fueran un solo macro-grupo.

**5. Con los blobs separados, ¿el codo y la silueta coinciden en el mismo $k$? ¿Ese $k$ es 5?**
Sí. Al separar físicamente las coordenadas de los centros en el arreglo, tanto el punto de inflexión de la curva de inercia (codo) como el pico máximo del puntaje de silueta se mueven de lugar y ambos coinciden de forma exacta en el valor óptimo de **$k = 5$**.

**6. Si el codo siguiera en 4, ¿qué faltaría mover?**
Si el codo se mantuviera en 4, indicaría que la distancia relativa entre algunos centros sigue siendo muy corta, lo que provoca que las nubes se sigan mezclando en la percepción del modelo. Para solucionarlo, faltaría **aumentar la distancia entre los centros** para alejarlos más, o bien **reducir el valor numérico en `blob_std`** para hacer el radio de las nubes más pequeño (compacto) y evitar así su solapamiento espacial.
