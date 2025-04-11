//2211605
grammar MiniGo;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    self.ltk = self.type
    tk = self.type
    if tk == self.UNCLOSE_STRING:
        result = super().emit()
        raise UncloseString(result.text)
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit()
        raise IllegalEscape(result.text)
    elif tk == self.ERROR_CHAR:
        result = super().emit()
        raise ErrorToken(result.text)
    else:
        return super().emit()


def handleNewLine(self):
    if hasattr(
            self,
            'ltk') and self.ltk in [
            self.IDENTIFIER,
            self.INT_LIT,
            self.FLOAT_LIT,
            self.BOOL_LIT,
            self.STRING_LIT,
            self.RPAREN,
            self.RBRACKET,
            self.RBRACE,
            self.STRING,
            self.INT,
            self.FLOAT,
            self.BOOLEAN,
            self.NIL_LIT,
            self.RETURN,
            self.CONTINUE,
            self.BREAK]:
        self.type = self.SEMICOLON
        self.text = ';'
    else:
        self.skip()
}

options{
	language = Python3;
}

//! ---------------- PARSER ---------------------- */
program: declarationList EOF;

statement:
	( callStatement
	| assignmentStatement
	| ifStatement
	| forStatement 
	| declarationStatement) SEMICOLON;


inBlockStatement:
	( returnStatement
	| breakStatement
	| continueStatement) SEMICOLON;


declarationStatement:
     variableDeclaration
    | constantDeclaration;

declaration:
	(variableDeclaration
	| constantDeclaration
	| typeDeclaration
	| functionDeclaration
    | methodDeclaration) SEMICOLON;

variableDeclaration:
	VAR IDENTIFIER types (ASSIGN expression)? | VAR IDENTIFIER ASSIGN expression;

constantDeclaration:
	CONST IDENTIFIER ASSIGN expression;

typeDeclaration: TYPE (structType | interfaceType);

methodDeclaration:
	FUNC LPAREN receiver recType RPAREN IDENTIFIER LPAREN parameter_type? RPAREN types?
		block;

receiver: IDENTIFIER;

recType: IDENTIFIER;

functionDeclaration:
	FUNC IDENTIFIER LPAREN parameter_type? RPAREN types? block;

block: LBRACE inBlockStatementList RBRACE;

assignmentStatement: lhs assign_op expression;

assign_op:
	SHORT_ASSIGN
	| ADD_ASSIGN
	| SUBTRACT_ASSIGN
	| MULTIPLY_ASSIGN
	| DIVIDE_ASSIGN
	| MODULO_ASSIGN;

ifStatement: IF LPAREN condition RPAREN block (ELSE (ifStatement | block))?;

forStatement: FOR (condition | forClause | rangeClause)? block;

forClause:
	initStmt SEMICOLON condition SEMICOLON postStmt;

initStmt: scalarAssignment | variableDeclaration;
postStmt: scalarAssignment;
condition: expression;

scalarAssignment: IDENTIFIER assign_op expression;

rangeClause:
	IDENTIFIER COMMA IDENTIFIER SHORT_ASSIGN RANGE expression;

breakStatement: BREAK;

continueStatement: CONTINUE;

returnStatement: RETURN expression?;

callStatement: IDENTIFIER expressionParts | builtInFunctionCall;

expressionParts: expressionPart expressionParts?;

expressionPart: arguments | selector | index;

expression: logicalExpr;

logicalExpr: logicalExpr OR higherLogicalExpr | higherLogicalExpr;

higherLogicalExpr: higherLogicalExpr AND relationalExpr | relationalExpr;

relationalExpr: relationalExpr rel_op additiveExpr  | additiveExpr;

additiveExpr: additiveExpr add_op multiplicativeExpr | multiplicativeExpr;

multiplicativeExpr: multiplicativeExpr mul_op unaryExpr | unaryExpr;

unaryExpr: primaryExpr | unary_op unaryExpr;

