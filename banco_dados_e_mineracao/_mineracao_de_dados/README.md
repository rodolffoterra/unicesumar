# ⛏️ Mineração de Dados com WEKA

## Banco de Dados e Mineração de Dados

**Professor:** Rodolfo Terra\
**Tema:** Mineração de Dados, KDD, Aprendizado de Máquina e WEKA

-   LinkedIn: https://www.linkedin.com/in/rodolffoterra/
-   GitHub: https://github.com/rodolffoterra

------------------------------------------------------------------------

# 📚 Sobre esta aula

Nas aulas anteriores, estudamos como os dados são armazenados,
consultados, integrados e organizados para análise.

Agora avançamos para uma nova pergunta:

> **O que podemos descobrir a partir dos dados?**

Uma organização pode possuir milhares ou milhões de registros de
clientes, vendas, produtos, imóveis, transações ou atendimentos.
Consultas SQL e dashboards ajudam a responder perguntas conhecidas. A
**Mineração de Dados** permite avançar para a descoberta de relações,
padrões e comportamentos presentes nos dados.

Exemplos:

-   quais clientes apresentam comportamentos semelhantes?
-   quais características ajudam a prever determinado resultado?
-   qual poderá ser o preço de um imóvel?
-   quais produtos apresentam relações de compra?
-   existem registros com comportamento incomum?
-   podemos classificar automaticamente novos registros?

Nesta aula utilizaremos o **WEKA** como ambiente prático para
compreender esse processo.

------------------------------------------------------------------------

# 🎯 Objetivos de aprendizagem

Ao final da aula, o estudante deverá ser capaz de:

-   compreender o conceito de Mineração de Dados;
-   entender a relação entre dados, informação, conhecimento e decisão;
-   compreender as etapas do processo KDD;
-   diferenciar aprendizado supervisionado e não supervisionado;
-   reconhecer problemas de classificação, regressão, agrupamento e
    associação;
-   compreender atributos e variável-alvo;
-   preparar conjuntos de dados para análise;
-   conhecer os formatos CSV e ARFF;
-   utilizar a interface do WEKA;
-   importar conjuntos de dados;
-   selecionar algoritmos;
-   executar experimentos;
-   interpretar resultados;
-   compreender métricas como Accuracy, MAE e RAE;
-   reconhecer a importância da avaliação de modelos.

------------------------------------------------------------------------

# 1. Do dado ao conhecimento

Podemos visualizar a evolução da informação desta forma:

``` text
DADOS
  ↓
INFORMAÇÃO
  ↓
PADRÕES
  ↓
CONHECIMENTO
  ↓
DECISÃO
```

Um conjunto com milhares de vendas contém **dados**.

Quando organizamos esses dados e calculamos o faturamento por produto,
obtemos **informação**.

Quando identificamos comportamentos recorrentes ou relações entre
variáveis, encontramos **padrões**.

Quando interpretamos esses padrões no contexto do negócio, produzimos
**conhecimento**.

Finalmente, esse conhecimento pode apoiar uma **decisão**.

------------------------------------------------------------------------

# 2. O que é Mineração de Dados?

**Mineração de Dados (Data Mining)** é o processo de explorar conjuntos
de dados com técnicas computacionais e estatísticas para identificar
padrões, relações, tendências ou estruturas úteis.

A ideia central não é simplesmente armazenar dados.

Também não é apenas executar uma consulta.

O objetivo é encontrar conhecimento potencialmente útil dentro dos
dados.

``` text
GRANDE VOLUME DE DADOS
          ↓
   MINERAÇÃO DE DADOS
          ↓
       PADRÕES
          ↓
     CONHECIMENTO
          ↓
       DECISÃO
```

------------------------------------------------------------------------

# 3. SQL, BI e Mineração de Dados

Essas tecnologias podem trabalhar juntas, mas respondem a tipos
diferentes de perguntas.

### SQL

Pergunta conhecida:

> Quanto vendemos no último mês?

``` sql
SELECT SUM(valor)
FROM vendas
WHERE data >= '2026-08-01'
  AND data < '2026-09-01';
```

### Business Intelligence

Pergunta conhecida acompanhada ao longo do tempo:

> Como o faturamento evoluiu durante o ano?

Um dashboard pode apresentar gráficos e indicadores.

### Mineração de Dados

Busca relações ou comportamentos que podem não ser evidentes:

> Quais características estão relacionadas à perda de clientes?

> Quais grupos de clientes apresentam comportamentos semelhantes?

> É possível prever o valor de uma propriedade pelas suas
> características?

------------------------------------------------------------------------

# 4. KDD --- Knowledge Discovery in Databases

A Mineração de Dados normalmente é apresentada dentro de um processo
maior denominado **KDD --- Knowledge Discovery in Databases**.

``` text
SELEÇÃO
   ↓
PRÉ-PROCESSAMENTO
   ↓
TRANSFORMAÇÃO
   ↓
MINERAÇÃO
   ↓
AVALIAÇÃO
   ↓
CONHECIMENTO
```

Um ponto fundamental:

> **Mineração de Dados é uma etapa do processo de descoberta de
> conhecimento.**

------------------------------------------------------------------------

# 5. Etapa 1 --- Seleção

Primeiro escolhemos os dados relevantes para o problema.

Imagine uma base de imóveis contendo:

``` text
id
data
preco
quartos
banheiros
area
andares
vista
condicao
ano_construcao
localizacao
```

Se queremos prever o **preço**, precisamos avaliar quais atributos serão
utilizados.

Perguntas importantes:

-   qual problema queremos resolver?
-   qual é a variável que desejamos prever?
-   quais atributos podem contribuir?
-   existem atributos irrelevantes?
-   existe informação que não estaria disponível no momento da previsão?

> Um bom projeto começa pela compreensão do problema, não pela escolha
> do algoritmo.

------------------------------------------------------------------------

# 6. Etapa 2 --- Pré-processamento

Dados reais raramente chegam perfeitos.

Podemos encontrar:

-   valores ausentes;
-   duplicidades;
-   erros de digitação;
-   tipos incorretos;
-   categorias inconsistentes;
-   registros inválidos;
-   valores extremos;
-   atributos irrelevantes.

Exemplo:

``` text
SP
São Paulo
SAO PAULO
são paulo
```

Após tratamento:

``` text
São Paulo
```

Outro exemplo:

``` text
idade = ?
preco = NULL
cidade = ""
```

Esses problemas precisam ser avaliados antes da modelagem.

------------------------------------------------------------------------

# 7. Etapa 3 --- Transformação

Depois da limpeza, os dados podem precisar ser transformados.

Exemplos:

-   normalização;
-   padronização;
-   conversão de tipos;
-   criação de atributos;
-   seleção de atributos;
-   discretização;
-   codificação de categorias;
-   redução de dimensionalidade.

Exemplo:

``` text
data_nascimento
        ↓
      idade
```

Ou:

``` text
quantidade × preco_unitario
             ↓
        valor_total
```

O objetivo é representar os dados de maneira adequada para o algoritmo.

------------------------------------------------------------------------

# 8. Etapa 4 --- Mineração

Nesta etapa aplicamos algoritmos para encontrar padrões ou construir
modelos.

Algumas tarefas importantes:

``` text
MINERAÇÃO DE DADOS
       |
       +-- Classificação
       |
       +-- Regressão
       |
       +-- Agrupamento
       |
       +-- Associação
       |
       +-- Detecção de Anomalias
```

A escolha depende da pergunta que queremos responder.

------------------------------------------------------------------------

# 9. Etapa 5 --- Avaliação

Executar um algoritmo não significa que encontramos uma boa solução.

Precisamos avaliar:

-   o modelo apresenta bom desempenho?
-   os erros são aceitáveis?
-   o resultado generaliza para dados não vistos?
-   o modelo supera uma referência simples?
-   o resultado faz sentido para o problema?
-   existe risco de overfitting?
-   a métrica utilizada é adequada?

> **Um modelo só é útil quando seus resultados são avaliados e
> interpretados corretamente.**

------------------------------------------------------------------------

# 10. Aprendizado Supervisionado

No **aprendizado supervisionado**, temos uma variável que queremos
prever.

Exemplo:

    Área   Quartos   Banheiros    Preço
  ------ --------- ----------- --------
      80         2           1   280000
     120         3           2   430000
     180         4           3   690000

Aqui:

``` text
ENTRADAS
Área
Quartos
Banheiros
    ↓
 MODELO
    ↓
SAÍDA
Preço
```

O algoritmo aprende relações utilizando exemplos nos quais a resposta já
é conhecida.

