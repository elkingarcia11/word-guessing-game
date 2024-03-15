from flask import Flask, render_template
import mysql.connector
import os
from python.utils.word_guesses_database import db_instance

app = Flask(__name__)


@app.route('/')
def index():
    random_word = db_instance.get_random_word()
    print(random_word)
    topic = random_word[1]  # topic
    hint = random_word[2]  # hint
    answer = random_word[3]  # answer
    return render_template('index.html', topic=topic, hint=hint, answer=answer)


if __name__ == '__main__':
    app.run(debug=True)
