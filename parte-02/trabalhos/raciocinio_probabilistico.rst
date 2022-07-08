============================================
Trabalho Prático - Raciocínio Probabilístico
============================================

**Gabriel Medeiros Lopes Carneiro (19103977)**

**Mikaella Cristina Bernardo Vieira (18103860)**

Parte 1
=======

#. Qual é a probabilidade de ter NÃO haver uma compra de gasolina dado que o cartão foi fraudado? Mostre os cálculos e as probabilidades que você está computando e dê uma resposta numérica.

    .. math::

        P(G_n | F_s) = 80 / 100 = 0.8

#. Qual a probabilidade do mundo estar no seguinte estado: (F=sim, G=sim, I>50, S=fem, C=não)? Mostre os cálculos e as probabilidades que você está computando e dê uma resposta numérica.

    Como

    .. math::

        P(F_s, G_s, I_{>50}, S_f, C_n) = P(F_s) * P(G_s | F_s) * P(I_{>50}) * P(S_f) * P(C_n | F_s, I_{>50}, S_f)

    precisamos calcular cada uma dessas probabilidades.

    .. math::

        P(F_s)                      &=& 0.001   \\
        P(G_s | F_s)                &=& 0.2     \\
        P(I_{>50})                  &=& 0.35    \\
        P(S_f)                      &=& 0.5     \\
        P(C_n | F_s, I_{>50}, S_f)  &=& 0.05

    Logo,

    .. math::

        P(F_s, G_s, I_{>50}, S_f, C_n) &=& 0.001 * 0.2 * 0.35 * 0.5 * 0.05 \\
        &=& 0.00000175 \\
        &=& 0.175 · 10^{-5}


#. Qual a probabilidade de haver uma compra de gasolina nas últimas 24 horas? Mostre os cálculos e as probabilidades que você está computando e dê uma resposta numérica.

    .. math::

        P(G_s) &=& P(F_s) * P(G_s | F_s) + P(F_n) * P(G_s | F_n) \\
        &=& 0.001 * 0.2 + 0.999 * 0.01 \\
        &=& 0.01019


#. Qual a probabilidade de haver uma compra de créditos para celular nas últimas 24 horas? Mostre os cálculos e as probabilidades que você está computando e dê uma resposta numérica.

    .. math::

        \begin{array}{lll}
        P(C_s) &=&
        P(C_s | F_s, I_{<30}, S_m) * P(F_s) * P(I_{<30}) * P(S_m) \\
        && + P(C_s | F_s, I_{<30}, S_f) * P(F_s) * P(I_{<30}) * P(S_f) \\
        && + P(C_s | F_s, I_{≤30 ≤ 50}, S_m) * P(F_s) * P(I_{≤30 ≤ 50}) * P(S_m) \\
        && + P(C_s | F_s, I_{≤30 ≤ 50}, S_f) * P(F_s) * P(I_{≤30 ≤ 50}) * P(S_f) \\
        && + P(C_s | F_s, I_{>50}, S_m) * P(F_s) * P(I_{>50}) * P(S_m) \\
        && + P(C_s | F_s, I_{>50}, S_f) * P(F_s) * P(I_{>50}) * P(S_f) \\
        && + P(C_s | F_n, I_{<30}, S_m) * P(F_n) * P(I_{<30}) * P(S_m) \\
        && + P(C_s | F_n, I_{<30}, S_f) * P(F_n) * P(I_{<30}) * P(S_f) \\
        && + P(C_s | F_n, I_{≤30 ≤ 50}, S_m) * P(F_n) * P(I_{≤30 ≤ 50}) * P(S_m) \\
        && + P(C_s | F_n, I_{≤30 ≤ 50}, S_f) * P(F_n) * P(I_{≤30 ≤ 50}) * P(S_f) \\
        && + P(C_s | F_n, I_{>50}, S_m) * P(F_n) * P(I_{>50}) * P(S_m) \\
        && + P(C_s | F_n, I_{>50}, S_f) * P(F_n) * P(I_{>50}) * P(S_f) \\
        \\
        &=& 0.95 * 0.001 * 0.25 * 0.5 \\
        &&+ 0.95 * 0.001 * 0.25 * 0.5 \\
        &&+ 0.95 * 0.001 * 0.40 * 0.5 \\
        &&+ 0.95 * 0.001 * 0.40 * 0.5 \\
        &&+ 0.95 * 0.001 * 0.35 * 0.5 \\
        &&+ 0.95 * 0.001 * 0.35 * 0.5 \\
        &&+ 0.80 * 0.999 * 0.25 * 0.5 \\
        &&+ 0.75 * 0.999 * 0.25 * 0.5 \\
        &&+ 0.75 * 0.999 * 0.40 * 0.5 \\
        &&+ 0.75 * 0.999 * 0.40 * 0.5 \\
        &&+ 0.50 * 0.999 * 0.35 * 0.5 \\
        &&+ 0.60 * 0.999 * 0.35 * 0.5 \\
        \\
        &=& 0.5 [0.95 * 0.001 * 2 * (0.25 + 0.40 + 0.35) \\
        &&+ 0.999 (0.80 * 0.25 + 0.75 * 0.25 + 2 * 0.75 * 0.40 + 0.50 * 0.35 + 0.60 * 0.35) ] \\
        \\
        &=& 0.5 [0.95 * 0.002 + 0.999 * 1.3725] \\
        &=& 0.68651375
        \end{array}


#. Qual a probabilidade de haver uma compra de créditos para celular nas últimas 24 horas, dado que a houve a compra de gasolina? Mostre os cálculos e as probabilidades que você está computando e dê uma resposta numérica.

#. Qual a probabilidade um cartão de crédito ter sido fraudado, dado que houve a compra de créditos para celular, mas não houve a compra de gasolina nas últimas 24 horas? Mostre os cálculos e as probabilidades que você está computando e dê uma resposta numérica.

Parte 2
=======

#. Modele a situação anterior com uma Rede Bayesiana, indicando as variáveis aleatórias, seus domínios, topologia da rede e tabelas de probabilidade condicionais.

#. Calcule a probabilidade de um aluno colar.

#. Calcule a probabilidade de um aluno frequentar o ensino Secundário dado que ele viu algum colega colando e que se sentiu penalizado na nota.