Duas tarefas supervisionadas fundamentais são:

-   **Classificação**
-   **Regressão**

------------------------------------------------------------------------

# 11. Classificação

Na classificação, a variável-alvo representa uma **categoria ou
classe**.

Exemplos:

``` text
E-mail → Spam / Não Spam
```

``` text
Cliente → Pode cancelar / Não deve cancelar
```

``` text
Passageiro → Sobreviveu / Não sobreviveu
```

Exemplo conceitual:

    Idade   Classe   Tarifa Resultado
  ------- -------- -------- -----------
       22        3     7.25 Não
       38        1    71.28 Sim
       26        3     7.93 Sim

O modelo tenta aprender uma função:

``` text
ATRIBUTOS
    ↓
MODELO
    ↓
CLASSE
```

------------------------------------------------------------------------

# 12. Regressão

Na regressão, queremos prever um **valor numérico**.

Exemplos:

-   preço de imóvel;
-   faturamento;
-   temperatura;
-   demanda;
-   consumo;
-   tempo de entrega.

Exemplo:

``` text
Área = 150 m²
Quartos = 3
Banheiros = 2
        ↓
     MODELO
        ↓
Preço previsto = R$ 520.000
```

A diferença principal pode ser lembrada assim:

``` text
CLASSIFICAÇÃO → categoria
REGRESSÃO     → número
```

------------------------------------------------------------------------

# 13. Aprendizado Não Supervisionado

No aprendizado não supervisionado, não fornecemos uma classe conhecida
para o algoritmo prever.

Queremos descobrir estruturas presentes nos dados.

``` text
DADOS
  ↓
ALGORITMO
  ↓
ESTRUTURAS / GRUPOS / RELAÇÕES
```

Exemplos importantes:

-   clusterização;
-   regras de associação;
-   exploração de padrões.

------------------------------------------------------------------------

# 14. Clusterização

Clusterização significa formar grupos de registros semelhantes.

Exemplo de clientes:

``` text
CLIENTES
   ↓
ALGORITMO
   ↓
+------------------+
| Grupo 1          |
| Alto valor       |
+------------------+

+------------------+
| Grupo 2          |
| Compradores      |
| ocasionais       |
+------------------+

+------------------+
| Grupo 3          |
| Baixo engajamento|
+------------------+
```

O algoritmo não recebe necessariamente os nomes desses grupos. A
interpretação dos clusters faz parte da análise.

------------------------------------------------------------------------

# 15. Regras de Associação

Regras de associação procuram relações de ocorrência entre itens.

Exemplo clássico:

``` text
Cliente compra A
       ↓
frequentemente também compra B
```

Aplicações:

-   cesta de compras;
-   recomendação;
-   combinação de produtos;
-   comportamento de consumo.

Uma regra pode assumir a forma:

``` text
{Produto A, Produto B} → {Produto C}
```

Isso não significa causalidade. Significa uma associação encontrada nos
dados.

------------------------------------------------------------------------

# 16. O que é WEKA?

**WEKA --- Waikato Environment for Knowledge Analysis** é uma ferramenta
utilizada para experimentação com técnicas de aprendizado de máquina e
Mineração de Dados.

Ela permite trabalhar com várias etapas por meio de interface gráfica.

Entre suas funcionalidades estão:

-   carregamento de datasets;
-   pré-processamento;
-   filtros;
-   seleção de atributos;
-   classificação;
-   regressão;
-   clusterização;
-   regras de associação;
-   visualização;
-   avaliação de modelos.

Para fins didáticos, o WEKA permite observar conceitos de aprendizado de
máquina sem exigir que toda a implementação dos algoritmos seja
programada manualmente.

------------------------------------------------------------------------

# 17. Interface inicial do WEKA

Ao abrir o WEKA, encontramos diferentes ambientes.

Um dos mais importantes para esta aula é:

## Explorer

No **Explorer**, encontramos abas como:

``` text
Preprocess
Classify
Cluster
Associate
Select attributes
Visualize
```

### Preprocess

Carregar e preparar os dados.

### Classify

Executar algoritmos de classificação e também diversos algoritmos
aplicáveis a regressão.

### Cluster

Executar algoritmos de agrupamento.

### Associate

Descobrir regras de associação.

### Select attributes

Analisar e selecionar atributos.

### Visualize

Explorar visualmente os dados.

