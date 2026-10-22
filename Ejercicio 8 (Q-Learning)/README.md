[README.md](https://github.com/user-attachments/files/33845277/README.md)
# Reporte Breve: Ejercicio 1 — Q-learning en Cliff Walking

**Semilla utilizada:** 42 (configurada en `cliff.yaml`)

### 1. ¿Por qué el camino de 13 pasos, pegado al acantilado, es óptimo?
En este entorno, cada paso ordinario tiene una recompensa de -1. Para maximizar el retorno (es decir, obtener la menor penalización posible), el agente debe encontrar la ruta que requiera la menor cantidad de pasos para llegar desde el inicio (S) hasta la meta (G). 

Partiendo de S en la coordenada `(3, 0)`, el camino más directo que evita el acantilado implica subir una casilla al Norte hacia `(2, 0)`, avanzar en línea recta 11 casillas al Este por la fila 2 (justo por encima del acantilado) hasta `(2, 11)`, y finalmente dar un paso al Sur para entrar a la meta en `(3, 11)`. Esta secuencia suma exactamente 13 pasos. Dado que cada paso cuesta -1 y el retorno no tiene descuento ($\gamma = 1$), el retorno total de este camino es -13. Cualquier otro camino seguro (por ejemplo, transitando por las filas 0 o 1) requeriría desviarse más hacia el norte, sumando pasos adicionales (15 o 17 pasos) y resultando en un retorno menor (-15 o -17).

### 2. ¿Por qué la curva de entrenamiento queda por debajo de −13 aunque la política greedy ya sea óptima?
Esto se debe a la política de exploración $\epsilon$-greedy utilizada durante la fase de entrenamiento. Con $\epsilon = 0.1$, el agente toma una acción completamente aleatoria el 10% de las veces. 

Dado que la política óptima aprendida por Q-learning camina exactamente por el borde del acantilado (fila 2), cualquier paso aleatorio hacia el Sur en esas casillas provoca que el agente caiga, recibiendo una penalización masiva de -100. La gráfica de entrenamiento muestra la suma real de recompensas obtenidas en cada episodio *con la exploración encendida*. Por lo tanto, el promedio se ve fuertemente arrastrado hacia abajo por estas caídas constantes. El retorno óptimo de -13 solo se observa en la evaluación final, cuando apagamos la exploración ($\epsilon = 0$) y el agente sigue la política greedy de forma estricta.

### 3. En el paso que cae al acantilado, ¿cuál es `s'` en el backup de Q-learning, y por qué ese backup no trata el acantilado como estado terminal?
Cuando el agente ejecuta una acción que lo lleva al acantilado, las reglas del entorno dictan que es penalizado con -100 y devuelto inmediatamente a la casilla de inicio. Por lo tanto, el estado siguiente **$s'$ es S** (la coordenada `(3, 0)`).

El backup de Q-learning no trata esta transición como un estado terminal porque las reglas estipulan explícitamente que **el episodio continúa** (la bandera `done` es `False`). En la ecuación de actualización:
$Q(s, a) \leftarrow Q(s, a) + \alpha [ r + \gamma \max_{a'} Q(s', a') - Q(s, a) ]$

Al no ser un estado terminal, el valor futuro estimado ($\max_{a'} Q(s', a')$) no se fuerza a 0. En su lugar, el algoritmo evalúa cuál es el máximo valor $Q$ posible desde la casilla de inicio $S$, permitiendo que el agente asimile que, tras el castigo, el juego sigue desde el principio y aún hay recompensas (o penalizaciones) por venir.
