from ..semantic_analiser import semantic_analiser
import unittest
from ..AST import AST
from ..AST.AST import Node
from ..exceptions import exceptions

class SemTest(unittest.TestCase):
    def test_ok(self):
        semantic_analiser.run(ast_gen_ok())
        
    def test_VarNotFound(self):                
        self.assertRaises(
            exceptions.VariableNotDefinedError,
            semantic_analiser.run,
            ast_gen_var_not_found01()
            )
        self.assertRaises(
            exceptions.VariableNotDefinedError,
            semantic_analiser.run,
            ast_gen_var_not_found02()
            )

# Tests performed:
# - Test 1: regular program. Should be OK.
# - Test 2: use undefined variable inside play. Should raise VariableNotDefinedError.
# - Test 3: use undefined variable inside another variable. Should raise VariableNotDefinedError.

def run():
    suite = unittest.TestLoader().loadTestsFromTestCase(SemTest)
    unittest.TextTestRunner(verbosity=2).run(suite)


def ast_gen_ok():
    head = AST.EntryNode([
        AST.ProgramNode([
            AST.VarNode([
                AST.TokenNode('bixo'),
                AST.AccNode([
                    AST.SeqNotasNode([
                        AST.TokenNode(65),
                        AST.SeqNotasNode([
                            AST.TokenNode(66)
                        ])
                    ])
                ])
            ]),
            AST.ProgramNode([
                AST.AmpNode([AST.TokenNode(100)]),
                AST.ProgramNode([
                    AST.DurNode([AST.TokenNode(200)]),
                    AST.ProgramNode([
                        AST.CommandNode([
                            AST.DurNode([AST.TokenNode(3)]),
                            AST.CommandNode([
                                AST.AmpNode([AST.TokenNode(10)]),
                                AST.PlayNode([
                                    AST.ExpressionNode([
                                        AST.AccNode([AST.TokenNode(72)]),
                                        AST.ExpressionNode([
                                            AST.AccNode([
                                                AST.SeqNotasNode([
                                                    AST.TokenNode(60),
                                                    AST.SeqNotasNode([
                                                        AST.TokenNode(61),
                                                        AST.SeqNotasNode([
                                                            AST.TokenNode(62)
                                                        ])
                                                    ])
                                                ])
                                            ]),
                                            AST.ExpressionNode([
                                                AST.AccNode([AST.TokenNode('bixo')])
                                            ])
                                        ])
                                    ])
                                ])
                            ])
                        ])
                    ])
                ])
            ])
        ])
    ])
    return head

def ast_gen_var_not_found01():
    head = AST.EntryNode([
        AST.ProgramNode([
            AST.ProgramNode([
                AST.AmpNode([AST.TokenNode(100)]),
                AST.ProgramNode([
                    AST.DurNode([AST.TokenNode(200)]),
                    AST.ProgramNode([
                        AST.CommandNode([
                            AST.DurNode([AST.TokenNode(3)]),
                            AST.CommandNode([
                                AST.AmpNode([AST.TokenNode(10)]),
                                AST.PlayNode([
                                    AST.ExpressionNode([
                                        AST.AccNode([AST.TokenNode(72)]),
                                        AST.ExpressionNode([
                                            AST.AccNode([
                                                AST.SeqNotasNode([
                                                    AST.TokenNode(60),
                                                    AST.SeqNotasNode([
                                                        AST.TokenNode(61),
                                                        AST.SeqNotasNode([
                                                            AST.TokenNode(62)
                                                        ])
                                                    ])
                                                ])
                                            ]),
                                            AST.ExpressionNode([
                                                AST.AccNode([AST.TokenNode('bixo')])
                                            ])
                                        ])
                                    ])
                                ])
                            ])
                        ])
                    ])
                ])
            ])
        ])
    ])
    return head

def ast_gen_var_not_found02():
    head = AST.EntryNode([
        AST.ProgramNode([
            AST.VarNode([
                AST.TokenNode('bixo'),
                AST.AccNode([
                    AST.SeqNotasNode([
                        AST.TokenNode(65),
                        AST.SeqNotasNode([
                            AST.TokenNode('notDefined')
                        ])
                    ])
                ])
            ]),
            AST.ProgramNode([
                AST.AmpNode([AST.TokenNode(100)]),
                AST.ProgramNode([
                    AST.DurNode([AST.TokenNode(200)]),
                    AST.ProgramNode([
                        AST.CommandNode([
                            AST.DurNode([AST.TokenNode(3)]),
                            AST.CommandNode([
                                AST.AmpNode([AST.TokenNode(10)]),
                                AST.PlayNode([
                                    AST.ExpressionNode([
                                        AST.AccNode([AST.TokenNode(72)]),
                                        AST.ExpressionNode([
                                            AST.AccNode([
                                                AST.SeqNotasNode([
                                                    AST.TokenNode(60),
                                                    AST.SeqNotasNode([
                                                        AST.TokenNode(61),
                                                        AST.SeqNotasNode([
                                                            AST.TokenNode(62)
                                                        ])
                                                    ])
                                                ])
                                            ]),
                                            AST.ExpressionNode([
                                                AST.AccNode([AST.TokenNode('bixo')])
                                            ])
                                        ])
                                    ])
                                ])
                            ])
                        ])
                    ])
                ])
            ])
        ])
    ])
    return head