------------------------------------------------------------------------

# 18. CSV e ARFF

O WEKA pode trabalhar com diferentes formatos.

Dois formatos importantes para nossas atividades são:

-   CSV;
-   ARFF.

### CSV

``` csv
area,quartos,banheiros,preco
80,2,1,280000
120,3,2,430000
180,4,3,690000
```

### ARFF

ARFF significa **Attribute-Relation File Format**.

Exemplo:

``` text
@relation imoveis

@attribute area numeric
@attribute quartos numeric
@attribute banheiros numeric
@attribute preco numeric

@data
80,2,1,280000
120,3,2,430000
180,4,3,690000
```

O ARFF descreve explicitamente os atributos e seus tipos antes dos
dados.

------------------------------------------------------------------------

# 19. Estrutura de um arquivo ARFF

Um arquivo ARFF possui duas grandes partes.

## Cabeçalho

``` text
@relation casas

@attribute area numeric
@attribute quartos numeric
@attribute cidade {Sorocaba,Campinas,Itu}
@attribute preco numeric
```

## Dados

``` text
@data
100,2,Sorocaba,350000
140,3,Campinas,480000
200,4,Itu,720000
```

É importante configurar corretamente os tipos.

Um atributo pode ser:

``` text
numeric
```

ou nominal:

``` text
{Sim,Nao}
```

Um tipo incorreto pode impedir determinados algoritmos de trabalhar
corretamente com o dataset.

------------------------------------------------------------------------

# 20. A variável-alvo

Antes de executar um modelo supervisionado, precisamos identificar a
variável que desejamos prever.

### Classificação

``` text
idade
sexo
classe
tarifa
    ↓
sobreviveu
```

`Sobreviveu` é a classe.

### Regressão

``` text
quartos
banheiros
area
localizacao
    ↓
preco
```

`Preço` é a variável-alvo.

> **Antes de escolher o algoritmo, saiba exatamente o que deseja
> prever.**

------------------------------------------------------------------------

# 21. Preparando o dataset no WEKA

No **Explorer → Preprocess**:

1.  selecione **Open file**;
2.  carregue o dataset;
3.  observe a quantidade de instâncias;
4.  observe os atributos;
5.  confira os tipos;
6.  identifique valores ausentes;
7.  visualize distribuições;
8.  remova atributos que não fazem sentido para o problema, quando
    necessário;
9.  confirme qual atributo será utilizado como alvo.

Exemplo:

``` text
Instances: 6.480
Attributes: 18
```

Um identificador como:

``` text
id = 7129300520
```

pode ser útil para identificar o registro, mas não necessariamente é
útil como variável preditiva.

------------------------------------------------------------------------

# 22. Treino e Teste

Um dos conceitos mais importantes em aprendizado de máquina é não
avaliar o modelo apenas nos mesmos registros utilizados para treiná-lo.

Precisamos verificar seu comportamento em dados não utilizados durante o
aprendizado.

``` text
DATASET
   |
   +--------> TREINO
   |             |
   |           MODELO
   |
   +--------> TESTE
                 |
              AVALIAÇÃO
```

O conjunto de treino é utilizado para aprender.

O conjunto de teste é utilizado para avaliar.

------------------------------------------------------------------------

# 23. Percentage Split

No WEKA, uma das estratégias disponíveis é dividir o conjunto por
percentual.

Exemplo:

``` text
70% → Treinamento
30% → Teste
```

O modelo aprende utilizando uma parte e é avaliado na outra.

Essa estratégia é simples e didática, embora o resultado possa depender
da divisão realizada.

------------------------------------------------------------------------

# 24. Cross-Validation

Outra estratégia importante é a **validação cruzada**.

Exemplo:

``` text
10-fold Cross-Validation
```

Conceitualmente, o dataset é dividido em partes.

Em diferentes rodadas:

-   algumas partes são usadas para treinamento;
-   uma parte é usada para validação;
-   o processo é repetido.

``` text
Fold 1 → Teste
Fold 2 → Teste
Fold 3 → Teste
...
Fold 10 → Teste
```

Ao final, os resultados são combinados.

Isso permite avaliar o modelo em diferentes subconjuntos dos dados.

------------------------------------------------------------------------

# 25. Executando um modelo no WEKA

Fluxo geral:

``` text
1. Abrir WEKA
        ↓
2. Explorer
        ↓
3. Preprocess
        ↓
4. Open File
        ↓
5. Preparar dados
        ↓
6. Classify
        ↓
7. Choose
        ↓
8. Selecionar algoritmo
        ↓
9. Definir avaliação
        ↓
10. Start
        ↓
11. Interpretar resultado
```

O botão **Start** não encerra a análise.

Na realidade, ele inicia a etapa mais importante para o estudante:

> **interpretar o que o modelo produziu.**

------------------------------------------------------------------------

# 26. Accuracy

Em problemas de classificação, uma métrica bastante conhecida é a
**Accuracy (Acurácia)**.

Ela representa o percentual de previsões corretas.

``` text
Accuracy =
Número de previsões corretas
-----------------------------
Número total de previsões
```

Exemplo:

``` text
100 registros avaliados
95 previsões corretas
5 previsões incorretas
```

Então:

``` text
Accuracy = 95%
```

Quanto maior, melhor --- **mas a acurácia não deve ser analisada
isoladamente**.

Em datasets muito desbalanceados, uma acurácia alta pode esconder um
modelo ruim para a classe que realmente importa.

------------------------------------------------------------------------

# 27. Exemplo de problema com Accuracy

Imagine:

``` text
1.000 clientes
```

Destes:

``` text
950 → não cancelaram
 50 → cancelaram
```

Um modelo que sempre responda:

``` text
"Não vai cancelar"
```

teria:

``` text
950 acertos
```

e:

``` text
Accuracy = 95%
```

Mesmo assim, ele não identificaria nenhum dos clientes que realmente
cancelaram.

Portanto:

> **Uma métrica deve ser interpretada dentro do contexto do problema e
> da distribuição das classes.**

------------------------------------------------------------------------

# 28. Matriz de Confusão

Em classificação, a matriz de confusão ajuda a compreender onde o modelo
acertou e errou.

Exemplo binário:

                      Previsto: Sim         Previsto: Não
  ----------- --------------------- ---------------------
  Real: Sim     Verdadeiro Positivo        Falso Negativo
  Real: Não          Falso Positivo   Verdadeiro Negativo

Ela permite analisar não apenas quantos acertos ocorreram, mas **qual
tipo de erro** o modelo cometeu.

Em problemas reais, tipos diferentes de erro podem ter custos muito
diferentes.

------------------------------------------------------------------------

# 29. MAE --- Mean Absolute Error

Em regressão, precisamos medir a diferença entre o valor real e o valor
previsto.

O **MAE --- Mean Absolute Error** representa o erro absoluto médio.

``` text
Valor real     = 500.000
Valor previsto = 470.000

Erro absoluto  = 30.000
```

Para vários registros:

``` text
MAE = média dos erros absolutos
```

Formalmente:

``` text
MAE = (1/n) × Σ |real - previsto|
```

### Interpretação

> **Quanto menor o MAE, melhor.**

Se o MAE de um modelo de imóveis for:

``` text
MAE = R$ 45.000
```

isso indica que, em média, as previsões apresentam erro absoluto de
aproximadamente R\$ 45 mil.

A unidade do MAE é a mesma da variável prevista.

------------------------------------------------------------------------

# 30. RAE --- Relative Absolute Error

O **RAE --- Relative Absolute Error** compara o erro absoluto do modelo
com o erro de um modelo simples de referência.

De forma conceitual:

``` text
RAE =
Erro do modelo
--------------
Erro de referência
```

Normalmente o resultado é apresentado em percentual.

### Interpretação

``` text
RAE menor → melhor
```

Se:

``` text
RAE = 60%
```

o erro absoluto acumulado do modelo corresponde a aproximadamente 60% do
erro da referência utilizada.

Se estiver próximo de:

``` text
100%
```

o modelo está próximo do desempenho dessa referência simples.

Valores acima de 100% indicam que, segundo essa comparação, o modelo
pode estar pior que a referência.

> O RAE ajuda a responder: **o modelo realmente está melhor do que uma
> previsão básica?**

------------------------------------------------------------------------

# 31. Accuracy × MAE × RAE

Essas métricas não possuem a mesma finalidade.

  Métrica    Aplicação principal   Interpretação
  ---------- --------------------- ----------------------------------
  Accuracy   Classificação         percentual de acertos
  MAE        Regressão             magnitude média do erro absoluto
  RAE        Regressão             erro relativo a uma referência

