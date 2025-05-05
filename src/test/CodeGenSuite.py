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
    # def test_array_literal_3(self):
    #     input = """
    #         func main() {
    #             var a [2][2]int = [2][2]int{{1,2},{3,4}}
    #             b := a[0]
    #             for i := 0; i < 2; i += 1 {
    #                 putInt(b[i])
    #             }
    #         }
    #         """
    #     expect = "12"
    #     self.assertTrue(TestCodeGen.test(input,expect,509))
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
    # def test_return(self):
    #     input = """
    #     func foo() int{
    #         return 5;
    #     }
    #     func main() {
    #         putInt(foo());
    #     };"""
    #     expect = "5"
    #     self.assertTrue(TestCodeGen.test(input,expect,531))
    # def test_return_2(self):
    #     input = """
    #     func foo1() int{
    #         return 5;
    #     }
    #     func foo2() int{
    #         return foo1();
    #     }
    #     func main() {
    #         var a int = foo2();
    #         putInt(a);
    #     };"""
    #     expect = "5"
    #     self.assertTrue(TestCodeGen.test(input,expect,532))
    # def test_param_decl(self):
    #     input = """
    #     func foo1(x int) int{
    #         return x + 1;
    #     }
    #     func foo2(x int) int{
    #         return x + 2;
    #     }
    #     func main() {
    #         var a int = foo1(5);
    #         var b int = foo2(a);
    #         putInt(b);
    #     };"""
    #     expect = "8"
    #     self.assertTrue(TestCodeGen.test(input,expect,533))

    # def test_param_decl_2(self):
    #     input = """
    #     func foo1(x int) int{
    #         return x + 1;
    #     }
    #     func foo2(x int, y int) int{
    #         return x + y;
    #     }
    #     func main() {
    #         var a int = foo1(5);
    #         var b int = foo2(a, 10);
    #         putInt(b);
    #     };"""
    #     expect = "16"
    #     self.assertTrue(TestCodeGen.test(input,expect,534))

    # def test_func_call(self):
    #     input = """
    #     func foo1(x int) int{
    #         return x + 1;
    #     }
    #     func foo2() int{
    #         return foo1(foo1(5));
    #     }
    #     func main() {
    #         var a int = foo2();
    #         putInt(a);
    #     };"""
    #     expect = "7"
    #     self.assertTrue(TestCodeGen.test(input,expect,535))
    # def test_const_decl(self):
    #     input = """
    #     const a = 5;
    #     const b = 10;
    #     func main() {
    #         putInt(a + b);
    #     };"""
    #     expect = "15"
    #     self.assertTrue(TestCodeGen.test(input,expect,536))
    # def test_break_stmt(self):
    #     input = """
    #     func main() {
    #         var a int = 0;
    #         for a < 5 {
    #             if a == 3 {
    #                 break;
    #             }
    #             putInt(a);
    #             a += 1;
    #         }
    #     };"""
    #     expect = "012"
    #     self.assertTrue(TestCodeGen.test(input,expect,537))
    # def test_break_stmt_2(self):
    #     input = """
    #     func main() {
    #         var a int = 0;
    #         for a := 0; a < 5; a += 1 {
    #             if a == 3 {
    #                 break;
    #             }
    #             putInt(a);
    #         }
            
    #     };"""
    #     expect = "012"
    #     self.assertTrue(TestCodeGen.test(input,expect,538))
    # def test_continue_stmt(self):
    #     input = """
    #     func main() {
    #         var a int = 0;
    #         for a < 5 {
    #             a += 1;
    #             if a == 3 {
    #                 continue;
    #             }
    #             putInt(a);
                
    #         }
    #     };"""
    #     expect = "1245"
    #     self.assertTrue(TestCodeGen.test(input,expect,539))
    # def test_continue_stmt_2(self):
    #     input = """
    #     func main() {
    #         var a int = 0;
    #         for a := 0; a < 5; a += 1 {
    #             if a == 3 {
    #                 continue;
    #             }
    #             putInt(a);
    #         }
    #         putInt(a);
    #     };"""
    #     expect = "01245"
    #     self.assertTrue(TestCodeGen.test(input,expect,540))
    # def test_var_decl(self):
    #     input = """
    #     var a int = 5 + 5;
    #     var b int = 10;
    #     func main() {
    #         putInt(a + b);
    #     };"""
    #     expect = "20"
    #     self.assertTrue(TestCodeGen.test(input,expect,541))
    # def test_var_decl_2(self):
    #     input = """
    #     var a = 5 + 5;
    #     var b float = 10;
    #     func main() {
    #         putFloat(a + b);
    #     };"""
    #     expect = "20.0"
    #     self.assertTrue(TestCodeGen.test(input,expect,542))
    # def test_struct_decl(self):
    #     input = """
    #     type Test struct {
    #         x int
    #         y int
    #     }

    #     func main() {
    #         putInt(1)
    #     }
    #     """
    #     expect = "1"
    #     self.assertTrue(TestCodeGen.test(input,expect,543))
    # def test_struct_decl_2(self):
    #     input = """
    #     type Test struct {
    #         x int
    #         y int
    #     }

    #     func main() {
    #         var a Test
    #         putInt(1)
    #     }
    #     """
    #     expect = "1"
    #     self.assertTrue(TestCodeGen.test(input,expect,544))
    # def test_field_access(self):
    #     input = """
    #     type Test struct {
    #         x int
    #         y int
    #     }

    #     func main() {
    #         var a Test
    #         a.x := 5
    #         putInt(a.x)
    #     }
    #     """
    #     expect = "5"
    #     self.assertTrue(TestCodeGen.test(input,expect,545))
    # def test_field_access_2(self):
    #     input = """
    #     type Test2 struct {
    #         z int
    #     }
    #     type Test1 struct {
    #         y Test2
    #     }
    #     type Test struct {
    #         x Test1
    #     }

    #     func main() {
    #         var a Test
    #         var b Test1
    #         var c Test2
    #         c.z := 5
    #         b.y := c
    #         a.x := b
    #         putInt(a.x.y.z)
    #     }
    #     """
    #     expect = "5"
    #     self.assertTrue(TestCodeGen.test(input,expect,546))
    # def test_field_access_3(self):
    #     input = """
    #     type Test2 struct {
    #         z int
    #     }
    #     type Test1 struct {
    #         y Test2
    #     }
    #     type Test struct {
    #         x Test1
    #     }

    #     func main() {
    #         var a Test
    #         var b Test1
    #         var c Test2
    #         c.z := 5
    #         b.y := c
    #         a.x := b
    #         a.x.y.z := 10
    #         putInt(a.x.y.z)
    #     }
    #     """
    #     expect = "10"
    #     self.assertTrue(TestCodeGen.test(input,expect,547))    

    # def test_assign_stmt(self):
    #     input = """
    #     func main() {
    #         a := 5
    #         putInt(a)
    #     }
    #     """
    #     expect = "5"
    #     self.assertTrue(TestCodeGen.test(input,expect,548))
    # def test_struct_literal(self):
    #     input = """
    #     type Test struct {
    #         x int
    #         y int
    #     }

    #     func main() {
    #         a := Test{x:1, y:2}
    #         putInt(a.x)
    #     }
    #     """
    #     expect = "1"
    #     self.assertTrue(TestCodeGen.test(input,expect,549))
    
    # def test_struct_literal_2(self):
    #     input = """
    #     type Test struct {
    #         x float
    #         y int
    #     }

    #     func main() {
    #         a := Test{x:1, y:2}
    #         putInt(a.x)
    #     }
    #     """
    #     expect = "1"
    #     self.assertTrue(TestCodeGen.test(input,expect,550))

    # def test_struct_literal_3(self):
    #     input = """
    #     type Test struct {
    #         x int
    #         y int
    #     }

    #     func main() {
    #         a := Test{x:1, y:2}
    #         a := Test{x:3, y:4}
    #         putInt(a.x)
    #     }
    #     """
    #     expect = "3"
    #     self.assertTrue(TestCodeGen.test(input,expect,551))
    # def test_struct_literal_4(self):
    #     input = """
    #     type Test struct {
    #         x int
    #         y int
    #     }

    #     func main() {
    #         var a Test = Test{x:1, y:2}
    #         var b = Test{x:3, y:4}
    #         putInt(a.x)
    #     }
    #     """
    #     expect = "1"
    #     self.assertTrue(TestCodeGen.test(input,expect,552))
    
    # def test_struct_literal_5(self):
    #     input = """
    #     type Test struct {
    #         x int
    #         y int
    #     }
    #     var a Test = Test{x:1, y:2}
    #     var b = Test{x:3, y:4}
    #     func main() {
    #         putInt(a.x)
    #     }
    #     """
    #     expect = "1"
    #     self.assertTrue(TestCodeGen.test(input,expect,553))
    # def test_struct_literal_6(self):
    #     input = """
    #     type Test struct {
    #         x int
    #         y int
    #     }

    #     func main() {
    #         const a = Test{x:3, y:4}
    #         putInt(a.x)
    #     }
    #     """
    #     expect = "3"
    #     self.assertTrue(TestCodeGen.test(input,expect,554))
    
    # def test_struct_literal_7(self):
    #     input = """
    #     type Test struct {
    #         x int
    #         y int
    #     }

    #     const a = Test{x:3, y:4}
    #     func main() {
    #         putInt(a.x)
    #     }
    #     """
    #     expect = "3"
    #     self.assertTrue(TestCodeGen.test(input,expect,555))

    # def test_struct_literal_8(self):
    #     input = """
    #     type Test1 struct {
    #         x int
    #         y int
    #     }

    #     type Test struct {
    #         x Test1
    #     }

    #     func main() {
    #         a := Test1{x:1, y:2}
    #         c := Test{x:a}
    #         c.x := Test1{x:3, y:4}
    #         putInt(c.x.y)
    #     }
    #     """
    #     expect = "4"
    #     self.assertTrue(TestCodeGen.test(input,expect,556))
    def test_struct_literal_9(self):
        input = """
        var a = Test{x:Test1{x:1, y:2}}

        type Test struct {
            x Test1
        }

        type Test1 struct {
            x int
            y int
        }

        func main() {
            putInt(a.x.y)
        }
        """
        expect = "2"
        self.assertTrue(TestCodeGen.test(input,expect,557))
    # def test_method_decl(self):
    #     input = """
    #     type Test struct {
    #         x int
    #         y int
    #     }

    #     func (a Test) foo() int {
    #         return a.x + a.y
    #     }

    #     func main() {
    #         var a Test
    #         a.x := 5
    #         a.y := 10
    #         putInt(a.foo())
    #     }
    #     """
    #     expect = "15"
    #     self.assertTrue(TestCodeGen.test(input,expect,558))