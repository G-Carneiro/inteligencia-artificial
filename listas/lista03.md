---
header-includes:
    - \usepackage[edges]{forest}
    - \usepackage{adjustbox}
---

# Lista 03 - Algoritmo de Busca A$^*$

**Gabriel Medeiros Lopes Carneiro (19103977)**

**Mikaella Cristina Bernardo Vieira (18103860)**

## 1. Aplique o algoritmo A$^∗$ para determinar a rota de A até R

\newcommand{\newnode}[6]{
#1 \color{blue}(#5) \\ \color{olive}#3 + \color{purple}#4, align=center, edge label = {node[midway, above #6]{#2}}
}

[//]: # (\newnode{nome}{distância entre nós}{g(n)}{h(n)}{f(n) = g(n) + h(n)}{posição na aresta [left | right]})

$$
\begin{adjustbox}{width=\textwidth}
\begin{forest}
    forked edges, for tree={l sep+= 15pt, s sep+= 15pt, fork sep = 15pt}
    [A \color{blue}(240) \\ \color{olive}0 + \color{purple}240, align=center
        [\newnode{B}{73}{73}{186}{259}{left}%
            [\newnode{A}{73}{146}{240}{386}{left}]
            [\newnode{K}{83}{156}{122}{278}{left}]
        ] 
        [\newnode{C}{64}{64}{182}{246}{left}%
            [\newnode{A}{64}{128}{240}{368}{left}]
            [\newnode{I}{64}{128}{120}{248}{left}%
                [\newnode{C}{64}{192}{182}{374}{left}]
                [\newnode{F}{31}{159}{150}{309}{left}]
                [\newnode{L}{28}{156}{104}{260}{left}%
                    [\newnode{H}{36}{192}{139}{331}{left}]
                    [\newnode{I}{28}{156}{120}{276}{left}]
                    [\newnode{P}{63}{219}{65}{284}{left}]
                ]
                [\newnode{M}{20}{148}{100}{248}{left}%
                    [\newnode{I}{20}{168}{120}{288}{left}]
                    [\newnode{O}{50}{198}{72}{270}{left}%
                        [\newnode{M}{50}{148}{198}{346}{left}]
                        [\newnode{P}{41}{239}{65}{304}{left}]
                        [\newnode{R}{50}{248}{0}{248}{left}]
                    ]
                ]
            ]
        ]
        [\newnode{D}{89}{89}{163}{252}{left}%
            [\newnode{A}{89}{178}{240}{418}{left}]
            [\newnode{N}{89}{178}{77}{255}{left}%
                [\newnode{D}{89}{267}{163}{430}{left}]
                [\newnode{F}{84}{262}{150}{412}{left}]
                [\newnode{J}{53}{231}{130}{361}{left}]
            ]
        ] 
        [\newnode{E}{104}{104}{170}{274}{left}] 
    ]
\end{forest}
\end{adjustbox}
$$

- Ordem de "abertura" dos nós: $A → C → I → M → D → N → B → L → O$.
  - A:
    - Abertos: B, C, D, E
    - Fechados: A
  - C:
    - Abertos: B, D, E, I
    - Fechados: A, C 
  - I:
    - Abertos: B, D, E, F, L, M
    - Fechados: A, C, I
  - M:
    - Abertos: B, D, E, F, L, O
    - Fechados: A, C, I, M
  - D:
    - Abertos: B, E, F, L, N, O
    - Fechados: A, C, D, I, M
  - N:
    - Abertos: B, E, F, J, L, O
    - Fechados: A, C, D, I, M, N
  - B:
    - Abertos: E, F, J, K, L, O
    - Fechados: A, B, C, D, I, M, N
  - L:
    - Abertos: E, F, H, J, K, O, P
    - Fechados: A, B, C, D, I, L, M, N
  - O:
    - Abertos: E, F, H, J, K, P, R
    - Fechados: A, B, C, D, I, L, M, N, O
- Rota de A até R: $A → C → I → M → O → R$.
- Distância: 248.