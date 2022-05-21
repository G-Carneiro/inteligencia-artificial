---
header-includes:
    - \usepackage{forest}
---

# Lista 03 - Algoritmo de Busca A*

**Gabriel Medeiros Lopes Carneiro (19103977)**

**Mikaella Cristina Bernardo Vieira (18103860)**

## 1.

\newcommand{\newnode}[6]{
#1 \color{blue}(#5) \\ \color{olive}#3 + \color{purple}#4, align=center, edge label = {node[midway, #6]{#2}}
}

[//]: # (\newnode{nome}{distância entre nós}{g(n)}{h(n)}{f(n) = g(n) + h(n)}{posição na aresta [left | right]})

$$
\begin{forest}
    [A \color{blue}(240) \\ \color{olive}0 + \color{purple}240, align=center
        [\newnode{B}{73}{73}{186}{259}{left}] 
        [\newnode{C}{64}{64}{182}{246}{left}%
            [\newnode{I}{64}{128}{120}{248}{left}%
                [\newnode{F}{31}{159}{150}{309}{left}]
                [\newnode{L}{28}{156}{104}{260}{left}]
                [\newnode{M}{20}{148}{100}{248}{left}%
                    [\newnode{O}{50}{198}{72}{270}{left}]
                ]
            ]
        ] 
        [\newnode{D}{89}{89}{163}{252}{left}%
            [\newnode{N}{89}{178}{77}{255}{left}%
                [\newnode{F}{84}{262}{150}{412}{left}]
                [\newnode{J}{53}{231}{130}{361}{left}]
            ]
        ] 
        [\newnode{E}{104}{104}{170}{274}{left}] 
    ]
\end{forest}
$$