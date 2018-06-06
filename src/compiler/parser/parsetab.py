
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AMP AMPERSAND CALL COMMA CUE DUR END ENDREPEAT ENDSEQUENCE ENDTRACK EQUAL ID INSTR INT LBRACKET LPAREN MINUS MULTIPLY NEWLINE PLAY RBRACKET REPEAT RPAREN SEQUENCE SLEEP START SUM SYNC TONE TRACK TWOPOINTS VARprogram2 : START NEWLINE program ENDprogram : statement NEWLINEprogram : statement NEWLINE programstatement : command\n\t\t| param\n\t\t| assignation\n\t\t| loop\n\t\t| sequence\n\t\t| trackparam : AMP EQUAL INT\n\t| AMP EQUAL IDparam : DUR EQUAL INT\n\t| DUR EQUAL IDparam : INSTR EQUAL INTparam : TONE EQUAL INT\n\t| TONE EQUAL IDparam : SLEEP EQUAL INT\n\t| SLEEP EQUAL IDparam : CALL TWOPOINTS IDcommand : command COMMA paramcommand : PLAY TWOPOINTS playcontentplaycontent : LBRACKET seqexp RBRACKETplaycontent : IDplaycontent : accassignation : VAR ID EQUAL expexp : LBRACKET seqsound RBRACKET rec_opexp : nota rec_opexp : acc rec_opseqexp : exp COMMA seqexpseqexp : exprec_op : rec_op : SUM exprec_op : MINUS exprec_op : AMPERSAND expseqsound : sound COMMA seqsoundseqsound : soundsound : acc\n\t| notaacc : LPAREN seqnotas RPARENseqnotas : notaseqnotas : nota COMMA seqnotasnota : INTnota : IDloop : REPEAT INT TWOPOINTS NEWLINE program ENDREPEATsequence : SEQUENCE ID TWOPOINTS NEWLINE program ENDSEQUENCEtrack : TRACK ID TWOPOINTS NEWLINE program ENDTRACK'
    
