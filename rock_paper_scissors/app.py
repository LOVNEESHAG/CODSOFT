import random
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/game', methods=['POST'])
def game():
    choices = ['rock', 'paper', 'scissors']
    comp = random.choice(choices)
    operation = request.form['choice']

    if operation == comp:
        result = "Tie! Both chose the same"
    elif operation == 'rock':
        if comp == 'scissors':
            result = "You win! Computer chose scissors"
        else:
            result = "You lose! Computer chose paper"
    elif operation == 'paper':
        if comp == 'rock':
            result = "You win! Computer chose rock"
        else:
            result = "You lose! Computer chose scissors"
    elif operation == 'scissors':
        if comp == 'paper':
            result = "You win! Computer chose paper"
        else:
            result = "You lose! Computer chose rock"
    else:
        result = "Invalid input"

    return render_template('index.html', operation=operation, comp=comp, result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)