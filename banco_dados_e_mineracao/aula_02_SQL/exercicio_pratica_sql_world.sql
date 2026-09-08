-- ============================================================
-- AULA PRÁTICA — LINGUAGEM SQL COM O BANCO WORLD
-- Disciplina: Banco de Dados e Mineração de Dados
-- Professor Rodolfo Terra
-- Banco: world
-- SGBD: MySQL
-- ============================================================
--
-- OBJETIVO:
-- Praticar SELECT, WHERE, ORDER BY, LIMIT, funções de agregação,
-- GROUP BY, aliases e JOIN utilizando o banco de dados World.
--
-- IMPORTANTE:
-- A PARTE 1 contém apenas os desafios.
-- O gabarito começa na PARTE 2.
-- Tente resolver cada questão antes de consultar a resposta.
-- ============================================================


USE world;


-- ============================================================
-- AQUECIMENTO — CONHECENDO O BANCO
-- ============================================================

SHOW TABLES;

DESCRIBE city;
DESCRIBE country;
DESCRIBE countrylanguage;

SELECT * FROM city LIMIT 10;
SELECT * FROM country LIMIT 10;
SELECT * FROM countrylanguage LIMIT 10;


-- ============================================================
-- PARTE 1 — DESAFIOS
-- NÃO AVANCE PARA O GABARITO ANTES DE TENTAR RESOLVER.
-- ============================================================


-- ------------------------------------------------------------
-- DESAFIO 01
-- Quantas cidades existem cadastradas no Brasil?
-- Dica: a tabela city possui a coluna CountryCode.
-- ------------------------------------------------------------




-- ------------------------------------------------------------
-- DESAFIO 02
-- Quais são as 10 cidades mais populosas do mundo?
-- Exiba:
--   - nome da cidade
--   - população
-- Ordene da maior população para a menor.
-- ------------------------------------------------------------




-- ------------------------------------------------------------
-- DESAFIO 03
-- Qual país possui a maior população?
-- Exiba:
--   - nome do país
--   - população
-- ------------------------------------------------------------




-- ------------------------------------------------------------
-- DESAFIO 04
-- Quantos países existem em cada continente?
-- Exiba:
--   - continente
--   - quantidade de países
-- Ordene do continente com mais países para o com menos países.
-- ------------------------------------------------------------




-- ------------------------------------------------------------
-- DESAFIO 05
-- Qual é a expectativa de vida média por continente?
-- Exiba:
--   - continente
--   - expectativa de vida média
-- Ordene da maior média para a menor.
-- ------------------------------------------------------------




-- ------------------------------------------------------------
-- DESAFIO 06
-- Quais países possuem mais cidades cadastradas?
-- Exiba:
--   - nome do país
--   - quantidade de cidades
-- Utilize JOIN, COUNT, GROUP BY e ORDER BY.
-- ------------------------------------------------------------




-- ------------------------------------------------------------
-- DESAFIO 07
-- Quais cidades brasileiras possuem mais de 1 milhão
-- de habitantes?
-- Exiba:
--   - cidade
--   - estado/distrito
--   - população
-- Ordene da maior população para a menor.
-- ------------------------------------------------------------




-- ------------------------------------------------------------
-- DESAFIO 08
-- Quais são as 10 cidades mais populosas do Brasil?
-- Exiba:
--   - cidade
--   - distrito
--   - população
-- ------------------------------------------------------------




-- ------------------------------------------------------------
-- DESAFIO 09
-- Quais países possuem expectativa de vida superior a 80 anos?
-- Exiba:
--   - país
--   - continente
--   - expectativa de vida
-- Ordene da maior para a menor expectativa de vida.
-- ------------------------------------------------------------




-- ------------------------------------------------------------
-- DESAFIO 10
-- Qual é a soma da população das cidades brasileiras
-- cadastradas no banco?
-- Utilize SUM().
-- ------------------------------------------------------------




-- ------------------------------------------------------------
-- DESAFIO 11
-- Qual é a população média das cidades brasileiras
-- cadastradas no banco?
-- Utilize AVG().
-- ------------------------------------------------------------




-- ------------------------------------------------------------
-- DESAFIO 12
-- Qual é a menor e a maior população registrada
-- na tabela city?
-- Utilize MIN(), MAX() e aliases.
-- ------------------------------------------------------------




