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
| TONE | Variável de mudança de tom 'tone'  |
| COMMA | Caractere de continuidade ','  |
| NEWLINE | Caractere de nova linha '\n'  |
| START | Caractere de ínicio de código '^'  |
| END | Caractere de fim de código '$'  |
| VAR | Palavra-chave de nova variável 'var' |
| ID | ID de uma variável criada (qualquer string válida depois de 'var') |
| SUM | Caractere de soma de variáveis '+' |
| MINUS | Caractere de substração de variáveis '-'  |
| MULTIPLY | Caractere de multiplicação de variáveis '*'  |
| AMPERSAND | Caractere de append de variáveis '&'  |
| SEQUENCE | Declaração de uma label  |
| ENDSEQUENCE | Fim da declaração de uma label  |
| CALL | Chamada de uma label  |
| REPEAT | Declaração de um loop  |
| ENDREPEAT | Fim da declaração de um loop  |

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
| statement -> label |
| param -> AMP TWOPOINTS INT |
| param -> AMP TWOPOINTS ID |
| param -> DUR TWOPOINTS INT |
| param -> DUR TWOPOINTS ID |
| param -> TONE TWOPOINTS INT |
| param -> TONE TWOPOINTS ID |
| param -> INSTR TWOPOINTS INT |
| param -> CALL TWOPOINTS ID |
| command -> command COMMA param |
| playcontent -> LBRACKET seqexp RBRACKET |
| playcontent -> ID |
| playcontent -> acc |
| command -> PLAY TWOPOINTS playcontent |
| assignation -> VAR ID TWOPOINTS exp |
| exp -> LBRACKET seqsound RBRACKET rec_op |
| exp -> nota rec_op |
| exp -> acc rec_op |
| rec_op -> SUM exp |
| rec_op -> MINUS exp |
| rec_op -> AMPERSAND exp |
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
| loop -> REPEAT INT TWOPOINTS NEWLINE program ENDREPEAT |
| label -> SEQUENCE ID TWOPOINTS NEWLINE program ENDSEQUENCE |