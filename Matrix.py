class Matrix():
    def _init_(self, arr):
        pass

    def get_row_echelon_form(self, A):
        """Returns a row-echelon form of matrix A"""
        for i in range(min(len(A), len(A[0]))):
            for r in range(i, len(A)):       # for each row
                zero_row = A[r][i] == 0
                if zero_row:
                    continue
                # swap current row with first row
                A[i], A[r] = A[r], A[i]
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
    def solve_equation(self, B):
        pass
    def to_string(self):
        pass