primaryExpr:
	operand
	| primaryExpr index
	| primaryExpr selector
	| primaryExpr arguments
	| builtInFunctionCall;

selector: DOT IDENTIFIER;

arguments: LPAREN expressionList? RPAREN;

index: LBRACKET expression RBRACKET;

operand:
	IDENTIFIER
	| basicLit
	| arrayLit
	| structLit
	| LPAREN expression RPAREN;

basicLit: INT_LIT | FLOAT_LIT | STRING_LIT | BOOL_LIT | NIL_LIT;

arrayLit: arrayType arrayValue;

arrayValue: LBRACE arrayElems RBRACE;

arrayElems: (basicLit | arrayValue | IDENTIFIER) (COMMA arrayElems)?;

structLit: IDENTIFIER structvalue;

structvalue: LBRACE fieldValue? RBRACE;

fieldValue: IDENTIFIER COLON expression (COMMA fieldValue)?;

arrayType: LBRACKET (INT_LIT | IDENTIFIER) RBRACKET types;

structType: IDENTIFIER STRUCT LBRACE fieldDeclarations RBRACE;

fieldDeclarations: fieldDeclaration fieldDeclarations?;

fieldDeclaration: identifierList types SEMICOLON;

interfaceType: IDENTIFIER INTERFACE LBRACE interfaceElem RBRACE;

interfaceElem: methodElem interfaceElem?;

methodElem:
	IDENTIFIER LPAREN parameter_type? RPAREN types? SEMICOLON;

parameter_type: identifierList types (COMMA parameter_type)?;

rel_op:
	EQUAL
	| NOT_EQUAL
	| LESS_THAN
	| LESS_THAN_OR_EQUAL
	| GREATER_THAN
	| GREATER_THAN_OR_EQUAL;

add_op: ADD | SUBTRACT;

mul_op: MULTIPLY | DIVIDE | MODULO;

unary_op: SUBTRACT | NOT;

lhs: 
	IDENTIFIER
	| lhs selector
    | lhs index;

types: INT | FLOAT | BOOLEAN | STRING | arrayType | IDENTIFIER;

builtInFunctionCall:
      GETINT LPAREN RPAREN                     #getIntCall
    | PUTINT LPAREN expression RPAREN          #putIntCall
    | PUTINTLN LPAREN expression RPAREN        #putIntLnCall
    | GETFLOAT LPAREN RPAREN                   #getFloatCall
    | PUTFLOAT LPAREN expression RPAREN        #putFloatCall
    | PUTFLOATLN LPAREN expression RPAREN      #putFloatLnCall
    | GETBOOL LPAREN RPAREN                    #getBoolCall
    | PUTBOOL LPAREN expression RPAREN         #putBoolCall
    | PUTBOOLLN LPAREN expression RPAREN       #putBoolLnCall
    | GETSTRING LPAREN RPAREN                  #getStringCall
    | PUTSTRING LPAREN expression RPAREN       #putStringCall
    | PUTSTRINGLN LPAREN expression RPAREN     #putStringLnCall
    | PUTLN LPAREN RPAREN                      #putLnCall
    ;


identifierList: IDENTIFIER (COMMA identifierList)?;
expressionList: expression (COMMA expressionList)?;
inBlockStatementList: (statement | inBlockStatement) inBlockStatementList?;
declarationList: declaration declarationList?;

//! ---------------- LEXER ----------------------- */ Keywords 3.3.2 pdf
IF: 'if';
ELSE: 'else';
FOR: 'for';
RETURN: 'return';
FUNC: 'func';
TYPE: 'type';
STRUCT: 'struct';
INTERFACE: 'interface';
STRING: 'string';
INT: 'int';
FLOAT: 'float';
BOOLEAN: 'boolean';
CONST: 'const';
VAR: 'var';
CONTINUE: 'continue';
BREAK: 'break';
RANGE: 'range';
fragment NIL: 'nil';
fragment TRUE: 'true';
fragment FALSE: 'false';

