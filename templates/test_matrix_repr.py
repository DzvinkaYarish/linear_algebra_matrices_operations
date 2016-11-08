import unittest
import Matrix

class TestMatrixMethods(unittest.TestCase):

    def test_get_row_echelon_form(self):
        test_matrix = Matrix()
        self.assertEqual(test_matrix.get_row_echelon_form([[1, 2, 3], [2, 3, 1], [1, 1, 1]]), [[1, 2.0, 3.0], [0.0, - 1.0, -5.0], [0.0, 0.0, 3.0]])
        self.assertEqual(test_matrix.get_row_echelon_form([[1,0,0],[1,0,0],[1,0,0]]),[[1, 0, 0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]])
        self.assertEqual(test_matrix.get_row_echelon_form([[0,0,3],[0,1,2],[1,2,3]]), [[1, 2, 3], [0.0, 1.0, 2.0], [0.0, 0.0, 3.0]])
        self.assertEqual(test_matrix.get_row_echelon_form([[1, 0, 0], [0, 1, 0], [0, 0, 1]]), [[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    # def test_get_reduced_echelon_form(self):
    #     test_matrix = Matrix()
    #     self.assertEqual(test_matrix.get_reduced_echelon_form([[1, 2, 3], [2, 3, 1], [1, 1, 1]]), [[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    #     # self.assertEqual(test_matrix.get_reduced_echelon_form([[0,0,3],[0,1,2],[1,2,3]]),)
    #     # self.assertEqual(test_matrix.get_reduced_echelon_form([[1,0,0],[1,0,0],[1,0,0]]),)
    #     self.assertEqual(test_matrix.get_reduced_echelon_form([[1, 0, 0], [0, 1, 0], [0, 0, 1]]), [[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    # def test_solve_equation(self):
    #     test_matrix = Matrix()
    #
    # def test_toString(self):
    #     test_matrix = Matrix()
    def test_get_m(self):
        test_matrix = Matrix([[7.0, 3.0, -1.0, 2.0], [3.0, 8.0, 1.0, -4.0], [-1.0, 1.0, 4.0, -1.0], [2.0, -4.0, -1.0, 6.0] ])
        self.assertEqual(test_matrix.get_m(), 4)
        test_matrix1 = Matrix([[1,0,0],[0,1,0],[0,0,1]])
        self.assertEquals(test_matrix1.get_m(), 3)
        
    def test_get_n(self):
        test_matrix = Matrix(
            [[7.0, 3.0, -1.0, 2.0], [3.0, 8.0, 1.0, -4.0], [-1.0, 1.0, 4.0, -1.0], [2.0, -4.0, -1.0, 6.0]])
        self.assertEqual(test_matrix.get_n(), 4)
        test_matrix1 = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        self.assertEquals(test_matrix1.get_n(), 3)
        
if __name__ == '__main__':
    unittest.main()

