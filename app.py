from flask import Flask, render_template, request
import random

app = Flask(__name__)


@app.route("/")
def hello():
    return "HI, BITCHES"#lol Dzvinka wtf


@app.route("/main_page")
def new_tmpl():
    title = random.choice(['qewre','sdf', 'SADSDFG'])
    text =  "$\\left(\\begin{matrix} 1 & 2 & 3 \\\\ 4 & 5 & 6 \end{matrix}\\right)$\n"
    src = "http://www.mrwallpaper.com/wallpapers/carina-nebula-stars_tn1.jpg"
    #src = "home/dzvinka/Downloads/space-04.jpg"
    return render_template("main_page.html", title=title, text=text, source=src)



if __name__ == "__main__":
    app.run()
