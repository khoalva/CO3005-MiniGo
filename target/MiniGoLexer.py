# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2L")
        buf.write("\u027c\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\3\2")
        buf.write("\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3")
        buf.write("\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3")
        buf.write("\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\27\3\27\3\30")
        buf.write("\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3\34")
        buf.write("\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3 \3 \3 \3!\3!\3!")
        buf.write("\3\"\3\"\3\"\3#\3#\3$\3$\3$\3%\3%\3%\3&\3&\3&\3\'\3\'")
        buf.write("\3\'\3(\3(\3(\3)\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3")
        buf.write("/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64")
        buf.write("\3\65\3\65\3\65\3\65\5\65\u016d\n\65\3\66\3\66\3\66\7")
        buf.write("\66\u0172\n\66\f\66\16\66\u0175\13\66\5\66\u0177\n\66")
        buf.write("\3\67\3\67\3\67\6\67\u017c\n\67\r\67\16\67\u017d\38\3")
        buf.write("8\38\68\u0183\n8\r8\168\u0184\39\39\39\69\u018a\n9\r9")
        buf.write("\169\u018b\3:\6:\u018f\n:\r:\16:\u0190\3:\3:\7:\u0195")
        buf.write("\n:\f:\16:\u0198\13:\3:\5:\u019b\n:\5:\u019d\n:\3;\3;")
        buf.write("\5;\u01a1\n;\3;\6;\u01a4\n;\r;\16;\u01a5\3<\3<\3<\7<\u01ab")
        buf.write("\n<\f<\16<\u01ae\13<\3<\3<\3=\3=\3=\3>\3>\5>\u01b7\n>")
        buf.write("\3?\3?\3@\3@\7@\u01bd\n@\f@\16@\u01c0\13@\3A\5A\u01c3")
        buf.write("\nA\3A\3A\3A\3B\6B\u01c9\nB\rB\16B\u01ca\3B\3B\3C\3C\3")
        buf.write("C\3C\7C\u01d3\nC\fC\16C\u01d6\13C\3C\3C\3D\3D\3D\3D\3")
        buf.write("D\7D\u01df\nD\fD\16D\u01e2\13D\3D\3D\3D\3D\3D\3E\3E\3")
        buf.write("E\3E\3E\3E\3E\3F\3F\3F\3F\3F\3F\3F\3G\3G\3G\3G\3G\3G\3")
        buf.write("G\3G\3G\3H\3H\3H\3H\3H\3H\3H\3H\3H\3I\3I\3I\3I\3I\3I\3")
        buf.write("I\3I\3I\3J\3J\3J\3J\3J\3J\3J\3J\3J\3J\3J\3K\3K\3K\3K\3")
        buf.write("K\3K\3K\3K\3L\3L\3L\3L\3L\3L\3L\3L\3M\3M\3M\3M\3M\3M\3")
        buf.write("M\3M\3M\3M\3N\3N\3N\3N\3N\3N\3N\3N\3N\3N\3O\3O\3O\3O\3")
        buf.write("O\3O\3O\3O\3O\3O\3P\3P\3P\3P\3P\3P\3P\3P\3P\3P\3P\3P\3")
        buf.write("Q\3Q\3Q\3Q\3Q\3Q\3R\3R\3R\7R\u0260\nR\fR\16R\u0263\13")
        buf.write("R\3R\3R\5R\u0267\nR\3R\5R\u026a\nR\3R\3R\3S\3S\3S\7S\u0271")
        buf.write("\nS\fS\16S\u0274\13S\3S\3S\3S\3S\3T\3T\3T\3\u01e0\2U\3")
        buf.write("\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16")
        buf.write("\33\17\35\20\37\21!\22#\23%\2\'\2)\2+\24-\25/\26\61\27")
        buf.write("\63\30\65\31\67\329\33;\34=\35?\36A\37C E!G\"I#K$M%O&")
        buf.write("Q\'S(U)W*Y+[,]-_.a/c\60e\61g\62i\63k\2m\2o\2q\2s\64u\2")
        buf.write("w\65y\2{\66}\67\1778\u00819\u0083:\u0085;\u0087<\u0089")
        buf.write("=\u008b>\u008d?\u008f@\u0091A\u0093B\u0095C\u0097D\u0099")
        buf.write("E\u009bF\u009dG\u009fH\u00a1I\u00a3J\u00a5K\u00a7L\3\2")
        buf.write("\23\3\2\63;\3\2\62;\4\2DDdd\3\2\62\63\4\2QQqq\3\2\629")
        buf.write("\4\2ZZzz\5\2\62;CHch\4\2GGgg\4\2--//\5\2\f\f$$^^\7\2$")
        buf.write("$^^ppttvv\5\2C\\aac|\6\2\62;C\\aac|\5\2\13\13\16\17\"")
        buf.write("\"\4\2\f\f\17\17\6\2\f\f\17\17$$^^\2\u028f\2\3\3\2\2\2")
        buf.write("\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r")
        buf.write("\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3")
        buf.write("\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2")
        buf.write("\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2+\3\2\2\2\2-")
        buf.write("\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2")
        buf.write("\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?")
        buf.write("\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2")
        buf.write("I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2")
        buf.write("\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2")
        buf.write("\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2")
        buf.write("\2\2\2g\3\2\2\2\2i\3\2\2\2\2s\3\2\2\2\2w\3\2\2\2\2{\3")
        buf.write("\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083")
        buf.write("\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2")
        buf.write("\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091")
        buf.write("\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2")
        buf.write("\2\2\u0099\3\2\2\2\2\u009b\3\2\2\2\2\u009d\3\2\2\2\2\u009f")
        buf.write("\3\2\2\2\2\u00a1\3\2\2\2\2\u00a3\3\2\2\2\2\u00a5\3\2\2")
        buf.write("\2\2\u00a7\3\2\2\2\3\u00a9\3\2\2\2\5\u00ac\3\2\2\2\7\u00b1")
        buf.write("\3\2\2\2\t\u00b5\3\2\2\2\13\u00bc\3\2\2\2\r\u00c1\3\2")
        buf.write("\2\2\17\u00c6\3\2\2\2\21\u00cd\3\2\2\2\23\u00d7\3\2\2")
        buf.write("\2\25\u00de\3\2\2\2\27\u00e2\3\2\2\2\31\u00e8\3\2\2\2")
        buf.write("\33\u00f0\3\2\2\2\35\u00f6\3\2\2\2\37\u00fa\3\2\2\2!\u0103")
        buf.write("\3\2\2\2#\u0109\3\2\2\2%\u010f\3\2\2\2\'\u0113\3\2\2\2")
        buf.write(")\u0118\3\2\2\2+\u011e\3\2\2\2-\u0120\3\2\2\2/\u0122\3")
        buf.write("\2\2\2\61\u0124\3\2\2\2\63\u0126\3\2\2\2\65\u0128\3\2")
        buf.write("\2\2\67\u012b\3\2\2\29\u012e\3\2\2\2;\u0130\3\2\2\2=\u0133")
        buf.write("\3\2\2\2?\u0135\3\2\2\2A\u0138\3\2\2\2C\u013b\3\2\2\2")
        buf.write("E\u013e\3\2\2\2G\u0140\3\2\2\2I\u0143\3\2\2\2K\u0146\3")
        buf.write("\2\2\2M\u0149\3\2\2\2O\u014c\3\2\2\2Q\u014f\3\2\2\2S\u0152")
        buf.write("\3\2\2\2U\u0154\3\2\2\2W\u0156\3\2\2\2Y\u0158\3\2\2\2")
        buf.write("[\u015a\3\2\2\2]\u015c\3\2\2\2_\u015e\3\2\2\2a\u0160\3")
        buf.write("\2\2\2c\u0162\3\2\2\2e\u0164\3\2\2\2g\u0166\3\2\2\2i\u016c")
        buf.write("\3\2\2\2k\u0176\3\2\2\2m\u0178\3\2\2\2o\u017f\3\2\2\2")
        buf.write("q\u0186\3\2\2\2s\u018e\3\2\2\2u\u019e\3\2\2\2w\u01a7\3")
        buf.write("\2\2\2y\u01b1\3\2\2\2{\u01b6\3\2\2\2}\u01b8\3\2\2\2\177")
        buf.write("\u01ba\3\2\2\2\u0081\u01c2\3\2\2\2\u0083\u01c8\3\2\2\2")
        buf.write("\u0085\u01ce\3\2\2\2\u0087\u01d9\3\2\2\2\u0089\u01e8\3")
        buf.write("\2\2\2\u008b\u01ef\3\2\2\2\u008d\u01f6\3\2\2\2\u008f\u01ff")
        buf.write("\3\2\2\2\u0091\u0208\3\2\2\2\u0093\u0211\3\2\2\2\u0095")
        buf.write("\u021c\3\2\2\2\u0097\u0224\3\2\2\2\u0099\u022c\3\2\2\2")
        buf.write("\u009b\u0236\3\2\2\2\u009d\u0240\3\2\2\2\u009f\u024a\3")
        buf.write("\2\2\2\u00a1\u0256\3\2\2\2\u00a3\u025c\3\2\2\2\u00a5\u026d")
        buf.write("\3\2\2\2\u00a7\u0279\3\2\2\2\u00a9\u00aa\7k\2\2\u00aa")
        buf.write("\u00ab\7h\2\2\u00ab\4\3\2\2\2\u00ac\u00ad\7g\2\2\u00ad")
        buf.write("\u00ae\7n\2\2\u00ae\u00af\7u\2\2\u00af\u00b0\7g\2\2\u00b0")
        buf.write("\6\3\2\2\2\u00b1\u00b2\7h\2\2\u00b2\u00b3\7q\2\2\u00b3")
        buf.write("\u00b4\7t\2\2\u00b4\b\3\2\2\2\u00b5\u00b6\7t\2\2\u00b6")
        buf.write("\u00b7\7g\2\2\u00b7\u00b8\7v\2\2\u00b8\u00b9\7w\2\2\u00b9")
        buf.write("\u00ba\7t\2\2\u00ba\u00bb\7p\2\2\u00bb\n\3\2\2\2\u00bc")
        buf.write("\u00bd\7h\2\2\u00bd\u00be\7w\2\2\u00be\u00bf\7p\2\2\u00bf")
        buf.write("\u00c0\7e\2\2\u00c0\f\3\2\2\2\u00c1\u00c2\7v\2\2\u00c2")
        buf.write("\u00c3\7{\2\2\u00c3\u00c4\7r\2\2\u00c4\u00c5\7g\2\2\u00c5")
        buf.write("\16\3\2\2\2\u00c6\u00c7\7u\2\2\u00c7\u00c8\7v\2\2\u00c8")
        buf.write("\u00c9\7t\2\2\u00c9\u00ca\7w\2\2\u00ca\u00cb\7e\2\2\u00cb")
        buf.write("\u00cc\7v\2\2\u00cc\20\3\2\2\2\u00cd\u00ce\7k\2\2\u00ce")
        buf.write("\u00cf\7p\2\2\u00cf\u00d0\7v\2\2\u00d0\u00d1\7g\2\2\u00d1")
        buf.write("\u00d2\7t\2\2\u00d2\u00d3\7h\2\2\u00d3\u00d4\7c\2\2\u00d4")
        buf.write("\u00d5\7e\2\2\u00d5\u00d6\7g\2\2\u00d6\22\3\2\2\2\u00d7")
        buf.write("\u00d8\7u\2\2\u00d8\u00d9\7v\2\2\u00d9\u00da\7t\2\2\u00da")
        buf.write("\u00db\7k\2\2\u00db\u00dc\7p\2\2\u00dc\u00dd\7i\2\2\u00dd")
        buf.write("\24\3\2\2\2\u00de\u00df\7k\2\2\u00df\u00e0\7p\2\2\u00e0")
        buf.write("\u00e1\7v\2\2\u00e1\26\3\2\2\2\u00e2\u00e3\7h\2\2\u00e3")
        buf.write("\u00e4\7n\2\2\u00e4\u00e5\7q\2\2\u00e5\u00e6\7c\2\2\u00e6")
        buf.write("\u00e7\7v\2\2\u00e7\30\3\2\2\2\u00e8\u00e9\7d\2\2\u00e9")
        buf.write("\u00ea\7q\2\2\u00ea\u00eb\7q\2\2\u00eb\u00ec\7n\2\2\u00ec")
        buf.write("\u00ed\7g\2\2\u00ed\u00ee\7c\2\2\u00ee\u00ef\7p\2\2\u00ef")
        buf.write("\32\3\2\2\2\u00f0\u00f1\7e\2\2\u00f1\u00f2\7q\2\2\u00f2")
        buf.write("\u00f3\7p\2\2\u00f3\u00f4\7u\2\2\u00f4\u00f5\7v\2\2\u00f5")
        buf.write("\34\3\2\2\2\u00f6\u00f7\7x\2\2\u00f7\u00f8\7c\2\2\u00f8")
        buf.write("\u00f9\7t\2\2\u00f9\36\3\2\2\2\u00fa\u00fb\7e\2\2\u00fb")
        buf.write("\u00fc\7q\2\2\u00fc\u00fd\7p\2\2\u00fd\u00fe\7v\2\2\u00fe")
        buf.write("\u00ff\7k\2\2\u00ff\u0100\7p\2\2\u0100\u0101\7w\2\2\u0101")
        buf.write("\u0102\7g\2\2\u0102 \3\2\2\2\u0103\u0104\7d\2\2\u0104")
        buf.write("\u0105\7t\2\2\u0105\u0106\7g\2\2\u0106\u0107\7c\2\2\u0107")
        buf.write("\u0108\7m\2\2\u0108\"\3\2\2\2\u0109\u010a\7t\2\2\u010a")
        buf.write("\u010b\7c\2\2\u010b\u010c\7p\2\2\u010c\u010d\7i\2\2\u010d")
        buf.write("\u010e\7g\2\2\u010e$\3\2\2\2\u010f\u0110\7p\2\2\u0110")
        buf.write("\u0111\7k\2\2\u0111\u0112\7n\2\2\u0112&\3\2\2\2\u0113")
        buf.write("\u0114\7v\2\2\u0114\u0115\7t\2\2\u0115\u0116\7w\2\2\u0116")
        buf.write("\u0117\7g\2\2\u0117(\3\2\2\2\u0118\u0119\7h\2\2\u0119")
        buf.write("\u011a\7c\2\2\u011a\u011b\7n\2\2\u011b\u011c\7u\2\2\u011c")
        buf.write("\u011d\7g\2\2\u011d*\3\2\2\2\u011e\u011f\7-\2\2\u011f")
        buf.write(",\3\2\2\2\u0120\u0121\7/\2\2\u0121.\3\2\2\2\u0122\u0123")
        buf.write("\7,\2\2\u0123\60\3\2\2\2\u0124\u0125\7\61\2\2\u0125\62")
        buf.write("\3\2\2\2\u0126\u0127\7\'\2\2\u0127\64\3\2\2\2\u0128\u0129")
        buf.write("\7?\2\2\u0129\u012a\7?\2\2\u012a\66\3\2\2\2\u012b\u012c")
        buf.write("\7#\2\2\u012c\u012d\7?\2\2\u012d8\3\2\2\2\u012e\u012f")
        buf.write("\7>\2\2\u012f:\3\2\2\2\u0130\u0131\7>\2\2\u0131\u0132")
        buf.write("\7?\2\2\u0132<\3\2\2\2\u0133\u0134\7@\2\2\u0134>\3\2\2")
        buf.write("\2\u0135\u0136\7@\2\2\u0136\u0137\7?\2\2\u0137@\3\2\2")
        buf.write("\2\u0138\u0139\7(\2\2\u0139\u013a\7(\2\2\u013aB\3\2\2")
        buf.write("\2\u013b\u013c\7~\2\2\u013c\u013d\7~\2\2\u013dD\3\2\2")
        buf.write("\2\u013e\u013f\7#\2\2\u013fF\3\2\2\2\u0140\u0141\7<\2")
        buf.write("\2\u0141\u0142\7?\2\2\u0142H\3\2\2\2\u0143\u0144\7-\2")
        buf.write("\2\u0144\u0145\7?\2\2\u0145J\3\2\2\2\u0146\u0147\7/\2")
        buf.write("\2\u0147\u0148\7?\2\2\u0148L\3\2\2\2\u0149\u014a\7,\2")
        buf.write("\2\u014a\u014b\7?\2\2\u014bN\3\2\2\2\u014c\u014d\7\61")
        buf.write("\2\2\u014d\u014e\7?\2\2\u014eP\3\2\2\2\u014f\u0150\7\'")
        buf.write("\2\2\u0150\u0151\7?\2\2\u0151R\3\2\2\2\u0152\u0153\7\60")
        buf.write("\2\2\u0153T\3\2\2\2\u0154\u0155\7?\2\2\u0155V\3\2\2\2")
        buf.write("\u0156\u0157\7*\2\2\u0157X\3\2\2\2\u0158\u0159\7+\2\2")
        buf.write("\u0159Z\3\2\2\2\u015a\u015b\7}\2\2\u015b\\\3\2\2\2\u015c")
        buf.write("\u015d\7\177\2\2\u015d^\3\2\2\2\u015e\u015f\7]\2\2\u015f")
        buf.write("`\3\2\2\2\u0160\u0161\7_\2\2\u0161b\3\2\2\2\u0162\u0163")
        buf.write("\7.\2\2\u0163d\3\2\2\2\u0164\u0165\7=\2\2\u0165f\3\2\2")
        buf.write("\2\u0166\u0167\7<\2\2\u0167h\3\2\2\2\u0168\u016d\5k\66")
        buf.write("\2\u0169\u016d\5m\67\2\u016a\u016d\5o8\2\u016b\u016d\5")
        buf.write("q9\2\u016c\u0168\3\2\2\2\u016c\u0169\3\2\2\2\u016c\u016a")
        buf.write("\3\2\2\2\u016c\u016b\3\2\2\2\u016dj\3\2\2\2\u016e\u0177")
        buf.write("\7\62\2\2\u016f\u0173\t\2\2\2\u0170\u0172\t\3\2\2\u0171")
        buf.write("\u0170\3\2\2\2\u0172\u0175\3\2\2\2\u0173\u0171\3\2\2\2")
        buf.write("\u0173\u0174\3\2\2\2\u0174\u0177\3\2\2\2\u0175\u0173\3")
        buf.write("\2\2\2\u0176\u016e\3\2\2\2\u0176\u016f\3\2\2\2\u0177l")
        buf.write("\3\2\2\2\u0178\u0179\7\62\2\2\u0179\u017b\t\4\2\2\u017a")
        buf.write("\u017c\t\5\2\2\u017b\u017a\3\2\2\2\u017c\u017d\3\2\2\2")
        buf.write("\u017d\u017b\3\2\2\2\u017d\u017e\3\2\2\2\u017en\3\2\2")
        buf.write("\2\u017f\u0180\7\62\2\2\u0180\u0182\t\6\2\2\u0181\u0183")
        buf.write("\t\7\2\2\u0182\u0181\3\2\2\2\u0183\u0184\3\2\2\2\u0184")
        buf.write("\u0182\3\2\2\2\u0184\u0185\3\2\2\2\u0185p\3\2\2\2\u0186")
        buf.write("\u0187\7\62\2\2\u0187\u0189\t\b\2\2\u0188\u018a\t\t\2")
        buf.write("\2\u0189\u0188\3\2\2\2\u018a\u018b\3\2\2\2\u018b\u0189")
        buf.write("\3\2\2\2\u018b\u018c\3\2\2\2\u018cr\3\2\2\2\u018d\u018f")
        buf.write("\t\3\2\2\u018e\u018d\3\2\2\2\u018f\u0190\3\2\2\2\u0190")
        buf.write("\u018e\3\2\2\2\u0190\u0191\3\2\2\2\u0191\u0192\3\2\2\2")
        buf.write("\u0192\u019c\7\60\2\2\u0193\u0195\t\3\2\2\u0194\u0193")
        buf.write("\3\2\2\2\u0195\u0198\3\2\2\2\u0196\u0194\3\2\2\2\u0196")
        buf.write("\u0197\3\2\2\2\u0197\u019a\3\2\2\2\u0198\u0196\3\2\2\2")
        buf.write("\u0199\u019b\5u;\2\u019a\u0199\3\2\2\2\u019a\u019b\3\2")
        buf.write("\2\2\u019b\u019d\3\2\2\2\u019c\u0196\3\2\2\2\u019c\u019d")
        buf.write("\3\2\2\2\u019dt\3\2\2\2\u019e\u01a0\t\n\2\2\u019f\u01a1")
        buf.write("\t\13\2\2\u01a0\u019f\3\2\2\2\u01a0\u01a1\3\2\2\2\u01a1")
        buf.write("\u01a3\3\2\2\2\u01a2\u01a4\t\3\2\2\u01a3\u01a2\3\2\2\2")
        buf.write("\u01a4\u01a5\3\2\2\2\u01a5\u01a3\3\2\2\2\u01a5\u01a6\3")
        buf.write("\2\2\2\u01a6v\3\2\2\2\u01a7\u01ac\7$\2\2\u01a8\u01ab\n")
        buf.write("\f\2\2\u01a9\u01ab\5y=\2\u01aa\u01a8\3\2\2\2\u01aa\u01a9")
        buf.write("\3\2\2\2\u01ab\u01ae\3\2\2\2\u01ac\u01aa\3\2\2\2\u01ac")
        buf.write("\u01ad\3\2\2\2\u01ad\u01af\3\2\2\2\u01ae\u01ac\3\2\2\2")
        buf.write("\u01af\u01b0\7$\2\2\u01b0x\3\2\2\2\u01b1\u01b2\7^\2\2")
        buf.write("\u01b2\u01b3\t\r\2\2\u01b3z\3\2\2\2\u01b4\u01b7\5\'\24")
        buf.write("\2\u01b5\u01b7\5)\25\2\u01b6\u01b4\3\2\2\2\u01b6\u01b5")
        buf.write("\3\2\2\2\u01b7|\3\2\2\2\u01b8\u01b9\5%\23\2\u01b9~\3\2")
        buf.write("\2\2\u01ba\u01be\t\16\2\2\u01bb\u01bd\t\17\2\2\u01bc\u01bb")
        buf.write("\3\2\2\2\u01bd\u01c0\3\2\2\2\u01be\u01bc\3\2\2\2\u01be")
        buf.write("\u01bf\3\2\2\2\u01bf\u0080\3\2\2\2\u01c0\u01be\3\2\2\2")
        buf.write("\u01c1\u01c3\7\17\2\2\u01c2\u01c1\3\2\2\2\u01c2\u01c3")
        buf.write("\3\2\2\2\u01c3\u01c4\3\2\2\2\u01c4\u01c5\7\f\2\2\u01c5")
        buf.write("\u01c6\bA\2\2\u01c6\u0082\3\2\2\2\u01c7\u01c9\t\20\2\2")
        buf.write("\u01c8\u01c7\3\2\2\2\u01c9\u01ca\3\2\2\2\u01ca\u01c8\3")
        buf.write("\2\2\2\u01ca\u01cb\3\2\2\2\u01cb\u01cc\3\2\2\2\u01cc\u01cd")
        buf.write("\bB\3\2\u01cd\u0084\3\2\2\2\u01ce\u01cf\7\61\2\2\u01cf")
        buf.write("\u01d0\7\61\2\2\u01d0\u01d4\3\2\2\2\u01d1\u01d3\n\21\2")
        buf.write("\2\u01d2\u01d1\3\2\2\2\u01d3\u01d6\3\2\2\2\u01d4\u01d2")
        buf.write("\3\2\2\2\u01d4\u01d5\3\2\2\2\u01d5\u01d7\3\2\2\2\u01d6")
        buf.write("\u01d4\3\2\2\2\u01d7\u01d8\bC\3\2\u01d8\u0086\3\2\2\2")
        buf.write("\u01d9\u01da\7\61\2\2\u01da\u01db\7,\2\2\u01db\u01e0\3")
        buf.write("\2\2\2\u01dc\u01df\5\u0087D\2\u01dd\u01df\13\2\2\2\u01de")
        buf.write("\u01dc\3\2\2\2\u01de\u01dd\3\2\2\2\u01df\u01e2\3\2\2\2")
        buf.write("\u01e0\u01e1\3\2\2\2\u01e0\u01de\3\2\2\2\u01e1\u01e3\3")
        buf.write("\2\2\2\u01e2\u01e0\3\2\2\2\u01e3\u01e4\7,\2\2\u01e4\u01e5")
        buf.write("\7\61\2\2\u01e5\u01e6\3\2\2\2\u01e6\u01e7\bD\3\2\u01e7")
        buf.write("\u0088\3\2\2\2\u01e8\u01e9\7i\2\2\u01e9\u01ea\7g\2\2\u01ea")
        buf.write("\u01eb\7v\2\2\u01eb\u01ec\7K\2\2\u01ec\u01ed\7p\2\2\u01ed")
        buf.write("\u01ee\7v\2\2\u01ee\u008a\3\2\2\2\u01ef\u01f0\7r\2\2\u01f0")
        buf.write("\u01f1\7w\2\2\u01f1\u01f2\7v\2\2\u01f2\u01f3\7K\2\2\u01f3")
        buf.write("\u01f4\7p\2\2\u01f4\u01f5\7v\2\2\u01f5\u008c\3\2\2\2\u01f6")
        buf.write("\u01f7\7r\2\2\u01f7\u01f8\7w\2\2\u01f8\u01f9\7v\2\2\u01f9")
        buf.write("\u01fa\7K\2\2\u01fa\u01fb\7p\2\2\u01fb\u01fc\7v\2\2\u01fc")
        buf.write("\u01fd\7N\2\2\u01fd\u01fe\7p\2\2\u01fe\u008e\3\2\2\2\u01ff")
        buf.write("\u0200\7i\2\2\u0200\u0201\7g\2\2\u0201\u0202\7v\2\2\u0202")
        buf.write("\u0203\7H\2\2\u0203\u0204\7n\2\2\u0204\u0205\7q\2\2\u0205")
        buf.write("\u0206\7c\2\2\u0206\u0207\7v\2\2\u0207\u0090\3\2\2\2\u0208")
        buf.write("\u0209\7r\2\2\u0209\u020a\7w\2\2\u020a\u020b\7v\2\2\u020b")
        buf.write("\u020c\7H\2\2\u020c\u020d\7n\2\2\u020d\u020e\7q\2\2\u020e")
        buf.write("\u020f\7c\2\2\u020f\u0210\7v\2\2\u0210\u0092\3\2\2\2\u0211")
        buf.write("\u0212\7r\2\2\u0212\u0213\7w\2\2\u0213\u0214\7v\2\2\u0214")
        buf.write("\u0215\7H\2\2\u0215\u0216\7n\2\2\u0216\u0217\7q\2\2\u0217")
        buf.write("\u0218\7c\2\2\u0218\u0219\7v\2\2\u0219\u021a\7N\2\2\u021a")
        buf.write("\u021b\7p\2\2\u021b\u0094\3\2\2\2\u021c\u021d\7i\2\2\u021d")
        buf.write("\u021e\7g\2\2\u021e\u021f\7v\2\2\u021f\u0220\7D\2\2\u0220")
        buf.write("\u0221\7q\2\2\u0221\u0222\7q\2\2\u0222\u0223\7n\2\2\u0223")
        buf.write("\u0096\3\2\2\2\u0224\u0225\7r\2\2\u0225\u0226\7w\2\2\u0226")
        buf.write("\u0227\7v\2\2\u0227\u0228\7D\2\2\u0228\u0229\7q\2\2\u0229")
        buf.write("\u022a\7q\2\2\u022a\u022b\7n\2\2\u022b\u0098\3\2\2\2\u022c")
        buf.write("\u022d\7r\2\2\u022d\u022e\7w\2\2\u022e\u022f\7v\2\2\u022f")
        buf.write("\u0230\7D\2\2\u0230\u0231\7q\2\2\u0231\u0232\7q\2\2\u0232")
        buf.write("\u0233\7n\2\2\u0233\u0234\7N\2\2\u0234\u0235\7p\2\2\u0235")
        buf.write("\u009a\3\2\2\2\u0236\u0237\7i\2\2\u0237\u0238\7g\2\2\u0238")
        buf.write("\u0239\7v\2\2\u0239\u023a\7U\2\2\u023a\u023b\7v\2\2\u023b")
        buf.write("\u023c\7t\2\2\u023c\u023d\7k\2\2\u023d\u023e\7p\2\2\u023e")
        buf.write("\u023f\7i\2\2\u023f\u009c\3\2\2\2\u0240\u0241\7r\2\2\u0241")
        buf.write("\u0242\7w\2\2\u0242\u0243\7v\2\2\u0243\u0244\7U\2\2\u0244")
        buf.write("\u0245\7v\2\2\u0245\u0246\7t\2\2\u0246\u0247\7k\2\2\u0247")
        buf.write("\u0248\7p\2\2\u0248\u0249\7i\2\2\u0249\u009e\3\2\2\2\u024a")
        buf.write("\u024b\7r\2\2\u024b\u024c\7w\2\2\u024c\u024d\7v\2\2\u024d")
        buf.write("\u024e\7U\2\2\u024e\u024f\7v\2\2\u024f\u0250\7t\2\2\u0250")
        buf.write("\u0251\7k\2\2\u0251\u0252\7p\2\2\u0252\u0253\7i\2\2\u0253")
        buf.write("\u0254\7N\2\2\u0254\u0255\7p\2\2\u0255\u00a0\3\2\2\2\u0256")
        buf.write("\u0257\7r\2\2\u0257\u0258\7w\2\2\u0258\u0259\7v\2\2\u0259")
        buf.write("\u025a\7N\2\2\u025a\u025b\7p\2\2\u025b\u00a2\3\2\2\2\u025c")
        buf.write("\u0261\7$\2\2\u025d\u0260\n\f\2\2\u025e\u0260\5y=\2\u025f")
        buf.write("\u025d\3\2\2\2\u025f\u025e\3\2\2\2\u0260\u0263\3\2\2\2")
        buf.write("\u0261\u025f\3\2\2\2\u0261\u0262\3\2\2\2\u0262\u0269\3")
        buf.write("\2\2\2\u0263\u0261\3\2\2\2\u0264\u026a\7\2\2\3\u0265\u0267")
        buf.write("\7\17\2\2\u0266\u0265\3\2\2\2\u0266\u0267\3\2\2\2\u0267")
        buf.write("\u0268\3\2\2\2\u0268\u026a\7\f\2\2\u0269\u0264\3\2\2\2")
        buf.write("\u0269\u0266\3\2\2\2\u026a\u026b\3\2\2\2\u026b\u026c\b")
        buf.write("R\4\2\u026c\u00a4\3\2\2\2\u026d\u0272\7$\2\2\u026e\u0271")
        buf.write("\5y=\2\u026f\u0271\n\22\2\2\u0270\u026e\3\2\2\2\u0270")
        buf.write("\u026f\3\2\2\2\u0271\u0274\3\2\2\2\u0272\u0270\3\2\2\2")
        buf.write("\u0272\u0273\3\2\2\2\u0273\u0275\3\2\2\2\u0274\u0272\3")
        buf.write("\2\2\2\u0275\u0276\7^\2\2\u0276\u0277\n\r\2\2\u0277\u0278")
        buf.write("\bS\5\2\u0278\u00a6\3\2\2\2\u0279\u027a\13\2\2\2\u027a")
        buf.write("\u027b\bT\6\2\u027b\u00a8\3\2\2\2\36\2\u016c\u0173\u0176")
        buf.write("\u017d\u0184\u018b\u0190\u0196\u019a\u019c\u01a0\u01a5")
        buf.write("\u01aa\u01ac\u01b6\u01be\u01c2\u01ca\u01d4\u01de\u01e0")
        buf.write("\u025f\u0261\u0266\u0269\u0270\u0272\7\3A\2\b\2\2\3R\3")
        buf.write("\3S\4\3T\5")
        return buf.getvalue()


class MiniGoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    IF = 1
    ELSE = 2
    FOR = 3
    RETURN = 4
    FUNC = 5
    TYPE = 6
    STRUCT = 7
    INTERFACE = 8
    STRING = 9
    INT = 10
    FLOAT = 11
    BOOLEAN = 12
    CONST = 13
    VAR = 14
    CONTINUE = 15
    BREAK = 16
    RANGE = 17
    ADD = 18
    SUBTRACT = 19
    MULTIPLY = 20
    DIVIDE = 21
    MODULO = 22
    EQUAL = 23
    NOT_EQUAL = 24
    LESS_THAN = 25
    LESS_THAN_OR_EQUAL = 26
    GREATER_THAN = 27
    GREATER_THAN_OR_EQUAL = 28
    AND = 29
    OR = 30
    NOT = 31
    SHORT_ASSIGN = 32
    ADD_ASSIGN = 33
    SUBTRACT_ASSIGN = 34
    MULTIPLY_ASSIGN = 35
    DIVIDE_ASSIGN = 36
    MODULO_ASSIGN = 37
    DOT = 38
    ASSIGN = 39
    LPAREN = 40
    RPAREN = 41
    LBRACE = 42
    RBRACE = 43
    LBRACKET = 44
    RBRACKET = 45
    COMMA = 46
    SEMICOLON = 47
    COLON = 48
    INT_LIT = 49
    FLOAT_LIT = 50
    STRING_LIT = 51
    BOOL_LIT = 52
    NIL_LIT = 53
    IDENTIFIER = 54
    NEWLINE = 55
    WS = 56
    SINGLE_LINE_COMMENT = 57
    MULTI_LINE_COMMENT = 58
    GETINT = 59
    PUTINT = 60
    PUTINTLN = 61
    GETFLOAT = 62
    PUTFLOAT = 63
    PUTFLOATLN = 64
    GETBOOL = 65
    PUTBOOL = 66
    PUTBOOLLN = 67
    GETSTRING = 68
    PUTSTRING = 69
    PUTSTRINGLN = 70
    PUTLN = 71
    UNCLOSE_STRING = 72
    ILLEGAL_ESCAPE = 73
    ERROR_CHAR = 74

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'if'", "'else'", "'for'", "'return'", "'func'", "'type'", "'struct'", 
            "'interface'", "'string'", "'int'", "'float'", "'boolean'", 
            "'const'", "'var'", "'continue'", "'break'", "'range'", "'+'", 
            "'-'", "'*'", "'/'", "'%'", "'=='", "'!='", "'<'", "'<='", "'>'", 
            "'>='", "'&&'", "'||'", "'!'", "':='", "'+='", "'-='", "'*='", 
            "'/='", "'%='", "'.'", "'='", "'('", "')'", "'{'", "'}'", "'['", 
            "']'", "','", "';'", "':'", "'getInt'", "'putInt'", "'putIntLn'", 
            "'getFloat'", "'putFloat'", "'putFloatLn'", "'getBool'", "'putBool'", 
            "'putBoolLn'", "'getString'", "'putString'", "'putStringLn'", 
            "'putLn'" ]

    symbolicNames = [ "<INVALID>",
            "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", "INTERFACE", 
            "STRING", "INT", "FLOAT", "BOOLEAN", "CONST", "VAR", "CONTINUE", 
            "BREAK", "RANGE", "ADD", "SUBTRACT", "MULTIPLY", "DIVIDE", "MODULO", 
            "EQUAL", "NOT_EQUAL", "LESS_THAN", "LESS_THAN_OR_EQUAL", "GREATER_THAN", 
            "GREATER_THAN_OR_EQUAL", "AND", "OR", "NOT", "SHORT_ASSIGN", 
            "ADD_ASSIGN", "SUBTRACT_ASSIGN", "MULTIPLY_ASSIGN", "DIVIDE_ASSIGN", 
            "MODULO_ASSIGN", "DOT", "ASSIGN", "LPAREN", "RPAREN", "LBRACE", 
            "RBRACE", "LBRACKET", "RBRACKET", "COMMA", "SEMICOLON", "COLON", 
            "INT_LIT", "FLOAT_LIT", "STRING_LIT", "BOOL_LIT", "NIL_LIT", 
            "IDENTIFIER", "NEWLINE", "WS", "SINGLE_LINE_COMMENT", "MULTI_LINE_COMMENT", 
            "GETINT", "PUTINT", "PUTINTLN", "GETFLOAT", "PUTFLOAT", "PUTFLOATLN", 
            "GETBOOL", "PUTBOOL", "PUTBOOLLN", "GETSTRING", "PUTSTRING", 
            "PUTSTRINGLN", "PUTLN", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
            "ERROR_CHAR" ]

    ruleNames = [ "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", 
                  "INTERFACE", "STRING", "INT", "FLOAT", "BOOLEAN", "CONST", 
                  "VAR", "CONTINUE", "BREAK", "RANGE", "NIL", "TRUE", "FALSE", 
                  "ADD", "SUBTRACT", "MULTIPLY", "DIVIDE", "MODULO", "EQUAL", 
                  "NOT_EQUAL", "LESS_THAN", "LESS_THAN_OR_EQUAL", "GREATER_THAN", 
                  "GREATER_THAN_OR_EQUAL", "AND", "OR", "NOT", "SHORT_ASSIGN", 
                  "ADD_ASSIGN", "SUBTRACT_ASSIGN", "MULTIPLY_ASSIGN", "DIVIDE_ASSIGN", 
                  "MODULO_ASSIGN", "DOT", "ASSIGN", "LPAREN", "RPAREN", 
                  "LBRACE", "RBRACE", "LBRACKET", "RBRACKET", "COMMA", "SEMICOLON", 
                  "COLON", "INT_LIT", "DEC_LIT", "BIN_LIT", "OCT_LIT", "HEX_LIT", 
                  "FLOAT_LIT", "EXPONENT", "STRING_LIT", "ESC", "BOOL_LIT", 
                  "NIL_LIT", "IDENTIFIER", "NEWLINE", "WS", "SINGLE_LINE_COMMENT", 
                  "MULTI_LINE_COMMENT", "GETINT", "PUTINT", "PUTINTLN", 
                  "GETFLOAT", "PUTFLOAT", "PUTFLOATLN", "GETBOOL", "PUTBOOL", 
                  "PUTBOOLLN", "GETSTRING", "PUTSTRING", "PUTSTRINGLN", 
                  "PUTLN", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    grammarFileName = "MiniGo.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


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


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[63] = self.NEWLINE_action 
            actions[80] = self.UNCLOSE_STRING_action 
            actions[81] = self.ILLEGAL_ESCAPE_action 
            actions[82] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def NEWLINE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.handleNewLine()
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                    if len(self.text) >= 2 and self.text[-2:] == '\r\n':
                        raise UncloseString(self.text[:-2])  # Handles Windows-style line endings (\r\n)
                    elif self.text[-1] == '\n':
                        raise UncloseString(self.text[:-1])  # Handles Unix-style line endings (\n)
                    else:
                        raise UncloseString(self.text)       # Handles EOF case
                
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                raise IllegalEscape(self.text)

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise ErrorToken(self.text)
     


