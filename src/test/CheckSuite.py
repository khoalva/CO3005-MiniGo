import unittest
from TestUtils import TestChecker
from AST import *

class CheckSuite(unittest.TestCase):

    def test_401(self):
        input = """
    var x int;
    var x int;
        """
        self.assertTrue(TestChecker.test(input, """Redeclared Variable: x\n""", 401))

    def test_402(self):
        input = """
    func foo() {
        var x int;
        var x int;
    }
        """
        self.assertTrue(TestChecker.test(input, """Redeclared Variable: x\n""", 402))

    def test_403(self):
        input = """
    func foo() {
        var x int;
        x := 1
    }

        """
        self.assertTrue(TestChecker.test(input, "", 403))

    def test_404(self):
        input = """
    const c = 1;
    const c = 2;
        """
        self.assertTrue(TestChecker.test(input, """Redeclared Constant: c\n""", 404))

    def test_405(self):
        input = """
    func foo() {
        const c = 1;
        const c = 2;
    }
        """
        self.assertTrue(TestChecker.test(input, """Redeclared Constant: c\n""", 405))

    def test_406(self):
        input = """
    func foo(x int, x int) {}
        """
        self.assertTrue(TestChecker.test(input, """Redeclared Parameter: x\n""", 406))

    def test_407(self):
        input = """
    type S struct {
        f int;
    };
    type S struct {
        x int;
        y int;
    };
        """
        self.assertTrue(TestChecker.test(input, """Redeclared Type: S\n""", 407))

    def test_408(self):
        input = """
    type S struct {
        f int;
    };
    type S interface {
        m();
    };
        """
        self.assertTrue(TestChecker.test(input, """Redeclared Type: S\n""", 408))

    def test_409(self):
        input = """
    func foo() {}
    func foo() {}
        """
        self.assertTrue(TestChecker.test(input, """Redeclared Function: foo\n""", 409))

    def test_410(self):
        input = """
    type S struct {
        f int;
    };
    func (s S) m() {
        return
    };
    func (s S) m() {
        return
    };
        """
        self.assertTrue(TestChecker.test(input, """Redeclared Method: m\n""", 410))

    def test_411(self):
        input = """
    type S struct {
        f int;
        f int;
    };
        """
        self.assertTrue(TestChecker.test(input, """Redeclared Field: f\n""", 411))

    def test_412(self):
        input = """
    type I interface {
        m();
        m();
    };
        """
        self.assertTrue(TestChecker.test(input, """Redeclared Prototype: m\n""", 412))

    def test_413(self):
        input = """
    var x int;
    const x = 1;
        """
        self.assertTrue(TestChecker.test(input, """Redeclared Constant: x\n""", 413))

    def test_414(self):
        input = """
    var i int;
    func main() {
        for i := 0; i < 10; i += 1 {
            var i int;
        }
    }

    var i int;
        """
        self.assertTrue(TestChecker.test(input, """Redeclared Variable: i\n""", 414))
    def test_415(self):
        input = """
    var i int;
    var arr [2]int;
    v := 1
    for i, v := range arr {}
        """
        self.assertTrue(TestChecker.test(input, "", 415))

    def test_416(self):
        input = """
    func foo() {
        var x int
        var x int;

    }
        """
        self.assertTrue(TestChecker.test(input, """Redeclared Variable: x\n""", 416))

    def test_417(self):
        input = """
    func getInt() {}
        """
        self.assertTrue(TestChecker.test(input, """Redeclared Function: getInt\n""", 417))

    def test_418(self):
        input = """
    var S int;
    type S struct {
        f int;
        };
        """
        self.assertTrue(TestChecker.test(input, """Redeclared Type: S\n""", 418))

    def test_419(self):
        input = """
    func foo() {
        return
        };
    type S struct {
        f int;
    };
    func (s S) foo() {
        return
        };
        """
        self.assertTrue(TestChecker.test(input, "", 419))

    def test_420(self):
        input = """
    func foo(x int) {
        var x int;
    }
        """
        self.assertTrue(TestChecker.test(input, "", 420))
    
    def test_423(self):
        input = """
    func foo(x int) {
        return
    }
    func main() {
        foo(y);
    }
        """
        self.assertTrue(TestChecker.test(input, """Undeclared Identifier: y\n""", 423))
    
    def test_424(self):
        input = """
    func main() {
        bar();
    }
        """
        self.assertTrue(TestChecker.test(input, """Undeclared Function: bar\n""", 424))
    
    def test_425(self):
        input = """
    type S struct {
        f int;
    };
    func main() {
        var s S;
        s.m();
    }
        """
        self.assertTrue(TestChecker.test(input, """Undeclared Method: m\n""", 425))
    
    def test_426(self):
        input = """
    type S struct {
        x int;
    };
    func main() {
        var s S;
        s.y := 1;
    }
        """
        self.assertTrue(TestChecker.test(input, """Undeclared Field: y\n""", 426))
    
    def test_427(self):
        input = """
    var x S;
        """
        self.assertTrue(TestChecker.test(input, """Undeclared Type: S\n""", 427))
    
    def test_429(self):
        input = """
    func foo() {
        var x int = bar();
    }
        """
        self.assertTrue(TestChecker.test(input, """Undeclared Function: bar\n""", 429))
    
    def test_431(self):
        input = """
    type S struct {
        x int;
    };
    func main() {
        var s S = S{y: 1};
    }
        """
        self.assertTrue(TestChecker.test(input, """Undeclared Field: y\n""", 431))
    
    def test_432(self):
        input = """
    func foo() {
        for x < 10 {
            x := 1;
        }
    }
        """
        self.assertTrue(TestChecker.test(input, """Undeclared Identifier: x\n""", 432))
    
    def test_433(self):
        input = """
    func foo() {
        for i, v := range arr {
            var i int;
        }
    }
        """
        self.assertTrue(TestChecker.test(input, """Undeclared Identifier: arr\n""", 433))
    
    def test_434(self):
        input = """
    func foo() {
        var x int = a + b;
    }
        """
        self.assertTrue(TestChecker.test(input, """Undeclared Identifier: a\n""", 434))
    
    def test_435(self):
        input = """
    func main() {
        putDouble(1.0);
    }
        """
        self.assertTrue(TestChecker.test(input, """Undeclared Function: putDouble\n""", 435))
    
    def test_436(self):
        input = """
    func foo() {
        s.x := 1;
    }
        """
        self.assertTrue(TestChecker.test(input, """Undeclared Identifier: s\n""", 436))
    
    def test_437(self):
        input = """
    func foo() {
        arr[0] := 1;
    }
        """
        self.assertTrue(TestChecker.test(input, """Undeclared Identifier: arr\n""", 437))
    
    def test_438(self):
        input = """
    func foo() int {
        return x;
    }
        """
        self.assertTrue(TestChecker.test(input, """Undeclared Identifier: x\n""", 438))
    
    def test_439(self):
        input = """
    func foo() {
        var x [2]T;
    }
        """
        self.assertTrue(TestChecker.test(input, """Undeclared Type: T\n""", 439))
    
    def test_440(self):
        input = """
    var x I;
        """
        self.assertTrue(TestChecker.test(input, """Undeclared Type: I\n""", 440))
    
    def test_441(self):
        input = """
    func foo() {
        var x string;
        x := 1;
    }
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: Assign(Id(x),IntLiteral(1))\n""", 441))
    
    def test_442(self):
        input = """
    func foo() {
        var x int;
        x := "string";
    }
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: Assign(Id(x),StringLiteral("string"))\n""", 442))
    
    def test_443(self):
        input = """
    func foo() {
        var x [3]int;
        x := [2]int{1, 2};
    }
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: Assign(Id(x),ArrayLiteral([IntLiteral(2)],IntType,[IntLiteral(1),IntLiteral(2)]))\n""", 443))
    
    def test_444(self):
        input = """
    func foo() {
        var x [2]int;
        x := [2]string{"a", "b"};
    }
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: Assign(Id(x),ArrayLiteral([IntLiteral(2)],StringType,[StringLiteral("a"),StringLiteral("b")]))\n""", 444))

    def test_445(self):
        input = """
    func foo() {
        var x int;
        x := 1.5;
    }
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: Assign(Id(x),FloatLiteral(1.5))\n""", 445))

    def test_446(self):
        input = """
    type I interface { m() };
    type S struct {i int};
    func (s S) m() {return;}
    func foo() {
        var i I;
        i := S{};
    }
        """
        self.assertTrue(TestChecker.test(input, "", 446))
    
    def test_447(self):
        input = """
    func foo() {
        var x [2]int;
        x := 1;
    }
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: Assign(Id(x),IntLiteral(1))\n""", 447))
    
    def test_448(self):
        input = """
    func foo() {
        var x int;
        x += "string";
    }
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: BinaryOp(Id(x),+,StringLiteral("string"))\n""", 448))
    
    def test_449(self):
        input = """
    type S1 struct { x int };
    type S2 struct { y int };
    func foo() {
        var s S1;
        s := S2{y: 1};
    }
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: Assign(Id(s),StructLiteral(S2,[(y,IntLiteral(1))]))\n""", 449))
    
    def test_450(self):
        input = """
    func foo() {
        x := 1
        x := "string";
    }
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: Assign(Id(x),StringLiteral("string"))\n""", 450))
    
    def test_451(self):
        input = """
    var x int = "string";
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: VarDecl(x,IntType,StringLiteral("string"))\n""", 451))
    
    def test_452(self):
        input = """
    var x [2]int = [2]string{"a", "b"};
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: VarDecl(x,ArrayType(IntType,[IntLiteral(2)]),ArrayLiteral([IntLiteral(2)],StringType,[StringLiteral("a"),StringLiteral("b")]))\n""", 452))


    def test_453(self):
        input = """
    type S struct { x int };
    var s S = S{x: "string"};
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: StructLiteral(S,[(x,StringLiteral("string"))])\n""", 453))
    
    def test_454(self):
        input = """
    func foo() {
        var x = "string";
        x := 1;
    }
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: Assign(Id(x),IntLiteral(1))\n""", 454))
    
    def test_456(self):
        input = """
    func foo() {
        if (1) {
        return
        }
    }
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: If(IntLiteral(1),Block([Return()]))\n""", 456))
    
    def test_457(self):
        input = """
    func foo() {
        for 1 {
        continue
    }
    }
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: For(IntLiteral(1),Block([Continue()]))\n""", 457))

    def test_458(self):
        input = """
    func foo() {
        for i := "string"; i < 10; i += 1 {}
    }
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: BinaryOp(Id(i),<,IntLiteral(10))\n""", 458))
    
    def test_460(self):
        input = """
    func foo() {
        for i, v := range "string" {
            return
        }
    }
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: ForEach(Id(i),Id(v),StringLiteral("string"),Block([Return()]))\n""", 460))

    def test_461(self):
        input = """
    func foo() int { return 1; }
    func main() {
        foo();
    }
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: FuncCall(foo,[])\n""", 461))
    
    def test_462(self):
        input = """
    func foo() {return}
    func main() {
        var x int = foo();
    }
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: FuncCall(foo,[])\n""", 462))
    
    def test_463(self):
        input = """
    func foo(x int, y int) {return}
    func main() {
        foo(1);
    }
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: FuncCall(foo,[IntLiteral(1)])\n""", 463))
    
    def test_464(self):
        input = """
    func foo(s string) {return}
    func main() {
        foo(1);
    }
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: FuncCall(foo,[IntLiteral(1)])\n""", 464))
    
    def test_465(self):
        input = """
    type S struct {
        f int;
    };
    func (s S) m() {
        return
    }
    func main() {
        var x int;
        x.m();
    }
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: MethodCall(Id(x),m,[])\n""", 465))
    
    def test_466(self):
        input = """
    func main() {
        putInt("string");
    }
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: FuncCall(putInt,[StringLiteral("string")])\n""", 466))
    
    def test_467(self):
        input = """
    type S struct {
        f int;
    };
    func (s S) m() int { return 1; }
    func main() {
        var s S;
        s.m();
    }
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: MethodCall(Id(s),m,[])\n""", 467))
    
    def test_468(self):
        input = """
    type S struct {a int};
    func (s S) m() { return ; }
    func main() {
        var s S;
        var x int = s.m();
    }
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: MethodCall(Id(s),m,[])\n""", 468))
    
    def test_469(self):
        input = """
    type S struct {f int};
    func (s S) m() { return ; }
    func main() {
        var x int;
        x.m();
    }
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: MethodCall(Id(x),m,[])\n""", 469))
    def test_470(self):
        input = """
    type S struct {f int};
    func (s S) m() { return ; }
    func main() {
        var x int;
        x.m();
    }
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: MethodCall(Id(x),m,[])\n""", 470))
    def test_471(self):
        input = """
    type S struct {f int};
    func (s S) m() { return ; }
    func main() {
        var x int;
        x.m();
    }
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: MethodCall(Id(x),m,[])\n""", 471))
    def test_472(self):
        input = """
    type S struct {f int};
    func (s S) m() { return ; }
    func main() {
        var x int;
        x.m();
    }
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: MethodCall(Id(x),m,[])\n""", 472))
    def test_473(self):
        input = """
    type S struct {f int};
    func (s S) m() { return ; }
    func main() {
        var x int;
        x.m();
    }
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: MethodCall(Id(x),m,[])\n""", 473))
    def test_474(self):
        input = """
    type S struct {f int};
    func (s S) m() { return ; }
    func main() {
        var x int;
        x.m();
    }
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: MethodCall(Id(x),m,[])\n""", 474))
    def test_475(self):
        input = """
    type S struct {f int};
    func (s S) m() { return ; }
    func main() {
        var x int;
        x.m();
    }
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: MethodCall(Id(x),m,[])\n""", 475))
    def test_476(self):
        input = """
    type S struct {f int};
    func (s S) m() { return ; }
    func main() {
        var x int;
        x.m();
    }
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: MethodCall(Id(x),m,[])\n""", 476))
    def test_477(self):
        input = """
    type S struct {f int};
    func (s S) m() { return ; }
    func main() {
        var x int;
        x.m();
    }
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: MethodCall(Id(x),m,[])\n""", 477))
    def test_478(self):
        input = """
    type S struct {f int};
    func (s S) m() { return ; }
    func main() {
        var x int;
        x.m();
    }
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: MethodCall(Id(x),m,[])\n""", 478))
    def test_479(self):
        input = """
    type S struct {f int};
    func (s S) m() { return ; }
    func main() {
        var x int;
        x.m();
    }
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: MethodCall(Id(x),m,[])\n""", 479))
    def test_480(self):
        input = """
    type S struct {f int};
    func (s S) m() { return ; }
    func main() {
        var x int;
        x.m();
    }
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: MethodCall(Id(x),m,[])\n""", 480))
    def test_481(self):
        input = """
    type S struct {f int};
    func (s S) m() { return ; }
    func main() {
        var x int;
        x.m();
    }
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: MethodCall(Id(x),m,[])\n""", 481))
    def test_482(self):
        input = """
    type S struct {f int};
    func (s S) m() { return ; }
    func main() {
        var x int;
        x.m();
    }
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: MethodCall(Id(x),m,[])\n""", 482))
    def test_483(self):
        input = """
    type S struct {f int};
    func (s S) m() { return ; }
    func main() {
        var x int;
        x.m();
    }
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: MethodCall(Id(x),m,[])\n""", 483))
    def test_485(self):
        input = """
    type S struct {f int};
    func (s S) m() { return ; }
    func main() {
        var x int;
        x.m();
    }
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: MethodCall(Id(x),m,[])\n""", 484))
    def test_485(self):
        input = """
    type S struct {f int};
    func (s S) m() { return ; }
    func main() {
        var x int;
        x.m();
    }
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: MethodCall(Id(x),m,[])\n""", 485))
    def test_486(self):
        input = """
    type S struct {f int};
    func (s S) m() { return ; }
    func main() {
        var x int;
        x.m();
    }
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: MethodCall(Id(x),m,[])\n""", 486))
    def test_487(self):
        input = """
    type S struct {f int};
    func (s S) m() { return ; }
    func main() {
        var x int;
        x.m();
    }
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: MethodCall(Id(x),m,[])\n""", 487))
    def test_488(self):
        input = """
    type S struct {f int};
    func (s S) m() { return ; }
    func main() {
        var x int;
        x.m();
    }
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: MethodCall(Id(x),m,[])\n""", 488))
    def test_489(self):
        input = """
    type S struct {f int};
    func (s S) m() { return ; }
    func main() {
        var x int;
        x.m();
    }
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: MethodCall(Id(x),m,[])\n""", 489))
    def test_490(self):
        input = """
    type S struct {f int};
    func (s S) m() { return ; }
    func main() {
        var x int;
        x.m();
    }
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: MethodCall(Id(x),m,[])\n""", 490))
    def test_491(self):
        input = """
    type S struct {f int};
    func (s S) m() { return ; }
    func main() {
        var x int;
        x.m();
    }
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: MethodCall(Id(x),m,[])\n""", 491))
    def test_492(self):
        input = """
    type S struct {f int};
    func (s S) m() { return ; }
    func main() {
        var x int;
        x.m();
    }
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: MethodCall(Id(x),m,[])\n""", 492))
    def test_493(self):
        input = """
    type S struct {f int};
    func (s S) m() { return ; }
    func main() {
        var x int;
        x.m();
    }
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: MethodCall(Id(x),m,[])\n""", 493))
    def test_494(self):
        input = """
    type S struct {f int};
    func (s S) m() { return ; }
    func main() {
        var x int;
        x.m();
    }
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: MethodCall(Id(x),m,[])\n""", 494))
    def test_495(self):
        input = """
    type S struct {f int};
    func (s S) m() { return ; }
    func main() {
        var x int;
        x.m();
    }
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: MethodCall(Id(x),m,[])\n""", 495))
    def test_496(self):
        input = """
    type S struct {f int};
    func (s S) m() { return ; }
    func main() {
        var x int;
        x.m();
    }
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: MethodCall(Id(x),m,[])\n""", 496))
    def test_497(self):
        input = """
    type S struct {f int};
    func (s S) m() { return ; }
    func main() {
        var x int;
        x.m();
    }
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: MethodCall(Id(x),m,[])\n""", 497))
    def test_498(self):
        input = """
    type S struct {f int};
    func (s S) m() { return ; }
    func main() {
        var x int;
        x.m();
    }
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: MethodCall(Id(x),m,[])\n""", 498))

    def test_499(self):
        input = """
    type S struct {f int};
    func (s S) m() { return ; }
    func main() {
        var x int;
        x.m();
    }
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: MethodCall(Id(x),m,[])\n""", 499))

    def test_500(self):
        input = """
    type S struct {f int};
    func (s S) m() { return ; }
    func main() {
        var x int;
        x.m();
    }
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: MethodCall(Id(x),m,[])\n""", 500))

    def test_501(self):
        input = """
    type S struct {f int};
    func (s S) m() { return ; }
    func main() {
        var x int;
        x.m();
    }
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: MethodCall(Id(x),m,[])\n""", 501))
    def test_502(self):
        input = """
    type S struct {f int};
    func (s S) m() { return ; }
    func main() {
        var x int;
        x.m();
    }
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: MethodCall(Id(x),m,[])\n""", 502))
    def test_503(self):
        input = """
    type S struct {f int};
    func (s S) m() { return ; }
    func main() {
        var x int;
        x.m();
    }
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: MethodCall(Id(x),m,[])\n""", 503))
    def test_504(self):
        input = """
    type S struct {f int};
    func (s S) m() { return ; }
    func main() {
        var x int;
        x.m();
    }
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: MethodCall(Id(x),m,[])\n""", 504))
    def test_505(self):
        input = """
    type S struct {f int};
    func (s S) m() { return ; }
    func main() {
        var x int;
        x.m();
    }
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: MethodCall(Id(x),m,[])\n""", 505))
    def test_506(self):
        input = """
    type S struct {f int};
    func (s S) m() { return ; }
    func main() {
        var x int;
        x.m();
    }
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: MethodCall(Id(x),m,[])\n""", 506))
    def test_507(self):
        input = """
    type S struct {f int};
    func (s S) m() { return ; }
    func main() {
        var x int;
        x.m();
    }
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: MethodCall(Id(x),m,[])\n""", 507))
    def test_508(self):
        input = """
    type S struct {f int};
    func (s S) m() { return ; }
    func main() {
        var x int;
        x.m();
    }
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: MethodCall(Id(x),m,[])\n""", 508))