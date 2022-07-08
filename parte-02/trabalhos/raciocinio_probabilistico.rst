============================================
Trabalho Prático - Raciocínio Probabilístico
============================================

**Gabriel Medeiros Lopes Carneiro (19103977)**

**Mikaella Cristina Bernardo Vieira (18103860)**

Parte 1
=======

#. Qual é a probabilidade de ter NÃO haver uma compra de gasolina dado que o cartão foi fraudado? Mostre os cálculos e as probabilidades que você está computando e dê uma resposta numérica.

    P(G=n | F=s) = 80 / 100 = 0.8

#. Qual a probabilidade do mundo estar no seguinte estado: (F=sim, G=sim, I>50, S=fem, C=não)? Mostre os cálculos e as probabilidades que você está computando e dê uma resposta numérica.

    Como

    .. math::

        P(\text{F=s, G=s, I>50, S=f, C=n}) = P(\text{F=s}) * P(\text{G=s | F=s}) \\
        * P(\text{I>50}) * P(\text{S=f}) * P(\text{C=n | F=s, I>50, S=f})

    precisamos calcular cada uma dessas probabilidades.

    - P(F=s) = 0.1
    - P(G=s | F=s) = 0.2
    - P(I>50) = 0.35
    - P(S=f) = 0.5
    - P(C=n | F=s, I>50, S=f) = 0.05

    Logo,

    .. math::

        P(\text{F=s, G=s, I>50, S=f, C=n}) = 0.1 * 0.2 * 0.35 * 0.5 * 0.05 = 0.000175


#. Qual a probabilidade de haver uma compra de gasolina nas últimas 24 horas? Mostre os cálculos e as probabilidades que você está computando e dê uma resposta numérica.

    P(G=s) = (20 + 1) / (20 + 1 + 80 + 99) = 0.105

#. Qual a probabilidade de haver uma compra de créditos para celular nas últimas 24 horas? Mostre os cálculos e as probabilidades que você está computando e dê uma resposta numérica.

#. Qual a probabilidade de haver uma compra de créditos para celular nas últimas 24 horas, dado que a houve a compra de gasolina? Mostre os cálculos e as probabilidades que você está computando e dê uma resposta numérica.

#. Qual a probabilidade um cartão de crédito ter sido fraudado, dado que houve a compra de créditos para celular, mas não houve a compra de gasolina nas últimas 24 horas? Mostre os cálculos e as probabilidades que você está computando e dê uma resposta numérica.

Parte 2
=======

#. Modele a situação anterior com uma Rede Bayesiana, indicando as variáveis aleatórias, seus domínios, topologia da rede e tabelas de probabilidade condicionais.

#. Calcule a probabilidade de um aluno colar.

#. Calcule a probabilidade de um aluno frequentar o ensino Secundário dado que ele viu algum colega colando e que se sentiu penalizado na nota.