-- ------------------------------------------------------------
-- DESAFIO 13
-- Liste cidade + país + continente + população.
-- Utilize aliases para as tabelas:
--   ci = city
--   co = country
-- Mostre apenas os 20 primeiros registros.
-- ------------------------------------------------------------




-- ------------------------------------------------------------
-- DESAFIO 14
-- Quantas cidades existem cadastradas por continente?
-- Aqui será necessário:
--   city
--   country
--   INNER JOIN
--   COUNT
--   GROUP BY
-- ------------------------------------------------------------




-- ------------------------------------------------------------
-- DESAFIO 15
-- Qual é a população total das cidades cadastradas
-- em cada continente?
-- Exiba:
--   - continente
--   - população total das cidades
-- Ordene do maior total para o menor.
-- ------------------------------------------------------------




-- ------------------------------------------------------------
-- DESAFIO 16
-- Quantos idiomas oficiais estão cadastrados por país?
-- Considere somente registros com IsOfficial = 'T'.
-- Exiba:
--   - país
--   - quantidade de idiomas oficiais
-- Ordene da maior quantidade para a menor.
-- ------------------------------------------------------------




-- ------------------------------------------------------------
-- DESAFIO 17
-- Quais idiomas aparecem em mais países?
-- Exiba:
--   - idioma
--   - quantidade de países
-- Ordene do mais frequente para o menos frequente.
-- Mostre somente os 10 primeiros.
-- ------------------------------------------------------------




-- ------------------------------------------------------------
-- DESAFIO 18
-- Quantas cidades brasileiras existem em cada distrito/estado?
-- Exiba:
--   - District
--   - quantidade de cidades
-- Ordene da maior quantidade para a menor.
-- ------------------------------------------------------------




-- ------------------------------------------------------------
-- DESAFIO 19
-- Quais países da América do Sul possuem população
-- superior a 10 milhões de habitantes?
-- Exiba:
--   - país
--   - população
-- ------------------------------------------------------------




-- ------------------------------------------------------------
-- DESAFIO 20 — DESAFIO FINAL
-- Construa uma consulta que mostre os 10 países com maior
-- quantidade de cidades cadastradas.
--
-- Exiba:
--   - país
--   - continente
--   - quantidade de cidades
--   - soma da população das cidades cadastradas
--
-- Utilize:
--   INNER JOIN
--   COUNT
--   SUM
--   GROUP BY
--   ORDER BY
--   LIMIT
-- ------------------------------------------------------------






-- ============================================================
-- PARTE 2 — GABARITO
-- ============================================================
--
-- A partir daqui estão as respostas.
-- ============================================================


-- ------------------------------------------------------------
-- RESPOSTA 01
-- Quantas cidades existem cadastradas no Brasil?
-- Resultado esperado: 250
-- ------------------------------------------------------------

SELECT COUNT(*) AS quantidade_cidades
FROM city
WHERE CountryCode = 'BRA';


-- ------------------------------------------------------------
-- RESPOSTA 02
-- 10 cidades mais populosas do mundo
--
-- Resultado esperado:
-- Mumbai (Bombay)       10500000
-- Seoul                  9981619
-- São Paulo              9968485
-- Shanghai               9696300
-- Jakarta                9604900
-- Karachi                9269265
-- Istanbul               8787958
-- Ciudad de México       8591309
-- Moscow                 8389200
-- New York               8008278
-- ------------------------------------------------------------

SELECT
    Name AS cidade,
    Population AS populacao
FROM city
ORDER BY Population DESC
LIMIT 10;


-- ------------------------------------------------------------
-- RESPOSTA 03
-- País com maior população
-- Resultado esperado:
-- China | 1277558000
-- ------------------------------------------------------------

SELECT
    Name AS pais,
    Population AS populacao
FROM country
ORDER BY Population DESC
LIMIT 1;


-- ------------------------------------------------------------
-- RESPOSTA 04
-- Quantidade de países por continente
--
-- Resultado esperado:
-- Africa          58
-- Asia            51
-- Europe          46
-- North America   37
-- Oceania         28
-- South America   14
-- Antarctica       5
-- ------------------------------------------------------------

SELECT
    Continent AS continente,
    COUNT(*) AS quantidade
FROM country
GROUP BY Continent
ORDER BY quantidade DESC;


-- ------------------------------------------------------------
-- RESPOSTA 05
-- Expectativa de vida média por continente
--
-- Observação:
-- AVG() ignora valores NULL.
-- Antarctica não possui expectativa de vida disponível
-- neste conjunto de dados, portanto retorna NULL.
-- ------------------------------------------------------------

