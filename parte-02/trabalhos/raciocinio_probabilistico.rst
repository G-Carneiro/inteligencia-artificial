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

    .. math::

        \begin{array}{lll}
        P(C_s | G_s) &=& P(C_s) * P(G_s) \\
        &=& 0.68651375 * 0.01019 \\
        &=& 0.006995575
        \end{array}

#. Qual a probabilidade um cartão de crédito ter sido fraudado, dado que houve a compra de créditos para celular, mas não houve a compra de gasolina nas últimas 24 horas? Mostre os cálculos e as probabilidades que você está computando e dê uma resposta numérica.

    .. math::

        \begin{array}{lll}
        P(F_s | C_s, G_n) &=& P(C_s, G_n | F_s) * P(F_s) / P(C_s, G_n) \\
        &=& P(C_s | F_s) * P(G_n | F_s) * P(F_s) / (P(C_s) * P(G_n)) \\
        &=& P(C_s | F_s, I, S) * P(G_n | F_s) * P(F_s) / (P(C_s) * P(G_n)) \\
        &=& 0.00095 * 0.8 * 0.001 / (0.68651375 + (1 - 0.01019)) \\
        &=& 0.76 · 10^{-6} / 1.6763 \\
        &=& 0.453 · 10^{-6}
        \end{array}

Parte 2
=======

#. Modele a situação anterior com uma Rede Bayesiana, indicando as variáveis aleatórias, seus domínios, topologia da rede e tabelas de probabilidade condicionais.

    .. image:: ia.svg
        :width: 70%

    .. math::

        \begin{array}{l|l|l}
        P(A_u) & P(A_s) & P(A_f) \\
        \hline
        0.1 & 0.3 & 0.6
        \end{array}

        \begin{array}{l|l|l}
        & P(C_s) & P(C_n) \\
        \hline
        A_u & 0.6 & 0.4 \\
        \hline
        A_s & 0.8 & 0.2 \\
        \hline
        A_f & 0   & 1
        \end{array}

        \begin{array}{l|l|l}
        & P(V_s) & P(V_n) \\
        \hline
        A_u & 0.8 & 0.2 \\
        \hline
        A_s & 1 & 0 \\
        \hline
        A_f & 0.1 & 0.9
        \end{array}

        \begin{array}{l|l|l}
        & P(E_s) & P(E_n) \\
        \hline
        A_u & 0.5 & 0.5 \\
        \hline
        A_s & 0.5 & 0.5 \\
        \hline
        A_f & 0 & 1
        \end{array}

        \begin{array}{l|l|l}
        & P(P_s) & P(P_n) \\
        \hline
        C_s, E_s & 0.1 & 0.9 \\
        \hline
        C_s, E_n & 0 & 1 \\
        \hline
        C_n, E_s & 0.01 & 0.99 \\
        \hline
        C_n, E_n & 0 & 1
        \end{array}



#. Calcule a probabilidade de um aluno colar.

    .. math::

        \begin{array}{lll}
        P(C_s) &=& P(C_s | A_u) * P(A_u) + P(C_s | A_s) * P(A_s) + P(C_s | A_f) * P(A_f) \\
        &=& 0.6 * 0.1 + 0.8 * 0.3 + 0 * 0.6 \\
        &=& 0.30
        \end{array}

#. Calcule a probabilidade de um aluno frequentar o ensino Secundário dado que ele viu algum colega colando e que se sentiu penalizado na nota.

    .. math::

        \begin{array}{lll}
        P(E_s) &=& P(E_s | A_u) * P(A_u) + P(E_s | A_s) * P(A_s) + P(E_s | A_f) * P(A_f) \\
        &=& 0.5 * 0.1 + 0.5 * 0.3 + 0 * 0.6 \\
        &=& 0.2
        \end{array}

    .. math::

        \begin{array}{lll}
        P(V_s) &=& P(V_s | A_u) * P(A_u) + P(V_s | A_s) * P(A_s) + P(V_s | A_f) * P(A_f) \\
        &=& 0.8 * 0.1 + 1 * 0.3 + 0.1 * 0.6 \\
        &=& 0.44
        \end{array}

    .. math::

        \begin{array}{lll}
        P(P_s) &=&
        P(C_s) * P(E_s) * P(P_s | C_s, E_s) \\
        &&+ P(C_s) * P(E_n) * P(P_s | C_s, E_n) \\
        &&+ P(C_n) * P(E_s) * P(P_s | C_n, E_s) \\
        &&+ P(C_n) * P(E_n) * P(P_s | C_n, E_n) \\
        &=& 0.3 * 0.2 * 0.1 \\
        &&+ 0.3 * 0.8 * 0 \\
        &&+ 0.7 * 0.2 * 0.01 \\
        &&+ 0.7 * 0.8 * 0 \\
        &=& 0.074
        \end{array}

    .. math::

        \begin{array}{lll}
        P(A_s | V_s, P_s) &=& P(V_s, P_s | A_s) * P(A_s) / P(V_s, P_s) \\
        &=& P(A_s) * P(V_s | A_s) * P(P_s | A_s) * P(A_s) / (P(V_s) * P(P_s)) \\
        &=& 0.3 * 1 * 0.074 * 0.3 / (0.44 * 0.074) \\
        &=& 0.204545455
        \end{array}
