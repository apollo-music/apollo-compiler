# Lexer

## Tokens usados em Apollo

| Token | Descrição  |
|---|---|
| INT | Número inteiro  |
| PLAY | Função "play"  |
| TWOPOINTS | Caractere de associação ':'  |
| LBRACKET | Caractere de início de sequência '['  |
| RBRACKET | Caractere de fim de sequência ']'  |
| LPAREN | Caractere de início de acorde '('  |
| RPAREN | Caractere de fim de acorde ')'  |
| AMP | Variável de amplificação 'amp'  |
| DUR | Variável de duração de notas 'dur'  |
| COMMA | Caractere de continuidade ','  |
| NEWLINE | Caractere de nova linha '\n'  |
| START | Caractere de ínicio de código '^'  |
| END | Caractere de fim de código '$'  |
| VAR | Palavra-chave de nova variável 'var' |
| ID | ID de uma variável criada (qualquer string válida depois de 'var') |
| SUM | Caractere de soma de variáveis '+' |
| MINUS | Caractere de substração de variáveis '-'  |
| MULTIPLY | Caractere de multiplicação de variáveis '*'  |

# Parser

## Elementos do Parser de Apollo

| Elemento | Descrição |
|---|---|
| program2 | Todas as linhas de código entre os caracteres de START e END |
| program | Conjunto de linhas de código |
| statement | Gramática para qualquer frase na linha do programa  |
| param | Gramática para atribuição de novos valores à constantes musicais |
| command | Gramática para executar a função "play" com uma sequência de notas |
| assignation | Gramática para atribuição de uma variável à um valor inteiro ou sequência de notas |
| expression | Conjunto de acordes em sequência |
| acc | Qualquer número de notas tocadas juntas (uma ou mais notas) |
| seqnotas | Sequência de notas separadas pelo Token COMMA |
| nota | Nota individual (ID, INT ou resultado de uma operação) |

## Regras gramaticais

| Elemento | Regra |
|---|---|
| program2 | START NEWLINE program END NEWLINE |
| program | statement NEWLINE |
| program | statement NEWLINE program |
| statement | command \| param \| assignation |
| param | AMP TWOPOINTS INT |
| param | DUR TWOPOINTS INT |
| command | command COMMA param |
| command | PLAY TWOPOINTS LBRACKET expression RBRACKET |
| assignation | VAR ID TWOPOINTS LBRACKET expression RBRACKET |
| assignation | VAR ID TWOPOINTS acc |
| expression | acc |
| expression | acc COMMA expression |
| acc | LPAREN seqnotas RPAREN |
| acc | nota |
| seqnotas | nota |
| seqnotas | nota COMMA seqnotas |
| nota | nota SUM nota \| nota MINUS nota \| nota MULTIPLY nota |
| nota | INT |
| nota | ID |