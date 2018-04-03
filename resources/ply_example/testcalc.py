import calclex
import unittest

# Test it out
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
