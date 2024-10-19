""" MongoDB - популярная NoSQL база данных, хранит данные в виде документоа, структурированный формат json, binary json,
хранит данные в динамических, гибких структурах (документы), а не в таблицах (в отличии от традиционных реляционных баз данных)
подходит для работы с большими объемами данных и высокой гибкости в структуре данных

характеристика mongoDB:
- документно-ориентированная модель: хранение данных в формате ключ-значение и группировка в коллекции
- документы в mongoDB - json-подобные структуры, могут содержать сложные данные 
пример: 
{
  "_id": ObjectId("5f50c31f1d2d2b0012d9cbd0"),
  "name": "Alice",
  "age": 30,
  "address": {
    "street": "123 Main St",
    "city": "New York"
  },
  "hobbies": ["reading", "hiking"]
}
- отсутствие схемы, schema-less, нет жесткой схемы хранения данных, данные могут иметь разную структуру
- высокая производительность и масштабируемость: поддерживается горизонтальное масштабирование - распределение
данных на несколько серверов (шардирование) для повышения производительности и доступности
- автоматическое индексирование поля _id - уникальный идентификатор каждого документа, создание доп. индексов для ускорения запроса
- поддержка встроенных запросов и агрегаций - мощный язык запросов для поиска данных, таких как групптровка и суммирование
- хранение больших объемов данных - работа с приложениями с аналитикой, большими данными, iot...
- гибкость и простота работы с данными - используется в веб приложениях, микросервисах, проектах с динамискими требованиями к данными

 mongoDB - хороший выбор для:
 - веб приложений с частыми изменениями данных
 - проекты с быстрой разработкой, гибкость данных
 - bid data apps
 - iot
 - big data
 
."""

# задание: 
# 1) Найти и вывести все фильмы, снятые Кристофером Ноланом.
# 2) Найти и вывести все фильмы выпущенные между 2000 и 2020 годами, у которых рейтинг на Rotten Tomatoes превышает 80%.
# 3) Найти и вывести все фильмы с жанром "Action", и отсортируйте их по рейтингу IMDb в убывающем порядке.
# 4) Рассчитать и вывести средний доход от всех фильмов, снятых Квентином Тарантино.
# 5) Обновите все фильмы, у которых рейтинг IMDb ниже 6.0, и добавьте пометку "С низким рейтингом" в поле "Жанры", после чего выведите весь список.
# 6) Выведите список из 5 лучших фильмов по кассовым сборам по всему миру. 7) Найдите фильмы, в актерском составе которых есть как Леонардо Ди Каприо, так и Брэд Питт.

from pymongo import MongoClient
from bson import ObjectId

# connecting to the local database MongoDB
client = MongoClient("mongodb://localhost:27017/")

db = client["movieDB"]

movie_collection = db["movies"]

movies = [
    {
        "_id": ObjectId(), 
        "title": "Inception", 
        "director": "Christopher Nolan", 
        "year": 2010, 
        "genres": ["Sci-Fi", "Thriller"], 
        "ratings": {
            "imdb": 8.8, 
            "rottenTomatoes": 87
        }, 
        "cast": [
            {"actor": "Leonardo DiCaprio", "role": "Dom Cobb"}, 
            {"actor": "Joseph Gordon-Levitt", "role": "Arthur"}
        ], 
        "boxOffice": {
            "budget": 160000000, 
            "grossWorldwide": 829895144
        }
    },
    {
        "_id": ObjectId(), 
        "title": "The Dark Knight", 
        "director": "Christopher Nolan", 
        "year": 2008, 
        "genres": ["Action", "Crime"], 
        "ratings": {
            "imdb": 9.0, 
            "rottenTomatoes": 94
        }, 
        "cast": [
            {"actor": "Christian Bale", "role": "Bruce Wayne / Batman"}, 
            {"actor": "Heath Ledger", "role": "Joker"}
        ], 
        "boxOffice": {
            "budget": 185000000, 
            "grossWorldwide": 1004558444
        }
    },
    {
        "_id": ObjectId(), 
        "title": "Forrest Gump", 
        "director": "Robert Zemeckis", 
        "year": 1994, 
        "genres": ["Drama", "Romance"], 
        "ratings": {
            "imdb": 8.8, 
            "rottenTomatoes": 70
        }, 
        "cast": [
            {"actor": "Tom Hanks", "role": "Forrest Gump"}, 
            {"actor": "Robin Wright", "role": "Jenny Curran"}
        ], 
        "boxOffice": {
            "budget": 55000000, 
            "grossWorldwide": 678200000
        }
    },
    {
        "_id": ObjectId(), 
        "title": "Pulp Fiction", 
        "director": "Quentin Tarantino", 
        "year": 1994, 
        "genres": ["Crime", "Drama"], 
        "ratings": {
            "imdb": 8.9, 
            "rottenTomatoes": 92
        }, 
        "cast": [
            {"actor": "John Travolta", "role": "Vincent Vega"}, 
            {"actor": "Samuel L. Jackson", "role": "Jules Winnfield"}
        ], 
        "boxOffice": {
            "budget": 8000000, 
            "grossWorldwide": 213928762
        }
    },
    {
        "_id": ObjectId(), 
        "title": "Fight Club", 
        "director": "David Fincher", 
        "year": 1999, 
        "genres": ["Drama"], 
        "ratings": {
            "imdb": 8.8, 
            "rottenTomatoes": 79
        }, 
        "cast": [
            {"actor": "Brad Pitt", "role": "Tyler Durden"}, 
            {"actor": "Edward Norton", "role": "The Narrator"}
        ], 
        "boxOffice": {
            "budget": 63000000, 
            "grossWorldwide": 101209702
        }
    },
    {
        "_id": ObjectId(), 
        "title": "The Godfather", 
        "director": "Francis Ford Coppola", 
        "year": 1972, 
        "genres": ["Crime", "Drama"], 
        "ratings": {
            "imdb": 9.2, 
            "rottenTomatoes": 97
        }, 
        "cast": [
            {"actor": "Marlon Brando", "role": "Don Vito Corleone"}, 
            {"actor": "Al Pacino", "role": "Michael Corleone"}
        ], 
        "boxOffice": {
            "budget": 6000000, 
            "grossWorldwide": 246120974
        }
    },
    {
        "_id": ObjectId(), 
        "title": "Interstellar", 
        "director": "Christopher Nolan", 
        "year": 2014, 
        "genres": ["Adventure", "Drama"], 
        "ratings": {
            "imdb": 8.6, 
            "rottenTomatoes": 72
        }, 
        "cast": [
            {"actor": "Matthew McConaughey", "role": "Cooper"}, 
            {"actor": "Anne Hathaway", "role": "Brand"}
        ], 
        "boxOffice": {
            "budget": 165000000, 
            "grossWorldwide": 677471339
        }
    }
]

