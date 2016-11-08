import unittest
from matrix import Matrix
import scipy.linalg as spla
import numpy as np

class TestMatrixMethods(unittest.TestCase):

    def test_get_row_echelon_form(self):
        test_matrix = Matrix([[1, 2, 3], [2, 3, 1], [1, 1, 1]])
        self.assertTrue(np.allclose(test_matrix.get_row_echelon_form(), [[1, 2.0, 3.0], [0.0, - 1.0, -5.0], [0.0, 0.0, 3.0]]))

        test_matrix = Matrix([[1,0,0],[1,0,0],[1,0,0]])
        self.assertTrue(np.allclose(test_matrix.get_row_echelon_form(),[[1, 0, 0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]]))

        test_matrix = Matrix([[0,0,3],[0,1,2],[1,2,3]])
        self.assertTrue(np.allclose(test_matrix.get_row_echelon_form(), [[1, 2, 3], [0.0, 1.0, 2.0], [0.0, 0.0, 3.0]]))

        test_matrix = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        self.assertTrue(np.allclose(test_matrix.get_row_echelon_form(), [[1, 0, 0], [0, 1, 0], [0, 0, 1]]))

    def test_get_PLU(self):
        test_matrix = Matrix([[7.0, 3.0, -1.0, 2.0], [3.0, 8.0, 1.0, -4.0], [-1.0, 1.0, 4.0, -1.0], [2.0, -4.0, -1.0, 6.0]])
        L,U,P = test_matrix.get_PLU()
        # self.assertEquals(P.tolist(),[[1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0]])
        # self.assertEquals(U.tolist(),[[7.0, 3.0, -1.0, 2.0], [0.0, 6.71, 1.43, -4.86], [0.0, 0.0, 3.56, 0.33000000000000007], [0.0, 0.0, 5.551115123125783e-17, 1.8799999999999997]])
        # self.assertEqual(L.tolist(),[[1.0, 0.0, 0.0, 0.0], [0.4286, 1.0, 0.0, 0.0], [-0.1429, 0.2131, 1.0, 0.0], [0.2857, -0.7243, 0.0927, 1.0]] )
        self.assertTrue(np.allclose(L.dot(U), P * test_matrix.A))

    def test_get_PLU_1(self):
        test_matrix = Matrix([[2, 3, 4], [5, 4, 3], [9, 8, 7]])
        with self.assertRaises(ValueError):
            L, U, P = test_matrix.get_PLU()




    def test_get_PLU_2(self):
        test_matrix = Matrix([ [7, 3, -1, 2], [3, 8, 1, -4], [-1, 1, 4, -1], [2, -4, -1, 6] ])
        L,U,P = test_matrix.get_PLU()

        # self.assertEquals(L.tolist(), [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0615, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0923, 0.4444, 1.0, 0.0, 0.0, 0.0], [0.1077, 0.5556, 0.0, 1.0, 0.0, 0.0], [-0.0, 0.2222, 0.0, -0.5, 1.0, 0.0], [0.6615, -0.0, 0.0, -0.5, -0.0, 1.0]])
        # self.assertEquals(U.tolist(),[[65, 3, 4, 1, 2, 4], [0, 9, 8, 7, 6, 5], [0, 0, -1, 1, 32, 1], [0, 0, 0, 6, 5, 73], [0, 0, 0, 0, 1, 36], [0, 0, 0, 0, 0, 36]])
        # self.assertEquals(P.tolist(),[[0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0]])
        self.assertTrue(np.allclose(L.dot(U), P*test_matrix.A))





    def test_get_m(self):
        test_matrix = Matrix([[7.0, 3.0, -1.0, 2.0], [3.0, 8.0, 1.0, -4.0], [-1.0, 1.0, 4.0, -1.0], [2.0, -4.0, -1.0, 6.0]])
        self.assertEqual(test_matrix.get_m(), 4)
        test_matrix1 = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        self.assertEquals(test_matrix1.get_m(), 3)
        
    def test_get_n(self):
        test_matrix = Matrix(
            [[7.0, 3.0, -1.0, 2.0], [3.0, 8.0, 1.0, -4.0], [-1.0, 1.0, 4.0, -1.0], [2.0, -4.0, -1.0, 6.0]])
        self.assertEqual(test_matrix.get_n(), 4)
        test_matrix1 = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        self.assertEquals(test_matrix1.get_n(), 3)

    def test_check_matrix1(self):
        with self.assertRaises(ValueError):
            Matrix([[1, 2, 3], ["a", "v", "q"], [4, 3, 2]])


    def test_check_matrix2(self):

        with self.assertRaises(ValueError):
            Matrix([[1, 2], [1, 2, 3], [4, 3, 2]])

if __name__ == '__main__':
    unittest.main()



