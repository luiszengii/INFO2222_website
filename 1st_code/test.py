import sqlite3

# conn = sqlite3.connect('user.db')
# c = conn.cursor()
# c.execute("SELECT username FROM user")
# cur_data = c.fetchall()
# for a in cur_data:
#     print(a[0])

cur_username = "an"
conn = sqlite3.connect('user.db')
c = conn.cursor()
c.execute("SELECT mute FROM user WHERE username = ?", (cur_username,))
cur_data = c.fetchone()
print(cur_data)