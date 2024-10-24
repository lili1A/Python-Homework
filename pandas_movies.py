import pandas as pd

# Путь к файлу CSV
file_path = '//Users/liliiagubaeva/Library/CloudStorage/OneDrive-AsiaPacificUniversity/pamdas_movies_hw.csv'

# Чтение CSV файла
df = pd.read_csv(file_path)

# Просмотр первых строк данных
print(df.head())

# наличие пропущенных значений
print(df.isnull().sum())  # количество пропущенных значений в каждом столбце

# для заполнения колонки votes, мне кажется, что лучше использовать mean() - среднее значение по столбцу
# Заполнение пропущенных значений средним в колонке 'Votes'
df['Votes'] = df['Votes'].fillna(df['Votes'].mean())
# сохранение в таблицу
df.to_csv('//Users/liliiagubaeva/Library/CloudStorage/OneDrive-AsiaPacificUniversity/pamdas_movies_hw.csv', index=False)
print(df)
# наверное логичнее заполнить revenue с помощью mean, но я хочу заполнить Медианное значение (median)
df['Revenue (Millions)'] = df['Revenue (Millions)'].fillna(df['Revenue (Millions)'].median())
print(df)