
from flask import Flask, render_template, request, session, url_for, redirect, jsonify
from forms import IUPACChecker
import iupac_checker
import pubchem_api as api

app = Flask(__name__)

difficultyList = ["easy", "medium", "hard", "insane", "random"]
correctName = ""

@app.route('/')
def home():
    return redirect(url_for('index', difficulty = 'easy'))

@app.route("/<difficulty>", methods=["GET", "POST"])
def index(difficulty):
    if difficulty in difficultyList:
        global correctName
        image, IUPAC_name = api.get_data(difficulty)
        correctName = IUPAC_name
        return render_template("test.html", image=image, iupac=IUPAC_name)
    return render_template("404.html")        

@app.route('/guess', methods = ['POST'])
def test(): 
    response = request.form.get('userGuess')
    isCorrect = iupac_checker.checker(response,correctName)
    json = {
        "isCorrect": isCorrect, 
        "correctAnswer": correctName,
        "userResponse": response  
        }
    return jsonify(json)

if __name__ == "__main__":
    app.run(debug=True)