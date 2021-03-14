
from flask import Flask, render_template, request, session, url_for, redirect, jsonify
from forms import IUPACChecker
import iupac_checker
import pubchem_api as api
import cid_sorter as sorter

app = Flask(__name__)

difficultyList = ["easy", "medium", "hard", "insane", "random"]
correctName = ""
cid = 1

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
    elif difficulty == "DEBUG":
        global cid
        image, IUPAC_name, cid = api.get_data_DEBUG(cid)
        return render_template("test.html", image=image, iupac=IUPAC_name, cid = cid)

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

@app.route('/debug', methods = ['POST'])
def debug():
    easy = request.form.get('easy')
    medium = request.form.get('medium')
    hard = request.form.get('hard')
    insane = request.form.get('insane')

    if easy == "true":
        sorter.difficultySorter("easy")
    elif medium == "true" :
        sorter.difficultySorter("medium")
    elif hard == "true" :
        sorter.difficultySorter("hard")
    elif insane == "true" : 
        sorter.difficultySorter("insane")
    else: 
        raise Exception("Nothing true yet a button was pressed?")

    global cid
    cid += 1

    return ''

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
    
@app.route('/shutdown', methods=['GET'])
def shutdown():
    shutdown_server()
    return 'Server shutting down...'

if __name__ == "__main__":
    app.run(debug=True)