//Operators 3.3.3 pdf
ADD: '+';
SUBTRACT: '-';
MULTIPLY: '*';
DIVIDE: '/';
MODULO: '%';

EQUAL: '==';
NOT_EQUAL: '!=';
LESS_THAN: '<';
LESS_THAN_OR_EQUAL: '<=';
GREATER_THAN: '>';
GREATER_THAN_OR_EQUAL: '>=';

AND: '&&';
OR: '||';
NOT: '!';

SHORT_ASSIGN: ':=';
ADD_ASSIGN: '+=';
SUBTRACT_ASSIGN: '-=';
MULTIPLY_ASSIGN: '*=';
DIVIDE_ASSIGN: '/=';
MODULO_ASSIGN: '%=';

DOT: '.';
ASSIGN: '=';
//Separators 3.3.4 pdf
LPAREN: '(';
RPAREN: ')';

LBRACE: '{';
RBRACE: '}';

LBRACKET: '[';
RBRACKET: ']';

COMMA: ',';
SEMICOLON: ';';
COLON: ':';


//Literals 3.3.5 pdf
INT_LIT: DEC_LIT | BIN_LIT | OCT_LIT | HEX_LIT;

fragment DEC_LIT: '0' | [1-9][0-9]*; // Decimal literal
fragment BIN_LIT: '0' [bB][01]+; // Binary literal
fragment OCT_LIT: '0' [oO][0-7]+; // Octal literal
fragment HEX_LIT: '0' [xX][0-9a-fA-F]+; // Hexadecimal literal

FLOAT_LIT: [0-9]+ '.' ([0-9]* EXPONENT?)?;

fragment EXPONENT: [eE] [+-]? [0-9]+;

STRING_LIT: '"' (~[\n\\"] | ESC)* '"';

fragment ESC: '\\' [tnr"\\];

BOOL_LIT: TRUE | FALSE;
NIL_LIT: NIL;

//Identifiers 3.3.1 pdf
IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]*;
//skip 3.1 and 3.2 pdf

NEWLINE: '\r'?'\n' {self.handleNewLine()};
WS: [ \t\r\f]+ -> skip;  // Ignore other whitespace

SINGLE_LINE_COMMENT:
	'//' ~[\r\n]* -> skip; // Single-line comment
MULTI_LINE_COMMENT:
	'/*' (MULTI_LINE_COMMENT | .)*? '*/' -> skip; // Multi-line comment (supports nesting)

//Built-in functions 9 pdf
GETINT: 'getInt';
PUTINT: 'putInt';
PUTINTLN: 'putIntLn';
GETFLOAT: 'getFloat';
PUTFLOAT: 'putFloat';
PUTFLOATLN: 'putFloatLn';
GETBOOL: 'getBool';
PUTBOOL: 'putBool';
PUTBOOLLN: 'putBoolLn';
GETSTRING: 'getString';
PUTSTRING: 'putString';
PUTSTRINGLN: 'putStringLn';
PUTLN: 'putLn';


//ERROR pdf BTL1 + lexererr.py
UNCLOSE_STRING:
    '"' (~[\n\\"] | ESC)* (EOF | '\r'? '\n') {
        if len(self.text) >= 2 and self.text[-2:] == '\r\n':
            raise UncloseString(self.text[:-2])  # Handles Windows-style line endings (\r\n)
        elif self.text[-1] == '\n':
            raise UncloseString(self.text[:-1])  # Handles Unix-style line endings (\n)
        else:
            raise UncloseString(self.text)       # Handles EOF case
    };
ILLEGAL_ESCAPE:
	'"' (ESC | ~["\\\r\n])* '\\' ~[tnr"\\] {
    raise IllegalEscape(self.text)
};
ERROR_CHAR: . {raise ErrorToken(self.text)};