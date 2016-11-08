import numpy as np
import scipy.linalg as spla

class Matrix():
    def __init__(self, arr):
        self.A = np.matrix(arr)
        pass

    def get_row_echelon_form(self, A):
        """Returns a row-echelon form of matrix A"""
        for i in range(min(len(A), len(A[0]))):
            for j in range(i, len(A)):       # for each row
                zero_row = A[j][i] == 0
                if zero_row:
                    continue
                # swap current row with first row
                A[i], A[j] = A[j], A[i]
                # reduce the matrix by looking at each column
                first_row_first_col = A[i][i]

                for cur_row in range(i + 1, len(A)):
                    # divide chosen row by a chosen earlier element from first row and multiply by -1
                    scalarMultiple = -1 * A[cur_row][i] / first_row_first_col
                    for cc in range(i, len(A[0])):  # for each element in a first row
                        A[cur_row][cc] += A[i][cc] * scalarMultiple
                break
        return A

    def get_reduced_echelon_form(self):

        pass
    def get_m(self):
        return self.A.shape[0]

    def get_n(self):
        return self.A.shape[1]


    def get_PLU(self):
        L = np.matrix([[0.0 for i in range(self.get_n())] for j in range(self.get_n())])
        U = np.copy(self.A)
        P = np.matrix([[0.0 for i in range(self.get_n())] for j in range(self.get_n())])  # Identity matrix to store permutations on A's rows
        for i in range(self.get_n()):
            P[i,i] = 1


        for i in range(self.get_n() - 1):
            entries_below_pivot_cur_row = [abs(U[j, i]) for j in range(i, self.get_n())]
            max_entry = max(entries_below_pivot_cur_row)
            if max_entry == 0:
                return "Matrix is singular"

            tmp =  np.copy(U[i, :])
            U[i, :] = U[entries_below_pivot_cur_row.index(max_entry) + i, :]
            U[entries_below_pivot_cur_row.index(max_entry) + i, :] = tmp

            tmp =  np.copy(P[i, :])
            P[i, :] = P[entries_below_pivot_cur_row.index(max_entry) + i, :]
            P[entries_below_pivot_cur_row.index(max_entry) + i, :] = tmp  # swap i and j rows in P and U matrices


            scalar_values = [-U[j,i] / U[i,i] for j in range(i + 1, self.get_n())] # find multiple of row to eliminate first non zero entries below
            for j in range(i + 1, self.get_n()):

                L[j,i] = -scalar_values[j - i -1] # set the correspondent entry of L matrix
                for k in range(self.get_n()):
                  U[j, k] += scalar_values[j - i - 1] * U[i, k]  # eliminate non-zero entries below pivot entry



        for i in range(self.get_n()):
            L[i,i] = 1.0            # make all entries on L's main diagonal 1's

        return L, U, P

    def solve_equation(self, B):
        pass
    def to_string(self):
        pass



