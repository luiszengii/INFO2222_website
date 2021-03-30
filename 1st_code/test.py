import sqlite3

conn = sqlite3.connect('user.db')
c = conn.cursor()
# c.execute("INSERT INTO user(username, password, admin) VALUES (?,?,?)", ("an", 123, 1))
# c.execute("SELECT * FROM user")
c.execute("SELECT admin,mute FROM user WHERE username = ?", ("an",))
cur_data = c.fetchone()

print(cur_data)