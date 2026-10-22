#!/usr/bin/env python3
"""Program 3: train Q-learning (or SARSA) for several episodes."""

from __future__ import annotations

import sys
import matplotlib.pyplot as plt #Para Gnerar la grafica dl final, de los 10 episodios
from dataclasses import replace
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

from qlearn.agent import greedy_return, train  # noqa: E402
from qlearn.cli import build_parser, load, make_rng  # noqa: E402
from qlearn.format import format_env, format_grid_policy, format_q, format_returns  # noqa: E402


def main() -> None:
    parser = build_parser("Train tabular Q-learning / SARSA.")
    parser.add_argument(
        "--method",
        choices=("q-learning", "sarsa"),
        default="q-learning",
        help="Update rule (default: q-learning, off-policy)",
    )
    args = parser.parse_args()
    env = load(args)
    env = replace(
        env,
        seed=args.seed if args.seed is not None else env.seed,
        episodes=args.episodes if args.episodes is not None else env.episodes,
        epsilon=args.epsilon if args.epsilon is not None else env.epsilon,
        alpha=args.alpha if args.alpha is not None else env.alpha,
        gamma=args.gamma if args.gamma is not None else env.gamma,
    )
    rng = make_rng(env, None)

    print(format_env(env))
    print()
    print(f"method = {args.method}    behaviour = ε-greedy")
    print()

    Q, returns = train(env, rng, method=args.method)
    print("Q")
    print("-" * 72)
    print(format_q(env, Q))
    print()
    if env.kind == "grid":
        print("Greedy policy (arrows)")
        print("-" * 72)
        print(format_grid_policy(env, Q))
        print()
    print("Recompensa por episodios de entrenamiento:")
    print(format_returns(returns))
    
    # Calcula y muestra la media movil de los 10 episodios
    window = 10
    if len(returns) >= window:
        moving_avg = [sum(returns[i:i+window])/window for i in range(len(returns)-window+1)]
        print(f"Media movil (ultimos 10 episodios): {moving_avg[-1]:.2f}")

    print("\n--- Evaluacion final Greedy (ε = 0) ---")
    ret_greedy = greedy_return(env, Q)
    print(f"Retorno greedy desde inicio: {ret_greedy:g}")



# === CODIGO PARA GENERAR LA GRAFICA UNICAMENTE ===
    window = 10
    if len(returns) >= window:
        moving_avg = [sum(returns[i:i+window])/window for i in range(len(returns)-window+1)]
        
        plt.figure(figsize=(10, 5))
        
        # Graficar los retornos crudos (en azul claro)
        plt.plot(returns, label='Recompensa por episodio (ε=0.1)', alpha=0.3, color='blue')
        
        # Graficar la media móvil (en rojo)
        # Se desplaza el eje X por el tamaño de la ventana para que coincida
        eje_x_media = range(window - 1, len(returns))
        plt.plot(eje_x_media, moving_avg, label=f'Media móvil ({window} ep)', color='red', linewidth=2)
        
        # Añadir etiquetas y título
        plt.xlabel('Episodios')
        plt.ylabel('Retorno acumulado (Recompensa)')
        plt.title('Entrenamiento Q-learning - Cliff Walking')
        plt.legend()
        plt.grid(True, linestyle='--', alpha=0.7)
        
        # Guardar la gráfica como imagen y mostrarla en pantalla
        plt.savefig('curva de entrenamiento.png')
        print("\nGrafica guardada como 'curva_entrenamiento.png'")
        plt.show()

if __name__ == "__main__":
    main()
