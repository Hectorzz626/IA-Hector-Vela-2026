# Reporte de Búsqueda Informada
**Alumno:** Héctor Jesús Vela Acosta

## 1. Pareja de ciudades elegida y subgrafo
**Origen:** Timisoara
**Destino:** Bucharest

**Heurística utilizada:** straight-line distance to Bucharest (AIMA table)

**Diagrama ASCII del subgrafo evaluado:**
```text
             [Timisoara]
             h=329
             /        \
           111         118
           /             \
       [Lugoj]          [Arad]
       h=244            h=366
          |               |
          70             140
          |               |
      [Mehadia]        [Sibiu]
      h=241            h=253
          |               |
          75              80
          |               |
      [Drobeta]    [Rimnicu Vilcea]
      h=242            h=193
          |               |
         120              97
          |               |
      [Craiova]       [Pitesti]
      h=160            h=100
          \              /
           138          101
             \          /
              \        /
              [Bucharest]
                 h=0
```

## 2. Tabla Comparativa de Algoritmos

| Algoritmo | Status | Path | Depth (Hops) | Cost (km) | Nodos Expandidos | Heurística |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Greedy** | success | Timisoara → Lugoj → Mehadia → Drobeta → Craiova → Pitesti → Bucharest | 6 | 615 | 6 | straight-line |
| **A\*** | success | Timisoara → Arad → Sibiu → Rimnicu Vilcea → Pitesti → Bucharest | 5 | 536 | 10 | straight-line |

## 3. Análisis de Resultados

* **¿A* encontró el camino de menos km? ¿Greedy coincidió o se desvió?**
  Sí, A* encontró el camino óptimo en términos de distancia real, con un costo total de 536 km. Greedy, por otro lado, se desvió significativamente: encontró una ruta de 615 km, lo que demuestra su falta de garantía de optimalidad.

* **¿Por qué Greedy puede devolver un camino más caro aunque h sea admisible?**
  Esto sucede porque Greedy basa sus decisiones **exclusivamente** en el valor heurístico $h(n)$ (la distancia en línea recta estimada al destino), ignorando por completo el costo acumulado $g(n)$ (los kilómetros reales ya recorridos). En el primer paso desde Timisoara, Greedy evalúa a sus vecinos y ve que Lugoj tiene una $h=244$, mientras que Arad tiene $h=366$. Ciegamente elige Lugoj porque "parece" estar más cerca de Bucharest en línea recta. Sin embargo, el camino real por carretera desde Lugoj hacia el sur (Mehadia, Drobeta, Craiova) resulta ser mucho más largo y costoso en kilómetros reales que la ruta norte por Arad y Sibiu. A* evita este error porque evalúa la suma $f(n) = g(n) + h(n)$, balanceando la cercanía aparente con el costo real incurrido.

* **En el camino de A*, ¿f tiende a no disminuir a lo largo de la ruta?**
  Efectivamente, los valores de $f(n)$ en el camino de A* muestran un comportamiento monótono no decreciente (tienden a aumentar o mantenerse, pero nunca a disminuir). Observando la ejecución: 
  Timisoara ($f=329$) $\rightarrow$ Arad ($f=484$) $\rightarrow$ Sibiu ($f=511$) $\rightarrow$ Rimnicu Vilcea ($f=531$) $\rightarrow$ Pitesti ($f=535$) $\rightarrow$ Bucharest ($f=536$).
  Este comportamiento ascendente de la función $f$ se debe a que la heurística de distancia en línea recta de la tabla AIMA es **consistente** (además de admisible). En grafos donde la heurística es consistente, el costo estimado total nunca disminuye a medida que avanzamos por un camino, asegurando que cuando A* expande un nodo, ha encontrado el camino óptimo hacia él.
