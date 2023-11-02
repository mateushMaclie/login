import sqlite3

# Устанавливаем соединение с базой данных
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()
login=input()
# Выбираем всех пользователей
cursor.execute('SELECT * FROM LOSERS')
users = cursor.fetchall()
print (users)
counter=0
for user in users:
    for name in user:
        if name == login:
            
            flag=True
            counter+=1

if counter>=1:
    print('est')
elif counter<1:
    print('u need zaregacca')
    login=input('pishi login ')
    password=input('a teper parol ')
    cursor.execute('INSERT INTO LOSERS(username,password) VALUES(?,?)',(login,password))


connection.commit()
connection.close()