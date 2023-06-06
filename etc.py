import pandas as pd

# Открытие файла Excel
# excel_file = pd.read_excel('C:/excel/test.xlsx')
# # Обработка данных из файла
# # Вы можете использовать стандартные методы pandas, такие как head() и tail(),
# # для просмотра данных:
# excel_file.head()
# excel_file.tail()
df = pd.read_excel('C:/excel/test.xlsx', usecols=[0,1,7])
print(df)
lst = []
for i in df.values.tolist():
    lst.extend(i)
    for a in i:
        print([a])