SELECT
    Continent AS continente,
    ROUND(AVG(LifeExpectancy), 2) AS expectativa_vida_media
FROM country
GROUP BY Continent
ORDER BY expectativa_vida_media DESC;


-- ------------------------------------------------------------
-- RESPOSTA 06
-- Países com mais cidades cadastradas
--
-- Primeiros resultados esperados:
-- China                 363
-- India                 341
-- United States         274
-- Brazil                250
-- Japan                 248
-- Russian Federation    189
-- Mexico                173
-- Philippines           136
-- Germany                93
-- Indonesia              85
-- ------------------------------------------------------------

SELECT
    co.Name AS pais,
    COUNT(ci.ID) AS cidades
FROM country co
INNER JOIN city ci
    ON co.Code = ci.CountryCode
GROUP BY co.Name
ORDER BY cidades DESC;


-- ------------------------------------------------------------
-- RESPOSTA 07
-- Cidades brasileiras com mais de 1 milhão de habitantes
-- ------------------------------------------------------------

SELECT
    Name AS cidade,
    District AS distrito,
    Population AS populacao
FROM city
WHERE CountryCode = 'BRA'
  AND Population > 1000000
ORDER BY Population DESC;


-- ------------------------------------------------------------
-- RESPOSTA 08
-- 10 cidades mais populosas do Brasil
--
-- Resultado esperado:
-- São Paulo          São Paulo            9968485
-- Rio de Janeiro     Rio de Janeiro       5598953
-- Salvador           Bahia                2302832
-- Belo Horizonte     Minas Gerais         2139125
-- Fortaleza          Ceará                2097757
-- Brasília           Distrito Federal     1969868
-- Curitiba            Paraná               1584232
-- Recife              Pernambuco           1378087
-- Porto Alegre        Rio Grande do Sul    1314032
-- Manaus              Amazonas             1255049
-- ------------------------------------------------------------

SELECT
    Name AS cidade,
    District AS distrito,
    Population AS populacao
FROM city
WHERE CountryCode = 'BRA'
ORDER BY Population DESC
LIMIT 10;


-- ------------------------------------------------------------
-- RESPOSTA 09
-- Países com expectativa de vida superior a 80 anos
--
-- Resultado esperado:
-- Andorra       83.5
-- Macao         81.6
-- San Marino    81.1
-- Japan         80.7
-- Singapore     80.1
-- ------------------------------------------------------------

SELECT
    Name AS pais,
    Continent AS continente,
    LifeExpectancy AS expectativa_vida
FROM country
WHERE LifeExpectancy > 80
ORDER BY LifeExpectancy DESC;


-- ------------------------------------------------------------
-- RESPOSTA 10
-- Soma da população das cidades brasileiras
-- Resultado esperado: 85876862
-- ------------------------------------------------------------

SELECT
    SUM(Population) AS populacao_total
FROM city
WHERE CountryCode = 'BRA';


-- ------------------------------------------------------------
-- RESPOSTA 11
-- População média das cidades brasileiras
-- Resultado aproximado: 343507.45
-- ------------------------------------------------------------

SELECT
    ROUND(AVG(Population), 2) AS populacao_media
FROM city
WHERE CountryCode = 'BRA';


-- ------------------------------------------------------------
-- RESPOSTA 12
-- Menor e maior população registrada em city
--
-- Resultado esperado:
-- menor = 42
-- maior = 10500000
-- ------------------------------------------------------------

SELECT
    MIN(Population) AS menor,
    MAX(Population) AS maior
FROM city;


-- Consultando também quais cidades possuem esses valores:

SELECT
    ID,
    Name,
    CountryCode,
    District,
    Population
FROM city
WHERE Population = (SELECT MIN(Population) FROM city)
   OR Population = (SELECT MAX(Population) FROM city)
ORDER BY Population;


-- ------------------------------------------------------------
-- RESPOSTA 13
-- Cidade + país + continente + população
-- ------------------------------------------------------------

SELECT
    ci.Name AS cidade,
    co.Name AS pais,
    co.Continent AS continente,
    ci.Population AS populacao
FROM city ci
INNER JOIN country co
    ON ci.CountryCode = co.Code
LIMIT 20;


-- ------------------------------------------------------------
-- RESPOSTA 14
-- Quantidade de cidades cadastradas por continente
-- ------------------------------------------------------------

