import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans

# Сбор и анализ данных

# Загрузка данных из CSV-файла в Pandas DataFrame
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
x = customer_data.iloc[:, [3, 4]].values
print(x)

# WCSS -> Within Clusters Sum of Squares (Сумма квадратов внутри кластеров)
wcss = []

for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans.fit(x)

    wcss.append(kmeans.inertia_)

# Построение графика локтя(elbow)
sns.set()
plt.plot(range(1, 11), wcss)
plt.title('The Elbow Point Graph')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show()

# Обучение модели кластеризации k-средних
kmeans = KMeans(n_clusters=5, init='k-means++', random_state=0)

# вернуть метку для каждой точки данных на основе их кластера
y = kmeans.fit_predict(x)

print(y)

# 5 кластеров - 0, 1, 2, 3, 4
# Визуализация всех кластеров
plt.figure(figsize=(8, 8))
plt.scatter(x[y == 0, 0], x[y == 0, 1], s=50, c='green', label='Cluster 1')
plt.scatter(x[y == 1, 0], x[y == 1, 1], s=50, c='red', label='Cluster 2')
plt.scatter(x[y == 2, 0], x[y == 2, 1], s=50, c='yellow', label='Cluster 3')
plt.scatter(x[y == 3, 0], x[y == 3, 1], s=50, c='violet', label='Cluster 4')
plt.scatter(x[y == 4, 0], x[y == 4, 1], s=50, c='blue', label='Cluster 5')

plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=100, c='cyan', label='Centroids')

plt.title('Customer Groups')
plt.xlabel('Annual Income')
plt.ylabel('Spending Score')
plt.show()
