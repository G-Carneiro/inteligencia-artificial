livro(uma_mulher_na_escuridao).
livro(a_garota_no_gelo).
livro(crepusculo).
livro(it_a_coisa).
livro(os_sete_maridos_de_evelyn_hugo).
livro(arena_treze).
livro(a_culpa_eh_das_estrelas).
livro(assassinato_no_expresso_oriente).
livro(a_vida_invisivel_de_addie_larue).
livro(a_outra_sra_parrish).
livro(harry_potter).
livro(por_lugares_incriveis).

/* Genero dos Livros */

thriller(uma_mulher_na_escuridao).
thriller(a_garota_no_gelo).
thriller(assassinato_no_expresso_oriente).
romance(crepusculo).
romance(por_lugares_incriveis).
romance(os_sete_maridos_de_evelyn_hugo).
terror(it_a_coisa).
acao_e_avetura(arena_treze).
drama(a_culpa_eh_das_estrelas).
fantasia(harry_potter).
fantasia(a_vida_invisivel_de_addie_larue).
suspense(a_outra_sra_parrish).

/* Autor */

charlie_donlea(uma_mulher_na_escuridao).
robert_bryndza(a_garota_no_gelo).
stephenie_meyer(crepusculo).
stephen_king(it_a_coisa).
taylor_jenkins_reid(os_sete_maridos_de_evelyn_hugo).
joseph_delaney(arena_treze).
jennifer_niven(por_lugares_incriveis).
john_green(a_culpa_eh_das_estrelas).
agatha_christie(assassinato_no_expresso_oriente).
ve_schwab(a_vida_invisivel_de_addie_larue).
liv_constantine(a_outra_sra_parrish).
jk_rowling(harry_potter).

 /* Editora */

faro_editora(uma_mulher_na_escuridao).
gutenberg(a_garota_no_gelo).
intrinseca(crepusculo).
intrinseca(a_culpa_eh_das_estrelas).
suma(it_a_coisa).
paralela(os_sete_maridos_de_evelyn_hugo).
bertrand_brasil(arena_treze).
seguinte(por_lugares_incriveis).
rocco(harry_potter).
harperCollins(a_outra_sra_parrish).
harperCollins(assassinato_no_expresso_oriente).
galera(a_vida_invisivel_de_addie_larue).

/* Best Seller */

nBest_seller(uma_mulher_na_escuridao).
nBest_seller(it_a_coisa).
nBest_seller(os_sete_maridos_de_evelyn_hugo).
nBest_seller(arena_treze).
nBest_seller(por_lugares_incriveis).
nBest_seller(a_culpa_eh_das_estrelas).
nBest_seller(a_vida_invisivel_de_addie_larue).
best_seller(a_garota_no_gelo).
best_seller(crepusculo).
best_seller(assassinato_no_expresso_oriente).
best_seller(a_outra_sra_parrish).
best_seller(harry_potter).

 /* Saga */

nSaga(uma_mulher_na_escuridao).
nSaga(it_a_coisa).
nSaga(os_sete_maridos_de_evelyn_hugo).
nSaga(por_lugares_incriveis).
nSaga(a_culpa_eh_das_estrelas).
nSaga(a_vida_invisivel_de_addie_larue).
nSaga(assassinato_no_expresso_oriente).
nSaga(a_outra_sra_parrish).
saga(arena_treze).
saga(a_garota_no_gelo).
saga(crepusculo).
saga(harry_potter).

/* Ano de Lancamento */

ano2021(a_vida_invisivel_de_addie_larue).
ano2019(uma_mulher_na_escuridao).
ano2019(os_sete_maridos_de_evelyn_hugo).
ano2017(a_outra_sra_parrish).
ano2016(arena_treze).
ano2016(a_garota_no_gelo).
ano2015(por_lugares_incriveis).
ano2014(it_a_coisa).
ano2014(a_culpa_eh_das_estrelas).
ano2008(crepusculo).
ano1997(harry_potter).
ano1934(assassinato_no_expresso_oriente).

listaDeSugestoes() :- atomics_to_string(
    ["Th1 = Um thriller da editora gutenberg que faca parte de uma saga",
    "Th2 = Um classico romace policial de 34 de um assasinato em um trem de uma autora de destaque",
    "Th3 = Um thriller psicologico sobre obsessao, assasinato e a busca pela verdade do autor de dois best sellers charlie donlea",
    "R1 = Um romance da intriseca com vampiros que faca parte de uma saga de livros",
    "R2 = Um romace juvenil, sobre jovens problematicos lancado no ano de 2015",
    "R3 = Glamour e escandalos, uma historia sobre uma mulher poderosa e decidida do ano 2019 da autora TJR ",
    "Tr = Um terror sobre palhacos de um autor muito renomado",
    "AA = distopia futuristica com uma fantasia epica romana do ano de 2016",
    "D = Um romance fofo e tragico de john green que vai te fazer chorar o final de semana inteiro",
    "F1 = Uma famosa historia de fantasia sobre bruxos que faz parte de uma saga de livros",
    "F2 = Um livro de fantasia sobre eternidade e esquecimento do ano 2021",
    "S = Suspense psicologico da editora harper collins sobre uma mulher fria e manipuladora que entra na vida de um 'casal de ouro' "], '\n', String), writeln(String).

suggest(X) :- listaDeSugestoes(), write("Digite um codigo: "), nl, read_line_to_string(user_input, P), retornaLivro(P, X).

retornaLivro("Th1", X) :- gutenberg(X), thriller(X), saga(X).
retornaLivro("Th2", X) :- thriller(X), agatha_christie(X), ano1934(X).
retornaLivro("Th3", X) :- charlie_donlea(X), thriller(X).
retornaLivro("R1", X) :- romance(X), saga(X).
retornaLivro("R2", X) :- romance(X), ano2015(X).
retornaLivro("R3", X) :- romance(X), taylor_jenkins_reid(X), ano2019(X).
retornaLivro("Tr", X) :- terror(X), stephen_king(X).
retornaLivro("AA", X) :- acao_e_avetura(X), ano2016(X).
retornaLivro("D", X) :- drama(X), john_green(X).
retornaLivro("F1", X) :- fantasia(X), saga(X). 
retornaLivro("F2", X) :- fantasia(X), ano2021(X).
retornaLivro("S", X) :- suspense(X), harperCollins(X);
