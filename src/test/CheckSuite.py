import unittest
from TestUtils import TestChecker
from AST import *

class CheckSuite(unittest.TestCase):

    def test_401(self):
        input = """
    var x int;
 
type TIEN struct {
    Votien int;
}

func (v TIEN) getInt () {
    const c = v.Votien;
    var d = v.tien;
}
        """
        self.assertTrue(TestChecker.test(input, """Undeclared Field: tien\n""", 401))

   