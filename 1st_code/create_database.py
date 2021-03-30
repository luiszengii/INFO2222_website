import sqlite3
conn = sqlite3.connect('user.db') # Warning: This file is created in the current directory
conn.execute("CREATE TABLE user (username TEXT PRIMARY KEY, password TEXT, admin INTEGER DEFAULT 0, mute TEXT DEFAULT 0)")
