from flask import Flask, render_template, request
import random
from matrix import Matrix

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
            new_matrix = Matrix(to_list(matrix))
            return render_template('solve_equations.html', matrix=matrix, solution=to_string(new_matrix.solve_equation()))
        else:
            return render_template('solve_equations.html')
    except:
        return render_template('solve_equations.html', error_message="Impossible to find matrix inversion.")


if __name__ == "__main__":
    app.run(debug=True)
