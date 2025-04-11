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
        {
            var x int;
        }
    }
        """
        self.assertTrue(TestChecker.test(input, """Redeclared Variable: x\n""", 403))

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
    type S struct {};
    type S struct {};
        """
        self.assertTrue(TestChecker.test(input, """Redeclared Type: S\n""", 407))

    def test_408(self):
        input = """
    type S struct {};
    type S interface {};
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
    type S struct {};
    func (s S) m() {};
    func (s S) m() {};
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
    for i := 0; i < 10; i += 1 {
        var i int;
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
    type S struct {};
        """
        self.assertTrue(TestChecker.test(input, """Redeclared Type: S\n""", 418))

    def test_419(self):
        input = """
    func foo() {};
    type S struct {};
    func (s S) foo() {};
        """
        self.assertTrue(TestChecker.test(input, """Redeclared Method: foo\n""", 419))

    def test_420(self):
        input = """
    func foo(x int) {
        var x int;
    }
        """
        self.assertTrue(TestChecker.test(input, "", 420))

