import unittest
from matrix import Matrix
import scipy.linalg as spla
import numpy as np
from errors import SingularMatrixError

class TestMatrixMethods(unittest.TestCase):
    def test_get_row_echelon_form(self):
        test_matrix = Matrix([[1, 2, 3], [2, 3, 1], [1, 1, 1]])
        U, E = test_matrix.get_row_echelon_form([[1,2,3],[0, -1, -5],[0,0,3]])
        U = U.tolist()
        E = E.tolist()

        self.assertEquals(U, [[1,2,3],[0, -1, -5],[0,0,3]])
        self.assertEquals(E,[[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]])

    def test_get_row_echelon_form2(self):
        test_matrix = Matrix([[1, 0, 0], [1, 0, 0], [1, 0, 0]])
        U, E = test_matrix.get_row_echelon_form([[1, 0, 0], [1, 0, 0], [1, 0, 0]])
        U = U.tolist()
        E = E.tolist()
        self.assertEquals(U, [[1, 0, 0], [0, 0, 0], [0, 0, 0]])
        self.assertEquals(E, [[1.0, 0.0, 0.0], [-1.0, 1.0, 0.0], [-1.0, 0.0, 1.0]])

    def test_get_row_echelon_form3(self):
        test_matrix = Matrix([[0, 0, 1], [0, 1, 0], [1, 0, 0]])
        U, E = test_matrix.get_row_echelon_form([[0, 0, 1], [0, 1, 0], [1, 0, 0]])
        U = U.tolist()
        E = E.tolist()
        print("ddddd", U, E)
        self.assertEquals(U, [[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        self.assertEquals(E, [[0.0, 0.0, 1.0], [0.0, 1.0, 0.0], [1.0, 0.0, 0.0]])



    def test_reduced_echelon_form_2(self):
        test_matrix = Matrix([[0,0,1], [0,1,0], [1,0,0]])
        expectation = [[1,0,0],[0,1,0],[0,0,1]]
        U, E = test_matrix.get_reduced_row_echelon_form([[0,0,1], [0,1,0], [1,0,0]])
        self.assertEqual(U.tolist(), expectation)
        self.assertEqual(E.tolist(),[[0.0, 0.0, 1.0], [0.0, 1.0, 0.0], [1.0, 0.0, 0.0]])



    def test_reduced_echelon_form_4(self):
         test_matrix = Matrix([[0,0,0,0,1], [0,0,0,1,0], [0,0,1,0,0],[0,1,0,0,0],[1,0,0,0,0]])
         expectation = [[1,0,0,0,0],[0,1,0,0,0],[0,0,1,0,0], [0,0,0,1,0],[0,0,0,0,1]]
         U, E = test_matrix.get_reduced_row_echelon_form([[1,0,0,0,0],[0,1,0,0,0],[0,0,1,0,0], [0,0,0,1,0],[0,0,0,0,1]])
         self.assertEqual(U.tolist(), expectation)
         self.assertEqual(E.tolist(), [[1.0, 0.0, 0.0, 0.0, 0.0], [-0.0, 1.0, 0.0, 0.0, 0.0], [-0.0, -0.0, 1.0, 0.0, 0.0], [-0.0, -0.0, -0.0, 1.0, 0.0], [-0.0, -0.0, -0.0, -0.0, 1.0]])



    def test_get_PLU(self):
        test_matrix = Matrix(
            [[7.0, 3.0, -1.0, 2.0], [3.0, 8.0, 1.0, -4.0], [-1.0, 1.0, 4.0, -1.0], [2.0, -4.0, -1.0, 6.0]])
        L, U, P = test_matrix.get_PLU()
        self.assertTrue(np.allclose(L.dot(U), P * test_matrix.A))

    def test_get_PLU_1(self):
        test_matrix = Matrix([[2, 3, 4], [5, 4, 3], [9, 8, 7]])
        with self.assertRaises(SingularMatrixError):
            L, U, P = test_matrix.get_PLU()

    def test_get_PLU_2(self):
        test_matrix = Matrix([[7, 3, -1, 2], [3, 8, 1, -4], [-1, 1, 4, -1], [2, -4, -1, 6]])
        L, U, P = test_matrix.get_PLU()

        # self.assertEquals(L.tolist(), [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0615, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0923, 0.4444, 1.0, 0.0, 0.0, 0.0], [0.1077, 0.5556, 0.0, 1.0, 0.0, 0.0], [-0.0, 0.2222, 0.0, -0.5, 1.0, 0.0], [0.6615, -0.0, 0.0, -0.5, -0.0, 1.0]])
        # self.assertEquals(U.tolist(),[[65, 3, 4, 1, 2, 4], [0, 9, 8, 7, 6, 5], [0, 0, -1, 1, 32, 1], [0, 0, 0, 6, 5, 73], [0, 0, 0, 0, 1, 36], [0, 0, 0, 0, 0, 36]])
        # self.assertEquals(P.tolist(),[[0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0]])
        self.assertTrue(np.allclose(L.dot(U), P * test_matrix.A))

    def test_get_m(self):
        test_matrix = Matrix(
            [[7.0, 3.0, -1.0, 2.0], [3.0, 8.0, 1.0, -4.0], [-1.0, 1.0, 4.0, -1.0], [2.0, -4.0, -1.0, 6.0]])
        self.assertEqual(test_matrix.get_m(), 4)
        test_matrix1 = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        self.assertEqual(test_matrix1.get_m(), 3)

    def test_get_n(self):
        test_matrix = Matrix(
            [[7.0, 3.0, -1.0, 2.0], [3.0, 8.0, 1.0, -4.0], [-1.0, 1.0, 4.0, -1.0], [2.0, -4.0, -1.0, 6.0]])
        self.assertEqual(test_matrix.get_n(), 4)
        test_matrix1 = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        self.assertEqual(test_matrix1.get_n(), 3)

    def test_check_matrix1(self):
        with self.assertRaises(ValueError):
            Matrix([[1, 2, 3], ["a", "v", "q"], [4, 3, 2]])

    def test_check_matrix2(self):
        with self.assertRaises(ValueError):
            Matrix([[1, 2], [1, 2, 3], [4, 3, 2]])

    def test_solve_equation(self):
        test_matrix = Matrix([[0, 0, 1], [0, 1, 0], [1, 0, 0]])
        test = test_matrix.solve_equation([[3],[4],[5]])
        self.assertEqual(test.tolist(),[[5.0], [4.0], [3.0]])

    def test_solve_equation_1(self):
        test_matrix = Matrix([[3,43,0,12],[432,21,654,32],[765,43,23,54],[76,4,3,2]])
        test = test_matrix.solve_equation([[54], [98], [0], [2]])
        self.assertEqual(test.tolist(),[[-0.03843933611513756], [1.4474166123917926], [0.16188527197785355], [-0.6769663603751386]])

    def test_solve_equation_2(self):
        test_matrix = Matrix([[3, 43, 0, 12], [432, 21, 654, 32], [765, 43, 23, 54], [76, 4, 3, 2]])
        test = test_matrix.solve_equation([[4],[6],[1],[9]])
        self.assertEqual(test.tolist(),[[0.14544402790042696], [0.825490558326782], [0.01994223794671919], [-2.707767533789866]])


if __name__ == '__main__':
    unittest.main()



