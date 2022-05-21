# Lista 02 - Prova Automática de Teoremas

**Gabriel Medeiros Lopes Carneiro (19103977)**

**Mikaella Cristina Bernardo Vieira (18103860)**

## 1. Prove algo referente a lista 1.


Seja `SerialKiller(x) = SK(x)`, `Apelido(x, y) = A(x, y)` e `TotaldeVitimas(x, z) = TV(x, z)`, onde `x` representa o serial killer, `y` o seu apelido e `z` o número de vítimas.

Do texto, sabe-se que conjunto $G$ é:

$$
\begin{array}{ll}
(1)     &   \text{SK(Albert\_Fish)}                 \\
(2)     &   \text{A(Albert\_Fish, Maniaco\_da\_Lua)} \\
(3)     &   \text{TV(Albert\_Fish, 15)}             \\
\end{array}
$$

Provaremos que Albert Fish é um serial killer que matou 15 vítimas, e cujo apelido era Maníaco da Lua.
Logo,

$$
W = \text{SK(Albert\_Fish)} ∧ \text{A(Albert\_Fish, Maniaco\_da\_Lua)} ∧ \text{TV(Albert\_Fish, 15)}
$$

Negando $W$:

$$
\begin{matrix}
¬(\text{SK(Albert\_Fish)} ∧ \text{A(Albert\_Fish, Maniaco\_da\_Lua)} ∧ \text{TV(Albert\_Fish, 15)}) \\ \\
¬\text{SK(Albert\_Fish)} ∨ ¬\text{A(Albert\_Fish, Maniaco\_da\_Lua)} ∨ ¬\text{TV(Albert\_Fish, 15)}
\end{matrix}
$$

Tem-se $H = G ∪ \{¬W\}$:

$$
\begin{array}{ll}
(1)     &   \text{SK(Albert\_Fish)}                     \\
(2)     &   \text{A(Albert\_Fish, Maniaco\_da\_Lua)}    \\
(3)     &   \text{TV(Albert\_Fish, 15)}                 \\
(4)     &   ¬\text{SK(Albert\_Fish)} ∨ ¬\text{A(Albert\_Fish, Maniaco\_da\_Lua)} ∨ ¬\text{TV(Albert\_Fish, 15)}
\end{array}
$$


Resolução:

$$
\begin{array}{lll}
(5)     &   ¬\text{A(Albert\_Fish, Maniaco\_da\_Lua)} ∨ ¬\text{TV(Albert\_Fish, 15)}    &   \text{de (1) e (4)} \\
(6)     &   ¬\text{TV(Albert\_Fish, 15)}    &   \text{de (2) e (5)} \\
(7)     &   \square   & \text{de (3) e (6)}
\end{array}
$$

## 2. Prove os seguintes teoremas utilizando o método da Resolução (lembre-se de negar o teorema):

### a. $(P ∧ (¬Q ∨ R)) → ((P ∧ ¬Q) ∨ (P ∧ R))$

Negando o teorema

$$
¬((P ∧ (¬Q ∨ R)) → ((P ∧ ¬Q) ∨ (P ∧ R)))
$$

Eliminando implicação

$$
¬(¬(P ∧ (¬Q ∨ R)) ∨ ((P ∧ ¬Q) ∨ (P ∧ R)))
$$

Redução do escopo das negações

$$
\begin{matrix}
¬((¬P ∨ ¬(¬Q ∨ R)) ∨ ((P ∧ ¬Q) ∨ (P ∧ R))) \\ \\
¬((¬P ∨ (Q ∧ ¬R)) ∨ ((P ∧ ¬Q) ∨ (P ∧ R))) \\ \\
¬(¬P ∨ (Q ∧ ¬R)) ∧ ¬((P ∧ ¬Q) ∨ (P ∧ R)) \\ \\
(P ∧ ¬(Q ∧ ¬R)) ∧ (¬(P ∧ ¬Q) ∧ ¬(P ∧ R)) \\ \\
(P ∧ (¬Q ∨ R)) ∧ ((¬P ∨ Q) ∧ (¬P ∨ ¬R)) \\ \\
P ∧ (¬Q ∨ R) ∧ (¬P ∨ Q) ∧ (¬P ∨ ¬R) \\ \\
\end{matrix}
$$