Não devemos procurar **Accuracy** como principal medida para um problema
de previsão numérica contínua.

Da mesma forma, MAE possui interpretação especialmente natural quando
queremos entender erro de valores numéricos.

------------------------------------------------------------------------

# 32. Exemplo de Regressão --- Preço de Imóveis

Imagine um dataset contendo:

``` text
bedrooms
bathrooms
sqft_living
floors
waterfront
view
condition
grade
yr_built
price
```

Nosso objetivo:

``` text
ATRIBUTOS DO IMÓVEL
        ↓
MODELO DE REGRESSÃO
        ↓
PREÇO ESTIMADO
```

No WEKA:

``` text
Preprocess
    ↓
Carregar dataset
    ↓
Classify
    ↓
Selecionar algoritmo de regressão
    ↓
Selecionar price como alvo
    ↓
Cross-validation ou Percentage Split
    ↓
Start
    ↓
Interpretar MAE / RAE e demais métricas
```

------------------------------------------------------------------------

# 33. Por que usar uma amostra?

Datasets grandes podem tornar uma demonstração em sala mais lenta.

Durante uma aula ao vivo, podemos utilizar uma **amostra aleatória
representativa** do conjunto original para acelerar a execução.

Exemplo:

``` text
DATASET ORIGINAL
      ↓
AMOSTRAGEM ALEATÓRIA
      ↓
30% DOS REGISTROS
      ↓
DATASET DIDÁTICO
      ↓
WEKA
```

O objetivo didático é reduzir o tempo de processamento sem simplesmente
escolher apenas os primeiros registros.

É importante entender que, em projetos reais, a estratégia de amostragem
precisa ser avaliada cuidadosamente para evitar vieses.

------------------------------------------------------------------------

# 34. Exemplo de Classificação --- Titanic

Outro exemplo didático é o dataset Titanic.

Possíveis atributos:

``` text
PassengerId
Pclass
Sex
Age
SibSp
Parch
Fare
Embarked
```

Variável-alvo:

``` text
Survived
```

Podemos representar:

``` text
0 → Não sobreviveu
1 → Sobreviveu
```

ou transformar didaticamente a classe em valores nominais.

O problema é de **classificação**, pois queremos prever uma categoria.

------------------------------------------------------------------------

# 35. Interpretando o resultado

Nunca devemos concluir:

> "O modelo é bom porque o WEKA executou sem erro."

Precisamos perguntar:

-   qual foi a estratégia de avaliação?
-   quantos registros foram utilizados?
-   qual é a distribuição da variável-alvo?
-   qual métrica estamos analisando?
-   existe desbalanceamento?
-   qual é o erro?
-   existe uma baseline?
-   o modelo generaliza?
-   o resultado faz sentido para o domínio?

------------------------------------------------------------------------

# 36. Overfitting

Um modelo pode aprender muito bem os exemplos de treinamento e
apresentar desempenho ruim em novos dados.

Isso é chamado de **overfitting**.

``` text
TREINO
  ↓
Modelo "decora" detalhes
  ↓
Excelente no treino
  ↓
Ruim em novos dados
```

O objetivo não é decorar o dataset.

O objetivo é aprender padrões que consigam **generalizar**.

Por isso, estratégias de teste e validação são essenciais.

------------------------------------------------------------------------

# 37. Fluxo completo de um experimento

``` text
PROBLEMA DE NEGÓCIO
        ↓
SELEÇÃO DOS DADOS
        ↓
PRÉ-PROCESSAMENTO
        ↓
TRANSFORMAÇÃO
        ↓
DEFINIÇÃO DO ALVO
        ↓
ESCOLHA DA TAREFA
        ↓
ESCOLHA DO ALGORITMO
        ↓
TREINAMENTO
        ↓
VALIDAÇÃO
        ↓
MÉTRICAS
        ↓
INTERPRETAÇÃO
        ↓
CONHECIMENTO
        ↓
DECISÃO
```

Esse fluxo é mais importante do que simplesmente memorizar onde clicar
no WEKA.

------------------------------------------------------------------------

# 38. Parte prática --- WEKA

## Atividade proposta

### Etapa 1 --- Importar a base

``` text
WEKA
 ↓
Explorer
 ↓
Preprocess
 ↓
Open File
```

Verificar:

-   instâncias;
-   atributos;
-   tipos;
-   valores ausentes;
-   variável-alvo.

### Etapa 2 --- Preparar os dados

Avaliar:

-   atributos desnecessários;
-   tipos incorretos;
-   campos identificadores;
-   valores ausentes;
-   necessidade de filtros.

### Etapa 3 --- Escolher a tarefa

``` text
Classificação?
ou
Regressão?
```

### Etapa 4 --- Executar

``` text
Classify
 ↓
Choose
 ↓
Algoritmo
 ↓
Test options
 ↓
Start
```

### Etapa 5 --- Interpretar

Para classificação, observar métricas apropriadas e a matriz de
confusão.

Para regressão, observar especialmente:

``` text
MAE
RAE
```

e demais métricas fornecidas pelo experimento.

------------------------------------------------------------------------

# 39. O que observar durante a demonstração

Ao executar o WEKA, não foque apenas no resultado final.

Observe o processo:

### Dataset

``` text
Quantas instâncias?
Quantos atributos?
```

### Atributos

``` text
Numeric?
Nominal?
Missing?
```

### Alvo

``` text
O que estamos tentando prever?
```

### Algoritmo

``` text
Por que ele é adequado para esta tarefa?
```

### Avaliação

``` text
Training set?
Percentage split?
Cross-validation?
```

### Resultado

``` text
Qual métrica?
O que significa?
É boa para esse problema?
```

------------------------------------------------------------------------

# 40. Erros comuns

### 1. Escolher o algoritmo antes de entender o problema

Primeiro definimos a pergunta.

### 2. Usar atributo-alvo incorreto

O modelo pode tentar prever a coluna errada.

### 3. Confundir classificação com regressão

``` text
Categoria → Classificação
Número contínuo → Regressão
```

### 4. Ignorar os tipos dos atributos

Um campo configurado incorretamente pode mudar ou impedir a análise.

### 5. Usar identificadores como se fossem características úteis

IDs frequentemente identificam registros, mas não necessariamente
carregam informação preditiva.

### 6. Avaliar apenas no treinamento

Bom desempenho no treino não garante generalização.

### 7. Olhar apenas uma métrica

Métricas precisam ser interpretadas em conjunto e no contexto.

### 8. Achar que correlação ou associação significa causalidade

Encontrar uma relação não prova que uma variável causa a outra.

------------------------------------------------------------------------

# 41. WEKA não substitui a análise

Uma ferramenta pode:

-   executar algoritmos;
-   calcular métricas;
-   criar visualizações;
-   facilitar experimentos.

Mas ela não decide sozinha:

-   qual problema importa;
-   quais dados são confiáveis;
-   quais atributos fazem sentido;
-   qual erro é aceitável;
-   se existe viés;
-   se o resultado tem valor para o negócio.

> **Ferramentas executam algoritmos. Pessoas interpretam resultados e
> tomam decisões.**

------------------------------------------------------------------------

# 42. Resumo dos principais conceitos

  Conceito             Resumo
  -------------------- ------------------------------------------------
  Mineração de Dados   descoberta de padrões e relações úteis
  KDD                  processo de descoberta de conhecimento
  Seleção              escolha dos dados relevantes
  Pré-processamento    tratamento de problemas nos dados
  Transformação        adequação dos dados
  Classificação        previsão de categorias
  Regressão            previsão de valores numéricos
  Clusterização        descoberta de grupos semelhantes
  Associação           descoberta de relações entre itens
  WEKA                 ambiente para experimentação em ML/Data Mining
  ARFF                 formato nativo muito utilizado pelo WEKA
  Treino               dados utilizados para aprendizagem
  Teste                dados utilizados para avaliação
  Cross-validation     avaliação por múltiplas divisões
  Accuracy             percentual de acertos em classificação
  MAE                  erro absoluto médio
  RAE                  erro absoluto relativo a uma referência
  Overfitting          modelo aprende excessivamente o treino

------------------------------------------------------------------------

# 43. Mapa mental da aula

