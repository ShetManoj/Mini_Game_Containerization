from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Choices available in the game
choices = ["rock", "paper", "scissors"]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    player_choice = request.form['choice']
    computer_choice = random.choice(choices)

    if player_choice == computer_choice:
        result = "It's a tie!"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        result = "Winner!"
    else:
        result = "You lose!"

    return render_template('result.html', player_choice=player_choice, 
                           computer_choice=computer_choice, result=result)

if __name__ == '__main__':
    app.run(debug=True) 
    

