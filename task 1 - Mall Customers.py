import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# from sklearn.cluster import KMeans


# Сбор и анализ данных

# 1. Загрузка данных из CSV-файла в Pandas DataFrame
customer_data = pd.read_csv(
    'C:/Users/devdi/PycharmProjects/Work_with_datasets_pandas_numpy/Datasets/Task-1 - Mall_Customers.csv')

# Первые пять строк в датафрейме
print(customer_data.head())

# Найти количество строк и столбцов
print(customer_data.shape)

# Получение некоторой информации о наборе данных
print(customer_data.info())

# Проверка пропущенных значений
print(customer_data.isnull().sum())

# Выбор столбца «Годовой доход(Annual Income)» и столбца «Оценка расходов(Spending Score)»
x = customer_data.iloc[:,[3,4]].values
print(x)
