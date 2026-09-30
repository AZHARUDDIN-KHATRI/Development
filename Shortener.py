import sqlite3
import string
import random
from flask import Flask, request, redirect, jsonify

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('urls.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS url_map (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            long_url TEXT NOT NULL,
            short_code TEXT UNIQUE NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def generate_short_code():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(6))

@app.route('/shorten', methods=['POST'])
def shorten_url():
    data = request.get_json()
    long_url = data.get('url')
    if not long_url:
        return jsonify({"error": "URL is required"}), 400

    short_code = generate_short_code()
    
    conn = sqlite3.connect('urls.db')
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO url_map (long_url, short_code) VALUES (?, ?)', (long_url, short_code))
        conn.commit()
    except sqlite3.IntegrityError:
        short_code = generate_short_code() # Retry once if collision occurs
        cursor.execute('INSERT INTO url_map (long_url, short_code) VALUES (?, ?)', (long_url, short_code))
        conn.commit()
    finally:
        conn.close()

    return jsonify({"short_url": f"http://localhost:5000/{short_code}"}), 201

@app.route('/<short_code>', methods=['GET'])
def redirect_to_url(short_code):
    conn = sqlite3.connect('urls.db')
    cursor = conn.cursor()
    cursor.execute('SELECT long_url FROM url_map WHERE short_code = ?', (short_code,))
    row = cursor.fetchone()
    conn.close()
    
    if row:
        return redirect(row[0])
    return jsonify({"error": "URL not found"}), 404

if __name__ == '__main__':
    init_db()
    app.run(debug=True)