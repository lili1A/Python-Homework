# labels в pandas - метки или имена строк или столбцов в dataframe/series
# dataframe: обращение к данным по имени столбца
# задание
""" Написать программу с использованием Pandas которая создаёт и выводит DataFrame при помощи Питоновского словаря, который использует labels в качестве индекса.
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19], 'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']} labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
При помощи созданного датафрейма необходимо сделать subset, состоящий только из тех студентов, которые прошли экзамен.
Заменить пустые значения в графе score, на любую, плохую, по вашему мнению, оценку. """

import pandas as pd
#students dataframe 
exam_data = {
    'Name': ['Anastasia','Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'Score': [12.5, 9, 16.5, 7, 9, 20, 14.5, 5.5, 8, 19], 
    'Attemts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'Qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes'],
    'Labels': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    }
# making a dataframe
df = pd.DataFrame(exam_data)
print(df)
# labels как индексы строк 
df = df.set_index('Labels')
print("Set of students")
print(df)

exam_pass = df[df['Qualify'] == 'yes']
print("Subset of students who passed exam:")
print(exam_pass)