_lr_action_items = {'START':([0,],[2,]),'$end':([1,23,],[0,-1,]),'NEWLINE':([2,5,6,7,8,9,10,11,38,39,41,42,44,45,46,47,48,49,50,51,52,53,55,56,57,61,62,63,64,67,75,77,81,82,87,90,91,92,94,95,96,97,],[3,24,-4,-5,-6,-7,-8,-9,-20,-21,-23,-24,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,68,69,70,-31,-31,-42,-43,-25,-22,-27,-28,-39,-31,-32,-33,-34,-44,-45,-46,-26,]),'PLAY':([3,24,68,69,70,],[12,12,12,12,12,]),'AMP':([3,24,25,68,69,70,],[13,13,13,13,13,13,]),'DUR':([3,24,25,68,69,70,],[14,14,14,14,14,14,]),'INSTR':([3,24,25,68,69,70,],[15,15,15,15,15,15,]),'TONE':([3,24,25,68,69,70,],[16,16,16,16,16,16,]),'SLEEP':([3,24,25,68,69,70,],[17,17,17,17,17,17,]),'CALL':([3,24,25,68,69,70,],[18,18,18,18,18,18,]),'VAR':([3,24,68,69,70,],[19,19,19,19,19,]),'REPEAT':([3,24,68,69,70,],[20,20,20,20,20,]),'SEQUENCE':([3,24,68,69,70,],[21,21,21,21,21,]),'TRACK':([3,24,68,69,70,],[22,22,22,22,22,]),'END':([4,24,37,],[23,-2,-3,]),'COMMA':([6,38,39,41,42,44,45,46,47,48,49,50,51,52,53,60,61,62,63,64,66,72,73,74,75,77,81,82,87,90,91,92,97,],[25,-20,-21,-23,-24,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,76,-31,-31,-42,-43,83,88,-37,-38,-22,-27,-28,-39,-31,-32,-33,-34,-26,]),'TWOPOINTS':([12,18,34,35,36,],[26,32,55,56,57,]),'EQUAL':([13,14,15,16,17,33,],[27,28,29,30,31,54,]),'ID':([19,21,22,26,27,28,30,31,32,40,43,54,58,76,78,79,80,83,88,],[33,35,36,41,45,47,50,52,53,64,64,64,64,64,64,64,64,64,64,]),'INT':([20,27,28,29,30,31,40,43,54,58,76,78,79,80,83,88,],[34,44,46,48,49,51,63,63,63,63,63,63,63,63,63,63,]),'ENDREPEAT':([24,37,84,],[-2,-3,94,]),'ENDSEQUENCE':([24,37,85,],[-2,-3,95,]),'ENDTRACK':([24,37,86,],[-2,-3,96,]),'LBRACKET':([26,40,54,76,78,79,80,],[40,58,58,58,58,58,58,]),'LPAREN':([26,40,54,58,76,78,79,80,88,],[43,43,43,43,43,43,43,43,43,]),'RBRACKET':([59,60,61,62,63,64,71,72,73,74,77,81,82,87,89,90,91,92,97,98,],[75,-30,-31,-31,-42,-43,87,-36,-37,-38,-27,-28,-39,-31,-29,-32,-33,-34,-26,-35,]),'SUM':([61,62,63,64,82,87,],[78,78,-42,-43,-39,78,]),'MINUS':([61,62,63,64,82,87,],[79,79,-42,-43,-39,79,]),'AMPERSAND':([61,62,63,64,82,87,],[80,80,-42,-43,-39,80,]),'RPAREN':([63,64,65,66,93,],[-42,-43,82,-40,-41,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program2':([0,],[1,]),'program':([3,24,68,69,70,],[4,37,84,85,86,]),'statement':([3,24,68,69,70,],[5,5,5,5,5,]),'command':([3,24,68,69,70,],[6,6,6,6,6,]),'param':([3,24,25,68,69,70,],[7,7,38,7,7,7,]),'assignation':([3,24,68,69,70,],[8,8,8,8,8,]),'loop':([3,24,68,69,70,],[9,9,9,9,9,]),'sequence':([3,24,68,69,70,],[10,10,10,10,10,]),'track':([3,24,68,69,70,],[11,11,11,11,11,]),'playcontent':([26,],[39,]),'acc':([26,40,54,58,76,78,79,80,88,],[42,62,62,73,62,62,62,62,73,]),'seqexp':([40,76,],[59,89,]),'exp':([40,54,76,78,79,80,],[60,67,60,90,91,92,]),'nota':([40,43,54,58,76,78,79,80,83,88,],[61,66,61,74,61,61,61,61,66,74,]),'seqnotas':([43,83,],[65,93,]),'seqsound':([58,88,],[71,98,]),'sound':([58,88,],[72,72,]),'rec_op':([61,62,87,],[77,81,97,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program2","S'",1,None,None,None),
  ('program2 -> START NEWLINE program END','program2',4,'p_program2','apollo_yacc.py',17),
  ('program -> statement NEWLINE','program',2,'p_program_statement_newline','apollo_yacc.py',21),
  ('program -> statement NEWLINE program','program',3,'p_program_statement_program','apollo_yacc.py',25),
  ('statement -> command','statement',1,'p_statement','apollo_yacc.py',29),
  ('statement -> param','statement',1,'p_statement','apollo_yacc.py',30),
  ('statement -> assignation','statement',1,'p_statement','apollo_yacc.py',31),
  ('statement -> loop','statement',1,'p_statement','apollo_yacc.py',32),
  ('statement -> sequence','statement',1,'p_statement','apollo_yacc.py',33),
  ('statement -> track','statement',1,'p_statement','apollo_yacc.py',34),
  ('param -> AMP EQUAL INT','param',3,'p_param_AMP','apollo_yacc.py',38),
  ('param -> AMP EQUAL ID','param',3,'p_param_AMP','apollo_yacc.py',39),
  ('param -> DUR EQUAL INT','param',3,'p_param_DUR','apollo_yacc.py',43),
  ('param -> DUR EQUAL ID','param',3,'p_param_DUR','apollo_yacc.py',44),
  ('param -> INSTR EQUAL INT','param',3,'p_param_INSTR','apollo_yacc.py',48),
  ('param -> TONE EQUAL INT','param',3,'p_param_TONE','apollo_yacc.py',52),
  ('param -> TONE EQUAL ID','param',3,'p_param_TONE','apollo_yacc.py',53),
  ('param -> SLEEP EQUAL INT','param',3,'p_param_SLEEP','apollo_yacc.py',57),
  ('param -> SLEEP EQUAL ID','param',3,'p_param_SLEEP','apollo_yacc.py',58),
  ('param -> CALL TWOPOINTS ID','param',3,'p_param_CALL','apollo_yacc.py',62),
  ('command -> command COMMA param','command',3,'p_command_param','apollo_yacc.py',66),
  ('command -> PLAY TWOPOINTS playcontent','command',3,'p_command_PLAY','apollo_yacc.py',70),
  ('playcontent -> LBRACKET seqexp RBRACKET','playcontent',3,'p_playcontent_seqexp','apollo_yacc.py',74),
  ('playcontent -> ID','playcontent',1,'p_playcontent_ID','apollo_yacc.py',78),
  ('playcontent -> acc','playcontent',1,'p_playcontent_acc','apollo_yacc.py',82),
  ('assignation -> VAR ID EQUAL exp','assignation',4,'p_assignation_expression','apollo_yacc.py',86),
  ('exp -> LBRACKET seqsound RBRACKET rec_op','exp',4,'p_expression_seq','apollo_yacc.py',90),
  ('exp -> nota rec_op','exp',2,'p_expression_nota','apollo_yacc.py',94),
  ('exp -> acc rec_op','exp',2,'p_expression_acc','apollo_yacc.py',98),
  ('seqexp -> exp COMMA seqexp','seqexp',3,'p_seqexp_comma','apollo_yacc.py',102),
  ('seqexp -> exp','seqexp',1,'p_seqexp','apollo_yacc.py',106),
  ('rec_op -> <empty>','rec_op',0,'p_recursive_op_empty','apollo_yacc.py',110),
  ('rec_op -> SUM exp','rec_op',2,'p_recursive_op_sum','apollo_yacc.py',114),
  ('rec_op -> MINUS exp','rec_op',2,'p_recursive_op_minus','apollo_yacc.py',118),
  ('rec_op -> AMPERSAND exp','rec_op',2,'p_recursive_op_ampersand','apollo_yacc.py',122),
  ('seqsound -> sound COMMA seqsound','seqsound',3,'p_seqsound_comma','apollo_yacc.py',126),
  ('seqsound -> sound','seqsound',1,'p_seqsound','apollo_yacc.py',130),
  ('sound -> acc','sound',1,'p_sound','apollo_yacc.py',134),
  ('sound -> nota','sound',1,'p_sound','apollo_yacc.py',135),
  ('acc -> LPAREN seqnotas RPAREN','acc',3,'p_acc_seqnotas','apollo_yacc.py',139),
  ('seqnotas -> nota','seqnotas',1,'p_seqnotas_nota','apollo_yacc.py',143),
  ('seqnotas -> nota COMMA seqnotas','seqnotas',3,'p_seqnotas_notaseqnotas','apollo_yacc.py',147),
  ('nota -> INT','nota',1,'p_nota','apollo_yacc.py',151),
  ('nota -> ID','nota',1,'p_nota_id','apollo_yacc.py',155),
  ('loop -> REPEAT INT TWOPOINTS NEWLINE program ENDREPEAT','loop',6,'p_loop_repeat','apollo_yacc.py',159),
  ('sequence -> SEQUENCE ID TWOPOINTS NEWLINE program ENDSEQUENCE','sequence',6,'p_sequence_definition','apollo_yacc.py',163),
  ('track -> TRACK ID TWOPOINTS NEWLINE program ENDTRACK','track',6,'p_track_definition','apollo_yacc.py',167),
]
