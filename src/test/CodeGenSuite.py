import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    # def test_int_literal(self):
    #     input = """func main() {putInt(5);};"""
    #     expect = "5"
    #     self.assertTrue(TestCodeGen.test(input,expect,501))
    # def test_local_var(self):
    #     input = """func main() {var a int = 20;  putInt(a);};"""
    #     expect = "20"
    #     self.assertTrue(TestCodeGen.test(input,expect,502))
    # def test_gllobal_var(self):
    #     input = """var a int = 10; func main() { putInt(a);};"""
    #     expect = "10"
    #     self.assertTrue(TestCodeGen.test(input,expect,503))
    # def test_int_ast(self):
    #     input = Program([FuncDecl("main",[],VoidType(),Block([FuncCall("putInt", [IntLiteral(25)])]))])
    #     expect = "25"
    #     self.assertTrue(TestCodeGen.test(input,expect,504))
    # def test_local_var_ast(self):
    #     input = Program([FuncDecl("main",[],VoidType(),Block([VarDecl("a",IntType(),IntLiteral(500)),FuncCall("putInt", [Id("a")])]))])
    #     expect = "500"
    #     self.assertTrue(TestCodeGen.test(input,expect,505))
    # def test_global_var_ast(self):  
    #     input = Program([VarDecl("a",IntType(),IntLiteral(5000)),FuncDecl("main",[],VoidType(),Block([FuncCall("putInt", [Id("a")])]))])
    #     expect = "5000"
    #     self.assertTrue(TestCodeGen.test(input,expect,506))
    # def test_array_literal(self):
    #     input = """func main() {var a [2]int = [2]int{1,2}; putInt(a[1]);};"""
    #     expect = "2"
    #     self.assertTrue(TestCodeGen.test(input,expect,507))
    # def test_array_literal_2(self):
    #     input = """func main() {var a [2][2]int = [2][2]int{{1,2},{3,4}}; putInt(a[1][0]);};"""
    #     expect = "3"
    #     self.assertTrue(TestCodeGen.test(input,expect,508))
    # # def test_array_literal_3(self):
    # #     input = """func main() {var a [2][2]int = [2][2]int{{1,2},{3,4}}; putInt(a[0];};"""
    # #     expect = "{1,2}"
    # #     self.assertTrue(TestCodeGen.test(input,expect,509))
    # def test_binary_op(self):
    #     input = """func main() {var a int = 5; var b int = 10; putInt(a + b);};"""
    #     expect = "15"
    #     self.assertTrue(TestCodeGen.test(input,expect,510))
    # def test_binary_op_2(self):
    #     input = """func main() {var a int = 5; var b int = 10; putInt(a - b);};"""
    #     expect = "-5"
    #     self.assertTrue(TestCodeGen.test(input,expect,511))
    # def test_binary_op_3(self):
    #     input = """func main() {var a int = 5; var b int = 10; putInt(a * b);};"""
    #     expect = "50"
    #     self.assertTrue(TestCodeGen.test(input,expect,512))
    # def test_binary_op_4(self):
    #     input = """func main() {var a int = 5; var b int = 10; putInt(a / b);};"""
    #     expect = "0"
    #     self.assertTrue(TestCodeGen.test(input,expect,513))
    # def test_binary_op_5(self):
    #     input = """func main() {var a int = 10; var b int = 9; putInt(a % b);};"""
    #     expect = "1"
    #     self.assertTrue(TestCodeGen.test(input,expect,514))
    # def test_binary_op_6(self):
    #     input = """func main() {var a int = 5; var b float = 10.0; putFloat(a + b);};"""
    #     expect = "15.0"
    #     self.assertTrue(TestCodeGen.test(input,expect,515))
    # def test_binary_op_7(self):
    #     input = """func main() {var a int = 5; var b float = 10.0; putBool(a < b);};"""
    #     expect = "true"
    #     self.assertTrue(TestCodeGen.test(input,expect,516))
    # def test_binary_op_8(self):
    #     input = """func main() {var a string = "Hello "; var b string = "World!"; putString(a + b);};"""
    #     expect = "Hello World!"
    #     self.assertTrue(TestCodeGen.test(input,expect,517))
    # def test_binary_op_9(self):
    #     input = """func main() {var a boolean = true; var b boolean = false; putBool(a && b);};"""
    #     expect = "false"
    #     self.assertTrue(TestCodeGen.test(input,expect,518))
    # def test_binary_op_10(self):
    #     input = """func main() {var a boolean = true; var b boolean = false; putBool(a || b);};"""
    #     expect = "true"
    #     self.assertTrue(TestCodeGen.test(input,expect,519))
    # def test_binary_op_11(self):
    #     input = """func main() {var a int = 5; var b int = 10; putInt(a == b);};"""
    #     expect = "0"
    #     self.assertTrue(TestCodeGen.test(input,expect,520))
    # def test_binary_op_12(self):
    #     input = """func main() {var a boolean = true; var b boolean = false; var c boolean = false; putBool(a && b && c);};"""
    #     expect = "false"
    #     self.assertTrue(TestCodeGen.test(input,expect,521))
    # def test_unary_op(self):
    #     input = """func main() {var a int = 5; putInt(-a);};"""
    #     expect = "-5"
    #     self.assertTrue(TestCodeGen.test(input,expect,522))
    # def test_unary_op_2(self):
    #     input = """func main() {var a boolean = true; putBool(!a);};"""
    #     expect = "false"
    #     self.assertTrue(TestCodeGen.test(input,expect,523))
    # def test_if(self):
    #     input = """func main() {var a int = 5; if (a == 5) {putInt(1);} else {putInt(0);};};"""
    #     expect = "1"
    #     self.assertTrue(TestCodeGen.test(input,expect,524))
    # def test_if_2(self):
    #     input = """func main() {var a int = 5; if (a == 10) {putInt(1);} else {putInt(0);};};"""
    #     expect = "0"
    #     self.assertTrue(TestCodeGen.test(input,expect,525))
    # def test_for(self):
    #     input = """func main() {var a int = 0; for a := 0; a < 5; a += 1 {putInt(a);};};"""
    #     expect = "01234"
    #     self.assertTrue(TestCodeGen.test(input,expect,526))
    # def test_for_2(self):
    #     input = """func main() {var a int = 0; for a < 5 {putInt(a); a += 1;};};"""
    #     expect = "01234"
    #     self.assertTrue(TestCodeGen.test(input,expect,527))
    # def test_for_3(self):
    #     input = """func main() {var a int = 0; for a := 0; a < 5; a += 1 {putInt(a); a += 1;};};"""
    #     expect = "024"
    #     self.assertTrue(TestCodeGen.test(input,expect,528))
    # def test_for_4(self):
    #     input = """func main() {var a int = 0; var b int = 5; for a := 0; a < b; a += 1 {putInt(a); a += 1; b += 1;};};"""
    #     expect = "02468"
    #     self.assertTrue(TestCodeGen.test(input,expect,529))
    # def test_for_5(self):
    #     input = """
    #     func main() {
    #         var a int = 0
    #         var b int = 5 
    #         var c int = 1
    #         for a := 0; a < b; a += c {
    #             putInt(a); 
    #             a += 1 
    #             b += 1
    #             c += 1
    #         }
    #     }
    #     """
    #     expect = "03"
    #     self.assertTrue(TestCodeGen.test(input,expect,530))
    def test_return(self):
        input = """
        func foo() int{
            return 5;
        }
        func main() {
            putInt(foo());
        };"""
        expect = "5"
        self.assertTrue(TestCodeGen.test(input,expect,531))