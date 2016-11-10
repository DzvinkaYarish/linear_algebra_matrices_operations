from flask import Flask, render_template, request
import random
from matrix import Matrix
from errors import SingularMatrixError
import numpy as np

app = Flask(__name__)

def to_list(m):
    matrix = [[float(j) for j in i.split(" ")]for i in m.split("\n")]
    return matrix

def to_string(m):
    matrix = [" ".join(i)+"\n" for i in m]
    print(matrix)
    return matrix

@app.route('/', methods=["GET", "POST"])
def get_index():
    try:
        if request.method == "POST":
            matrix = request.form['matrix']
            b = request.form['vB']
            print(matrix)
            print(b)
            new_matrix = Matrix(to_list(matrix))
            b = np.matrix([[float(i)] for i in b.split("\n")])
            solution = new_matrix.solve_equation(b)
            print(solution)
            return render_template('solve_equations.html', matrix=matrix, solution=to_string(solution))
        else:
            return render_template('solve_equations.html')
    except ValueError:
        return render_template('solve_equations.html', error_message="Wrong format.")
    except SingularMatrixError:
         return render_template('solve_equations.html', error_message="Not singular.")
    except IndexError:
        return render_template('solve_equations.html', error_message="Not square.")




if __name__ == "__main__":
    app.run(debug=True)
