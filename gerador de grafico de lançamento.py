import numpy as np
import matplotlib.pyplot as plt
import math

if input("Deseja impor valores? Se sim, digite 's': ").lower() == "s":
    angulos = []
    angulos.append(float(input("Digite o ângulo 1 do foguete (em graus): ")))
    angulos.append(float(input("Digite o ângulo 2 do foguete (em graus): ")))
    angulos.append(float(input("Digite o ângulo 3 do foguete (em graus): ")))
    velocidade = float(input("Digite a velocidade do foguete (em metros por segundo): "))
    gravidade = float(input("Digite a gravidade do planeta (em metros por segundo ao quadrado): "))
    altura_inicial = float(input("Digite a altura inicial do foguete (em metros): "))
    distancia_inicial = float(input("Digite a distância inicial do foguete (em metros): "))
else:
    angulos = [30, 45, 75, 40, 90]
    velocidade = 20000
    gravidade = 9.87
    altura_inicial = 0
    distancia_inicial = 0

cores = ["red", "blue", "green", "black", "yellow"]

if input("Deseja impor um tempo? Se sim, digite 's': ").lower() == "s":
    tempo_inicial = float(input("Digite o tempo inicial em segundos: "))
    tempo_final = float(input("Digite o tempo final em segundos: "))
    reparticoes = int(input("Quantas repartições? "))
else:
    tempo_inicial = 0
    tempo_final = 0
    reparticoes = 1000

plt.figure(figsize=(10, 6))

maior_distancia = distancia_inicial
maior_altura = altura_inicial
menor_distancia = distancia_inicial
menor_altura = altura_inicial

for i in range(len(angulos)):
    angulo_atual = angulos[i]

    velocidade_x_atual = velocidade * math.cos(math.radians(angulo_atual))
    velocidade_y_atual = velocidade * math.sin(math.radians(angulo_atual))

    discriminante = (
        velocidade_y_atual ** 2
        + 2 * gravidade * altura_inicial
    )

    tempo_voo = (
        velocidade_y_atual + math.sqrt(discriminante)
    ) / gravidade

    if tempo_final == 0:
        tempo_atual_final = tempo_voo
    else:
        tempo_atual_final = min(tempo_final, tempo_voo)

    tempo = np.linspace(
        tempo_inicial,
        tempo_atual_final,
        reparticoes
    )

    altura = (
        altura_inicial
        + velocidade_y_atual * tempo
        - 0.5 * gravidade * tempo ** 2
    )

    distancia = (
        distancia_inicial
        + velocidade_x_atual * tempo
    )

    altura = np.maximum(altura, 0)

    maior_distancia = max(maior_distancia, np.max(distancia))
    menor_distancia = min(menor_distancia, np.min(distancia))
    maior_altura = max(maior_altura, np.max(altura))
    menor_altura = min(menor_altura, np.min(altura))

    plt.plot(
        distancia,
        altura,
        c=cores[i % len(cores)],
        label=f"Ângulo: {angulo_atual}°"
    )

plt.scatter(
    distancia_inicial,
    altura_inicial,
    c="red",
    s=100,
    zorder=5,
    label="Ponto de Lançamento"
)

if input(
    'Deseja impor uma posição de encontro? Se sim, escreva "s": '
).lower() == "s":

    ponto_x = float(
        input("Digite a posição em x do ponto de encontro: ")
    )

    ponto_y = float(
        input("Digite a posição em y do ponto de encontro: ")
    )

    plt.scatter(
        ponto_x,
        ponto_y,
        c="blue",
        s=150,
        marker="*",
        zorder=5,
        label="Ponto de Encontro"
    )

plt.title("Trajetória de Foguetes para Diferentes Ângulos")

margem_x = max((maior_distancia - menor_distancia) * 0.05, 1)
margem_y = max(maior_altura * 0.05, 1)

plt.xlim(
    menor_distancia - margem_x,
    maior_distancia + margem_x
)

plt.ylim(
    max(0, menor_altura - margem_y),
    maior_altura + margem_y
)

plt.xlabel("X (m)")
plt.ylabel("Y (m)")
plt.legend()
plt.grid(True)

plt.show()