# Lexer Errors
class LexerError(Exception):
    """Base class for exceptions in this module."""
    pass

class CharacterError(LexerError):
    """Exception raised for errors in the input.

    Attributes:
        expr -- input expression in which the error occurred
        msg  -- explanation of the error
    """

    def __init__(self, msg):
        self.msg = "Invalid Character: " + msg
