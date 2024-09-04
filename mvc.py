""" Создайте класс Статья.
Необходимо хранить следующую информацию:
■ название статьи,
■ автор статьи,
■ количество знаков,
■ название издания или сайта,где статья была впервые опубликована, ■ краткое описание.
Создайте необходимые методы для этого класса. Реализуйте паттерн MVC для класса Статья и код для использования модели, контроллера и представления.
Реализация MVC должна просматриваться просто в наличии необходимых классов/структур/модулей в коде, не обязательно делать задание на каком-то сложном фреймворке. """

# M — модель предметной области, ядро приложения, не влияет на другие части приложения
# V — шаблон, получает данные от c, не знаеь о базе данных
# C — функция-обработчик (в других фреймворках могут быть другие сущности)
# использует m для выполнения запрашиваемых операций, генерация v

# разделение приложения на 3 слои, взаимодействуюшие друг с другом
# важно при создании модульных приложений, можно добавлять новые слои

# model - модель предметной области сущности, логика и процесс 
# contriller - получение, интерпретация, валидация информации
# создание и обновление views, запросы и изменение в model
# view - презентация
# user - клиент

# M: информация о статье, поля для характеристик, методы
# V: интерфейс для отображения информации,　получение данных пользователя, передача результата 
# C: взаимодействие с клиентом 

#  import oc  возможность взаимодействовать с операционной системой. Он содержит функции для работы с файлами и директориями, параметрами окружения, а также для других операций, связанных с операционной системой.
# import pathlib # объектно-ориентированный интерфейс для работы с путями файловой системы

# model - logic and data abt article
class Article:
    def __init__(self, title, author, char_count, publisher, describtion):
        self.title = title
        self.author = author
        self.char_count = char_count
        self.publisher = publisher 
        self.describtion = describtion
        
    def __str__(self):
        return (f"Name: {self.title} \n Title:{self.title} \n Author: {self.author} \n Characters number: {self.char_count} \n Publisher: {self.publisher} \n Describtion: {self.describtion}")
        
# view - data output in console

class ArticleView:
    def display_article(slef, article):
        print(article)
        
# controller - user input

class ArticeController: 
    def __init__(self, model, view):
        self.model = model
        self.view = view 
        
    def set_atricle_details(self, title, author, char_count, publisher, describtion):
        self.model.title = title
        self.model.author = author
        self.model.char_count = char_count
        self.model.publisher = publisher
        self.model.describtion = describtion
        
    def display_article(self):
        self.view.display_article(self.model)
        
if __name__ == "__main__":
    # instance 
    article = Article(title= "Потеря слуха",
            author= "SmartAids",
            char_count= 3210,
            publisher= "Хекслер",
            describtion= "This article is about lose of hearing and some interesting facts about it"
                      )
        # объект представления
    view = ArticleView()
    # объект контроллера 
    controller = ArticeController(article, view)
    
    # display
    controller.display_article()
      
        


