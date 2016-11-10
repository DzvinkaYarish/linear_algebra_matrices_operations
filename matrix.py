import numpy as np
from errors import SingularMatrixError


class Matrix:
    def __init__(self, arr):
        arr = [[float(i) for i in row] for row in arr]
        self.check_matrix(arr)
        self.A = np.matrix(arr)


    def get_row_echelon_form(self, A):
        """Returns a row-echelon form of matrix A"""
        E = np.matrix([[0.0 for i in range(self.get_n())] for j in range(self.get_n())])
        for i in range(self.get_n()):
            E[i,i] = 1.0
        U = np.copy(A)
        for i in range(min(len(U), len(U[0]))):
            for j in range(i, len(U)):       # for each row
                zero_row = U[j][i] == 0
                if zero_row:
                    continue
                # swap current row with first row
                tmp = np.copy(U[j])
                U[j] = U[i]
                U[i] = tmp

                tmp = np.copy(E[j])
                E[j] = E[i]
                E[i] = tmp


                # reduce the matrix by looking at each column
                first_row_first_col = U[i][i]

                for cur_row in range(i + 1, len(U)):
                    # divide chosen row by a chosen earlier element from first row and multiply by -1
                    scalarMultiple = -1 * U[cur_row][i] / first_row_first_col
                    for cc in range(i, len(U[0])):  # for each element in a first row

                        U[cur_row][cc] += U[i][cc] * scalarMultiple
                    E[cur_row] += E[i] * scalarMultiple

        return U, E

    def get_reduced_row_echelon_form(self, A,alreadyrow=False):
        """ Turns any square matrix into REF -> RREF
                """
        # for i in range(min(len(A), len(A[0]))):
        #     # at the end of for loop, matrix will be in row-echelon form
        #     for row in range(i, len(A)):
        #         # find the first row with a nonzero entry in first column
        #         zero_row = A[row][i] == 0  # this finds a row that begins with 0
        #         if zero_row:  # if not found yet...
        #             continue
        #         A[i], A[row] = A[row], A[i]  # swaps current row with the first row
        #         # make entries below the 1 column 0
        #         firstrow_col = A[i][i]
        #         for r in range(i + 1, len(A)):
        #             row_first = A[r][i]
        #             scalar_multiple = -1 * row_first / firstrow_col
        #             for c in range(i, len(A[0])):
        #                 A[r][c] += A[i][c] * scalar_multiple
        #         break


                # Now - to RREF
        if not alreadyrow:
            U, E = self.get_row_echelon_form(A)
        else:
            U = np.copy(A)
            E = np.matrix([[0.0 for i in range(self.get_n())] for j in range(self.get_n())])
        for i in range(self.get_n()):
            E[i,i] = 1.0
        count = 0
        #if all([all([j == 0 for j in i]) for i in A]):



        for i in range(min(len(U), len(U[0])) - 1, -1, -1):
            # divide the last non-zero row by the first non-zero entry
            first_elem_col = -1
            first_elem = -1
            for col in range(len(U[0])):
                if U[i][col] == 0:
                   # E[i, col] = E[i, col] / first_elem
                    continue
                if first_elem_col == -1:
                    first_elem_col = col
                    first_elem = U[i][col]
                U[i][col] = U[i][col] / first_elem
            E[i] = E[i] / first_elem
            # make all numbers above the main entry(=1) zero
            for r in range(i):
                row_above = U[r][first_elem_col]
                scalar_multiple = -1 * row_above
                for c in range(len(U[0])):
                    U[r][c] += (U[i][c] * scalar_multiple)
                    E[r, c] += (E[i, c] * scalar_multiple)



        return U, E

    def get_m(self):
        return self.A.shape[0]

    def get_n(self):
        return self.A.shape[1]

    def get_PLU(self):
        L = np.matrix([[0.0 for i in range(self.get_n())] for j in range(self.get_n())])
        U = np.copy(self.A)
        P = np.matrix([[0.0 for i in range(self.get_n())] for j in range(self.get_n())])  #Identity matrix to store permutations on A's rows
        for i in range(self.get_n()):
            P[i,i] = 1


        for i in range(self.get_n() - 1):
            entries_below_pivot_cur_row = [abs(U[j, i]) for j in range(i, self.get_n())]
            max_entry = max(entries_below_pivot_cur_row)
            if max_entry == 0:
                raise SingularMatrixError
            tmp =  np.copy(U[i, :])
            U[i, :] = U[entries_below_pivot_cur_row.index(max_entry) + i, :]
            U[entries_below_pivot_cur_row.index(max_entry) + i, :] = tmp

            tmp =  np.copy(P[i, :])
            P[i, :] = P[entries_below_pivot_cur_row.index(max_entry) + i, :]
            P[entries_below_pivot_cur_row.index(max_entry) + i, :] = tmp  # swap i and j rows in all P and U matrices


            scalar_values = [-U[j,i] / U[i,i] for j in range(i + 1, self.get_n())] # find multiple of row to eliminate first non zero entries below
            for j in range(i + 1, self.get_n()):

                L[j,i] = -scalar_values[j - i -1] # set the correspondent entry of L matrix
                for k in range(self.get_n()):
                    U[j, k] += scalar_values[j - i - 1] * U[i, k] # eliminate non-zero entries below pivot entry


        for i in range(self.get_n()):
            L[i,i] = 1.0            # make all entries on L's main diagonal 1's
        det = 1
        for i in range(self.get_n()):
            det *= U[i,i]
        if not det:
            raise SingularMatrixError()
        return L, U, P

    def solve_equation(self, B):
        L, U, P = self.get_PLU()
        PB = P.dot(B)

        a = self.get_reduced_row_echelon_form(L)[1]

        y = a.dot(PB)

        b = self.get_reduced_row_echelon_form(U, alreadyrow=True)[1]

        x = b.dot(y)

        return x
    def to_string(self):
        pass

    # -------------------- CHECKING MATRIX --------------------------------------------
    @staticmethod
    def __check_square__(arr):
        A = arr
        check_lst = []     # list of lengths of each row
        for row in A:
            check_lst.append(len(row))
        new_set = set(check_lst)
        if len(new_set) == 1 and check_lst[0] == len(A):
            return True
        else:
            return False

    @staticmethod
    def __check_number__(arr):
        A = arr
        for row in A:
            for i in row:
                if type(i) == float or type(i) == int:
                    continue
                else:
                    return False
        return True

    @staticmethod
    def __check_all_zeros__(arr):
        return not np.any(arr)

    def check_matrix(self, arr):
        if not self.__check_number__(arr):
            raise ValueError("Elements in this matrix must be integer or float, but they are not!")

        if not self. __check_square__(arr):
            raise IndexError("Matrix is not square!")
        if self.__check_all_zeros__(arr):
            raise SingularMatrixError()







