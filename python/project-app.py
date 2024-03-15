from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# Configure MySQL connection
db_config = {
    'host': 'localhost',
    'port': 3307,
    'user': 'DB_USER',
    'password': 'insert_password',
    'database': 'wordguesses',
}

@app.route('/')
def index():
    # Connect to the database
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # Fetch words
    cursor.execute('SELECT * FROM word_guesses ORDER BY RAND() LIMIT 1')
    random_row = cursor.fetchone()

    # Close the database connection
    cursor.close()
    conn.close()

    return render_template('index.html', students=students, courses=courses)

if __name__ == '__main__':
    app.run(debug=True)
 