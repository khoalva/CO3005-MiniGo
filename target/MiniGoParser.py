# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3L")
        buf.write("\u0250\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\t")
        buf.write("D\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\5\3\u0091\n\3\3\3\3")
        buf.write("\3\3\4\3\4\3\4\5\4\u0098\n\4\3\4\3\4\3\5\3\5\5\5\u009e")
        buf.write("\n\5\3\6\3\6\3\6\3\6\3\6\5\6\u00a5\n\6\3\6\3\6\3\7\3\7")
        buf.write("\3\7\3\7\3\7\5\7\u00ae\n\7\3\7\3\7\3\7\3\7\5\7\u00b4\n")
        buf.write("\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\5\t\u00be\n\t\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\3\n\5\n\u00c8\n\n\3\n\3\n\5\n\u00cc")
        buf.write("\n\n\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\r\3\r\5\r\u00d8")
        buf.write("\n\r\3\r\3\r\5\r\u00dc\n\r\3\r\3\r\3\16\3\16\3\16\3\16")
        buf.write("\3\17\3\17\3\17\3\17\3\20\3\20\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\5\21\u00f2\n\21\5\21\u00f4\n\21\3\22\3")
        buf.write("\22\3\22\3\22\5\22\u00fa\n\22\3\22\3\22\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\24\3\24\5\24\u0106\n\24\3\25\3\25\3")
        buf.write("\26\3\26\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33\5\33\u011d\n")
        buf.write("\33\3\34\3\34\3\34\5\34\u0122\n\34\3\35\3\35\5\35\u0126")
        buf.write("\n\35\3\36\3\36\3\36\5\36\u012b\n\36\3\37\3\37\3 \3 \3")
        buf.write(" \3 \3 \3 \7 \u0135\n \f \16 \u0138\13 \3!\3!\3!\3!\3")
        buf.write("!\3!\7!\u0140\n!\f!\16!\u0143\13!\3\"\3\"\3\"\3\"\3\"")
        buf.write("\3\"\3\"\7\"\u014c\n\"\f\"\16\"\u014f\13\"\3#\3#\3#\3")
        buf.write("#\3#\3#\3#\7#\u0158\n#\f#\16#\u015b\13#\3$\3$\3$\3$\3")
        buf.write("$\3$\3$\7$\u0164\n$\f$\16$\u0167\13$\3%\3%\3%\3%\5%\u016d")
        buf.write("\n%\3&\3&\3&\5&\u0172\n&\3&\3&\3&\3&\3&\3&\7&\u017a\n")
        buf.write("&\f&\16&\u017d\13&\3\'\3\'\3\'\3(\3(\5(\u0184\n(\3(\3")
        buf.write("(\3)\3)\3)\3)\3*\3*\3*\3*\3*\3*\3*\3*\5*\u0194\n*\3+\3")
        buf.write("+\3,\3,\3,\3-\3-\3-\3-\3.\3.\3.\5.\u01a2\n.\3.\3.\5.\u01a6")
        buf.write("\n.\3/\3/\3/\3\60\3\60\5\60\u01ad\n\60\3\60\3\60\3\61")
        buf.write("\3\61\3\61\3\61\3\61\5\61\u01b6\n\61\3\62\3\62\3\62\3")
        buf.write("\62\3\62\3\63\3\63\3\63\3\63\3\63\3\63\3\64\3\64\5\64")
        buf.write("\u01c5\n\64\3\65\3\65\3\65\3\65\3\66\3\66\3\66\3\66\3")
        buf.write("\66\3\66\3\67\3\67\5\67\u01d3\n\67\38\38\38\58\u01d8\n")
        buf.write("8\38\38\58\u01dc\n8\38\38\39\39\39\39\59\u01e4\n9\3:\3")
        buf.write(":\3;\3;\3<\3<\3=\3=\3>\3>\3>\3>\3>\3>\3>\7>\u01f5\n>\f")
        buf.write(">\16>\u01f8\13>\3?\3?\3?\3?\3?\3?\5?\u0200\n?\3@\3@\3")
        buf.write("@\3@\3@\3@\3@\3@\3@\3@\3@\3@\3@\3@\3@\3@\3@\3@\3@\3@\3")
        buf.write("@\3@\3@\3@\3@\3@\3@\3@\3@\3@\3@\3@\3@\3@\3@\3@\3@\3@\3")
        buf.write("@\3@\3@\3@\3@\3@\3@\3@\3@\3@\3@\3@\3@\3@\3@\3@\3@\5@\u0239")
        buf.write("\n@\3A\3A\3A\5A\u023e\nA\3B\3B\3B\5B\u0243\nB\3C\3C\5")
        buf.write("C\u0247\nC\3C\5C\u024a\nC\3D\3D\5D\u024e\nD\3D\2\t>@B")
        buf.write("DFJzE\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.")
        buf.write("\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|~\u0080")
        buf.write("\u0082\u0084\u0086\2\t\3\2\"\'\3\2\63\67\4\2\63\6388\3")
        buf.write("\2\31\36\3\2\24\25\3\2\26\30\4\2\25\25!!\2\u025a\2\u0088")
        buf.write("\3\2\2\2\4\u0090\3\2\2\2\6\u0097\3\2\2\2\b\u009d\3\2\2")
        buf.write("\2\n\u00a4\3\2\2\2\f\u00b3\3\2\2\2\16\u00b5\3\2\2\2\20")
        buf.write("\u00ba\3\2\2\2\22\u00bf\3\2\2\2\24\u00cf\3\2\2\2\26\u00d1")
        buf.write("\3\2\2\2\30\u00d3\3\2\2\2\32\u00df\3\2\2\2\34\u00e3\3")
        buf.write("\2\2\2\36\u00e7\3\2\2\2 \u00e9\3\2\2\2\"\u00f5\3\2\2\2")
        buf.write("$\u00fd\3\2\2\2&\u0105\3\2\2\2(\u0107\3\2\2\2*\u0109\3")
        buf.write("\2\2\2,\u010b\3\2\2\2.\u010f\3\2\2\2\60\u0116\3\2\2\2")
        buf.write("\62\u0118\3\2\2\2\64\u011a\3\2\2\2\66\u0121\3\2\2\28\u0123")
        buf.write("\3\2\2\2:\u012a\3\2\2\2<\u012c\3\2\2\2>\u012e\3\2\2\2")
        buf.write("@\u0139\3\2\2\2B\u0144\3\2\2\2D\u0150\3\2\2\2F\u015c\3")
        buf.write("\2\2\2H\u016c\3\2\2\2J\u0171\3\2\2\2L\u017e\3\2\2\2N\u0181")
        buf.write("\3\2\2\2P\u0187\3\2\2\2R\u0193\3\2\2\2T\u0195\3\2\2\2")
        buf.write("V\u0197\3\2\2\2X\u019a\3\2\2\2Z\u01a1\3\2\2\2\\\u01a7")
        buf.write("\3\2\2\2^\u01aa\3\2\2\2`\u01b0\3\2\2\2b\u01b7\3\2\2\2")
        buf.write("d\u01bc\3\2\2\2f\u01c2\3\2\2\2h\u01c6\3\2\2\2j\u01ca\3")
        buf.write("\2\2\2l\u01d0\3\2\2\2n\u01d4\3\2\2\2p\u01df\3\2\2\2r\u01e5")
        buf.write("\3\2\2\2t\u01e7\3\2\2\2v\u01e9\3\2\2\2x\u01eb\3\2\2\2")
        buf.write("z\u01ed\3\2\2\2|\u01ff\3\2\2\2~\u0238\3\2\2\2\u0080\u023a")
        buf.write("\3\2\2\2\u0082\u023f\3\2\2\2\u0084\u0246\3\2\2\2\u0086")
        buf.write("\u024b\3\2\2\2\u0088\u0089\5\u0086D\2\u0089\u008a\7\2")
        buf.write("\2\3\u008a\3\3\2\2\2\u008b\u0091\5\66\34\2\u008c\u0091")
        buf.write("\5\34\17\2\u008d\u0091\5 \21\2\u008e\u0091\5\"\22\2\u008f")
        buf.write("\u0091\5\b\5\2\u0090\u008b\3\2\2\2\u0090\u008c\3\2\2\2")
        buf.write("\u0090\u008d\3\2\2\2\u0090\u008e\3\2\2\2\u0090\u008f\3")
        buf.write("\2\2\2\u0091\u0092\3\2\2\2\u0092\u0093\7\61\2\2\u0093")
        buf.write("\5\3\2\2\2\u0094\u0098\5\64\33\2\u0095\u0098\5\60\31\2")
        buf.write("\u0096\u0098\5\62\32\2\u0097\u0094\3\2\2\2\u0097\u0095")
        buf.write("\3\2\2\2\u0097\u0096\3\2\2\2\u0098\u0099\3\2\2\2\u0099")
        buf.write("\u009a\7\61\2\2\u009a\7\3\2\2\2\u009b\u009e\5\f\7\2\u009c")
        buf.write("\u009e\5\16\b\2\u009d\u009b\3\2\2\2\u009d\u009c\3\2\2")
        buf.write("\2\u009e\t\3\2\2\2\u009f\u00a5\5\f\7\2\u00a0\u00a5\5\16")
        buf.write("\b\2\u00a1\u00a5\5\20\t\2\u00a2\u00a5\5\30\r\2\u00a3\u00a5")
        buf.write("\5\22\n\2\u00a4\u009f\3\2\2\2\u00a4\u00a0\3\2\2\2\u00a4")
        buf.write("\u00a1\3\2\2\2\u00a4\u00a2\3\2\2\2\u00a4\u00a3\3\2\2\2")
        buf.write("\u00a5\u00a6\3\2\2\2\u00a6\u00a7\7\61\2\2\u00a7\13\3\2")
        buf.write("\2\2\u00a8\u00a9\7\20\2\2\u00a9\u00aa\78\2\2\u00aa\u00ad")
        buf.write("\5|?\2\u00ab\u00ac\7)\2\2\u00ac\u00ae\5<\37\2\u00ad\u00ab")
        buf.write("\3\2\2\2\u00ad\u00ae\3\2\2\2\u00ae\u00b4\3\2\2\2\u00af")
        buf.write("\u00b0\7\20\2\2\u00b0\u00b1\78\2\2\u00b1\u00b2\7)\2\2")
        buf.write("\u00b2\u00b4\5<\37\2\u00b3\u00a8\3\2\2\2\u00b3\u00af\3")
        buf.write("\2\2\2\u00b4\r\3\2\2\2\u00b5\u00b6\7\17\2\2\u00b6\u00b7")
        buf.write("\78\2\2\u00b7\u00b8\7)\2\2\u00b8\u00b9\5<\37\2\u00b9\17")
        buf.write("\3\2\2\2\u00ba\u00bd\7\b\2\2\u00bb\u00be\5d\63\2\u00bc")
        buf.write("\u00be\5j\66\2\u00bd\u00bb\3\2\2\2\u00bd\u00bc\3\2\2\2")
        buf.write("\u00be\21\3\2\2\2\u00bf\u00c0\7\7\2\2\u00c0\u00c1\7*\2")
        buf.write("\2\u00c1\u00c2\5\24\13\2\u00c2\u00c3\5\26\f\2\u00c3\u00c4")
        buf.write("\7+\2\2\u00c4\u00c5\78\2\2\u00c5\u00c7\7*\2\2\u00c6\u00c8")
        buf.write("\5p9\2\u00c7\u00c6\3\2\2\2\u00c7\u00c8\3\2\2\2\u00c8\u00c9")
        buf.write("\3\2\2\2\u00c9\u00cb\7+\2\2\u00ca\u00cc\5|?\2\u00cb\u00ca")
        buf.write("\3\2\2\2\u00cb\u00cc\3\2\2\2\u00cc\u00cd\3\2\2\2\u00cd")
        buf.write("\u00ce\5\32\16\2\u00ce\23\3\2\2\2\u00cf\u00d0\78\2\2\u00d0")
        buf.write("\25\3\2\2\2\u00d1\u00d2\78\2\2\u00d2\27\3\2\2\2\u00d3")
        buf.write("\u00d4\7\7\2\2\u00d4\u00d5\78\2\2\u00d5\u00d7\7*\2\2\u00d6")
        buf.write("\u00d8\5p9\2\u00d7\u00d6\3\2\2\2\u00d7\u00d8\3\2\2\2\u00d8")
        buf.write("\u00d9\3\2\2\2\u00d9\u00db\7+\2\2\u00da\u00dc\5|?\2\u00db")
        buf.write("\u00da\3\2\2\2\u00db\u00dc\3\2\2\2\u00dc\u00dd\3\2\2\2")
        buf.write("\u00dd\u00de\5\32\16\2\u00de\31\3\2\2\2\u00df\u00e0\7")
        buf.write(",\2\2\u00e0\u00e1\5\u0084C\2\u00e1\u00e2\7-\2\2\u00e2")
        buf.write("\33\3\2\2\2\u00e3\u00e4\5z>\2\u00e4\u00e5\5\36\20\2\u00e5")
        buf.write("\u00e6\5<\37\2\u00e6\35\3\2\2\2\u00e7\u00e8\t\2\2\2\u00e8")
        buf.write("\37\3\2\2\2\u00e9\u00ea\7\3\2\2\u00ea\u00eb\7*\2\2\u00eb")
        buf.write("\u00ec\5*\26\2\u00ec\u00ed\7+\2\2\u00ed\u00f3\5\32\16")
        buf.write("\2\u00ee\u00f1\7\4\2\2\u00ef\u00f2\5 \21\2\u00f0\u00f2")
        buf.write("\5\32\16\2\u00f1\u00ef\3\2\2\2\u00f1\u00f0\3\2\2\2\u00f2")
        buf.write("\u00f4\3\2\2\2\u00f3\u00ee\3\2\2\2\u00f3\u00f4\3\2\2\2")
        buf.write("\u00f4!\3\2\2\2\u00f5\u00f9\7\5\2\2\u00f6\u00fa\5*\26")
        buf.write("\2\u00f7\u00fa\5$\23\2\u00f8\u00fa\5.\30\2\u00f9\u00f6")
        buf.write("\3\2\2\2\u00f9\u00f7\3\2\2\2\u00f9\u00f8\3\2\2\2\u00f9")
        buf.write("\u00fa\3\2\2\2\u00fa\u00fb\3\2\2\2\u00fb\u00fc\5\32\16")
        buf.write("\2\u00fc#\3\2\2\2\u00fd\u00fe\5&\24\2\u00fe\u00ff\7\61")
        buf.write("\2\2\u00ff\u0100\5*\26\2\u0100\u0101\7\61\2\2\u0101\u0102")
        buf.write("\5(\25\2\u0102%\3\2\2\2\u0103\u0106\5,\27\2\u0104\u0106")
        buf.write("\5\f\7\2\u0105\u0103\3\2\2\2\u0105\u0104\3\2\2\2\u0106")
        buf.write("\'\3\2\2\2\u0107\u0108\5,\27\2\u0108)\3\2\2\2\u0109\u010a")
        buf.write("\5<\37\2\u010a+\3\2\2\2\u010b\u010c\78\2\2\u010c\u010d")
        buf.write("\5\36\20\2\u010d\u010e\5<\37\2\u010e-\3\2\2\2\u010f\u0110")
        buf.write("\78\2\2\u0110\u0111\7\60\2\2\u0111\u0112\78\2\2\u0112")
        buf.write("\u0113\7\"\2\2\u0113\u0114\7\23\2\2\u0114\u0115\5<\37")
        buf.write("\2\u0115/\3\2\2\2\u0116\u0117\7\22\2\2\u0117\61\3\2\2")
        buf.write("\2\u0118\u0119\7\21\2\2\u0119\63\3\2\2\2\u011a\u011c\7")
        buf.write("\6\2\2\u011b\u011d\5<\37\2\u011c\u011b\3\2\2\2\u011c\u011d")
        buf.write("\3\2\2\2\u011d\65\3\2\2\2\u011e\u011f\78\2\2\u011f\u0122")
        buf.write("\58\35\2\u0120\u0122\5~@\2\u0121\u011e\3\2\2\2\u0121\u0120")
        buf.write("\3\2\2\2\u0122\67\3\2\2\2\u0123\u0125\5:\36\2\u0124\u0126")
        buf.write("\58\35\2\u0125\u0124\3\2\2\2\u0125\u0126\3\2\2\2\u0126")
        buf.write("9\3\2\2\2\u0127\u012b\5N(\2\u0128\u012b\5L\'\2\u0129\u012b")
        buf.write("\5P)\2\u012a\u0127\3\2\2\2\u012a\u0128\3\2\2\2\u012a\u0129")
        buf.write("\3\2\2\2\u012b;\3\2\2\2\u012c\u012d\5> \2\u012d=\3\2\2")
        buf.write("\2\u012e\u012f\b \1\2\u012f\u0130\5@!\2\u0130\u0136\3")
        buf.write("\2\2\2\u0131\u0132\f\4\2\2\u0132\u0133\7 \2\2\u0133\u0135")
        buf.write("\5@!\2\u0134\u0131\3\2\2\2\u0135\u0138\3\2\2\2\u0136\u0134")
        buf.write("\3\2\2\2\u0136\u0137\3\2\2\2\u0137?\3\2\2\2\u0138\u0136")
        buf.write("\3\2\2\2\u0139\u013a\b!\1\2\u013a\u013b\5B\"\2\u013b\u0141")
        buf.write("\3\2\2\2\u013c\u013d\f\4\2\2\u013d\u013e\7\37\2\2\u013e")
        buf.write("\u0140\5B\"\2\u013f\u013c\3\2\2\2\u0140\u0143\3\2\2\2")
        buf.write("\u0141\u013f\3\2\2\2\u0141\u0142\3\2\2\2\u0142A\3\2\2")
        buf.write("\2\u0143\u0141\3\2\2\2\u0144\u0145\b\"\1\2\u0145\u0146")
        buf.write("\5D#\2\u0146\u014d\3\2\2\2\u0147\u0148\f\4\2\2\u0148\u0149")
        buf.write("\5r:\2\u0149\u014a\5D#\2\u014a\u014c\3\2\2\2\u014b\u0147")
        buf.write("\3\2\2\2\u014c\u014f\3\2\2\2\u014d\u014b\3\2\2\2\u014d")
        buf.write("\u014e\3\2\2\2\u014eC\3\2\2\2\u014f\u014d\3\2\2\2\u0150")
        buf.write("\u0151\b#\1\2\u0151\u0152\5F$\2\u0152\u0159\3\2\2\2\u0153")
        buf.write("\u0154\f\4\2\2\u0154\u0155\5t;\2\u0155\u0156\5F$\2\u0156")
        buf.write("\u0158\3\2\2\2\u0157\u0153\3\2\2\2\u0158\u015b\3\2\2\2")
        buf.write("\u0159\u0157\3\2\2\2\u0159\u015a\3\2\2\2\u015aE\3\2\2")
        buf.write("\2\u015b\u0159\3\2\2\2\u015c\u015d\b$\1\2\u015d\u015e")
        buf.write("\5H%\2\u015e\u0165\3\2\2\2\u015f\u0160\f\4\2\2\u0160\u0161")
        buf.write("\5v<\2\u0161\u0162\5H%\2\u0162\u0164\3\2\2\2\u0163\u015f")
        buf.write("\3\2\2\2\u0164\u0167\3\2\2\2\u0165\u0163\3\2\2\2\u0165")
        buf.write("\u0166\3\2\2\2\u0166G\3\2\2\2\u0167\u0165\3\2\2\2\u0168")
        buf.write("\u016d\5J&\2\u0169\u016a\5x=\2\u016a\u016b\5H%\2\u016b")
        buf.write("\u016d\3\2\2\2\u016c\u0168\3\2\2\2\u016c\u0169\3\2\2\2")
        buf.write("\u016dI\3\2\2\2\u016e\u016f\b&\1\2\u016f\u0172\5R*\2\u0170")
        buf.write("\u0172\5~@\2\u0171\u016e\3\2\2\2\u0171\u0170\3\2\2\2\u0172")
        buf.write("\u017b\3\2\2\2\u0173\u0174\f\6\2\2\u0174\u017a\5P)\2\u0175")
        buf.write("\u0176\f\5\2\2\u0176\u017a\5L\'\2\u0177\u0178\f\4\2\2")
        buf.write("\u0178\u017a\5N(\2\u0179\u0173\3\2\2\2\u0179\u0175\3\2")
        buf.write("\2\2\u0179\u0177\3\2\2\2\u017a\u017d\3\2\2\2\u017b\u0179")
        buf.write("\3\2\2\2\u017b\u017c\3\2\2\2\u017cK\3\2\2\2\u017d\u017b")
        buf.write("\3\2\2\2\u017e\u017f\7(\2\2\u017f\u0180\78\2\2\u0180M")
        buf.write("\3\2\2\2\u0181\u0183\7*\2\2\u0182\u0184\5\u0082B\2\u0183")
        buf.write("\u0182\3\2\2\2\u0183\u0184\3\2\2\2\u0184\u0185\3\2\2\2")
        buf.write("\u0185\u0186\7+\2\2\u0186O\3\2\2\2\u0187\u0188\7.\2\2")
        buf.write("\u0188\u0189\5<\37\2\u0189\u018a\7/\2\2\u018aQ\3\2\2\2")
        buf.write("\u018b\u0194\78\2\2\u018c\u0194\5T+\2\u018d\u0194\5V,")
        buf.write("\2\u018e\u0194\5\\/\2\u018f\u0190\7*\2\2\u0190\u0191\5")
        buf.write("<\37\2\u0191\u0192\7+\2\2\u0192\u0194\3\2\2\2\u0193\u018b")
        buf.write("\3\2\2\2\u0193\u018c\3\2\2\2\u0193\u018d\3\2\2\2\u0193")
        buf.write("\u018e\3\2\2\2\u0193\u018f\3\2\2\2\u0194S\3\2\2\2\u0195")
        buf.write("\u0196\t\3\2\2\u0196U\3\2\2\2\u0197\u0198\5b\62\2\u0198")
        buf.write("\u0199\5X-\2\u0199W\3\2\2\2\u019a\u019b\7,\2\2\u019b\u019c")
        buf.write("\5Z.\2\u019c\u019d\7-\2\2\u019dY\3\2\2\2\u019e\u01a2\5")
        buf.write("T+\2\u019f\u01a2\5X-\2\u01a0\u01a2\78\2\2\u01a1\u019e")
        buf.write("\3\2\2\2\u01a1\u019f\3\2\2\2\u01a1\u01a0\3\2\2\2\u01a2")
        buf.write("\u01a5\3\2\2\2\u01a3\u01a4\7\60\2\2\u01a4\u01a6\5Z.\2")
        buf.write("\u01a5\u01a3\3\2\2\2\u01a5\u01a6\3\2\2\2\u01a6[\3\2\2")
        buf.write("\2\u01a7\u01a8\78\2\2\u01a8\u01a9\5^\60\2\u01a9]\3\2\2")
        buf.write("\2\u01aa\u01ac\7,\2\2\u01ab\u01ad\5`\61\2\u01ac\u01ab")
        buf.write("\3\2\2\2\u01ac\u01ad\3\2\2\2\u01ad\u01ae\3\2\2\2\u01ae")
        buf.write("\u01af\7-\2\2\u01af_\3\2\2\2\u01b0\u01b1\78\2\2\u01b1")
        buf.write("\u01b2\7\62\2\2\u01b2\u01b5\5<\37\2\u01b3\u01b4\7\60\2")
        buf.write("\2\u01b4\u01b6\5`\61\2\u01b5\u01b3\3\2\2\2\u01b5\u01b6")
        buf.write("\3\2\2\2\u01b6a\3\2\2\2\u01b7\u01b8\7.\2\2\u01b8\u01b9")
        buf.write("\t\4\2\2\u01b9\u01ba\7/\2\2\u01ba\u01bb\5|?\2\u01bbc\3")
        buf.write("\2\2\2\u01bc\u01bd\78\2\2\u01bd\u01be\7\t\2\2\u01be\u01bf")
        buf.write("\7,\2\2\u01bf\u01c0\5f\64\2\u01c0\u01c1\7-\2\2\u01c1e")
        buf.write("\3\2\2\2\u01c2\u01c4\5h\65\2\u01c3\u01c5\5f\64\2\u01c4")
        buf.write("\u01c3\3\2\2\2\u01c4\u01c5\3\2\2\2\u01c5g\3\2\2\2\u01c6")
        buf.write("\u01c7\5\u0080A\2\u01c7\u01c8\5|?\2\u01c8\u01c9\7\61\2")
        buf.write("\2\u01c9i\3\2\2\2\u01ca\u01cb\78\2\2\u01cb\u01cc\7\n\2")
        buf.write("\2\u01cc\u01cd\7,\2\2\u01cd\u01ce\5l\67\2\u01ce\u01cf")
        buf.write("\7-\2\2\u01cfk\3\2\2\2\u01d0\u01d2\5n8\2\u01d1\u01d3\5")
        buf.write("l\67\2\u01d2\u01d1\3\2\2\2\u01d2\u01d3\3\2\2\2\u01d3m")
        buf.write("\3\2\2\2\u01d4\u01d5\78\2\2\u01d5\u01d7\7*\2\2\u01d6\u01d8")
        buf.write("\5p9\2\u01d7\u01d6\3\2\2\2\u01d7\u01d8\3\2\2\2\u01d8\u01d9")
        buf.write("\3\2\2\2\u01d9\u01db\7+\2\2\u01da\u01dc\5|?\2\u01db\u01da")
        buf.write("\3\2\2\2\u01db\u01dc\3\2\2\2\u01dc\u01dd\3\2\2\2\u01dd")
        buf.write("\u01de\7\61\2\2\u01deo\3\2\2\2\u01df\u01e0\5\u0080A\2")
        buf.write("\u01e0\u01e3\5|?\2\u01e1\u01e2\7\60\2\2\u01e2\u01e4\5")
        buf.write("p9\2\u01e3\u01e1\3\2\2\2\u01e3\u01e4\3\2\2\2\u01e4q\3")
        buf.write("\2\2\2\u01e5\u01e6\t\5\2\2\u01e6s\3\2\2\2\u01e7\u01e8")
        buf.write("\t\6\2\2\u01e8u\3\2\2\2\u01e9\u01ea\t\7\2\2\u01eaw\3\2")
        buf.write("\2\2\u01eb\u01ec\t\b\2\2\u01ecy\3\2\2\2\u01ed\u01ee\b")
        buf.write(">\1\2\u01ee\u01ef\78\2\2\u01ef\u01f6\3\2\2\2\u01f0\u01f1")
        buf.write("\f\4\2\2\u01f1\u01f5\5L\'\2\u01f2\u01f3\f\3\2\2\u01f3")
        buf.write("\u01f5\5P)\2\u01f4\u01f0\3\2\2\2\u01f4\u01f2\3\2\2\2\u01f5")
        buf.write("\u01f8\3\2\2\2\u01f6\u01f4\3\2\2\2\u01f6\u01f7\3\2\2\2")
        buf.write("\u01f7{\3\2\2\2\u01f8\u01f6\3\2\2\2\u01f9\u0200\7\f\2")
        buf.write("\2\u01fa\u0200\7\r\2\2\u01fb\u0200\7\16\2\2\u01fc\u0200")
        buf.write("\7\13\2\2\u01fd\u0200\5b\62\2\u01fe\u0200\78\2\2\u01ff")
        buf.write("\u01f9\3\2\2\2\u01ff\u01fa\3\2\2\2\u01ff\u01fb\3\2\2\2")
        buf.write("\u01ff\u01fc\3\2\2\2\u01ff\u01fd\3\2\2\2\u01ff\u01fe\3")
        buf.write("\2\2\2\u0200}\3\2\2\2\u0201\u0202\7=\2\2\u0202\u0203\7")
        buf.write("*\2\2\u0203\u0239\7+\2\2\u0204\u0205\7>\2\2\u0205\u0206")
        buf.write("\7*\2\2\u0206\u0207\5<\37\2\u0207\u0208\7+\2\2\u0208\u0239")
        buf.write("\3\2\2\2\u0209\u020a\7?\2\2\u020a\u020b\7*\2\2\u020b\u020c")
        buf.write("\5<\37\2\u020c\u020d\7+\2\2\u020d\u0239\3\2\2\2\u020e")
        buf.write("\u020f\7@\2\2\u020f\u0210\7*\2\2\u0210\u0239\7+\2\2\u0211")
        buf.write("\u0212\7A\2\2\u0212\u0213\7*\2\2\u0213\u0214\5<\37\2\u0214")
        buf.write("\u0215\7+\2\2\u0215\u0239\3\2\2\2\u0216\u0217\7B\2\2\u0217")
        buf.write("\u0218\7*\2\2\u0218\u0219\5<\37\2\u0219\u021a\7+\2\2\u021a")
        buf.write("\u0239\3\2\2\2\u021b\u021c\7C\2\2\u021c\u021d\7*\2\2\u021d")
        buf.write("\u0239\7+\2\2\u021e\u021f\7D\2\2\u021f\u0220\7*\2\2\u0220")
        buf.write("\u0221\5<\37\2\u0221\u0222\7+\2\2\u0222\u0239\3\2\2\2")
        buf.write("\u0223\u0224\7E\2\2\u0224\u0225\7*\2\2\u0225\u0226\5<")
        buf.write("\37\2\u0226\u0227\7+\2\2\u0227\u0239\3\2\2\2\u0228\u0229")
        buf.write("\7F\2\2\u0229\u022a\7*\2\2\u022a\u0239\7+\2\2\u022b\u022c")
        buf.write("\7G\2\2\u022c\u022d\7*\2\2\u022d\u022e\5<\37\2\u022e\u022f")
        buf.write("\7+\2\2\u022f\u0239\3\2\2\2\u0230\u0231\7H\2\2\u0231\u0232")
        buf.write("\7*\2\2\u0232\u0233\5<\37\2\u0233\u0234\7+\2\2\u0234\u0239")
        buf.write("\3\2\2\2\u0235\u0236\7I\2\2\u0236\u0237\7*\2\2\u0237\u0239")
        buf.write("\7+\2\2\u0238\u0201\3\2\2\2\u0238\u0204\3\2\2\2\u0238")
        buf.write("\u0209\3\2\2\2\u0238\u020e\3\2\2\2\u0238\u0211\3\2\2\2")
        buf.write("\u0238\u0216\3\2\2\2\u0238\u021b\3\2\2\2\u0238\u021e\3")
        buf.write("\2\2\2\u0238\u0223\3\2\2\2\u0238\u0228\3\2\2\2\u0238\u022b")
        buf.write("\3\2\2\2\u0238\u0230\3\2\2\2\u0238\u0235\3\2\2\2\u0239")
        buf.write("\177\3\2\2\2\u023a\u023d\78\2\2\u023b\u023c\7\60\2\2\u023c")
        buf.write("\u023e\5\u0080A\2\u023d\u023b\3\2\2\2\u023d\u023e\3\2")
        buf.write("\2\2\u023e\u0081\3\2\2\2\u023f\u0242\5<\37\2\u0240\u0241")
        buf.write("\7\60\2\2\u0241\u0243\5\u0082B\2\u0242\u0240\3\2\2\2\u0242")
        buf.write("\u0243\3\2\2\2\u0243\u0083\3\2\2\2\u0244\u0247\5\4\3\2")
        buf.write("\u0245\u0247\5\6\4\2\u0246\u0244\3\2\2\2\u0246\u0245\3")
        buf.write("\2\2\2\u0247\u0249\3\2\2\2\u0248\u024a\5\u0084C\2\u0249")
        buf.write("\u0248\3\2\2\2\u0249\u024a\3\2\2\2\u024a\u0085\3\2\2\2")
        buf.write("\u024b\u024d\5\n\6\2\u024c\u024e\5\u0086D\2\u024d\u024c")
        buf.write("\3\2\2\2\u024d\u024e\3\2\2\2\u024e\u0087\3\2\2\2\62\u0090")
        buf.write("\u0097\u009d\u00a4\u00ad\u00b3\u00bd\u00c7\u00cb\u00d7")
        buf.write("\u00db\u00f1\u00f3\u00f9\u0105\u011c\u0121\u0125\u012a")
        buf.write("\u0136\u0141\u014d\u0159\u0165\u016c\u0171\u0179\u017b")
        buf.write("\u0183\u0193\u01a1\u01a5\u01ac\u01b5\u01c4\u01d2\u01d7")
        buf.write("\u01db\u01e3\u01f4\u01f6\u01ff\u0238\u023d\u0242\u0246")
        buf.write("\u0249\u024d")
        return buf.getvalue()


