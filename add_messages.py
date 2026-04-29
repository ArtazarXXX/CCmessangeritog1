from db import get_db_connection

con = get_db_connection()
cursor = con.cursor()

messages = [
    ('admin', 'admin', 'Добро пожаловать в чат!'),
    ('user1', 'user', 'Привет всем!'),
    ('user2', 'user', 'Как дела?'),
    ('admin', 'admin', 'Правила чата: уважайте друг друга'),
    ('user3', 'user', 'Отличный мессенджер!')
]

for username, role, message in messages:
    cursor.execute('INSERT INTO Messages (username, role, message) VALUES (?, ?, ?)', (username, role, message))

con.commit()
con.close()
print('Messages added')
