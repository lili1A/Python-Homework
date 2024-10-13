import mysql.connector
import random

# Подключение к базе данных
try:
    print("Подключение к базе данных...")
    connection = mysql.connector.connect(
        host="localhost",  # измените на ваш хост
        user="root",  # измените на ваше имя пользователя
        password="Mersedese233",  # измените на ваш пароль
        database="People"  # измените на вашу базу данных
    )
    cursor = connection.cursor()
    print("Подключение установлено!")

    first_names = ["John", "Emily", "Michael", "Sarah", "David", "Laura"]
    last_names = ["Doe", "Smith", "Johnson", "Williams", "Brown", "Davis"]

    email_domains = ["gmail.com", "yahoo.com", "hotmail.com"]

    def generate_person():
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        email = f"{first_name.lower()}{last_name[0].upper()}@{random.choice(email_domains)}"
        
        insert_query = "INSERT INTO People (FirstName, LastName, Email) VALUES (%s, %s, %s)"
        cursor.execute(insert_query, (first_name, last_name, email))
        connection.commit()


    print("Генерация и добавление данных в таблицу People...")
    for i in range(10):
        generate_person()
        print(f"Добавлена запись {i+1}")

    print("Все данные добавлены успешно!")
    
except mysql.connector.Error as err:
    print(f"Ошибка подключения к базе данных: {err}")
    
except Exception as e:
    print(f"Произошла ошибка: {e}")

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals():
        connection.close()
    print("Подключение к базе данных закрыто.")