``` text
                    MINERAÇÃO DE DADOS
                           |
             +-------------+-------------+
             |                           |
            KDD                    APRENDIZADO
             |                           |
   +---------+---------+          +------+------+
   |         |         |          |             |
Seleção   Preparação Mineração Supervisionado Não supervisionado
                         |          |             |
                         |     +----+----+    +---+---+
                         |     |         |    |       |
                         | Classificação Regressão Cluster Associação
                         |
                       WEKA
                         |
           +-------------+-------------+
           |             |             |
       Preprocess      Classify       Avaliar
                                       |
                              +--------+--------+
                              |                 |
                           Accuracy          MAE / RAE
                              |
                         INTERPRETAÇÃO
                              |
                         CONHECIMENTO
                              |
                            DECISÃO
```

------------------------------------------------------------------------

# 44. Questões para revisão

1.  O que é Mineração de Dados?
2.  Qual é a diferença entre dados e conhecimento?
3.  O que significa KDD?
4.  Quais são as principais etapas do KDD?
5.  Por que pré-processamento é importante?
6.  Qual a diferença entre classificação e regressão?
7.  O que caracteriza aprendizado supervisionado?
8.  O que caracteriza aprendizado não supervisionado?
9.  O que é clusterização?
10. O que são regras de associação?
11. Para que serve o WEKA?
12. Qual a finalidade da aba Preprocess?
13. O que é um arquivo ARFF?
14. Por que precisamos definir corretamente a variável-alvo?
15. Qual a diferença entre treino e teste?
16. O que é validação cruzada?
17. O que significa Accuracy?
18. Por que uma Accuracy alta nem sempre significa um bom modelo?
19. O que significa MAE?
20. Como interpretar o RAE?
21. O que é overfitting?
22. Por que não devemos avaliar um modelo apenas no conjunto de
    treinamento?
23. Por que um identificador pode ser inadequado como atributo
    preditivo?
24. Qual é a importância da interpretação humana dos resultados?

------------------------------------------------------------------------

# 45. Conclusão

Nesta aula avançamos da análise tradicional para a descoberta de
padrões.

O processo começa com uma pergunta relevante e passa por seleção,
preparação e transformação dos dados. Em seguida, escolhemos uma tarefa
adequada --- como classificação, regressão, agrupamento ou associação
--- e aplicamos algoritmos.

O WEKA permite experimentar essas técnicas de forma visual e didática.

Mas executar um algoritmo é apenas parte do trabalho.

Precisamos avaliar os resultados, compreender as métricas e interpretar
o modelo dentro do contexto do problema.

``` text
DADOS
  ↓
PREPARAÇÃO
  ↓
ALGORITMOS
  ↓
MODELOS
  ↓
AVALIAÇÃO
  ↓
PADRÕES
  ↓
CONHECIMENTO
  ↓
DECISÃO
```

> **Mineração de Dados não é simplesmente executar algoritmos. É
> transformar dados em descobertas que possam gerar conhecimento.**

------------------------------------------------------------------------

# 🧪 Roteiro rápido para o laboratório

``` text
1. Abrir o WEKA
2. Selecionar Explorer
3. Acessar Preprocess
4. Importar CSV/ARFF
5. Inspecionar atributos
6. Corrigir/preparar os dados
7. Definir variável-alvo
8. Abrir Classify
9. Escolher o algoritmo
10. Definir Cross-validation ou Percentage Split
11. Executar Start
12. Localizar as métricas
13. Interpretar os resultados
14. Comparar modelos
15. Relacionar o resultado ao problema
```

------------------------------------------------------------------------

# 🎯 Para lembrar

``` text
CLASSIFICAÇÃO
      ↓
Prevê uma CATEGORIA
```

``` text
REGRESSÃO
      ↓
Prevê um VALOR NUMÉRICO
```

``` text
ACCURACY
      ↓
Percentual de ACERTOS
      ↓
Maior geralmente é melhor
```

``` text
MAE
      ↓
Erro absoluto MÉDIO
      ↓
Menor é melhor
```

``` text
RAE
      ↓
Erro em relação a uma REFERÊNCIA
      ↓
Menor é melhor
```

------------------------------------------------------------------------

## 👨‍🏫 Professor

**Professor Rodolfo Terra**\
**Disciplina:** Banco de Dados e Mineração de Dados

-   LinkedIn: https://www.linkedin.com/in/rodolffoterra/
-   GitHub: https://github.com/rodolffoterra

------------------------------------------------------------------------

> **"Os dados mostram o que aconteceu. A Mineração de Dados nos ajuda a
> descobrir padrões que podem explicar comportamentos e apoiar o que
> faremos a seguir."**