class MiniGoParser ( Parser ):

    grammarFileName = "MiniGo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'else'", "'for'", "'return'", 
                     "'func'", "'type'", "'struct'", "'interface'", "'string'", 
                     "'int'", "'float'", "'boolean'", "'const'", "'var'", 
                     "'continue'", "'break'", "'range'", "'+'", "'-'", "'*'", 
                     "'/'", "'%'", "'=='", "'!='", "'<'", "'<='", "'>'", 
                     "'>='", "'&&'", "'||'", "'!'", "':='", "'+='", "'-='", 
                     "'*='", "'/='", "'%='", "'.'", "'='", "'('", "')'", 
                     "'{'", "'}'", "'['", "']'", "','", "';'", "':'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'getInt'", "'putInt'", "'putIntLn'", 
                     "'getFloat'", "'putFloat'", "'putFloatLn'", "'getBool'", 
                     "'putBool'", "'putBoolLn'", "'getString'", "'putString'", 
                     "'putStringLn'", "'putLn'" ]

    symbolicNames = [ "<INVALID>", "IF", "ELSE", "FOR", "RETURN", "FUNC", 
                      "TYPE", "STRUCT", "INTERFACE", "STRING", "INT", "FLOAT", 
                      "BOOLEAN", "CONST", "VAR", "CONTINUE", "BREAK", "RANGE", 
                      "ADD", "SUBTRACT", "MULTIPLY", "DIVIDE", "MODULO", 
                      "EQUAL", "NOT_EQUAL", "LESS_THAN", "LESS_THAN_OR_EQUAL", 
                      "GREATER_THAN", "GREATER_THAN_OR_EQUAL", "AND", "OR", 
                      "NOT", "SHORT_ASSIGN", "ADD_ASSIGN", "SUBTRACT_ASSIGN", 
                      "MULTIPLY_ASSIGN", "DIVIDE_ASSIGN", "MODULO_ASSIGN", 
                      "DOT", "ASSIGN", "LPAREN", "RPAREN", "LBRACE", "RBRACE", 
                      "LBRACKET", "RBRACKET", "COMMA", "SEMICOLON", "COLON", 
                      "INT_LIT", "FLOAT_LIT", "STRING_LIT", "BOOL_LIT", 
                      "NIL_LIT", "IDENTIFIER", "NEWLINE", "WS", "SINGLE_LINE_COMMENT", 
                      "MULTI_LINE_COMMENT", "GETINT", "PUTINT", "PUTINTLN", 
                      "GETFLOAT", "PUTFLOAT", "PUTFLOATLN", "GETBOOL", "PUTBOOL", 
                      "PUTBOOLLN", "GETSTRING", "PUTSTRING", "PUTSTRINGLN", 
                      "PUTLN", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_inBlockStatement = 2
    RULE_declarationStatement = 3
    RULE_declaration = 4
    RULE_variableDeclaration = 5
    RULE_constantDeclaration = 6
    RULE_typeDeclaration = 7
    RULE_methodDeclaration = 8
    RULE_receiver = 9
    RULE_recType = 10
    RULE_functionDeclaration = 11
    RULE_block = 12
    RULE_assignmentStatement = 13
    RULE_assign_op = 14
    RULE_ifStatement = 15
    RULE_forStatement = 16
    RULE_forClause = 17
    RULE_initStmt = 18
    RULE_postStmt = 19
    RULE_condition = 20
    RULE_scalarAssignment = 21
    RULE_rangeClause = 22
    RULE_breakStatement = 23
    RULE_continueStatement = 24
    RULE_returnStatement = 25
    RULE_callStatement = 26
    RULE_expressionParts = 27
    RULE_expressionPart = 28
    RULE_expression = 29
    RULE_logicalExpr = 30
    RULE_higherLogicalExpr = 31
    RULE_relationalExpr = 32
    RULE_additiveExpr = 33
    RULE_multiplicativeExpr = 34
    RULE_unaryExpr = 35
    RULE_primaryExpr = 36
    RULE_selector = 37
    RULE_arguments = 38
    RULE_index = 39
    RULE_operand = 40
    RULE_basicLit = 41
    RULE_arrayLit = 42
    RULE_arrayValue = 43
    RULE_arrayElems = 44
    RULE_structLit = 45
    RULE_structvalue = 46
    RULE_fieldValue = 47
    RULE_arrayType = 48
    RULE_structType = 49
    RULE_fieldDeclarations = 50
    RULE_fieldDeclaration = 51
    RULE_interfaceType = 52
    RULE_interfaceElem = 53
    RULE_methodElem = 54
    RULE_parameter_type = 55
    RULE_rel_op = 56
    RULE_add_op = 57
    RULE_mul_op = 58
    RULE_unary_op = 59
    RULE_lhs = 60
    RULE_types = 61
    RULE_builtInFunctionCall = 62
    RULE_identifierList = 63
    RULE_expressionList = 64
    RULE_inBlockStatementList = 65
    RULE_declarationList = 66

    ruleNames =  [ "program", "statement", "inBlockStatement", "declarationStatement", 
                   "declaration", "variableDeclaration", "constantDeclaration", 
                   "typeDeclaration", "methodDeclaration", "receiver", "recType", 
                   "functionDeclaration", "block", "assignmentStatement", 
                   "assign_op", "ifStatement", "forStatement", "forClause", 
                   "initStmt", "postStmt", "condition", "scalarAssignment", 
                   "rangeClause", "breakStatement", "continueStatement", 
                   "returnStatement", "callStatement", "expressionParts", 
                   "expressionPart", "expression", "logicalExpr", "higherLogicalExpr", 
                   "relationalExpr", "additiveExpr", "multiplicativeExpr", 
                   "unaryExpr", "primaryExpr", "selector", "arguments", 
                   "index", "operand", "basicLit", "arrayLit", "arrayValue", 
                   "arrayElems", "structLit", "structvalue", "fieldValue", 
                   "arrayType", "structType", "fieldDeclarations", "fieldDeclaration", 
                   "interfaceType", "interfaceElem", "methodElem", "parameter_type", 
                   "rel_op", "add_op", "mul_op", "unary_op", "lhs", "types", 
                   "builtInFunctionCall", "identifierList", "expressionList", 
                   "inBlockStatementList", "declarationList" ]

    EOF = Token.EOF
    IF=1
    ELSE=2
    FOR=3
    RETURN=4
    FUNC=5
    TYPE=6
    STRUCT=7
    INTERFACE=8
    STRING=9
    INT=10
    FLOAT=11
    BOOLEAN=12
    CONST=13
    VAR=14
    CONTINUE=15
    BREAK=16
    RANGE=17
    ADD=18
    SUBTRACT=19
    MULTIPLY=20
    DIVIDE=21
    MODULO=22
    EQUAL=23
    NOT_EQUAL=24
    LESS_THAN=25
    LESS_THAN_OR_EQUAL=26
    GREATER_THAN=27
    GREATER_THAN_OR_EQUAL=28
    AND=29
    OR=30
    NOT=31
    SHORT_ASSIGN=32
    ADD_ASSIGN=33
    SUBTRACT_ASSIGN=34
    MULTIPLY_ASSIGN=35
    DIVIDE_ASSIGN=36
    MODULO_ASSIGN=37
    DOT=38
    ASSIGN=39
    LPAREN=40
    RPAREN=41
    LBRACE=42
    RBRACE=43
    LBRACKET=44
    RBRACKET=45
    COMMA=46
    SEMICOLON=47
    COLON=48
    INT_LIT=49
    FLOAT_LIT=50
    STRING_LIT=51
    BOOL_LIT=52
    NIL_LIT=53
    IDENTIFIER=54
    NEWLINE=55
    WS=56
    SINGLE_LINE_COMMENT=57
    MULTI_LINE_COMMENT=58
    GETINT=59
    PUTINT=60
    PUTINTLN=61
    GETFLOAT=62
    PUTFLOAT=63
    PUTFLOATLN=64
    GETBOOL=65
    PUTBOOL=66
    PUTBOOLLN=67
    GETSTRING=68
    PUTSTRING=69
    PUTSTRINGLN=70
    PUTLN=71
    UNCLOSE_STRING=72
    ILLEGAL_ESCAPE=73
    ERROR_CHAR=74

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declarationList(self):
            return self.getTypedRuleContext(MiniGoParser.DeclarationListContext,0)


        def EOF(self):
            return self.getToken(MiniGoParser.EOF, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MiniGoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self.declarationList()
            self.state = 135
            self.match(MiniGoParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def callStatement(self):
            return self.getTypedRuleContext(MiniGoParser.CallStatementContext,0)


        def assignmentStatement(self):
            return self.getTypedRuleContext(MiniGoParser.AssignmentStatementContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(MiniGoParser.IfStatementContext,0)


        def forStatement(self):
            return self.getTypedRuleContext(MiniGoParser.ForStatementContext,0)


        def declarationStatement(self):
            return self.getTypedRuleContext(MiniGoParser.DeclarationStatementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = MiniGoParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 137
                self.callStatement()
                pass

            elif la_ == 2:
                self.state = 138
                self.assignmentStatement()
                pass

            elif la_ == 3:
                self.state = 139
                self.ifStatement()
                pass

            elif la_ == 4:
                self.state = 140
                self.forStatement()
                pass

            elif la_ == 5:
                self.state = 141
                self.declarationStatement()
                pass


            self.state = 144
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InBlockStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def returnStatement(self):
            return self.getTypedRuleContext(MiniGoParser.ReturnStatementContext,0)


        def breakStatement(self):
            return self.getTypedRuleContext(MiniGoParser.BreakStatementContext,0)


        def continueStatement(self):
            return self.getTypedRuleContext(MiniGoParser.ContinueStatementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_inBlockStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInBlockStatement" ):
                return visitor.visitInBlockStatement(self)
            else:
                return visitor.visitChildren(self)




    def inBlockStatement(self):

        localctx = MiniGoParser.InBlockStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_inBlockStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.RETURN]:
                self.state = 146
                self.returnStatement()
                pass
            elif token in [MiniGoParser.BREAK]:
                self.state = 147
                self.breakStatement()
                pass
            elif token in [MiniGoParser.CONTINUE]:
                self.state = 148
                self.continueStatement()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 151
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableDeclaration(self):
            return self.getTypedRuleContext(MiniGoParser.VariableDeclarationContext,0)


        def constantDeclaration(self):
            return self.getTypedRuleContext(MiniGoParser.ConstantDeclarationContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_declarationStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclarationStatement" ):
                return visitor.visitDeclarationStatement(self)
            else:
                return visitor.visitChildren(self)




    def declarationStatement(self):

        localctx = MiniGoParser.DeclarationStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_declarationStatement)
        try:
            self.state = 155
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 153
                self.variableDeclaration()
                pass
            elif token in [MiniGoParser.CONST]:
                self.enterOuterAlt(localctx, 2)
                self.state = 154
                self.constantDeclaration()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def variableDeclaration(self):
            return self.getTypedRuleContext(MiniGoParser.VariableDeclarationContext,0)


        def constantDeclaration(self):
            return self.getTypedRuleContext(MiniGoParser.ConstantDeclarationContext,0)


        def typeDeclaration(self):
            return self.getTypedRuleContext(MiniGoParser.TypeDeclarationContext,0)


        def functionDeclaration(self):
            return self.getTypedRuleContext(MiniGoParser.FunctionDeclarationContext,0)


        def methodDeclaration(self):
            return self.getTypedRuleContext(MiniGoParser.MethodDeclarationContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = MiniGoParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 157
                self.variableDeclaration()
                pass

            elif la_ == 2:
                self.state = 158
                self.constantDeclaration()
                pass

            elif la_ == 3:
                self.state = 159
                self.typeDeclaration()
                pass

            elif la_ == 4:
                self.state = 160
                self.functionDeclaration()
                pass

            elif la_ == 5:
                self.state = 161
                self.methodDeclaration()
                pass


            self.state = 164
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def types(self):
            return self.getTypedRuleContext(MiniGoParser.TypesContext,0)


        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_variableDeclaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableDeclaration" ):
                return visitor.visitVariableDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def variableDeclaration(self):

        localctx = MiniGoParser.VariableDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_variableDeclaration)
        self._la = 0 # Token type
        try:
            self.state = 177
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 166
                self.match(MiniGoParser.VAR)
                self.state = 167
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 168
                self.types()
                self.state = 171
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.ASSIGN:
                    self.state = 169
                    self.match(MiniGoParser.ASSIGN)
                    self.state = 170
                    self.expression()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 173
                self.match(MiniGoParser.VAR)
                self.state = 174
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 175
                self.match(MiniGoParser.ASSIGN)
                self.state = 176
                self.expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstantDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONST(self):
            return self.getToken(MiniGoParser.CONST, 0)

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_constantDeclaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstantDeclaration" ):
                return visitor.visitConstantDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def constantDeclaration(self):

        localctx = MiniGoParser.ConstantDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_constantDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self.match(MiniGoParser.CONST)
            self.state = 180
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 181
            self.match(MiniGoParser.ASSIGN)
            self.state = 182
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MiniGoParser.TYPE, 0)

        def structType(self):
            return self.getTypedRuleContext(MiniGoParser.StructTypeContext,0)


        def interfaceType(self):
            return self.getTypedRuleContext(MiniGoParser.InterfaceTypeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_typeDeclaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeDeclaration" ):
                return visitor.visitTypeDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def typeDeclaration(self):

        localctx = MiniGoParser.TypeDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_typeDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self.match(MiniGoParser.TYPE)
            self.state = 187
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 185
                self.structType()
                pass

            elif la_ == 2:
                self.state = 186
                self.interfaceType()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def LPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.LPAREN)
            else:
                return self.getToken(MiniGoParser.LPAREN, i)

        def receiver(self):
            return self.getTypedRuleContext(MiniGoParser.ReceiverContext,0)


        def recType(self):
            return self.getTypedRuleContext(MiniGoParser.RecTypeContext,0)


        def RPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.RPAREN)
            else:
                return self.getToken(MiniGoParser.RPAREN, i)

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def parameter_type(self):
            return self.getTypedRuleContext(MiniGoParser.Parameter_typeContext,0)


        def types(self):
            return self.getTypedRuleContext(MiniGoParser.TypesContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_methodDeclaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodDeclaration" ):
                return visitor.visitMethodDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def methodDeclaration(self):

        localctx = MiniGoParser.MethodDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_methodDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            self.match(MiniGoParser.FUNC)
            self.state = 190
            self.match(MiniGoParser.LPAREN)
            self.state = 191
            self.receiver()
            self.state = 192
            self.recType()
            self.state = 193
            self.match(MiniGoParser.RPAREN)
            self.state = 194
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 195
            self.match(MiniGoParser.LPAREN)
            self.state = 197
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.IDENTIFIER:
                self.state = 196
                self.parameter_type()


            self.state = 199
            self.match(MiniGoParser.RPAREN)
            self.state = 201
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LBRACKET) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                self.state = 200
                self.types()


            self.state = 203
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReceiverContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_receiver

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReceiver" ):
                return visitor.visitReceiver(self)
            else:
                return visitor.visitChildren(self)




    def receiver(self):

        localctx = MiniGoParser.ReceiverContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_receiver)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            self.match(MiniGoParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RecTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_recType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRecType" ):
                return visitor.visitRecType(self)
            else:
                return visitor.visitChildren(self)




    def recType(self):

        localctx = MiniGoParser.RecTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_recType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            self.match(MiniGoParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def parameter_type(self):
            return self.getTypedRuleContext(MiniGoParser.Parameter_typeContext,0)


        def types(self):
            return self.getTypedRuleContext(MiniGoParser.TypesContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_functionDeclaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionDeclaration" ):
                return visitor.visitFunctionDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def functionDeclaration(self):

        localctx = MiniGoParser.FunctionDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_functionDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            self.match(MiniGoParser.FUNC)
            self.state = 210
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 211
            self.match(MiniGoParser.LPAREN)
            self.state = 213
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.IDENTIFIER:
                self.state = 212
                self.parameter_type()


            self.state = 215
            self.match(MiniGoParser.RPAREN)
            self.state = 217
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LBRACKET) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                self.state = 216
                self.types()


            self.state = 219
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def inBlockStatementList(self):
            return self.getTypedRuleContext(MiniGoParser.InBlockStatementListContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = MiniGoParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            self.match(MiniGoParser.LBRACE)
            self.state = 222
            self.inBlockStatementList()
            self.state = 223
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(MiniGoParser.LhsContext,0)


        def assign_op(self):
            return self.getTypedRuleContext(MiniGoParser.Assign_opContext,0)


        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_assignmentStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignmentStatement" ):
                return visitor.visitAssignmentStatement(self)
            else:
                return visitor.visitChildren(self)




    def assignmentStatement(self):

        localctx = MiniGoParser.AssignmentStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_assignmentStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            self.lhs(0)
            self.state = 226
            self.assign_op()
            self.state = 227
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SHORT_ASSIGN(self):
            return self.getToken(MiniGoParser.SHORT_ASSIGN, 0)

        def ADD_ASSIGN(self):
            return self.getToken(MiniGoParser.ADD_ASSIGN, 0)

        def SUBTRACT_ASSIGN(self):
            return self.getToken(MiniGoParser.SUBTRACT_ASSIGN, 0)

        def MULTIPLY_ASSIGN(self):
            return self.getToken(MiniGoParser.MULTIPLY_ASSIGN, 0)

        def DIVIDE_ASSIGN(self):
            return self.getToken(MiniGoParser.DIVIDE_ASSIGN, 0)

        def MODULO_ASSIGN(self):
            return self.getToken(MiniGoParser.MODULO_ASSIGN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_assign_op

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_op" ):
                return visitor.visitAssign_op(self)
            else:
                return visitor.visitChildren(self)




    def assign_op(self):

        localctx = MiniGoParser.Assign_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_assign_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.SHORT_ASSIGN) | (1 << MiniGoParser.ADD_ASSIGN) | (1 << MiniGoParser.SUBTRACT_ASSIGN) | (1 << MiniGoParser.MULTIPLY_ASSIGN) | (1 << MiniGoParser.DIVIDE_ASSIGN) | (1 << MiniGoParser.MODULO_ASSIGN))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MiniGoParser.IF, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def condition(self):
            return self.getTypedRuleContext(MiniGoParser.ConditionContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.BlockContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.BlockContext,i)


        def ELSE(self):
            return self.getToken(MiniGoParser.ELSE, 0)

        def ifStatement(self):
            return self.getTypedRuleContext(MiniGoParser.IfStatementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_ifStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = MiniGoParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 231
            self.match(MiniGoParser.IF)
            self.state = 232
            self.match(MiniGoParser.LPAREN)
            self.state = 233
            self.condition()
            self.state = 234
            self.match(MiniGoParser.RPAREN)
            self.state = 235
            self.block()
            self.state = 241
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ELSE:
                self.state = 236
                self.match(MiniGoParser.ELSE)
                self.state = 239
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.IF]:
                    self.state = 237
                    self.ifStatement()
                    pass
                elif token in [MiniGoParser.LBRACE]:
                    self.state = 238
                    self.block()
                    pass
                else:
                    raise NoViableAltException(self)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def condition(self):
            return self.getTypedRuleContext(MiniGoParser.ConditionContext,0)


        def forClause(self):
            return self.getTypedRuleContext(MiniGoParser.ForClauseContext,0)


        def rangeClause(self):
            return self.getTypedRuleContext(MiniGoParser.RangeClauseContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_forStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStatement" ):
                return visitor.visitForStatement(self)
            else:
                return visitor.visitChildren(self)




    def forStatement(self):

        localctx = MiniGoParser.ForStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_forStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243
            self.match(MiniGoParser.FOR)
            self.state = 247
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 244
                self.condition()

            elif la_ == 2:
                self.state = 245
                self.forClause()

            elif la_ == 3:
                self.state = 246
                self.rangeClause()


            self.state = 249
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def initStmt(self):
            return self.getTypedRuleContext(MiniGoParser.InitStmtContext,0)


        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.SEMICOLON)
            else:
                return self.getToken(MiniGoParser.SEMICOLON, i)

        def condition(self):
            return self.getTypedRuleContext(MiniGoParser.ConditionContext,0)


        def postStmt(self):
            return self.getTypedRuleContext(MiniGoParser.PostStmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_forClause

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForClause" ):
                return visitor.visitForClause(self)
            else:
                return visitor.visitChildren(self)




    def forClause(self):

        localctx = MiniGoParser.ForClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_forClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
            self.initStmt()
            self.state = 252
            self.match(MiniGoParser.SEMICOLON)
            self.state = 253
            self.condition()
            self.state = 254
            self.match(MiniGoParser.SEMICOLON)
            self.state = 255
            self.postStmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InitStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def scalarAssignment(self):
            return self.getTypedRuleContext(MiniGoParser.ScalarAssignmentContext,0)


        def variableDeclaration(self):
            return self.getTypedRuleContext(MiniGoParser.VariableDeclarationContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_initStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInitStmt" ):
                return visitor.visitInitStmt(self)
            else:
                return visitor.visitChildren(self)




    def initStmt(self):

        localctx = MiniGoParser.InitStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_initStmt)
        try:
            self.state = 259
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 257
                self.scalarAssignment()
                pass
            elif token in [MiniGoParser.VAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 258
                self.variableDeclaration()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PostStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def scalarAssignment(self):
            return self.getTypedRuleContext(MiniGoParser.ScalarAssignmentContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_postStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPostStmt" ):
                return visitor.visitPostStmt(self)
            else:
                return visitor.visitChildren(self)




    def postStmt(self):

        localctx = MiniGoParser.PostStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_postStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 261
            self.scalarAssignment()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_condition

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)




    def condition(self):

        localctx = MiniGoParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 263
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ScalarAssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def assign_op(self):
            return self.getTypedRuleContext(MiniGoParser.Assign_opContext,0)


        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_scalarAssignment

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScalarAssignment" ):
                return visitor.visitScalarAssignment(self)
            else:
                return visitor.visitChildren(self)




    def scalarAssignment(self):

        localctx = MiniGoParser.ScalarAssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_scalarAssignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 266
            self.assign_op()
            self.state = 267
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RangeClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.IDENTIFIER)
            else:
                return self.getToken(MiniGoParser.IDENTIFIER, i)

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def SHORT_ASSIGN(self):
            return self.getToken(MiniGoParser.SHORT_ASSIGN, 0)

        def RANGE(self):
            return self.getToken(MiniGoParser.RANGE, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_rangeClause

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRangeClause" ):
                return visitor.visitRangeClause(self)
            else:
                return visitor.visitChildren(self)




    def rangeClause(self):

        localctx = MiniGoParser.RangeClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_rangeClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 269
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 270
            self.match(MiniGoParser.COMMA)
            self.state = 271
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 272
            self.match(MiniGoParser.SHORT_ASSIGN)
            self.state = 273
            self.match(MiniGoParser.RANGE)
            self.state = 274
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(MiniGoParser.BREAK, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_breakStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakStatement" ):
                return visitor.visitBreakStatement(self)
            else:
                return visitor.visitChildren(self)




    def breakStatement(self):

        localctx = MiniGoParser.BreakStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_breakStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 276
            self.match(MiniGoParser.BREAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinueStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(MiniGoParser.CONTINUE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_continueStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinueStatement" ):
                return visitor.visitContinueStatement(self)
            else:
                return visitor.visitChildren(self)




    def continueStatement(self):

        localctx = MiniGoParser.ContinueStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_continueStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 278
            self.match(MiniGoParser.CONTINUE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(MiniGoParser.RETURN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_returnStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStatement" ):
                return visitor.visitReturnStatement(self)
            else:
                return visitor.visitChildren(self)




    def returnStatement(self):

        localctx = MiniGoParser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_returnStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 280
            self.match(MiniGoParser.RETURN)
            self.state = 282
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 19)) & ~0x3f) == 0 and ((1 << (_la - 19)) & ((1 << (MiniGoParser.SUBTRACT - 19)) | (1 << (MiniGoParser.NOT - 19)) | (1 << (MiniGoParser.LPAREN - 19)) | (1 << (MiniGoParser.LBRACKET - 19)) | (1 << (MiniGoParser.INT_LIT - 19)) | (1 << (MiniGoParser.FLOAT_LIT - 19)) | (1 << (MiniGoParser.STRING_LIT - 19)) | (1 << (MiniGoParser.BOOL_LIT - 19)) | (1 << (MiniGoParser.NIL_LIT - 19)) | (1 << (MiniGoParser.IDENTIFIER - 19)) | (1 << (MiniGoParser.GETINT - 19)) | (1 << (MiniGoParser.PUTINT - 19)) | (1 << (MiniGoParser.PUTINTLN - 19)) | (1 << (MiniGoParser.GETFLOAT - 19)) | (1 << (MiniGoParser.PUTFLOAT - 19)) | (1 << (MiniGoParser.PUTFLOATLN - 19)) | (1 << (MiniGoParser.GETBOOL - 19)) | (1 << (MiniGoParser.PUTBOOL - 19)) | (1 << (MiniGoParser.PUTBOOLLN - 19)) | (1 << (MiniGoParser.GETSTRING - 19)) | (1 << (MiniGoParser.PUTSTRING - 19)) | (1 << (MiniGoParser.PUTSTRINGLN - 19)) | (1 << (MiniGoParser.PUTLN - 19)))) != 0):
                self.state = 281
                self.expression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def expressionParts(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionPartsContext,0)


        def builtInFunctionCall(self):
            return self.getTypedRuleContext(MiniGoParser.BuiltInFunctionCallContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_callStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallStatement" ):
                return visitor.visitCallStatement(self)
            else:
                return visitor.visitChildren(self)




    def callStatement(self):

        localctx = MiniGoParser.CallStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_callStatement)
        try:
            self.state = 287
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 284
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 285
                self.expressionParts()
                pass
            elif token in [MiniGoParser.GETINT, MiniGoParser.PUTINT, MiniGoParser.PUTINTLN, MiniGoParser.GETFLOAT, MiniGoParser.PUTFLOAT, MiniGoParser.PUTFLOATLN, MiniGoParser.GETBOOL, MiniGoParser.PUTBOOL, MiniGoParser.PUTBOOLLN, MiniGoParser.GETSTRING, MiniGoParser.PUTSTRING, MiniGoParser.PUTSTRINGLN, MiniGoParser.PUTLN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 286
                self.builtInFunctionCall()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionPartsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressionPart(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionPartContext,0)


        def expressionParts(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionPartsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expressionParts

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionParts" ):
                return visitor.visitExpressionParts(self)
            else:
                return visitor.visitChildren(self)




    def expressionParts(self):

        localctx = MiniGoParser.ExpressionPartsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_expressionParts)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 289
            self.expressionPart()
            self.state = 291
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.DOT) | (1 << MiniGoParser.LPAREN) | (1 << MiniGoParser.LBRACKET))) != 0):
                self.state = 290
                self.expressionParts()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionPartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arguments(self):
            return self.getTypedRuleContext(MiniGoParser.ArgumentsContext,0)


        def selector(self):
            return self.getTypedRuleContext(MiniGoParser.SelectorContext,0)


        def index(self):
            return self.getTypedRuleContext(MiniGoParser.IndexContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expressionPart

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionPart" ):
                return visitor.visitExpressionPart(self)
            else:
                return visitor.visitChildren(self)




    def expressionPart(self):

        localctx = MiniGoParser.ExpressionPartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_expressionPart)
        try:
            self.state = 296
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.LPAREN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 293
                self.arguments()
                pass
            elif token in [MiniGoParser.DOT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 294
                self.selector()
                pass
            elif token in [MiniGoParser.LBRACKET]:
                self.enterOuterAlt(localctx, 3)
                self.state = 295
                self.index()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicalExpr(self):
            return self.getTypedRuleContext(MiniGoParser.LogicalExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = MiniGoParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 298
            self.logicalExpr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def higherLogicalExpr(self):
            return self.getTypedRuleContext(MiniGoParser.HigherLogicalExprContext,0)


        def logicalExpr(self):
            return self.getTypedRuleContext(MiniGoParser.LogicalExprContext,0)


        def OR(self):
            return self.getToken(MiniGoParser.OR, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_logicalExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalExpr" ):
                return visitor.visitLogicalExpr(self)
            else:
                return visitor.visitChildren(self)



    def logicalExpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.LogicalExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 60
        self.enterRecursionRule(localctx, 60, self.RULE_logicalExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 301
            self.higherLogicalExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 308
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.LogicalExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logicalExpr)
                    self.state = 303
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 304
                    self.match(MiniGoParser.OR)
                    self.state = 305
                    self.higherLogicalExpr(0) 
                self.state = 310
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class HigherLogicalExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relationalExpr(self):
            return self.getTypedRuleContext(MiniGoParser.RelationalExprContext,0)


        def higherLogicalExpr(self):
            return self.getTypedRuleContext(MiniGoParser.HigherLogicalExprContext,0)


        def AND(self):
            return self.getToken(MiniGoParser.AND, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_higherLogicalExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHigherLogicalExpr" ):
                return visitor.visitHigherLogicalExpr(self)
            else:
                return visitor.visitChildren(self)



    def higherLogicalExpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.HigherLogicalExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 62
        self.enterRecursionRule(localctx, 62, self.RULE_higherLogicalExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 312
            self.relationalExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 319
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.HigherLogicalExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_higherLogicalExpr)
                    self.state = 314
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 315
                    self.match(MiniGoParser.AND)
                    self.state = 316
                    self.relationalExpr(0) 
                self.state = 321
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class RelationalExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def additiveExpr(self):
            return self.getTypedRuleContext(MiniGoParser.AdditiveExprContext,0)


        def relationalExpr(self):
            return self.getTypedRuleContext(MiniGoParser.RelationalExprContext,0)


        def rel_op(self):
            return self.getTypedRuleContext(MiniGoParser.Rel_opContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_relationalExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelationalExpr" ):
                return visitor.visitRelationalExpr(self)
            else:
                return visitor.visitChildren(self)



    def relationalExpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.RelationalExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 64
        self.enterRecursionRule(localctx, 64, self.RULE_relationalExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 323
            self.additiveExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 331
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.RelationalExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_relationalExpr)
                    self.state = 325
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 326
                    self.rel_op()
                    self.state = 327
                    self.additiveExpr(0) 
                self.state = 333
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AdditiveExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplicativeExpr(self):
            return self.getTypedRuleContext(MiniGoParser.MultiplicativeExprContext,0)


        def additiveExpr(self):
            return self.getTypedRuleContext(MiniGoParser.AdditiveExprContext,0)


        def add_op(self):
            return self.getTypedRuleContext(MiniGoParser.Add_opContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_additiveExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdditiveExpr" ):
                return visitor.visitAdditiveExpr(self)
            else:
                return visitor.visitChildren(self)



    def additiveExpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.AdditiveExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 66
        self.enterRecursionRule(localctx, 66, self.RULE_additiveExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 335
            self.multiplicativeExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 343
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.AdditiveExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_additiveExpr)
                    self.state = 337
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 338
                    self.add_op()
                    self.state = 339
                    self.multiplicativeExpr(0) 
                self.state = 345
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class MultiplicativeExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unaryExpr(self):
            return self.getTypedRuleContext(MiniGoParser.UnaryExprContext,0)


        def multiplicativeExpr(self):
            return self.getTypedRuleContext(MiniGoParser.MultiplicativeExprContext,0)


        def mul_op(self):
            return self.getTypedRuleContext(MiniGoParser.Mul_opContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_multiplicativeExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicativeExpr" ):
                return visitor.visitMultiplicativeExpr(self)
            else:
                return visitor.visitChildren(self)



    def multiplicativeExpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.MultiplicativeExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 68
        self.enterRecursionRule(localctx, 68, self.RULE_multiplicativeExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 347
            self.unaryExpr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 355
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.MultiplicativeExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplicativeExpr)
                    self.state = 349
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 350
                    self.mul_op()
                    self.state = 351
                    self.unaryExpr() 
                self.state = 357
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class UnaryExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primaryExpr(self):
            return self.getTypedRuleContext(MiniGoParser.PrimaryExprContext,0)


        def unary_op(self):
            return self.getTypedRuleContext(MiniGoParser.Unary_opContext,0)


        def unaryExpr(self):
            return self.getTypedRuleContext(MiniGoParser.UnaryExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_unaryExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryExpr" ):
                return visitor.visitUnaryExpr(self)
            else:
                return visitor.visitChildren(self)




    def unaryExpr(self):

        localctx = MiniGoParser.UnaryExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_unaryExpr)
        try:
            self.state = 362
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.LPAREN, MiniGoParser.LBRACKET, MiniGoParser.INT_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT, MiniGoParser.BOOL_LIT, MiniGoParser.NIL_LIT, MiniGoParser.IDENTIFIER, MiniGoParser.GETINT, MiniGoParser.PUTINT, MiniGoParser.PUTINTLN, MiniGoParser.GETFLOAT, MiniGoParser.PUTFLOAT, MiniGoParser.PUTFLOATLN, MiniGoParser.GETBOOL, MiniGoParser.PUTBOOL, MiniGoParser.PUTBOOLLN, MiniGoParser.GETSTRING, MiniGoParser.PUTSTRING, MiniGoParser.PUTSTRINGLN, MiniGoParser.PUTLN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 358
                self.primaryExpr(0)
                pass
            elif token in [MiniGoParser.SUBTRACT, MiniGoParser.NOT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 359
                self.unary_op()
                self.state = 360
                self.unaryExpr()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operand(self):
            return self.getTypedRuleContext(MiniGoParser.OperandContext,0)


        def builtInFunctionCall(self):
            return self.getTypedRuleContext(MiniGoParser.BuiltInFunctionCallContext,0)


        def primaryExpr(self):
            return self.getTypedRuleContext(MiniGoParser.PrimaryExprContext,0)


        def index(self):
            return self.getTypedRuleContext(MiniGoParser.IndexContext,0)


        def selector(self):
            return self.getTypedRuleContext(MiniGoParser.SelectorContext,0)


        def arguments(self):
            return self.getTypedRuleContext(MiniGoParser.ArgumentsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_primaryExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimaryExpr" ):
                return visitor.visitPrimaryExpr(self)
            else:
                return visitor.visitChildren(self)



    def primaryExpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.PrimaryExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 72
        self.enterRecursionRule(localctx, 72, self.RULE_primaryExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 367
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.LPAREN, MiniGoParser.LBRACKET, MiniGoParser.INT_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT, MiniGoParser.BOOL_LIT, MiniGoParser.NIL_LIT, MiniGoParser.IDENTIFIER]:
                self.state = 365
                self.operand()
                pass
            elif token in [MiniGoParser.GETINT, MiniGoParser.PUTINT, MiniGoParser.PUTINTLN, MiniGoParser.GETFLOAT, MiniGoParser.PUTFLOAT, MiniGoParser.PUTFLOATLN, MiniGoParser.GETBOOL, MiniGoParser.PUTBOOL, MiniGoParser.PUTBOOLLN, MiniGoParser.GETSTRING, MiniGoParser.PUTSTRING, MiniGoParser.PUTSTRINGLN, MiniGoParser.PUTLN]:
                self.state = 366
                self.builtInFunctionCall()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 377
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 375
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.PrimaryExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_primaryExpr)
                        self.state = 369
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 370
                        self.index()
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.PrimaryExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_primaryExpr)
                        self.state = 371
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 372
                        self.selector()
                        pass

                    elif la_ == 3:
                        localctx = MiniGoParser.PrimaryExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_primaryExpr)
                        self.state = 373
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 374
                        self.arguments()
                        pass

             
                self.state = 379
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class SelectorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_selector

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSelector" ):
                return visitor.visitSelector(self)
            else:
                return visitor.visitChildren(self)




    def selector(self):

        localctx = MiniGoParser.SelectorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_selector)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 380
            self.match(MiniGoParser.DOT)
            self.state = 381
            self.match(MiniGoParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def expressionList(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionListContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arguments

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArguments" ):
                return visitor.visitArguments(self)
            else:
                return visitor.visitChildren(self)




    def arguments(self):

        localctx = MiniGoParser.ArgumentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_arguments)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 383
            self.match(MiniGoParser.LPAREN)
            self.state = 385
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 19)) & ~0x3f) == 0 and ((1 << (_la - 19)) & ((1 << (MiniGoParser.SUBTRACT - 19)) | (1 << (MiniGoParser.NOT - 19)) | (1 << (MiniGoParser.LPAREN - 19)) | (1 << (MiniGoParser.LBRACKET - 19)) | (1 << (MiniGoParser.INT_LIT - 19)) | (1 << (MiniGoParser.FLOAT_LIT - 19)) | (1 << (MiniGoParser.STRING_LIT - 19)) | (1 << (MiniGoParser.BOOL_LIT - 19)) | (1 << (MiniGoParser.NIL_LIT - 19)) | (1 << (MiniGoParser.IDENTIFIER - 19)) | (1 << (MiniGoParser.GETINT - 19)) | (1 << (MiniGoParser.PUTINT - 19)) | (1 << (MiniGoParser.PUTINTLN - 19)) | (1 << (MiniGoParser.GETFLOAT - 19)) | (1 << (MiniGoParser.PUTFLOAT - 19)) | (1 << (MiniGoParser.PUTFLOATLN - 19)) | (1 << (MiniGoParser.GETBOOL - 19)) | (1 << (MiniGoParser.PUTBOOL - 19)) | (1 << (MiniGoParser.PUTBOOLLN - 19)) | (1 << (MiniGoParser.GETSTRING - 19)) | (1 << (MiniGoParser.PUTSTRING - 19)) | (1 << (MiniGoParser.PUTSTRINGLN - 19)) | (1 << (MiniGoParser.PUTLN - 19)))) != 0):
                self.state = 384
                self.expressionList()


            self.state = 387
            self.match(MiniGoParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IndexContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACKET(self):
            return self.getToken(MiniGoParser.LBRACKET, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def RBRACKET(self):
            return self.getToken(MiniGoParser.RBRACKET, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_index

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex" ):
                return visitor.visitIndex(self)
            else:
                return visitor.visitChildren(self)




    def index(self):

        localctx = MiniGoParser.IndexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_index)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 389
            self.match(MiniGoParser.LBRACKET)
            self.state = 390
            self.expression()
            self.state = 391
            self.match(MiniGoParser.RBRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def basicLit(self):
            return self.getTypedRuleContext(MiniGoParser.BasicLitContext,0)


        def arrayLit(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayLitContext,0)


        def structLit(self):
            return self.getTypedRuleContext(MiniGoParser.StructLitContext,0)


        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_operand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand" ):
                return visitor.visitOperand(self)
            else:
                return visitor.visitChildren(self)




    def operand(self):

        localctx = MiniGoParser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_operand)
        try:
            self.state = 401
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 393
                self.match(MiniGoParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 394
                self.basicLit()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 395
                self.arrayLit()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 396
                self.structLit()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 397
                self.match(MiniGoParser.LPAREN)
                self.state = 398
                self.expression()
                self.state = 399
                self.match(MiniGoParser.RPAREN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BasicLitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_LIT(self):
            return self.getToken(MiniGoParser.INT_LIT, 0)

        def FLOAT_LIT(self):
            return self.getToken(MiniGoParser.FLOAT_LIT, 0)

        def STRING_LIT(self):
            return self.getToken(MiniGoParser.STRING_LIT, 0)

        def BOOL_LIT(self):
            return self.getToken(MiniGoParser.BOOL_LIT, 0)

        def NIL_LIT(self):
            return self.getToken(MiniGoParser.NIL_LIT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_basicLit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBasicLit" ):
                return visitor.visitBasicLit(self)
            else:
                return visitor.visitChildren(self)




    def basicLit(self):

        localctx = MiniGoParser.BasicLitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_basicLit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 403
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.INT_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STRING_LIT) | (1 << MiniGoParser.BOOL_LIT) | (1 << MiniGoParser.NIL_LIT))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayLitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arrayType(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayTypeContext,0)


        def arrayValue(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayValueContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arrayLit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayLit" ):
                return visitor.visitArrayLit(self)
            else:
                return visitor.visitChildren(self)




    def arrayLit(self):

        localctx = MiniGoParser.ArrayLitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_arrayLit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 405
            self.arrayType()
            self.state = 406
            self.arrayValue()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def arrayElems(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayElemsContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_arrayValue

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayValue" ):
                return visitor.visitArrayValue(self)
            else:
                return visitor.visitChildren(self)




    def arrayValue(self):

        localctx = MiniGoParser.ArrayValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_arrayValue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 408
            self.match(MiniGoParser.LBRACE)
            self.state = 409
            self.arrayElems()
            self.state = 410
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayElemsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def basicLit(self):
            return self.getTypedRuleContext(MiniGoParser.BasicLitContext,0)


        def arrayValue(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayValueContext,0)


        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def arrayElems(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayElemsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arrayElems

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayElems" ):
                return visitor.visitArrayElems(self)
            else:
                return visitor.visitChildren(self)




    def arrayElems(self):

        localctx = MiniGoParser.ArrayElemsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_arrayElems)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 415
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.INT_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT, MiniGoParser.BOOL_LIT, MiniGoParser.NIL_LIT]:
                self.state = 412
                self.basicLit()
                pass
            elif token in [MiniGoParser.LBRACE]:
                self.state = 413
                self.arrayValue()
                pass
            elif token in [MiniGoParser.IDENTIFIER]:
                self.state = 414
                self.match(MiniGoParser.IDENTIFIER)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 419
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.COMMA:
                self.state = 417
                self.match(MiniGoParser.COMMA)
                self.state = 418
                self.arrayElems()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructLitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def structvalue(self):
            return self.getTypedRuleContext(MiniGoParser.StructvalueContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_structLit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructLit" ):
                return visitor.visitStructLit(self)
            else:
                return visitor.visitChildren(self)




    def structLit(self):

        localctx = MiniGoParser.StructLitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_structLit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 421
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 422
            self.structvalue()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructvalueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def fieldValue(self):
            return self.getTypedRuleContext(MiniGoParser.FieldValueContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_structvalue

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructvalue" ):
                return visitor.visitStructvalue(self)
            else:
                return visitor.visitChildren(self)




    def structvalue(self):

        localctx = MiniGoParser.StructvalueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_structvalue)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 424
            self.match(MiniGoParser.LBRACE)
            self.state = 426
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.IDENTIFIER:
                self.state = 425
                self.fieldValue()


            self.state = 428
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def COLON(self):
            return self.getToken(MiniGoParser.COLON, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def fieldValue(self):
            return self.getTypedRuleContext(MiniGoParser.FieldValueContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_fieldValue

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFieldValue" ):
                return visitor.visitFieldValue(self)
            else:
                return visitor.visitChildren(self)




    def fieldValue(self):

        localctx = MiniGoParser.FieldValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_fieldValue)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 430
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 431
            self.match(MiniGoParser.COLON)
            self.state = 432
            self.expression()
            self.state = 435
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.COMMA:
                self.state = 433
                self.match(MiniGoParser.COMMA)
                self.state = 434
                self.fieldValue()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACKET(self):
            return self.getToken(MiniGoParser.LBRACKET, 0)

        def RBRACKET(self):
            return self.getToken(MiniGoParser.RBRACKET, 0)

        def types(self):
            return self.getTypedRuleContext(MiniGoParser.TypesContext,0)


        def INT_LIT(self):
            return self.getToken(MiniGoParser.INT_LIT, 0)

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_arrayType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayType" ):
                return visitor.visitArrayType(self)
            else:
                return visitor.visitChildren(self)




    def arrayType(self):

        localctx = MiniGoParser.ArrayTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_arrayType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 437
            self.match(MiniGoParser.LBRACKET)
            self.state = 438
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.INT_LIT or _la==MiniGoParser.IDENTIFIER):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 439
            self.match(MiniGoParser.RBRACKET)
            self.state = 440
            self.types()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def STRUCT(self):
            return self.getToken(MiniGoParser.STRUCT, 0)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def fieldDeclarations(self):
            return self.getTypedRuleContext(MiniGoParser.FieldDeclarationsContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_structType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructType" ):
                return visitor.visitStructType(self)
            else:
                return visitor.visitChildren(self)




    def structType(self):

        localctx = MiniGoParser.StructTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_structType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 442
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 443
            self.match(MiniGoParser.STRUCT)
            self.state = 444
            self.match(MiniGoParser.LBRACE)
            self.state = 445
            self.fieldDeclarations()
            self.state = 446
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldDeclarationsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fieldDeclaration(self):
            return self.getTypedRuleContext(MiniGoParser.FieldDeclarationContext,0)


        def fieldDeclarations(self):
            return self.getTypedRuleContext(MiniGoParser.FieldDeclarationsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_fieldDeclarations

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFieldDeclarations" ):
                return visitor.visitFieldDeclarations(self)
            else:
                return visitor.visitChildren(self)




    def fieldDeclarations(self):

        localctx = MiniGoParser.FieldDeclarationsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_fieldDeclarations)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 448
            self.fieldDeclaration()
            self.state = 450
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.IDENTIFIER:
                self.state = 449
                self.fieldDeclarations()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifierList(self):
            return self.getTypedRuleContext(MiniGoParser.IdentifierListContext,0)


        def types(self):
            return self.getTypedRuleContext(MiniGoParser.TypesContext,0)


        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_fieldDeclaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFieldDeclaration" ):
                return visitor.visitFieldDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def fieldDeclaration(self):

        localctx = MiniGoParser.FieldDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_fieldDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 452
            self.identifierList()
            self.state = 453
            self.types()
            self.state = 454
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InterfaceTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def INTERFACE(self):
            return self.getToken(MiniGoParser.INTERFACE, 0)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def interfaceElem(self):
            return self.getTypedRuleContext(MiniGoParser.InterfaceElemContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_interfaceType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterfaceType" ):
                return visitor.visitInterfaceType(self)
            else:
                return visitor.visitChildren(self)




    def interfaceType(self):

        localctx = MiniGoParser.InterfaceTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_interfaceType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 456
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 457
            self.match(MiniGoParser.INTERFACE)
            self.state = 458
            self.match(MiniGoParser.LBRACE)
            self.state = 459
            self.interfaceElem()
            self.state = 460
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InterfaceElemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def methodElem(self):
            return self.getTypedRuleContext(MiniGoParser.MethodElemContext,0)


        def interfaceElem(self):
            return self.getTypedRuleContext(MiniGoParser.InterfaceElemContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_interfaceElem

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterfaceElem" ):
                return visitor.visitInterfaceElem(self)
            else:
                return visitor.visitChildren(self)




    def interfaceElem(self):

        localctx = MiniGoParser.InterfaceElemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_interfaceElem)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 462
            self.methodElem()
            self.state = 464
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.IDENTIFIER:
                self.state = 463
                self.interfaceElem()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodElemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def parameter_type(self):
            return self.getTypedRuleContext(MiniGoParser.Parameter_typeContext,0)


        def types(self):
            return self.getTypedRuleContext(MiniGoParser.TypesContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_methodElem

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodElem" ):
                return visitor.visitMethodElem(self)
            else:
                return visitor.visitChildren(self)




    def methodElem(self):

        localctx = MiniGoParser.MethodElemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_methodElem)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 466
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 467
            self.match(MiniGoParser.LPAREN)
            self.state = 469
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.IDENTIFIER:
                self.state = 468
                self.parameter_type()


            self.state = 471
            self.match(MiniGoParser.RPAREN)
            self.state = 473
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LBRACKET) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                self.state = 472
                self.types()


            self.state = 475
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Parameter_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifierList(self):
            return self.getTypedRuleContext(MiniGoParser.IdentifierListContext,0)


        def types(self):
            return self.getTypedRuleContext(MiniGoParser.TypesContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def parameter_type(self):
            return self.getTypedRuleContext(MiniGoParser.Parameter_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_parameter_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter_type" ):
                return visitor.visitParameter_type(self)
            else:
                return visitor.visitChildren(self)




    def parameter_type(self):

        localctx = MiniGoParser.Parameter_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_parameter_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 477
            self.identifierList()
            self.state = 478
            self.types()
            self.state = 481
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.COMMA:
                self.state = 479
                self.match(MiniGoParser.COMMA)
                self.state = 480
                self.parameter_type()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Rel_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUAL(self):
            return self.getToken(MiniGoParser.EQUAL, 0)

        def NOT_EQUAL(self):
            return self.getToken(MiniGoParser.NOT_EQUAL, 0)

        def LESS_THAN(self):
            return self.getToken(MiniGoParser.LESS_THAN, 0)

        def LESS_THAN_OR_EQUAL(self):
            return self.getToken(MiniGoParser.LESS_THAN_OR_EQUAL, 0)

        def GREATER_THAN(self):
            return self.getToken(MiniGoParser.GREATER_THAN, 0)

        def GREATER_THAN_OR_EQUAL(self):
            return self.getToken(MiniGoParser.GREATER_THAN_OR_EQUAL, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_rel_op

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRel_op" ):
                return visitor.visitRel_op(self)
            else:
                return visitor.visitChildren(self)




    def rel_op(self):

        localctx = MiniGoParser.Rel_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_rel_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 483
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.EQUAL) | (1 << MiniGoParser.NOT_EQUAL) | (1 << MiniGoParser.LESS_THAN) | (1 << MiniGoParser.LESS_THAN_OR_EQUAL) | (1 << MiniGoParser.GREATER_THAN) | (1 << MiniGoParser.GREATER_THAN_OR_EQUAL))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Add_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADD(self):
            return self.getToken(MiniGoParser.ADD, 0)

        def SUBTRACT(self):
            return self.getToken(MiniGoParser.SUBTRACT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_add_op

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdd_op" ):
                return visitor.visitAdd_op(self)
            else:
                return visitor.visitChildren(self)




    def add_op(self):

        localctx = MiniGoParser.Add_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_add_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 485
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.ADD or _la==MiniGoParser.SUBTRACT):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Mul_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MULTIPLY(self):
            return self.getToken(MiniGoParser.MULTIPLY, 0)

        def DIVIDE(self):
            return self.getToken(MiniGoParser.DIVIDE, 0)

        def MODULO(self):
            return self.getToken(MiniGoParser.MODULO, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_mul_op

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMul_op" ):
                return visitor.visitMul_op(self)
            else:
                return visitor.visitChildren(self)




    def mul_op(self):

        localctx = MiniGoParser.Mul_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_mul_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 487
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MULTIPLY) | (1 << MiniGoParser.DIVIDE) | (1 << MiniGoParser.MODULO))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Unary_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUBTRACT(self):
            return self.getToken(MiniGoParser.SUBTRACT, 0)

        def NOT(self):
            return self.getToken(MiniGoParser.NOT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_unary_op

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnary_op" ):
                return visitor.visitUnary_op(self)
            else:
                return visitor.visitChildren(self)




    def unary_op(self):

        localctx = MiniGoParser.Unary_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_unary_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 489
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.SUBTRACT or _la==MiniGoParser.NOT):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def lhs(self):
            return self.getTypedRuleContext(MiniGoParser.LhsContext,0)


        def selector(self):
            return self.getTypedRuleContext(MiniGoParser.SelectorContext,0)


        def index(self):
            return self.getTypedRuleContext(MiniGoParser.IndexContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)



    def lhs(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.LhsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 120
        self.enterRecursionRule(localctx, 120, self.RULE_lhs, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 492
            self.match(MiniGoParser.IDENTIFIER)
            self._ctx.stop = self._input.LT(-1)
            self.state = 500
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,40,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 498
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.LhsContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_lhs)
                        self.state = 494
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 495
                        self.selector()
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.LhsContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_lhs)
                        self.state = 496
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 497
                        self.index()
                        pass

             
                self.state = 502
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,40,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TypesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(MiniGoParser.INT, 0)

        def FLOAT(self):
            return self.getToken(MiniGoParser.FLOAT, 0)

        def BOOLEAN(self):
            return self.getToken(MiniGoParser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(MiniGoParser.STRING, 0)

        def arrayType(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayTypeContext,0)


        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_types

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypes" ):
                return visitor.visitTypes(self)
            else:
                return visitor.visitChildren(self)




    def types(self):

        localctx = MiniGoParser.TypesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_types)
        try:
            self.state = 509
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 503
                self.match(MiniGoParser.INT)
                pass
            elif token in [MiniGoParser.FLOAT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 504
                self.match(MiniGoParser.FLOAT)
                pass
            elif token in [MiniGoParser.BOOLEAN]:
                self.enterOuterAlt(localctx, 3)
                self.state = 505
                self.match(MiniGoParser.BOOLEAN)
                pass
            elif token in [MiniGoParser.STRING]:
                self.enterOuterAlt(localctx, 4)
                self.state = 506
                self.match(MiniGoParser.STRING)
                pass
            elif token in [MiniGoParser.LBRACKET]:
                self.enterOuterAlt(localctx, 5)
                self.state = 507
                self.arrayType()
                pass
            elif token in [MiniGoParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 6)
                self.state = 508
                self.match(MiniGoParser.IDENTIFIER)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BuiltInFunctionCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniGoParser.RULE_builtInFunctionCall

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class GetBoolCallContext(BuiltInFunctionCallContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniGoParser.BuiltInFunctionCallContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def GETBOOL(self):
            return self.getToken(MiniGoParser.GETBOOL, 0)
        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)
        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGetBoolCall" ):
                return visitor.visitGetBoolCall(self)
            else:
                return visitor.visitChildren(self)


    class GetIntCallContext(BuiltInFunctionCallContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniGoParser.BuiltInFunctionCallContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def GETINT(self):
            return self.getToken(MiniGoParser.GETINT, 0)
        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)
        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGetIntCall" ):
                return visitor.visitGetIntCall(self)
            else:
                return visitor.visitChildren(self)


    class PutLnCallContext(BuiltInFunctionCallContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniGoParser.BuiltInFunctionCallContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PUTLN(self):
            return self.getToken(MiniGoParser.PUTLN, 0)
        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)
        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPutLnCall" ):
                return visitor.visitPutLnCall(self)
            else:
                return visitor.visitChildren(self)


    class GetFloatCallContext(BuiltInFunctionCallContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniGoParser.BuiltInFunctionCallContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def GETFLOAT(self):
            return self.getToken(MiniGoParser.GETFLOAT, 0)
        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)
        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGetFloatCall" ):
                return visitor.visitGetFloatCall(self)
            else:
                return visitor.visitChildren(self)


    class PutBoolCallContext(BuiltInFunctionCallContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniGoParser.BuiltInFunctionCallContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PUTBOOL(self):
            return self.getToken(MiniGoParser.PUTBOOL, 0)
        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)
        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPutBoolCall" ):
                return visitor.visitPutBoolCall(self)
            else:
                return visitor.visitChildren(self)


    class PutFloatLnCallContext(BuiltInFunctionCallContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniGoParser.BuiltInFunctionCallContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PUTFLOATLN(self):
            return self.getToken(MiniGoParser.PUTFLOATLN, 0)
        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)
        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPutFloatLnCall" ):
                return visitor.visitPutFloatLnCall(self)
            else:
                return visitor.visitChildren(self)


    class GetStringCallContext(BuiltInFunctionCallContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniGoParser.BuiltInFunctionCallContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def GETSTRING(self):
            return self.getToken(MiniGoParser.GETSTRING, 0)
        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)
        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGetStringCall" ):
                return visitor.visitGetStringCall(self)
            else:
                return visitor.visitChildren(self)


    class PutIntCallContext(BuiltInFunctionCallContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniGoParser.BuiltInFunctionCallContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PUTINT(self):
            return self.getToken(MiniGoParser.PUTINT, 0)
        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)
        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPutIntCall" ):
                return visitor.visitPutIntCall(self)
            else:
                return visitor.visitChildren(self)


    class PutStringCallContext(BuiltInFunctionCallContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniGoParser.BuiltInFunctionCallContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PUTSTRING(self):
            return self.getToken(MiniGoParser.PUTSTRING, 0)
        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)
        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPutStringCall" ):
                return visitor.visitPutStringCall(self)
            else:
                return visitor.visitChildren(self)


    class PutBoolLnCallContext(BuiltInFunctionCallContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniGoParser.BuiltInFunctionCallContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PUTBOOLLN(self):
            return self.getToken(MiniGoParser.PUTBOOLLN, 0)
        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)
        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPutBoolLnCall" ):
                return visitor.visitPutBoolLnCall(self)
            else:
                return visitor.visitChildren(self)


    class PutIntLnCallContext(BuiltInFunctionCallContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniGoParser.BuiltInFunctionCallContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PUTINTLN(self):
            return self.getToken(MiniGoParser.PUTINTLN, 0)
        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)
        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPutIntLnCall" ):
                return visitor.visitPutIntLnCall(self)
            else:
                return visitor.visitChildren(self)


    class PutStringLnCallContext(BuiltInFunctionCallContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniGoParser.BuiltInFunctionCallContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PUTSTRINGLN(self):
            return self.getToken(MiniGoParser.PUTSTRINGLN, 0)
        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)
        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPutStringLnCall" ):
                return visitor.visitPutStringLnCall(self)
            else:
                return visitor.visitChildren(self)


    class PutFloatCallContext(BuiltInFunctionCallContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniGoParser.BuiltInFunctionCallContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PUTFLOAT(self):
            return self.getToken(MiniGoParser.PUTFLOAT, 0)
        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)
        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPutFloatCall" ):
                return visitor.visitPutFloatCall(self)
            else:
                return visitor.visitChildren(self)



    def builtInFunctionCall(self):

        localctx = MiniGoParser.BuiltInFunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_builtInFunctionCall)
        try:
            self.state = 566
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.GETINT]:
                localctx = MiniGoParser.GetIntCallContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 511
                self.match(MiniGoParser.GETINT)
                self.state = 512
                self.match(MiniGoParser.LPAREN)
                self.state = 513
                self.match(MiniGoParser.RPAREN)
                pass
            elif token in [MiniGoParser.PUTINT]:
                localctx = MiniGoParser.PutIntCallContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 514
                self.match(MiniGoParser.PUTINT)
                self.state = 515
                self.match(MiniGoParser.LPAREN)
                self.state = 516
                self.expression()
                self.state = 517
                self.match(MiniGoParser.RPAREN)
                pass
            elif token in [MiniGoParser.PUTINTLN]:
                localctx = MiniGoParser.PutIntLnCallContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 519
                self.match(MiniGoParser.PUTINTLN)
                self.state = 520
                self.match(MiniGoParser.LPAREN)
                self.state = 521
                self.expression()
                self.state = 522
                self.match(MiniGoParser.RPAREN)
                pass
            elif token in [MiniGoParser.GETFLOAT]:
                localctx = MiniGoParser.GetFloatCallContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 524
                self.match(MiniGoParser.GETFLOAT)
                self.state = 525
                self.match(MiniGoParser.LPAREN)
                self.state = 526
                self.match(MiniGoParser.RPAREN)
                pass
            elif token in [MiniGoParser.PUTFLOAT]:
                localctx = MiniGoParser.PutFloatCallContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 527
                self.match(MiniGoParser.PUTFLOAT)
                self.state = 528
                self.match(MiniGoParser.LPAREN)
                self.state = 529
                self.expression()
                self.state = 530
                self.match(MiniGoParser.RPAREN)
                pass
            elif token in [MiniGoParser.PUTFLOATLN]:
                localctx = MiniGoParser.PutFloatLnCallContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 532
                self.match(MiniGoParser.PUTFLOATLN)
                self.state = 533
                self.match(MiniGoParser.LPAREN)
                self.state = 534
                self.expression()
                self.state = 535
                self.match(MiniGoParser.RPAREN)
                pass
            elif token in [MiniGoParser.GETBOOL]:
                localctx = MiniGoParser.GetBoolCallContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 537
                self.match(MiniGoParser.GETBOOL)
                self.state = 538
                self.match(MiniGoParser.LPAREN)
                self.state = 539
                self.match(MiniGoParser.RPAREN)
                pass
            elif token in [MiniGoParser.PUTBOOL]:
                localctx = MiniGoParser.PutBoolCallContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 540
                self.match(MiniGoParser.PUTBOOL)
                self.state = 541
                self.match(MiniGoParser.LPAREN)
                self.state = 542
                self.expression()
                self.state = 543
                self.match(MiniGoParser.RPAREN)
                pass
            elif token in [MiniGoParser.PUTBOOLLN]:
                localctx = MiniGoParser.PutBoolLnCallContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 545
                self.match(MiniGoParser.PUTBOOLLN)
                self.state = 546
                self.match(MiniGoParser.LPAREN)
                self.state = 547
                self.expression()
                self.state = 548
                self.match(MiniGoParser.RPAREN)
                pass
            elif token in [MiniGoParser.GETSTRING]:
                localctx = MiniGoParser.GetStringCallContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 550
                self.match(MiniGoParser.GETSTRING)
                self.state = 551
                self.match(MiniGoParser.LPAREN)
                self.state = 552
                self.match(MiniGoParser.RPAREN)
                pass
            elif token in [MiniGoParser.PUTSTRING]:
                localctx = MiniGoParser.PutStringCallContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 553
                self.match(MiniGoParser.PUTSTRING)
                self.state = 554
                self.match(MiniGoParser.LPAREN)
                self.state = 555
                self.expression()
                self.state = 556
                self.match(MiniGoParser.RPAREN)
                pass
            elif token in [MiniGoParser.PUTSTRINGLN]:
                localctx = MiniGoParser.PutStringLnCallContext(self, localctx)
                self.enterOuterAlt(localctx, 12)
                self.state = 558
                self.match(MiniGoParser.PUTSTRINGLN)
                self.state = 559
                self.match(MiniGoParser.LPAREN)
                self.state = 560
                self.expression()
                self.state = 561
                self.match(MiniGoParser.RPAREN)
                pass
            elif token in [MiniGoParser.PUTLN]:
                localctx = MiniGoParser.PutLnCallContext(self, localctx)
                self.enterOuterAlt(localctx, 13)
                self.state = 563
                self.match(MiniGoParser.PUTLN)
                self.state = 564
                self.match(MiniGoParser.LPAREN)
                self.state = 565
                self.match(MiniGoParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentifierListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def identifierList(self):
            return self.getTypedRuleContext(MiniGoParser.IdentifierListContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_identifierList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifierList" ):
                return visitor.visitIdentifierList(self)
            else:
                return visitor.visitChildren(self)




    def identifierList(self):

        localctx = MiniGoParser.IdentifierListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_identifierList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 568
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 571
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.COMMA:
                self.state = 569
                self.match(MiniGoParser.COMMA)
                self.state = 570
                self.identifierList()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def expressionList(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionListContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expressionList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionList" ):
                return visitor.visitExpressionList(self)
            else:
                return visitor.visitChildren(self)




    def expressionList(self):

        localctx = MiniGoParser.ExpressionListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_expressionList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 573
            self.expression()
            self.state = 576
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.COMMA:
                self.state = 574
                self.match(MiniGoParser.COMMA)
                self.state = 575
                self.expressionList()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InBlockStatementListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(MiniGoParser.StatementContext,0)


        def inBlockStatement(self):
            return self.getTypedRuleContext(MiniGoParser.InBlockStatementContext,0)


        def inBlockStatementList(self):
            return self.getTypedRuleContext(MiniGoParser.InBlockStatementListContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_inBlockStatementList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInBlockStatementList" ):
                return visitor.visitInBlockStatementList(self)
            else:
                return visitor.visitChildren(self)




    def inBlockStatementList(self):

        localctx = MiniGoParser.InBlockStatementListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_inBlockStatementList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 580
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.IF, MiniGoParser.FOR, MiniGoParser.CONST, MiniGoParser.VAR, MiniGoParser.IDENTIFIER, MiniGoParser.GETINT, MiniGoParser.PUTINT, MiniGoParser.PUTINTLN, MiniGoParser.GETFLOAT, MiniGoParser.PUTFLOAT, MiniGoParser.PUTFLOATLN, MiniGoParser.GETBOOL, MiniGoParser.PUTBOOL, MiniGoParser.PUTBOOLLN, MiniGoParser.GETSTRING, MiniGoParser.PUTSTRING, MiniGoParser.PUTSTRINGLN, MiniGoParser.PUTLN]:
                self.state = 578
                self.statement()
                pass
            elif token in [MiniGoParser.RETURN, MiniGoParser.CONTINUE, MiniGoParser.BREAK]:
                self.state = 579
                self.inBlockStatement()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 583
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.IDENTIFIER) | (1 << MiniGoParser.GETINT) | (1 << MiniGoParser.PUTINT) | (1 << MiniGoParser.PUTINTLN) | (1 << MiniGoParser.GETFLOAT) | (1 << MiniGoParser.PUTFLOAT))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (MiniGoParser.PUTFLOATLN - 64)) | (1 << (MiniGoParser.GETBOOL - 64)) | (1 << (MiniGoParser.PUTBOOL - 64)) | (1 << (MiniGoParser.PUTBOOLLN - 64)) | (1 << (MiniGoParser.GETSTRING - 64)) | (1 << (MiniGoParser.PUTSTRING - 64)) | (1 << (MiniGoParser.PUTSTRINGLN - 64)) | (1 << (MiniGoParser.PUTLN - 64)))) != 0):
                self.state = 582
                self.inBlockStatementList()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration(self):
            return self.getTypedRuleContext(MiniGoParser.DeclarationContext,0)


        def declarationList(self):
            return self.getTypedRuleContext(MiniGoParser.DeclarationListContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_declarationList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclarationList" ):
                return visitor.visitDeclarationList(self)
            else:
                return visitor.visitChildren(self)




    def declarationList(self):

        localctx = MiniGoParser.DeclarationListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 132, self.RULE_declarationList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 585
            self.declaration()
            self.state = 587
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.FUNC) | (1 << MiniGoParser.TYPE) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR))) != 0):
                self.state = 586
                self.declarationList()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[30] = self.logicalExpr_sempred
        self._predicates[31] = self.higherLogicalExpr_sempred
        self._predicates[32] = self.relationalExpr_sempred
        self._predicates[33] = self.additiveExpr_sempred
        self._predicates[34] = self.multiplicativeExpr_sempred
        self._predicates[36] = self.primaryExpr_sempred
        self._predicates[60] = self.lhs_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def logicalExpr_sempred(self, localctx:LogicalExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def higherLogicalExpr_sempred(self, localctx:HigherLogicalExprContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def relationalExpr_sempred(self, localctx:RelationalExprContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def additiveExpr_sempred(self, localctx:AdditiveExprContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def multiplicativeExpr_sempred(self, localctx:MultiplicativeExprContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def primaryExpr_sempred(self, localctx:PrimaryExprContext, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 2)
         

    def lhs_sempred(self, localctx:LhsContext, predIndex:int):
            if predIndex == 8:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 1)
         




