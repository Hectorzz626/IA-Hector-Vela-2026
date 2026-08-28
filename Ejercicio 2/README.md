# Reporte de Ejecución: Modificación del Entorno Wumpus

**Estudiante:** Héctor Jesús Vela Acosta  
**Matrícula:** 21216275  

## 1. Diseño de la Cueva (`mi_cueva_4x4.yaml`)

**Diagrama del mapa:**
```text
[Y] Arriba
 4 |  Wumpus [1,4] |   Pit [2,4]   |    Vacío      |    Vacío      |
 3 |    Vacío      |    Vacío      |    Vacío      |   Pit [4,3]   |
 2 |    Vacío      |    Vacío      |   Oro [3,2]   |    Vacío      |
 1 |  Agente [1,1] |    Vacío      |    Vacío      |   Pit [4,1]   |
 -------------------------------------------------------------------
        Col 1            Col 2           Col 3           Col 4       [X] Derecha
```

## 2. Análisis de Agentes

### ¿Qué agentes lograron salir con el oro en tu mapa y cuáles no?
En la simulación, los agentes con capacidad para mapear el entorno lograron cumplir el objetivo. Tanto el **agente basado en modelo** como el **agente basado en metas** consiguieron el oro de forma muy eficiente, completando la tarea en 17 pasos y obteniendo un puntaje de 983. El **agente basado en utilidad** también logró asegurar el oro, pero realizó una exploración mucho más exhaustiva que le tomó 34 pasos, dejándolo con un puntaje final de 956. En contraste, el **agente de reflejo simple** fue el único que fracasó; agotó el límite máximo de 200 pasos sin encontrar el oro, terminando con un puntaje negativo.

### ¿Por qué el agente de reflejo simple falla en tu diseño?
El agente de reflejo simple falla en esta cueva porque carece de memoria y de un estado interno. Su lógica opera estrictamente con la percepción de la casilla actual. Al no poder recordar qué rutas ya exploró ni guardar un historial de las casillas seguras, es incapaz de planificar un camino hacia adelante o de regreso. Al enfrentarse a un entorno que requiere navegación secuencial, entra en un bucle cíclico (moviéndose entre las mismas casillas adyacentes repetidamente) hasta que el simulador interrumpe la ejecución por alcanzar el límite de pasos.

### ¿Cómo cambia el resultado del agente basado en modelo si acercas o alejas un pit de la casilla inicial?
Sabemos que un pit genera una brisa en las casillas contiguas. Si acercamos un pit a la casilla inicial, el agente basado en modelo detectará la brisa en sus primeros movimientos. Si la brisa restringe sus opciones iniciales y no tiene suficientes casillas seguras para explorar y triangular la posición exacta del pozo, su programación cautelosa hará que aborte la misión y regrese sin el oro para evitar morir. Por el contrario, si alejamos los pits de la casilla inicial, el agente tendrá espacio suficiente para moverse, lo que le permitirá registrar múltiples casillas seguras en su mapa mental. Con esa información recopilada, cuando finalmente encuentre una brisa, tendrá los datos deductivos necesarios para localizar matemáticamente el peligro y evadirlo con éxito.
