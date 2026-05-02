import random

# definição da classe particle (posição, velocidade, pbest)
class particle:
    def __init__(self, posicao, velocidade, pBest):
        # usamos [:] para criar uma cópia dos valores da lista
        self.posicao = posicao[:]
        self.velocidade = velocidade[:]
        self.pBest = pBest[:]
        # inicializamos o melhor fitness como infinito para a primeira comparação
        self.melhor_fitness_pessoal = float('inf')