# L3Pu5 Hare
# This is a simple python interpreter for the Oolang Language
#  https://esolangs.org/wiki/OOLANG

# Lexer -> Tokens -> Compiler/Interpret
from enum import Enum


sampleCode = """i.99.set;i.2int;k.1.set;k.2int;i.k.add;i.get;i.dec;i.get;
"""

class VirtualMachine:
    Tokens = []
    Index = 0
    Variables = {}

    def __init__(self):
        self.Tokens = []
        self.Index = 0
        self.Variables = {}
    
    def SetTokens(self, tokens):
        self.Tokens = tokens
    
    def DoToken(self):
        # Evaluate the Token
        thisToken = self.Tokens[self.Index]
        match thisToken.Type:
            case TokenType.SET:
                self.Variables[ thisToken.Parts[0] ] = thisToken.Parts[1]
            case TokenType.GET:
                print( self.Variables[ thisToken.Parts[0] ])
            case TokenType.TO_INT:
                self.Variables [ thisToken.Parts[0]] = int(self.Variables [ thisToken.Parts[0]]) 
            case TokenType.ADD:
                self.Variables[ thisToken.Parts[0] ] += self.Variables[ thisToken.Parts[1] ]  
            case TokenType.DEC:
                self.Variables[ thisToken.Parts[0] ] -= 1
            case TokenType.INC:
                self.Variables[ thisToken.Parts[0] ] += 1
        # Increment the Index
        self.Index += 1


class TokenType(Enum):
    UNDEFINED = 0
    PRINT = 1
    PRINTLN = 2
    IN = 3
    SET = 4
    GET = 5
    INC = 6
    DEC = 7
    TO_INT = 8
    TO_STR = 9
    ADD = 10
    SUB = 11
    MUL = 12
    DIV = 13
    STRSPLIT = 14
    STRCAT = 15
    STRLEN = 16
    LABEL = 17
    GOTO = 18

    def FromString(string):
        Translator = {
            "print":TokenType.PRINT,
            "println": TokenType.PRINTLN,
            "in": TokenType.IN,
            "set":  TokenType.SET,
            "get": TokenType.GET,
            "dec": TokenType.DEC,
            "inc": TokenType.INC,
            "2str": TokenType.TO_STR,
            "2int": TokenType.TO_INT,
            "add": TokenType.ADD,
            "sub": TokenType.SUB,
            "mul": TokenType.MUL,
            "div": TokenType.DIV,
            "strsplit": TokenType.STRSPLIT,
            "strcat": TokenType.STRCAT,
            "strlen": TokenType.STRLEN,
            "label": TokenType.LABEL,
            "goto": TokenType.GOTO,
        }
        if string in Translator:
            return Translator[string]
        else:
            print("Error: TokenType not identified.")
            return TokenType.UNDEFINED


class Token:
    Type = TokenType.UNDEFINED
    Parts = []

    def __init__(self, tokenType, tokenParts):
        self.Type = tokenType
        self.Parts = tokenParts


def parseTokens(tokens):
    tokenObjects = []
    for token in tokens:
        # i.99.set
        parts = token.split('.')
        # [i, 99, 'set']
        type = TokenType.FromString(parts[-1])
        if type == TokenType.UNDEFINED:
            pass
        else:
            tokenObjects.append( Token(type, parts ))
    return tokenObjects


def lex(code): 
    tokens = code.replace('\n', '').split(';')
    return tokens


tokens = lex(sampleCode)
tokens = parseTokens(tokens)
vm = VirtualMachine()
vm.SetTokens(tokens)

while ( vm.Index < len(vm.Tokens)):
    vm.DoToken()

print(vm.Variables)