# Lista 02 - Prova Automática de Teoremas

## 2. Prove os seguintes teoremas utilizando o método da Resolução (lembre-se de negar o teorema):

a. $(P \land (\neg Q \lor R)) \to ((P \land \neg Q) \lor (P \land R))$


    Negando o teorema
    
    $\neg ((P \land (\neg Q \lor R)) \to ((P \land \neg Q) \lor (P \land R)))$
    
    Eliminando implicação
    
    $\neg (\neg (P \land (\neg Q \lor R)) \lor ((P \land \neg Q) \lor (P \land R)))$

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

    Conjunto $G$

    $$
    \begin{matrix}
    (1)     &   P \\
    (2)     &   \neg Q \lor R \\
    (3)     &   \neg P \lor Q \\
    (4)     &   \neg P \lor \neg R
    \end{matrix}
    $$

    Resolução:

    $$
    \begin{array}{lll}
    (5)     &   R \lor \neg P   & \text{ de } (2) \text{ e } (3) \\
    (6)     &   \neg P          & \text{ de } (5) \text{ e } (4) \\
    (7)     &   \square         & \text{ de } (6) \text{ e } (1)
    \end{array}
    $$



    

