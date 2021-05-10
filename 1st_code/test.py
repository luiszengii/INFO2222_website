import sqlite3

conn = sqlite3.connect('user.db')
c = conn.cursor()
# c.execute("INSERT INTO user(username, password, admin) VALUES (?,?,?)", ("an", 123, 1))
# c.execute("SELECT * FROM user")
# c.execute("SELECT admin,mute FROM user WHERE username = ?", ("an",))
# c.execute('CREATE TABLE discussion (username TEXT, txt char(254), category char(20), foreign key(username) references user on delete cascade)')
c.execute('select * from discussion')
# c.execute('insert into discussion(username, txt, category) VALUES (?,?,?)', ("an", "123", "web"))
# c.execute('drop table discussion')
cur_data = c.fetchone()
print(cur_data)

conn.commit()
conn.close()