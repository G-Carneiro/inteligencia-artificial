# Lista 02 - Prova Automática de Teoremas

**Gabriel Medeiros Lopes Carneiro (19103977)**

**Mikaella Cristina Bernardo Vieira (18103860)**

## 2. Prove os seguintes teoremas utilizando o método da Resolução (lembre-se de negar o teorema):

### a. $(P ∧ (¬Q ∨ R)) → ((P ∧ ¬Q) ∨ (P ∧ R))$

Negando o teorema

$$
\neg ((P \land (\neg Q \lor R)) \to ((P \land \neg Q) \lor (P \land R)))
$$

Eliminando implicação

$$
\neg (\neg (P \land (\neg Q \lor R)) \lor ((P \land \neg Q) \lor (P \land R)))
$$

Redução do escopo das negações

$$
\begin{matrix}
\neg ((\neg P \lor \neg (\neg Q \lor R)) \lor ((P \land \neg Q) \lor (P \land R))) \\ \\
\neg ((\neg P \lor (Q \land \neg R)) \lor ((P \land \neg Q) \lor (P \land R))) \\ \\
\neg (\neg P \lor (Q \land \neg R)) \land \neg ((P \land \neg Q) \lor (P \land R)) \\ \\
(P \land \neg (Q \land \neg R)) \land (\neg (P \land \neg Q) \land \neg (P \land R)) \\ \\
(P \land (\neg Q \lor R)) \land ((\neg P \lor Q) \land (\neg P \lor \neg R)) \\ \\
P \land (\neg Q \lor R) \land (\neg P \lor Q) \land (\neg P \lor \neg R) \\ \\
\end{matrix}
$$

Conjunto $G$:

$$
\begin{array}{ll}
(1)     &   P \\
(2)     &   \neg Q \lor R \\
(3)     &   \neg P \lor Q \\
(4)     &   \neg P \lor \neg R
\end{array}
$$

Resolução:

$$
\begin{array}{lll}
(5)     &   R \lor \neg P   & \text{ de } (2) \text{ e } (3) \\
(6)     &   \neg P          & \text{ de } (5) \text{ e } (4) \\
(7)     &   \square         & \text{ de } (6) \text{ e } (1)
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
\neg (\exists x. (P(x) \land Q(x)) \to (∃ x. P(x) ∧ \exists x. Q(x)))
$$

Eliminando implicação

$$
\neg (\neg (\exists x. (P(x) \land Q(x))) ∨ (∃ x. P(x) ∧ \exists x. Q(x)))
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


### b. $∃x.(P(x) ∧ Q(x)) → (∃x. P(x) ∧ ∃x. Q(x))$


### c. $∀x.(P(x) ∨ Q(x)) → (∃x. P(x) ∨ ∀x. Q(x))$