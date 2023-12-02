Desenvolvimento de um analisador léxico que reconheça expressões aritméticas e alguns comandos ao estilo da linguagem “C” e declarações ao estilo “PASCAL”;O 

# Analisador Léxico deve reconhecer os seguintes padrões:

- Delimitadores: '(', ')', '.', ',', '{', '}', ';';

- Desconsiderando brancos, sinais de tabulação '\t' e fim de linha '\n','\r';

- Números: [0-9], números com e sem sinal, com fracionário opcional, exemplos de números aceitos: 3, 98, -76, 56.34, -87.45, etc.

- Letras: [AZaz];

- Identificadores: palavras formadas por uma Letra obrigatória seguida de zero ou mais Letras e Números;

  - Exemplo: soma, teste123, a, x, a12;

- Operadores aritméticos binários: '+', '-', '*', '/', '^';

  - cada operador identificado unicamente, por exemplo, um token OP_ADD para o '+';

- Operadores relacionais binários: '>', '<', '>=', '<=', '==', '!=';

    - cada operador identificado unicamente, por exemplo, um token OP_GT para o '>';

- Palavras Reservadas: 'if', 'else', 'while', 'var', 'int', 'real', '=';

    - cada operador identificado unicamente, por exemplo, um token CM_IF para o 'if';

A entrada pode ser via dispositivo ou por arquivos. Poderá ter, ou não, uma interface de entrada e manipulação.

# O resultado da análise deve ser uma lista de lexemas+tokens, por exemplo:

Entrada: “var int a,b; if(a>0){a=34/(3.4+5)}”

Saída:

-   ‘var’ → CM_VAR
-   ‘int’ → TYPE_INT
-   ‘a’ → ID
-   ‘b’ → ID
-   ‘;’ → DELIM
-   'if' → CM_IF
-   '(' → DELIM
-   'a' → ID
-   '>' → OP_GT
-   '0' → NUM
-   ')' → DELIM
-   '{' → DELIM
-   'a' → ID
-   '=' → CM_ATRIB
-   '34' → NUM
-   '/' → OP_DIV
-   '(' → DELIM
-   '3.4' → NUM
-   '+' → OP_ADD
-   '5' → NUM
-   ')' → DELIM
-   '}' → DELIM


# Sugestão:

- podem usar qualquer linguagem de programação, desde que eu possa compilar ou executar em qualquer ambiente;

- Tentem deixar separada a função (método ou classe) que classifica os lexemas em tokens (Léxico) da função que requisita a análise (Main, por exemplo). Isto será útil na separação posterior entre Léxico e Sintático.

# Os critérios de avaliação irão levar em conta os seguintes tópicos:

- Utilização correta de uma biblioteca REGEX;

- Clareza e Legibilidade de nomes de variáveis, métodos e classes;

- Comentários e Documentação;

- Organização do Código, classes, métodos e atributos seguem uma estrutura lógica;

- Atende aos requisitos e funcionalidades especificadas;

- Boas Práticas de Codificação: convenções de estilo, indentações e formatações;

- Reusabilidade com módulos reutilizáveis.