SELECT
    co.Continent AS continente,
    COUNT(ci.ID) AS quantidade_cidades
FROM country co
INNER JOIN city ci
    ON co.Code = ci.CountryCode
GROUP BY co.Continent
ORDER BY quantidade_cidades DESC;


-- ------------------------------------------------------------
-- RESPOSTA 15
-- População total das cidades cadastradas por continente
-- ------------------------------------------------------------

SELECT
    co.Continent AS continente,
    SUM(ci.Population) AS populacao_cidades
FROM country co
INNER JOIN city ci
    ON co.Code = ci.CountryCode
GROUP BY co.Continent
ORDER BY populacao_cidades DESC;


-- ------------------------------------------------------------
-- RESPOSTA 16
-- Quantidade de idiomas oficiais por país
-- ------------------------------------------------------------

SELECT
    co.Name AS pais,
    COUNT(cl.Language) AS idiomas_oficiais
FROM country co
INNER JOIN countrylanguage cl
    ON co.Code = cl.CountryCode
WHERE cl.IsOfficial = 'T'
GROUP BY co.Name
ORDER BY idiomas_oficiais DESC, co.Name;


-- ------------------------------------------------------------
-- RESPOSTA 17
-- Os 10 idiomas cadastrados em mais países
-- ------------------------------------------------------------

SELECT
    Language AS idioma,
    COUNT(DISTINCT CountryCode) AS quantidade_paises
FROM countrylanguage
GROUP BY Language
ORDER BY quantidade_paises DESC
LIMIT 10;


-- ------------------------------------------------------------
-- RESPOSTA 18
-- Quantidade de cidades brasileiras por distrito/estado
-- ------------------------------------------------------------

SELECT
    District AS distrito,
    COUNT(*) AS quantidade_cidades
FROM city
WHERE CountryCode = 'BRA'
GROUP BY District
ORDER BY quantidade_cidades DESC, District;


-- ------------------------------------------------------------
-- RESPOSTA 19
-- Países da América do Sul com mais de 10 milhões
-- de habitantes
-- ------------------------------------------------------------

SELECT
    Name AS pais,
    Population AS populacao
FROM country
WHERE Continent = 'South America'
  AND Population > 10000000
ORDER BY Population DESC;


-- ------------------------------------------------------------
-- RESPOSTA 20 — DESAFIO FINAL
-- 10 países com mais cidades cadastradas
-- ------------------------------------------------------------

SELECT
    co.Name AS pais,
    co.Continent AS continente,
    COUNT(ci.ID) AS quantidade_cidades,
    SUM(ci.Population) AS populacao_cidades
FROM country co
INNER JOIN city ci
    ON co.Code = ci.CountryCode
GROUP BY
    co.Code,
    co.Name,
    co.Continent
ORDER BY quantidade_cidades DESC
LIMIT 10;


-- ============================================================
-- EXTRAS PARA DEMONSTRAÇÃO EM SALA
-- ============================================================


-- Exibir somente cidades brasileiras
SELECT *
FROM city
WHERE CountryCode = 'BRA';


-- Exibir somente algumas colunas
SELECT
    Name,
    District,
    Population
FROM city
WHERE CountryCode = 'BRA';


-- AND: duas condições precisam ser verdadeiras
SELECT *
FROM country
WHERE Continent = 'South America'
  AND Population > 10000000;


-- OR: pelo menos uma condição precisa ser verdadeira
SELECT *
FROM country
WHERE Continent = 'Europe'
   OR Continent = 'South America';


-- ORDER BY crescente
SELECT
    Name,
    Population
FROM city
ORDER BY Population ASC
LIMIT 10;


-- ORDER BY decrescente
SELECT
    Name,
    Population
FROM city
ORDER BY Population DESC
LIMIT 10;


-- INNER JOIN simples
SELECT
    city.Name AS cidade,
    country.Name AS pais
FROM city
INNER JOIN country
    ON city.CountryCode = country.Code
LIMIT 10;


-- JOIN + WHERE
SELECT
    ci.Name AS cidade,
    co.Name AS pais,
    ci.Population AS populacao
FROM city ci
INNER JOIN country co
    ON ci.CountryCode = co.Code
WHERE co.Code = 'BRA'
  AND ci.Population > 1000000
ORDER BY ci.Population DESC;


-- ============================================================
-- FIM DA AULA PRÁTICA
-- ============================================================
