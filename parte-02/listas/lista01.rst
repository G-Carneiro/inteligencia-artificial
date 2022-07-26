#. Explique a diferença entre incerteza por aleatoriedade e por imprecisão.

    -  Aleatoriedade: eventos imprevisíveis.
    -  Imprecisão: conceitos mal definidos durante a observação ou pouca
       confiabilidade dos instrumentos usados na observação.
    -  Ignorância: implicação fraca.

#. Considere os conjuntos difusos :math:`A` e :math:`B`, no intervalo :math:`X=[0; 10]` de números reais, definidos pelas funções de pertinência

    .. math::

           A(x) = \dfrac{x}{x + 2} \qquad
           B(x) = 2^{-x}

    #. Represente graficamente os conjuntos difusos :math:`A` e :math:`B`.

    #. Obtenha a função de pertinência (graficamente e matematicamente) para os seguintes conjuntos:

        - :math:`\overline{A}`

        - :math:`\overline{B}`

        - :math:`A ∪ B`

        - :math:`A ∩ B`

        - :math:`\overline{A} ∩ B`

        - :math:`\overline{A} ∪ \overline{B}`

    #. Os conjuntos difusos atendem às leis de Morgan?

#. Qual a diferença entre :math:`α`-cut e strong :math:`α`-cut?

#. Os machos humanos têm um cromossomo X e um cromossomo Y, enquanto as fêmeas têm dois cromossomos X, cada cromossomo sendo herdado de um dos pais.

    A hemofilia é uma doença que apresenta herança recessiva ligada ao cromossomo X, o que significa que um homem que herda o gene que causa a doença no cromossomo X é afetado, enquanto uma fêmea que transporta o gene em somente um de seus dois cromossomos X não é afetada.
    A doença é geralmente fatal para mulheres que herdam dois genes, e isso é muito raro, já que a frequência de ocorrência do gene é reduzida em populações humanas.

    Considere uma mulher que tem um irmão afetado, o que implica que a sua mãe deve ser uma portadora do gene da hemofilia com um “bom” e um “mau” gene da hemofilia.
    Também nos é dito que seu pai não é afetado, assim a própria mulher tem uma chance de 50–50 de ter o gene.
    A variável de interesse desconhecida, o estado da mulher em relação ao gene da hemofilia, tem apenas dois valores: a mulher é uma portadora do gene :math:`(θ = 1)` ou não :math:`(θ = 0)`.
    Com base nas informações fornecidas até agora, a distribuição a “priori” para a variável desconhecida :math:`θ` pode ser expressa simplesmente como :math:`Pr (θ = 1) = Pr (θ = 0) = 1/2`.

    Os dados utilizados para atualizar esta informação prévia consiste no estado dos filhos da mulher.
    Suponhamos que ela tenha tido dois filhos e que nenhum dos dois é afetado pela hemofilia.
    Seja :math:`y_i = 1` ou :math:`0` a maneira de indicar se um filho é afetado ou não pela
    hemofilia.
    Os resultados dos dois filhos são intercambiáveis e, condicionados à variável desconhecida :math:`θ` são independentes.
    Assumimos também que os filhos não são gêmeos idênticos.

    Diga qual a probabilidade da mulher ser portadora do cromossomo da hemofilia :math:`(θ = 1)` sabendo que os filhos não apresentam a doença :math:`Pr(θ=1 ∣ y_1 = 0` e :math:`y_2 = 0)`.

#. Em um grupo de 50 turistas temos as seguintes variáveis descritas abaixo:


============= ========= ========
Nacionalidade Masculino Feminino
============= ========= ========
Brasileira    20        15
Estrangeira   5         10
============= ========= ========

Ao selecionar aleatoriamente uma pessoa do grupo obtenha as
probabilidades de ocorrência dos seguintes eventos:

- O turista é brasileiro.


.. math::

    35 / 50

- O turista é estrangeiro.

.. math::

    15 / 50

- O turista é masculino.

.. math::

    25 / 50

- O turista é feminino.

.. math::

    25 / 50

- O turista é feminino e brasileiro.

.. math::

    15 / 50

- O turista é feminino e estrangeiro.

.. math::

    10 / 50

- O turista é masculino e brasileiro.

.. math::

    20 / 50

- O turista é masculino e estrangeiro.

.. math::

    5 / 50

- O turista é feminino ou brasileiro.

.. math::

   25 / 50 + 35 / 50 - 15 / 50 \\
   45 / 50

- O turista é feminino ou estrangeiro.

.. math::

   25 / 50 + 15 / 50 - 10 / 50 \\
   30 / 50

- O turista é masculino ou brasileiro.

.. math::

   25 / 50 + 35 / 50 - 20 / 50 \\
   40 / 50

- O turista é masculino ou estrangeiro.

.. math::

   25 / 50 + 15 / 50 - 5 / 50 \\
   35 / 50

- O turista ser masculino se é brasileiro.

.. math::

   P(T_m | T_b) &=& P(T_m, T_b) / P(T_b) \\
   &=& (20 / 50) / (35 / 50) \\
   &=& 20 / 35
