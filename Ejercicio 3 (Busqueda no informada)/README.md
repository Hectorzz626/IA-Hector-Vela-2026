# Reporte de Búsqueda No Informada
**Alumno:** Héctor Jesús Vela Acosta

## 1. Pareja de ciudades elegida y subgrafo 
**Origen:** Timisoara  
**Destino:** Bucharest  

**Diagrama ASCII del subgrafo evaluado:**
```text
             [Timisoara]
                  |
                 118
                  |
               [Arad]
                  |
                 140
                  |
               [Sibiu]
               /     \
             99       80
            /           \
      [Fagaras]     [Rimnicu Vilcea]
          |               |
         211              97
          |               |
          |           [Pitesti]
           \             /
            \           101
             \         /
             [Bucharest]
```

## 2. Tabla Comparativa de Algoritmos

| Algoritmo | Status | Path | Depth (Hops) | Cost (km) | Nodos Expandidos |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **BFS** | success | Timisoara → Arad → Sibiu → Fagaras → Bucharest | 4 | 568 | 7 |
| **UCS** | success | Timisoara → Arad → Sibiu → Rimnicu Vilcea → Pitesti → Bucharest | 5 | 536 | 12 |
| **DFS** | success | Timisoara → Arad → Sibiu → Fagaras → Bucharest | 4 | 568 | 4 |
| **DLS** (limit ≤ 3) | cutoff | N/A | N/A | N/A | 3 (en límite 2) |
| **DLS** (limit 4) | success | Timisoara → Arad → Sibiu → Fagaras → Bucharest | 4 | 568 | 4 |
| **IDS** | success | Timisoara → Arad → Sibiu → Fagaras → Bucharest | 4 | 568 | 14 |

## 3. Análisis de Resultados

* **¿BFS encontró el camino con menos carreteras? ¿UCS el de menos km?**
  Sí, se observa claramente la diferencia de objetivos entre ambos. BFS encontró la solución con la menor cantidad de carreteras (4 saltos pasando por Fagaras), pero con un costo total mayor (568 km). UCS, cuyo objetivo es minimizar el costo acumulado sin importar la profundidad, encontró una ruta más barata de 536 km desviándose por Rimnicu Vilcea y Pitesti, lo que le requirió atravesar una ciudad adicional (5 saltos en total). Además, para garantizar esta optimalidad en kilómetros, UCS "trabajó" más, expandiendo 12 nodos en comparación con los 7 de BFS.

* **¿Por qué DFS puede devolver un camino más largo aunque el grafo sea el mismo?**
  Aunque en esta ejecución específica DFS encontró la misma ruta que BFS (debido a que los vecinos se expanden en orden alfabético y tuvo la "suerte" de encontrar Bucharest rápidamente por esa rama), DFS no tiene ninguna garantía de optimalidad. Si el orden de expansión hubiera forzado a DFS a tomar primero un camino alfabéticamente prioritario pero ineficiente, habría profundizado en esa rama hasta el final, devolviendo un camino con muchas más carreteras y un costo mucho mayor, simplemente porque se detiene en la primera solución que encuentra sin comparar otras opciones.

* **¿Con qué `--limit` DLS pasó de `cutoff` a solución, y cómo se relaciona eso con la profundidad del camino de BFS/IDS?**
  DLS pasó de devolver un estado de `cutoff` a encontrar una solución exacta (`success`) cuando el límite se estableció en 4. Todo límite menor o igual a 3 falló sistemáticamente. Esto es completamente congruente con los resultados de BFS e IDS, los cuales ya nos habían demostrado que la solución más corta (en términos de nodos o carreteras) se encuentra a una profundidad de 4. Como el camino a Bucharest desde Timisoara requiere un mínimo de 4 saltos, era topológicamente imposible que DLS la encontrara con un límite inferior.
