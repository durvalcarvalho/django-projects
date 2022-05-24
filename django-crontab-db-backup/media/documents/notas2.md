## Ficha de aprovação (pag. 3)

- Corrigir a data para a data de defesa do TCC 2.

## Resumo

- Por algum motivo seu texto não está mais justificado. Favor identificar qual foi a opção alterar e tornar o texto justificado novamente.
- O tempo do texto aqui também deve ser o pretérito.
- Falta incluir informações sobre os resultados obtidos (mais 2 ou 3 linhas, no máximo). Lembre-se de que o trabalho já foi desenvolvido, e o texto tem que refletir isso.
- As palavras-chave, exceto no caso de siglas, devem iniciar em minúsculas.

## Abstract

- Aplicar aqui as modificações que forem feitas no Resumo.

## Introdução

- Notas de rodapé 1, 2 e 3: colocar o link entre parêntesis e mover o ponto final para depois do fecha parêntesis.
- Nota de rodapé 4: terminar o período com ponto final.
- pág 15, parágrafo 3: remover o ponto final antes da referência que encerra o parágrafo.
- pág 16, parágrafo 2: "para mais detalhamento" -> "para um maior detalhamento"
- pág 16, parágrafo 3: após este parágrafo há um grande espaçamento. Se houver algum comando de espaçamento aqui (\newline, \\, etc), favor remover e deixar que o LaTeX posicione o texto sem este espaço

### Descrição do problema

- pág 16, parágrafo 1: "será analisado" -> "será analisada"

### Justificativa

- "que se siga" -> "que ela siga"

### Objetivos

- remover as subseções "Objetivo Geral" e "Objetivos Específicos"
- parágrafo 1: "com a pretensão" -> "com o intuito"
- parágrafo 1: "adotação" -> "adoção"

### Estrutura do Trabalho

- Antes do último parágrafo (logo após a listagem dos objetivos específicos), adicionar uma seção denominada "Estrutura do Trabalho"
- "onde é explicado" -> "onde são explicados"
- Creio que este texto ainda é remanescente do TCC 1. Favor atualizar para a estrutura atual (citar também os apêndices). Você pode citar um capítulo pelo nome usando o comando \nameref{} do LaTeX, passando o label do capítulo.

## Fundamentação Teórica

- "é introduzido" -> "é introduzida"
- Este texto também está desatualizado: são 3 seções no total. Favor atualizar este texto

### 1.1

- parágrafo 1: "humana, o" -> "humana. O"
- parágrafo 1: "Humano-Computador," -> "Humano-Computador"
- parágrafo 2: "Algum desses:" -> "Algum desses são:"

#### 1.1.1

- parágrafo 3: "particição" -> "participação"
- parágrafo 3: "como:" -> "como"
- pág 21, parágrafo 1: "sistema iterativo"? Não seria "sistema interativo"? Como há interface com usuários acredito que seja "interativo" o termo correto, mas avalie por favor a questão

#### 1.1.1.1

- Não se justifica uma divisão de texto com um único parágrafo. Retirar o texto "1.1.1.1 Inspeções por checklist", mas manter o parágrafo que se segue

### 1.2 Algoritmo Distância de Levenshtein

- Corrigir o nome da seção
- parágrafo 2: $O(m * n)$ -> $O(mn)$
- Remover a última frase, terminando em "tamanho das strings"
- Em seguida, adicionar um ou dois parágrafos, explicando o algoritmo à luz da programação dinâmica: quais seriam os casos base e quais são as transições. No material de TEP você vai achar esta abordagem. Pode se basear nele para isso
- Depois você volta com a frase que foi removida, falando da implementação, e a coloque aqui mesmo no texto, e não no Apêndice I. O \caption{} do Código deve vir na parte superior, como nas tabelas. Após esta modificação o Apẽndice pode ser removido

### 1.3 Guias, manuais e recomendações de desenvolvimento de CLIs

- Esta seção tem maior proximidade semântica com a Seção 1.1 do que a atual 1.2. Troque esta seção de posição com a antiga 1.2, para que esta siga a 1.1, e a parte de Levensthein fique como Seção 1.3 no final
- pág. 22, primeira linha: ", sendo brevemente ... escrito" -> ": o Apêndice A traz um breve histórico da evolução das CLIs."
- parágrafo 1: "de comando, no entanto elas" -> "de comando. No entanto, elas"
- parágrafo 2: "parâmetro" -> "parâmetros"

