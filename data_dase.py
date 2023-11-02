import sqlite3
from main import *

# Устанавливаем соединение с базой данных
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

# Создаем таблицу Users
cursor.execute('''
CREATE TABLE IF NOT EXISTS LOSERS (
username TEXT NOT NULL,
password TEXT NOT NULL


)
''')

cursor.execute('INSERT INTO LOSERS (username, password) VALUES (?, ?)', ('newuser', 'asd'))

if flag == False:
    cursor.execute('INSERT INTO LOSERS (username, password) VALUES (?, ?)', (login, password))
# Сохраняем изменения и закрываем соединение
print(users)
connection.commit()
connection.close()