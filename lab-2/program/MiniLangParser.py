# Generated from program/MiniLang.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,22,65,2,0,7,0,2,1,7,1,2,2,7,2,1,0,4,0,8,8,0,11,0,12,0,9,1,1,
        1,1,1,1,1,1,4,1,16,8,1,11,1,12,1,17,1,1,1,1,4,1,22,8,1,11,1,12,1,
        23,3,1,26,8,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,
        1,40,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,49,8,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,5,2,60,8,2,10,2,12,2,63,9,2,1,2,0,1,4,3,0,2,
        4,0,3,1,0,4,5,1,0,6,7,1,0,8,13,73,0,7,1,0,0,0,2,39,1,0,0,0,4,48,
        1,0,0,0,6,8,3,2,1,0,7,6,1,0,0,0,8,9,1,0,0,0,9,7,1,0,0,0,9,10,1,0,
        0,0,10,1,1,0,0,0,11,12,5,16,0,0,12,13,3,4,2,0,13,15,5,17,0,0,14,
        16,3,2,1,0,15,14,1,0,0,0,16,17,1,0,0,0,17,15,1,0,0,0,17,18,1,0,0,
        0,18,25,1,0,0,0,19,21,5,18,0,0,20,22,3,2,1,0,21,20,1,0,0,0,22,23,
        1,0,0,0,23,21,1,0,0,0,23,24,1,0,0,0,24,26,1,0,0,0,25,19,1,0,0,0,
        25,26,1,0,0,0,26,27,1,0,0,0,27,28,5,19,0,0,28,29,5,20,0,0,29,40,
        1,0,0,0,30,31,3,4,2,0,31,32,5,20,0,0,32,40,1,0,0,0,33,34,5,14,0,
        0,34,35,5,1,0,0,35,36,3,4,2,0,36,37,5,20,0,0,37,40,1,0,0,0,38,40,
        5,20,0,0,39,11,1,0,0,0,39,30,1,0,0,0,39,33,1,0,0,0,39,38,1,0,0,0,
        40,3,1,0,0,0,41,42,6,2,-1,0,42,43,5,2,0,0,43,44,3,4,2,0,44,45,5,
        3,0,0,45,49,1,0,0,0,46,49,5,15,0,0,47,49,5,14,0,0,48,41,1,0,0,0,
        48,46,1,0,0,0,48,47,1,0,0,0,49,61,1,0,0,0,50,51,10,5,0,0,51,52,7,
        0,0,0,52,60,3,4,2,6,53,54,10,4,0,0,54,55,7,1,0,0,55,60,3,4,2,5,56,
        57,10,1,0,0,57,58,7,2,0,0,58,60,3,4,2,2,59,50,1,0,0,0,59,53,1,0,
        0,0,59,56,1,0,0,0,60,63,1,0,0,0,61,59,1,0,0,0,61,62,1,0,0,0,62,5,
        1,0,0,0,63,61,1,0,0,0,8,9,17,23,25,39,48,59,61
    ]

