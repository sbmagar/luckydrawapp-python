from flask import Flask
import random
import os

app = Flask(__name__)
participants_file = "participants.txt"

def load_participants():
    if not os.path.exists(participants_file):
        return []
    with open(participants_file, "r") as f:
        return f.read().splitlines()

def save_participants(participants):
    with open(participants_file, "w") as f:
        f.write("\n".join(participants))

@app.route('/')
def pick_lucky_winner():
    participants = load_participants()
    if not participants:
        return "No participants found. Please register first."

    lucky_winner = random.choice(participants)
    # lucky_winner = participants.pop()
    # save_participants(participants)

    return f'Congratulations! The lucky winner is: {lucky_winner}'

@app.route('/register/<participant>') 
def register_participant(participant):
    participants = load_participants()
    participants.append(participant)
    save_participants(participants)
    return f'{participant} has been registered as a participant.'

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
