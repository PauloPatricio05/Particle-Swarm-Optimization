import random
# Define a classe Particle (posição, velocidade, pBest)
# Rascunho: w : Fator de inéricia, v = velocidade atual da partícula;
# c1 = fator cognitivo, puxa a partícula para o seu melhor resultado pessoal;
# c2 = fator social, puxa a partícula para o melhor resultado do grupo;
# r1 e r2 = números aleatórios entre 0 e 1;

class particle:

    def __init__(self,posicao,velocidade,pBest):
        self.posicao = posicao
        self.velocidade = velocidade
        self.pBest = pBest
    
    def nova_velocidade(self, w, c1,c2, gBest):
        r1 = random.random()
        r2 = random.random()

        self.velocidade = (w * self.velocidade + c1 * r1 * (self.pBest - self.posicao) + c2 * r2 * (gBest - self.posicao))

    def nova_posicao(self):
        self.posicao = self.posicao + self.velocidade