### 1.3.1 Standards ...

- Bullets: iniciar em minúscula e terminar com ponto-e-vírgula (exceto o último que termina com ponto final)
- primeiro bullet: "\textit{getopt\_long}" -> "\texttt{getopt\_long()}: para elementos de código, use sempre fonte monoespacada. No caso de funções e rotinas, use um par de parêntesis para enfatizar isso
- segundo bullet: fonte monoespaçada para --version

### 1.3.2 POSIX ...

- "POSIX, algumas" -> "POSIX. Algumas"
- primeiro bullet: usar fonte monoespaçada nos nomes dos programas (cat, ls, etc)
- segundo bullet: a mesma coisa aqui para bash, fish, etc
- pág 23, parágrafo 1: "trabalho, dessa forma ... escrito" -> "trabalho: consulte o Apêndice A para mais detalhes sobre a execução no terminal."
- pág 23, parágrafo 2: terminar com ponto final.
- Notas de rodapé 4 e 5: links entre parêntesis, terminar com ponto final
- Código 1: o \caption{} deve vir na parte superior do código
- bullets 3, 4 e 5: acertar as aspas simples: crase para a esquerda, ' para a direita
- bullet 6: "devem" -> "deve"
- Notas de rodapé 6, 7 e 8: links entre parêntesis, terminar com ponto final

### 1.3.3 CLI ...

- "dos 15 grupos seguintes:" -> "dos seguintes 15 grupos"
- Esta seção termina de forma abrupta. Seria interessante adicionar mais um parágrafo ou dois destacando os principais grupos e ilustrando, dentre eles, algumas boas práticas (como elas são redigidas e detalhadas, por exemplo)

## Metodologia

- "seção" -> "Seção" (ao referenciar um elemento do texto, ele deve vir em maiúscula: Seção, Capítulo, Tabela, Figura, Código, etc)

### 2.1 Levantamento...

- Tabela 1:
    * usar negrito no nome das colunas
    * terminar a tabela com uma linha horizontal

### 2.2 Materiais e métodos

- Tabela 2: na verdade este é um quadro: há um ambiente para quadros no ABNTex2. Se não tiver no seu modelo a gente arruma na reunião da sexta
- pág 28: "foi realizado" -> "foram realizados"
- Citar nominalmente o mantenedor do projeto, para que não fiquem dúvidas para o leitor
- Vale citar também que, durante a primeira metade do trabalho, o Falcão participava das reuniões

### 2.3 Desenho ...

- bullets: terminar a última com ponto final

## Resultados

- "seção" -> "Seção"
- "será mostrado" -> "serão mostrados"
- "é apresentado os" -> "serão apresentados os"
- "é apresentado as" -> "serão apresentadas as"

### 3.1 Manual

- parágrafo 2
    * "é detalhado e exemplificado" -> "são detalhados e exemplificados"
    * "é apresentado as" -> "são apresentadas as"o

### 3.2 Checklist

- parágrafo 1
    * lembre-se de que tempo verbal do texto é o pretérito. "irá auxiliar", na verdade, de ser "auxiliou". Ajustar todo o texto
    * "a columna" -> "as colunas"
    * "cuja função é" -> "cujas funções são"
    * "inspeção." -> "inspeção, respectivamente.

- parágrafo 2
    * "foi evidenciado" -> "foram evidenciadas"
    * "do do" -> ""
        

### 3.3 Relatório ...

- "foi de" -> "era o de"

### 3.4 Inconformidades ...

- "evidenciava" -> "evidenciavam"
- "foi realizado" -> "foi elaborada"
- Tabela 3:
    * rótulo: "prátics não estão" -> "práticas que não estão"
    * linha 3: usar fonte monoespaçada em -h e --help
    * linha 5: wildcards deve ir im itálico
- pag. 33, parágrafo 1:
    * "foram evidenciado" -> "foram identificadas"
    * "atendidas," -> "atendidas"

### 3.5 Ações corretivas
