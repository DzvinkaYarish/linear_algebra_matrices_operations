from flask import Flask, render_template, request
from matrix import Matrix
from errors import  SingularMatrixError
import numpy as np


process_matrix = Flask(__name__)


def str_to_arr(str_mat):
    arr = [[entry for entry in line.split()] for line in str_mat.split('\n')]
    return np.array(arr)

def arr_to_tex_matrix(arr):
     str_solution = '$\\left(\\begin{matrix}\n'
     for entry in arr:
         str_solution += str(entry) + "\\\\"
     str_solution += '\\end{matrix}\\right)$\n'
     return str_solution



@process_matrix.route("/solve_equations", methods = ["GET", "POST"])
def process_template():
    if request.method == "POST":
       arr = str_to_arr(request.form["matrix"])
       try:
           RHS = [[i] for i in arr[:, -1]]
           matrix = Matrix(arr[:,:-1,:])
           print(matrix)


       except ValueError as err:
           return render_template("/solve_equations.html", message= "Wrong matrix format.")
       except SingularMatrixError:
           return render_template("/solve_equations.html", message= "Matrix couldn't contain all zeros.")


       try:
           solution = matrix.solve_equation(RHS)
       except SingularMatrixError:
           return render_template("/solve_equation.html", message= "Matrix is singular.")

       return render_template("/solve_equations.html", solution= arr_to_tex_matrix(solution), matrix=matrix)
    else:
        return render_template("/solve_equations.html")


if __name__ == "__main__":
    process_matrix.run()




