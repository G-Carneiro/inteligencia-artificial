# Lista 01 - Representação de Conhecimento

**Gabriel Medeiros Lopes Carneiro (19103977)**

**Mikaella Cristina Bernardo Vieira (18103860)**

## 1. Apresente o texto usado

[//]: # (Uma vez que o termo “serial killer” foi inventado para descrever um tipo específico de criminoso, mas o termo é cercado de confusão. Nem os especialistas estão de acordo. )

[//]: # (Então vamos começar com a definição do FBI &#40;**Três ou mais eventos separados em três ou mais locais distintos com período de “calmaria” entre os homicídios**&#41;.)

[//]: # (Essa definição enfatiza três elementos: a quantidade &#40;onde tem de haver pelo menos três homicídios&#41;, o lugar &#40;Os assassinatos têm que ocorrer em locais diferentes&#41; e o tempo &#40;tem de haver um “período de calmaria” - um intervalo entre os assassinatos que pode durar algumas horas a vários anos&#41;.)

Talvez o horror pudesse ter sido evitado.
Certamente, sinais de alerta apareceram ao longo do caminho - sinais de que havia algo de errado com Jeffrey Dahmer. 
Algo de muito errado.
Dahmer, em meio ao ambiente de briga entre seus pais, se isolava cada vez mais em seu mundinho e passou adotar um passatempo único: matar animais, e ao longo dos anos ele foi se entregando mais à bebida e as suas fantasias obsessivas sobre assassinatos. 
Até que ele fez sua primeira vítima, uma rapaz jovem que ele levou para a sua casa e quando o rapaz anunciou que iria embora, Dahmer deu fim a vida dele, e a partir daí Jeffrey Dahmer fez muito mais vítimas. 
Até o momento em que ele foi descoberto e a polícia ficou horrorizada com o que descobriu. 
Dahmer guardava partes de suas vítimas para consumo próprio posteriormente e a polícia encontrou um total de 11 restos de mortais, mas Dahmer confessou mais tarde ter matado um total de 17 vítimas. 
Dahmer ficou conhecido como o canibal de Milwaukee.

Entre os psicopatas mais abomináveis, Albert Fish foi umas das figuras que mais se destacou pelos inúmeros atos monstruosos que ele praticou. 
Para começar, ele era um pedófilo crônico e, além disso, um sádico e masoquista e ele ainda tinha algumas outras parafilias muito bizarras. 
Suas vítimas eram crianças e até hoje ninguém sabe o número preciso das vítimas de Fish, mas parece ao certo que ele molestou várias centenas e assassinou pelo menos 15. 
E de muitos nomes que ele ficou conhecido, um deles foi maníaco da lua.

Em 1978 um vizinho de John Wayne Gacy chamou a polícia ao escutar gritos vindo de trás de sua casa, após a polícia questionar o dono eles foram embora convencidos de que não havia nada de errado. 
Mas um menino de 15 anos desapareceu e as investigações feitas pela polícia chegaram de novo em John Wayne Gacy que foi detido e ao se investigar a sua casa encontraram muitos itens pessoais, que claramente não pertenciam a Gacy e ao descerem no subsolo da casa encontraram nauseantes indícios de crimes hediondos. 
Gacy quando confrontado confessou as atrocidades que o marcaria como um dos serial killers mais monstruosos dos EUA, onde ele torturou e assassinou 33 garotos ao longo de um período de 6 anos. 
Gacy ficou conhecido como o palhaço assassino.

Ela era um tipo raro de psicopata: uma mulher que matava de forma indiscriminada, em parte por ganância, mas principalmente, pelo puro prazer de matar. 
Ainda mais raro era a extrema selvageria de seus crimes, já que em geral mulheres psicopatas costumam ter um modus operandi mais tradicional como o envenenamento. 
Belle Gunness era assustadoramente diferente.
Claro, ela não hesitaria em matar um cônjuge dispensável ou uma criança supérflua com uma dose de estricnina quando conveniente. 
Mas, em geral, suas vítimas foram violentamente assassinadas e a maioria era seus maridos, onde alguns desses eram atraídos por anúncios em jornais que Belle Guinness fez procurando homens para casar e outras vítimas incluíam crianças, como, por exemplo, a filha de um dos maridos que foi encontrada morta.
Não se sabe ao certo o número de vítimas de Belle Gunness, alguns dizem que foram 10 vítimas, já outros dizem que foram 42, é difícil dizer, mas o que se sabe é que não foram poucos. 
Ela ficou conhecida na época como lady barba azul.

**Referência:**  Livro Serial Killers Anatomia do Mal - Harold Schechter.


## 2. Apresente a representação feita em cada uma das técnicas

### Lógica

```prolog

SerialKiller(Jeffrey_Dahmer).
SerialKiller(Albert_Fish).
SerialKiller(John_Wayne_Gacy).
SerialKiller(Belle_Gunness).

Apelido(Jeffrey_Dahmer, Canibal_de_Milwaukee).
Apelido(Albert_Fish, Maniaco_da_Lua).
Apelido(John_Wayne_Gacy, Palhaco_Assassino).
Apelido(Belle_Gunness, Lady_Barba_Azul).

TotaldeVitimas(Jeffrey_Dahmer, 17).
TotaldeVitimas(Albert_Fish, 15).
TotaldeVitimas(John_Wayne_Gacy, 33).

MinimodeVitimas(Belle_Gunness, 10).
MaximodeVitimas(Belle_Gunness, 42).

TipodeVitimas(Jeffrey_Dahmer, garotos_jovens). 
TipodeVitimas(Albert_Fish, criancas). 
TipodeVitimas(John_Wayne_Gacy, garotos_jovens). 
TipodeVitimas(Belle_Gunness, maridos_e_crianças).

Caracteristica(Jeffrey_Dahmer, canibal). 
Caracteristica(Albert_Fish, pedofilo_cronico). 
Caracteristica(John_Wayne_Gacy, torturador). 
Caracteristica(Belle_Gunness, extremamente_selvagem).
```

### Redes Semânticas

**Obs:** representaremos os arcos com texto em **negrito**.

- Jeffrey_Dahmer **is a** SerialKiller.
- Albert_Fish **is a** SerialKiller.
- John_Wayne_Gacy **is a** SerialKiller.
- Belle_Gunness **is a** SerialKiller.
- Jeffrey_Dahmer **Apelido** Canibal_de_Milwaukee.
- Albert_Fish **Apelido** Maniaco_da_Lua.
- John_Wayne_Gacy **Apelido** Palhaco_Assassino.
- Belle_Gunness **Apelido** Lady_Barba_Azul.
- Jeffrey_Dahmer **TotaldeVitimas** 17.
- Albert_Fish **TotaldeVitimas** 15.
- John_Wayne_Gacy **TotaldeVitimas** 33.
- Belle_Gunness **MinimodeVitimas** 10.
- Belle_Gunness **MaximodeVitimas** 42.
- Jeffrey_Dahmer **TipodeVitimas** garotos_jovens.
- Albert_Fish **TipodeVitimas** crianças.
- John_Wayne_Gacy **TipodeVitimas** garotos_jovens.
- Belle_Gunness **TipodeVitimas** maridos_e_crianças.
- Jeffrey_Dahmer **Caracteristica** canibal.
- Albert_Fish **Caracteristica** pedofilo_cronico.
- John_Wayne_Gacy **Caracteristica** torturador.
- Belle_Gunness **Caracteristica** extremamente_selvagem.


### Quadros (Frames)

```
(Jeffrey_Dahmer
    <:INSTANCE-OF SerialKiller>
    <:Apelido Canibal_de_Milwaukee>
    <:TotaldeVitimas 17>
    <:TipodeVitimas garotos_jovens>
    <:Caracteristica canibal>
)
(Albert_Fish
    <:INSTANCE-OF SerialKiller>
    <:Apelido Maniaco_da_Lua>
    <:TotaldeVitimas 15>
    <:TipodeVitimas criancas>
    <:Caracteristica pedofilo_cronico>
)
(John_Wayne_Gacy
    <:INSTANCE-OF SerialKiller>
    <:Apelido Palhaco_Assassino>
    <:TotaldeVitimas 33>
    <:TipodeVitimas garotos_jovens>
    <:Caracteristica torturador>
)
(Belle_Gunness
    <:INSTANCE-OF SerialKiller>
    <:Apelido Lady_Barba_Azul>
    <:MinimodeVitimas 10>
    <:MaximodeVitimas 42>
    <:TipodeVitimas maridos_e_crianças>
    <:Caracteristica extremamente_selvagem>
)
```