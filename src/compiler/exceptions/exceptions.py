# Lexer Errors
class LexerError(Exception):
    """Base class for exceptions in the lexer module."""
    pass

class CharacterError(LexerError):
	"""Exception raised for errors in the input.

    Attributes:
        msg  -- explanation of the error
    """

	def __init__(self, msg):
		self.msg = "Invalid Character: " + msg

# Parser Errors
class ParserError(Exception):
    """Base class for exceptions in the parser module."""
    pass

class MySyntaxError(ParserError):
    """Exception raised for syntax errors.
    Attributes:
        msg  -- explanation of the error
    """

    def __init__(self, msg):
        self.msg = "Syntax Error: " + msg

# Semantic Analysis Errors
class SemanticError(Exception):
	pass

class VariableNotDefinedError(SemanticError):
    def __init__(self, msg):
        self.msg = "Semantic Error: " + msg + " has not been defined"
