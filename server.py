
from flask import Flask, render_template, request, session, url_for, redirect
from forms import IUPACChecker
import iupac_checker
import pubchem_api as api

app = Flask(__name__)

difficultyList = ["easy", "medium", "hard", "insane", "random"]

@app.route('/')
def home():
    return redirect(url_for('index', difficulty = 'easy'))

@app.route("/<difficulty>", methods=["GET", "POST"])
def index(difficulty):
    if difficulty in difficultyList:
        image, IUPAC_name = api.get_data(difficulty)
        guess = IUPACChecker(request.form)
        if request.method == "POST":
            iupac_checker.checker(guess.data["guess"], IUPAC_name)
        return render_template("test.html", image=image, iupac=IUPAC_name, form=guess)
    return render_template("404.html")        

if __name__ == "__main__":
    app.run(debug=True)