Conjunto $G$:

$$
\begin{array}{ll}
(1)     &   P \\
(2)     &   ¬Q ∨ R \\
(3)     &   ¬P ∨ Q \\
(4)     &   ¬P ∨ ¬R
\end{array}
$$

Resolução:

$$
\begin{array}{lll}
(5)     &   R ∨ ¬P      & \text{de (2) e (3)} \\
(6)     &   ¬P          & \text{de (5) e (4)} \\
(7)     &   \square     & \text{de (6) e (1)}
\end{array}
$$

### b. $∃x.∀y. P(x, y) → ∀y.∃x. P(x, y)$

Negando o teorema

$$
¬(∃x.∀y. P(x, y) → ∀y.∃x. P(x, y))
$$

Eliminando a implicação

$$
¬(¬(∃x.∀y. P(x, y)) ∨ ∀y.∃x. P(x, y))
$$

Redução do escopo das negações

$$
\begin{matrix}
¬¬(∃x.∀y. P(x, y)) ∧ ¬(∀y.∃x. P(x, y)) \\ \\
∃x.∀y. P(x, y) ∧ ¬(∀y.∃x. P(x, y)) \\ \\
∃x.∀y. P(x, y) ∧ ∃y.¬(∃x. P(x, y)) \\ \\
∃x.∀y. P(x, y) ∧ ∃y.∀x. ¬P(x, y)
\end{matrix}
$$

Renomeação das variáveis

$$
∃x_1.∀y_1. P(x_1, y_1) ∧ ∃y_2.∀x_2. ¬P(x_2, y_2)
$$

Eliminação dos quantificadores

$$
P(a, y_1) ∧ ¬P(x_2, b)
$$

Conjunto $G$:

$$
\begin{array}{ll}
(1)     &   P(a, y_1)   \\
(2)     &   ¬P(x_2, b) 
\end{array}
$$

Resolução:

$$
\begin{array}{lll}
(3)     &   \square     &   \text{de (1) e (2) com } θ: \{x_2/a, y_1/b\}    
\end{array}
$$

### c. $∃x. (P(x) ∧ Q(x)) → (∃x. P(x) ∧ ∃x. Q(x))$

Negando o teorema

$$
¬(∃x. (P(x) ∧ Q(x)) → (∃x. P(x) ∧ ∃x. Q(x)))
$$

Eliminando implicação

$$
¬(¬(∃x. (P(x) ∧ Q(x))) ∨ (∃x. P(x) ∧ ∃x. Q(x)))
$$

Redução do escopo das negações

$$
\begin{matrix}
¬(∀x. ¬(P(x) ∧ Q(x)) ∨ (∃x. P(x) ∧ ∃x. Q(x))) \\ \\
¬(∀x. (¬P(x) ∨ ¬Q(x)) ∨ (∃x. P(x) ∧ ∃x. Q(x))) \\ \\
¬(∀x. (¬P(x) ∨ ¬Q(x))) ∧ ¬(∃x. P(x) ∧ ∃x. Q(x)) \\ \\
∃x. ¬(¬P(x) ∨ ¬Q(x)) ∧ (¬(∃x. P(x)) ∨ ¬(∃x. Q(x))) \\ \\
∃x. (P(x) ∧ Q(x)) ∧ (∀x. ¬P(x) ∨ ∀x. ¬Q(x))
\end{matrix}
$$

Renomeação das variáveis    

$$
∃x_1. (P(x_1) ∧ Q(x_1)) ∧ (∀x_2. ¬P(x_2) ∨ ∀x_3. ¬Q(x_3))
$$

Mover quantificadores para o início da fórmula

$$
∃x_1.∀x_2.∀x_3. P(x_1) ∧ Q(x_1) ∧ (¬P(x_2) ∨ ¬Q(x_3))
$$

Eliminação dos quantificadores

$$
P(a) ∧ Q(a) ∧ (¬P(x_2) ∨ ¬Q(x_3))
$$

Conjunto $G$:

$$
\begin{array}{ll}
(1)     &   P(a)                \\
(2)     &   Q(a)                \\
(3)     &   ¬P(x_2) ∨ ¬Q(x_3) 
\end{array}
$$

Resolução:

$$
\begin{array}{lll}
(4)     &   ¬Q(x_3)   &   \text{de (1) e (3) com } θ: \{x_2 / a\} \\
(5)     &   \square   &   \text{de (2) e (4) com } θ: \{x_3/a\}
\end{array}
$$

## 3. Prove os seguintes teoremas utilizando o método de Tableaux (lembre-se denegar o teorema):

### a. $(P ∨ ¬Q) → ¬(P → Q)$

$$
\begin{array}{lllll}
(1) &   ¬((P ∨ ¬Q) → ¬(P → Q))  &       &           &   \text{Negando o teorema}\\
(2) &   P ∧ ¬Q                  &       &           &   \text{de (1) R.C. } →   \\
(3) &   P → Q                   &       &           &   \text{de (1) R.C. } →   \\
(4) &   P                       &       &           &   \text{de (2) R.C. } ∧   \\
(5) &   ¬Q                      &       &           &   \text{de (2) R.C. } ∧   \\
(6) &   ¬P                      &   ∣   &   Q       &   \text{de (3) R.D. } →   \\
(7) &   \square                 &   ∣   &   \square &   \text{de (4), (5) e (6)}
\end{array}
$$

### b. $∃x.(P(x) ∧ Q(x)) → (∃x.P(x) ∧ ∃x.Q(x))$

$$
\begin{array}{lllll}
(1) &   ¬(∃x.(P(x) ∧ Q(x)) → (∃x.P(x) ∧ ∃x.Q(x)))   &       &           &   \text{Negando o teorema}        \\
(2) &   ∃x.(P(x) ∧ Q(x))                            &       &           &   \text{de (1) R.C. } →           \\
(3) &   ¬(∃x.P(x) ∧ ∃x.Q(x))                        &       &           &   \text{de (1) R.C. } →           \\
(4) &   P(π) ∧ Q(π)                                 &       &           &   \text{de (2) R.E. } θ: \{x/π\}  \\
(5) &   P(π)                                        &       &           &   \text{de (4) R.C. } ∧           \\
(6) &   Q(π)                                        &       &           &   \text{de (4) R.C. } ∧           \\
(7) &   ¬∃x.P(x)                                    &   ∣   &   ¬∃x.Q(x)&   \text{de (3) R.D. } ∧           \\
(8) &   ¬P(π)                                       &   ∣   &   ¬Q(π)   &   \text{de (7) R.E. } θ: \{x/π\}  \\
(9) &   \square                                     &   ∣   &   \square &   \text{de (5), (6) e (8)}
\end{array}
$$

### c. $∀x.(P(x) ∨ Q(x)) → (∃x.P(x) ∨ ∀x.Q(x))$

$$
\begin{array}{lllll}
(1) &   ¬(∀x.(P(x) ∨ Q(x)) → (∃x.P(x) ∨ ∀x.Q(x)))   &       &           &   \text{Negando o teorema}            \\
(2) &   ∀x.(P(x) ∨ Q(x))                            &       &           &   \text{de (1) R.C. } →               \\
(3) &   ¬(∃x.P(x) ∨ ∀x.Q(x))                        &       &           &   \text{de (1) R.C. } →               \\
(4) &   ¬∃x.P(x)                                    &       &           &   \text{de (3) R.C. } ∨               \\
(5) &   ¬∀x.Q(x)                                    &       &           &   \text{de (3) R.C. } ∨               \\
(6) &   ¬P(t)                                       &       &           &   \text{de (4) R.E. } θ: \{x/t\}      \\
(7) &   ¬Q(t)                                       &       &           &   \text{de (5) R.U. } θ: \{x/t\}      \\
(8) &   P(t) ∨ Q(t)                                 &       &           &   \text{de (2) R.U. } θ: \{x/t\}      \\
(9) &   P(t)                                        &   ∣   &   Q(t)    &   \text{de (8) R.D. } ∨   \\
(10)&   \square                                     &   ∣   &   \square &   \text{de (6), (7) e (9)}
\end{array}
$$
