import sqlite3

def create_table():
    conn = sqlite3.connect('flashcards.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS flashcards
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, word TEXT, meaning TEXT)''')
    conn.commit()
    conn.close()

def add_flashcard(word, meaning):
    conn = sqlite3.connect('flashcards.db')
    c = conn.cursor()
    c.execute("INSERT INTO flashcards (word, meaning) VALUES (?, ?)", (word, meaning))
    conn.commit()
    conn.close()

def get_flashcards():
    conn = sqlite3.connect('flashcards.db')
    c = conn.cursor()
    c.execute("SELECT * FROM flashcards")
    flashcards = c.fetchall()
    conn.close()
    return flashcards

def update_flashcard(id, word, meaning):
    conn = sqlite3.connect('flashcards.db')
    c = conn.cursor()
    c.execute("UPDATE flashcards SET word = ?, meaning = ? WHERE id = ?", (word, meaning, id))
    conn.commit()
    conn.close()
