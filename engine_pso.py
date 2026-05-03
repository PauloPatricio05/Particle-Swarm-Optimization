import random
from particula import particle

def executar_pso(funcao, inercia_tipo, coop_tipo, n_particulas, dim, max_iter, c1, c2):
    enxame = []
    melhor_fitness_global = float('inf')
    melhor_posicao_global = None
    
    historico_fitness = []
    historico_posicoes = []  # 🔥 CORRETO: criado aqui

    # inicializacao
    for _ in range(n_particulas):
        pos_ini = [random.uniform(-5, 5) for _ in range(dim)]
        vel_ini = [random.uniform(-1, 1) for _ in range(dim)]
        p = particle(pos_ini, vel_ini, pos_ini[:])
        enxame.append(p)

    for t in range(max_iter):

        # inércia
        if inercia_tipo == "1":
            w = 0.7
        else:
            w = 0.9 - (t / max_iter) * 0.5

        # avaliação
        for p in enxame:
            resultado_atual = funcao(p.posicao)

            if resultado_atual < p.melhor_fitness_pessoal:
                p.melhor_fitness_pessoal = resultado_atual
                p.pBest = p.posicao[:]

            if resultado_atual < melhor_fitness_global:
                melhor_fitness_global = resultado_atual
                melhor_posicao_global = p.posicao[:]

        # atualização
        for i in range(n_particulas):
            p = enxame[i]

            if coop_tipo == "1":
                alvo = melhor_posicao_global
            else:
                vizinhos = [enxame[i-1], enxame[i], enxame[(i+1) % n_particulas]]
                campeao_vizinho = vizinhos[0]

                for v in vizinhos:
                    if v.melhor_fitness_pessoal < campeao_vizinho.melhor_fitness_pessoal:
                        campeao_vizinho = v

                alvo = campeao_vizinho.pBest

            for d in range(dim):
                r1, r2 = random.random(), random.random()

                p.velocidade[d] = (
                    w * p.velocidade[d]
                    + c1 * r1 * (p.pBest[d] - p.posicao[d])
                    + c2 * r2 * (alvo[d] - p.posicao[d])
                )

                p.posicao[d] = p.posicao[d] + p.velocidade[d]

        # histórico
        historico_fitness.append(melhor_fitness_global)

        # 🔥 ESSENCIAL PRA ANIMAÇÃO
        historico_posicoes.append([p.posicao[:] for p in enxame])

    return melhor_fitness_global, historico_fitness, historico_posicoes