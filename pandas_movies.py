import pandas as pd

# Путь к файлу CSV
file_path = '//Users/liliiagubaeva/Library/CloudStorage/OneDrive-AsiaPacificUniversity/pamdas_movies_hw.csv'

# Чтение CSV файла
df = pd.read_csv(file_path)

# Просмотр первых строк данных
print(df.head())