## Testes

Para realizar testes do compilador foi utilizado o UnitTests, uma biblioteca de Python simples para realizar testes unitários de código.

```
data = '''
3 + 4 * 10
  + -20 *2
'''
tokens = ['3', '+', '4', '*', '10', '+', "-", '20', '*', '2']


class CalcTest(unittest.TestCase):
    def test_calc(self):
        # Give the lexer some input
        calclex.lexer.input(data)
        # Tokenize
        for t in tokens:
            tok = calclex.lexer.token()
            self.assertEquals(t, str(tok.value))


if __name__ == '__main__':
    unittest.main()
```

Acima podemos ver um exemplo de uso para testar um lexer para uma calculadora simples. Criamos uma classe que deriva de unittest.TestCase e dentro dela temos definições de métodos que sempre começam 
com a palavra "test". Deste modo, quando chamamos unittest.main(), a framework irá procurar todos estes métodos para roá-los.

Para garantir um estado de sucesso e falha, podemos utilizar as funções de assert do unittest. Elas servem para compararmos resultados com o que esperamos de saida. Também é possivel 
esperar que um erro aconteça para podermos verificar se o programa está jogando os erros esperados.

Abaixo podemos ver os testes que foram feitos para cada um dos passos do compilador:

 1. __Lexer__
    * Test 1: regular program.
    * Test 2: like test 1, with empty spaces added.
    * Test 3: like test 1, with multiple '\t' added.
    * Test 4: like test 1, with a variable using ALL characters permitted in Apollo.
    * Test 5: contains invalid character '#'. Should raise exception CharacterError
 2. __Parser__
    * Test 1: regular program.
    * Test 2: like test 1, with empty spaces added.
    * Test 3: like test 1, with a variable using '[]' instead of '()'.
    * Test 4: uses '[]' inside of a '()'. Should raise exception MySyntaxError.
    * Test 5: doesn't contain a needed character ']'. Should raise exception MySyntaxError.
 3. __Semantic Analisys__
    * Test 1: regular program.
    * Test 2: use undefined variable inside play. Should raise VariableNotDefinedError.
    * Test 3: use undefined variable inside another variable. Should raise VariableNotDefinedError.
    * Test 4: use variable that stores a sequence inside a chord. Should raise SequenceInsideAccError.
 4. __Code Generation__
    * Tests 1-3: regular programs.