movie_collection.insert_many(movies)

print("Данные успешно добавлены!")

# проверка
all_movies = movie_collection.find()
for movie in all_movies:
    print(movie)

# запросы
print("check is done")
# 1) Найти и вывести все фильмы, снятые Кристофером Ноланом

nolan_movies =movie_collection.find({"director": "Christopher Nolan"})
for movie in nolan_movies:
    print(f"Фильмы, снятые Кристофером Ноланом: {movie}")
    
# 2) Найти и вывести все фильмы, выпущенные между 2000 и 2020 годами, у которых рейтинг на Rotten Tomatoes превышает 80%

#　В MongoDB операторы $gte и $lte используются для выполнения сравнений в запросах. Эти операторы позволяют фильтровать документы на основе значений полей
# $gte (greater than or equal, больше или равно)
# $lte (less than or equal, меньше или равно)
movies_between_200_2020 = movie_collection.find({
    "year": {"$gte": 2000, "$lte": 2020},
    "ratings.rottenTomatoes": {"$gt": 80}
})
for movie in movies_between_200_2020:
    print(f"Фильмы, выпущенные между 2000 и 2020 годами, с рейтингом больше 80% на Rotten Tomatoes {movie}")
    
# 3) Найти и вывести все фильмы с жанром "Action", отсортированные по рейтингу IMDb в убывающем порядке
action_movies = movie_collection.find({"genres": "Action"}).sort("ratings.imdb", -1)
for movies in action_movies:
    print(f"Экшн фильмы, отсортированные по рейтингу IMDB в убывающем порядке {movie}")
    
# 4) Рассчитать и вывести средний доход от всех фильмов, снятых Квентином Тарантино
# возвращение только поля grossWorldwide из поддокумента boxOffice
tarantino_movies = movie_collection.find({"director": "Quentin Tarantino"}, {"boxOffice.grossWorldwide": 1})
total_gross = 0 # накопление общего дохода от фильмов
count = 0 # количество фильмов
for movie in tarantino_movies:
    total_gross += movie["boxOffice"]["grossWorldwide"] # добавляется доход
    count += 1 # добавляется количество фильмов
if count > 0:
    average_gross = total_gross / count
    print(f"Средний доход от фильмов Тарантино: {average_gross}")
    
# 5) Обновить все фильмы с рейтингом IMDb ниже 6.0, добавив "С низким рейтингом" в поле "Жанры"

movie_collection.update_many(
    {"rating.imdb": {"$lt": 6.0}},
    {"$addToSet": {"genres": "С низким рейтингом"}}
)
all_movies = movie_collection.find()
for movie in all_movies:
    print(movie)

# 6) Вывести список из 5 лучших фильмов по кассовым сборам по всему миру

top_5_grossing_movies = movie_collection.find().sort("boxOffice.grossWorldwide", -1).limit(5)
for movie in top_5_grossing_movies:
    print(f"5 лучших фильмов по кассовым сборам по всему миру: {movie}")
    
# 7) Найти фильмы, в актерском составе которых есть как Леонардо Ди Каприо, так и Брэд Питт


# Поиск фильмов с Леонардо Ди Каприо
leo_movies = movie_collection.find({"cast.actor": "Leonardo DiCaprio"})
print("Фильмы с Леонардо Ди Каприо:")
for movie in leo_movies:
    print(movie)

# Поиск фильмов с Брэдом Питтом
brad_movies = movie_collection.find({"cast.actor": "Brad Pitt"})
print("\nФильмы с Брэдом Питтом:")
for movie in brad_movies:
    print(movie)

# Поиск фильмов с обоими актерами
leo_brad_movies = list(movie_collection.find({
    "cast.actor": {"$all": ["Leonardo DiCaprio", "Brad Pitt"]}
}))

# Проверка, есть ли фильмы с обоими актерами
if leo_brad_movies:
    print("\nФильмы с Леонардо Ди Каприо и Брэдом Питтом:")
    for movie in leo_brad_movies:
        print(movie)
else:
    print("\nФильмов с Леонардо Ди Каприо и Брэдом Питтом не найдено.")