class MiniLangParser ( Parser ):

    grammarFileName = "MiniLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'('", "')'", "'*'", "'/'", "'+'", 
                     "'-'", "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", 
                     "<INVALID>", "<INVALID>", "'if'", "'then'", "'else'", 
                     "'endif'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "MUL", "DIV", "ADD", "SUB", "EQ", "NEQ", "LT", "GT", 
                      "LEQ", "GEQ", "ID", "INT", "IF", "THEN", "ELSE", "ENDIF", 
                      "NEWLINE", "WS", "LINE_COMMENT" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_expr = 2

    ruleNames =  [ "prog", "stat", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    MUL=4
    DIV=5
    ADD=6
    SUB=7
    EQ=8
    NEQ=9
    LT=10
    GT=11
    LEQ=12
    GEQ=13
    ID=14
    INT=15
    IF=16
    THEN=17
    ELSE=18
    ENDIF=19
    NEWLINE=20
    WS=21
    LINE_COMMENT=22

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.StatContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.StatContext,i)


        def getRuleIndex(self):
            return MiniLangParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = MiniLangParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 7 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 6
                self.stat()
                self.state = 9 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 1163268) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniLangParser.RULE_stat

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class BlankContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NEWLINE(self):
            return self.getToken(MiniLangParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlank" ):
                listener.enterBlank(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlank" ):
                listener.exitBlank(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlank" ):
                return visitor.visitBlank(self)
            else:
                return visitor.visitChildren(self)


    class IfContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IF(self):
            return self.getToken(MiniLangParser.IF, 0)
        def expr(self):
            return self.getTypedRuleContext(MiniLangParser.ExprContext,0)

        def THEN(self):
            return self.getToken(MiniLangParser.THEN, 0)
        def ENDIF(self):
            return self.getToken(MiniLangParser.ENDIF, 0)
        def NEWLINE(self):
            return self.getToken(MiniLangParser.NEWLINE, 0)
        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.StatContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.StatContext,i)

        def ELSE(self):
            return self.getToken(MiniLangParser.ELSE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf" ):
                listener.enterIf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf" ):
                listener.exitIf(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf" ):
                return visitor.visitIf(self)
            else:
                return visitor.visitChildren(self)


    class PrintExprContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(MiniLangParser.ExprContext,0)

        def NEWLINE(self):
            return self.getToken(MiniLangParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintExpr" ):
                listener.enterPrintExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintExpr" ):
                listener.exitPrintExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintExpr" ):
                return visitor.visitPrintExpr(self)
            else:
                return visitor.visitChildren(self)


    class AssignContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(MiniLangParser.ID, 0)
        def expr(self):
            return self.getTypedRuleContext(MiniLangParser.ExprContext,0)

        def NEWLINE(self):
            return self.getToken(MiniLangParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)



    def stat(self):

        localctx = MiniLangParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        self._la = 0 # Token type
        try:
            self.state = 39
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                localctx = MiniLangParser.IfContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 11
                self.match(MiniLangParser.IF)
                self.state = 12
                self.expr(0)
                self.state = 13
                self.match(MiniLangParser.THEN)
                self.state = 15 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 14
                    self.stat()
                    self.state = 17 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 1163268) != 0)):
                        break

                self.state = 25
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==18:
                    self.state = 19
                    self.match(MiniLangParser.ELSE)
                    self.state = 21 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 20
                        self.stat()
                        self.state = 23 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 1163268) != 0)):
                            break



                self.state = 27
                self.match(MiniLangParser.ENDIF)
                self.state = 28
                self.match(MiniLangParser.NEWLINE)
                pass

            elif la_ == 2:
                localctx = MiniLangParser.PrintExprContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 30
                self.expr(0)
                self.state = 31
                self.match(MiniLangParser.NEWLINE)
                pass

            elif la_ == 3:
                localctx = MiniLangParser.AssignContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 33
                self.match(MiniLangParser.ID)
                self.state = 34
                self.match(MiniLangParser.T__0)
                self.state = 35
                self.expr(0)
                self.state = 36
                self.match(MiniLangParser.NEWLINE)
                pass

            elif la_ == 4:
                localctx = MiniLangParser.BlankContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 38
                self.match(MiniLangParser.NEWLINE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniLangParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ParensContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(MiniLangParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParens" ):
                listener.enterParens(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParens" ):
                listener.exitParens(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParens" ):
                return visitor.visitParens(self)
            else:
                return visitor.visitChildren(self)


    class MulDivContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.ExprContext,i)

        def MUL(self):
            return self.getToken(MiniLangParser.MUL, 0)
        def DIV(self):
            return self.getToken(MiniLangParser.DIV, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDiv" ):
                listener.enterMulDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDiv" ):
                listener.exitMulDiv(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDiv" ):
                return visitor.visitMulDiv(self)
            else:
                return visitor.visitChildren(self)


    class AddSubContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.ExprContext,i)

        def ADD(self):
            return self.getToken(MiniLangParser.ADD, 0)
        def SUB(self):
            return self.getToken(MiniLangParser.SUB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSub" ):
                listener.enterAddSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSub" ):
                listener.exitAddSub(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSub" ):
                return visitor.visitAddSub(self)
            else:
                return visitor.visitChildren(self)


    class IdContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(MiniLangParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId" ):
                listener.enterId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId" ):
                listener.exitId(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId" ):
                return visitor.visitId(self)
            else:
                return visitor.visitChildren(self)


    class IntContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(MiniLangParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt" ):
                listener.enterInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt" ):
                listener.exitInt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt" ):
                return visitor.visitInt(self)
            else:
                return visitor.visitChildren(self)


    class CompContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.ExprContext,i)

        def EQ(self):
            return self.getToken(MiniLangParser.EQ, 0)
        def NEQ(self):
            return self.getToken(MiniLangParser.NEQ, 0)
        def LT(self):
            return self.getToken(MiniLangParser.LT, 0)
        def GT(self):
            return self.getToken(MiniLangParser.GT, 0)
        def LEQ(self):
            return self.getToken(MiniLangParser.LEQ, 0)
        def GEQ(self):
            return self.getToken(MiniLangParser.GEQ, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComp" ):
                listener.enterComp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComp" ):
                listener.exitComp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComp" ):
                return visitor.visitComp(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniLangParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                localctx = MiniLangParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 42
                self.match(MiniLangParser.T__1)
                self.state = 43
                self.expr(0)
                self.state = 44
                self.match(MiniLangParser.T__2)
                pass
            elif token in [15]:
                localctx = MiniLangParser.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 46
                self.match(MiniLangParser.INT)
                pass
            elif token in [14]:
                localctx = MiniLangParser.IdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 47
                self.match(MiniLangParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 61
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 59
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                    if la_ == 1:
                        localctx = MiniLangParser.MulDivContext(self, MiniLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 50
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 51
                        _la = self._input.LA(1)
                        if not(_la==4 or _la==5):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 52
                        self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = MiniLangParser.AddSubContext(self, MiniLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 53
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 54
                        _la = self._input.LA(1)
                        if not(_la==6 or _la==7):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 55
                        self.expr(5)
                        pass

                    elif la_ == 3:
                        localctx = MiniLangParser.CompContext(self, MiniLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 56
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 57
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 16128) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 58
                        self.expr(2)
                        pass

             
                self.state = 63
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 1)
         




