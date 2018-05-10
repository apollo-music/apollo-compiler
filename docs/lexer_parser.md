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

| Regra |
|---|
| program2 -> START program END NEWLINE |
| program -> statement NEWLINE |
| program -> statement NEWLINE program |
| statement -> command |
| statement -> param |
| statement -> assignation |
| statement -> loop |
| param -> AMP TWOPOINTS INT |
| param -> DUR TWOPOINTS INT |
| param -> INSTR TWOPOINTS INT |
| command -> command COMMA param |
| command -> PLAY TWOPOINTS LBRACKET seqsound RBRACKET |
| assignation -> VAR ID TWOPOINTS exp |
| exp -> LBRACKET seqsound RBRACKET rec_op |
| exp -> nota rec_op |
| exp -> acc rec_op |
| rec_op -> SUM exp |
| rec_op -> MINUS exp |
| rec_op -> |
| seqsound -> sound COMMA seqsound|
| seqsound -> sound |
| sound -> acc |
| sound -> nota |
| expression -> acc |
| expression -> acc COMMA expression |
| acc -> LPAREN seqnotas RPAREN |
| seqnotas -> nota |
| seqnotas -> nota COMMA seqnotas |
| nota -> INT |
| nota -> ID |