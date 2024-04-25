from flask import Flask
from redis import Redis
import random

app = Flask(__name__)
redis = Redis(host="redis", port=6379)

@app.route('/')
def pick_lucky_winner():
    participants = redis.lrange('participants', 0, -1)
    if not participants:
        return "No participants found. Please register first."

    random.shuffle(participants)
    lucky_winner = participants.pop()
    redis.ltrim('participants', 0, -len(participants))

    return f'Congratulations! The lucky winner is: {lucky_winner.decode("utf-8")}'

@app.route('/register/<participant>') 
def register_participant(participant):
    redis.rpush('participants', participant)
    return f'{participant} has been registered as a participant.'

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
