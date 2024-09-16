import pandas as pd
import random

#Создаем DataFrame с учениками и оценками
data = {'Ученик': ['Андрей', 'Виктор', 'Светлана', 'Татьяна', 'Михаил', 'Оксана', 'Дмитрий', 'Мария', 'Полина', 'Кирилл'],
        'Русский язык': [4, 5, 4, 3, 5, 4, 5, 4, 5, 4],
        'Литература': [5, 4, 4, 4, 4, 5, 4, 5, 4, 4],
        'История': [5, 4, 4, 4, 4, 5, 4, 6, 5, 4],
        'Физика': [4, 5, 4, 3, 5, 4, 5, 4, 5, 4],
        'Математика': [5, 4, 4, 3, 5, 4, 5, 4, 5, 4]}
df = pd.DataFrame(data)
print(df)

students = ['Алексей', 'Мария', 'Иван', 'Ольга', 'Дмитрий', 'Елена', 'Сергей', 'Наталья', 'Андрей', 'Анна']
subjects = ['Математика', 'Физика', 'Химия', 'История', 'Литература']
grades = {subject: [random.randint(2, 5) for _ in range(10)] for subject in subjects}
df = pd.DataFrame(grades, index=students)
print(df)
#
#
# # Вычисляем средние оценки по каждому предмету
# avg_grades = df.mean()
# print("Средняя оценка по предметам:")
# print(avg_grades)
#
# # Вычисляем медианные оценки по каждому предмету
# median_grades = df.median()
# print("\nМедианная оценка по предметам:")
# print(median_grades)
#
# # Вычисление квартилей для оценок по математике
# q1_math = df['Математика'].quantile(0.25)
# q3_math = df['Математика'].quantile(0.75)
# iqr_math = q3_math - q1_math
# std_dev_math = df['Математика'].std()
#
# print("\nКвартили для оценок по математике:")
# print("Q1_math: ", q1_math)
# print("Q3_math: ", q3_math)
# print("IQR: ", iqr_math)
# print("Стандартное отклонение: ", std_dev_math)
#
# # Вычисление стандартного отклонения для всех предметов
# std_deviations = df.std()
# print("\nСтандартные отклонения по всем предметам:")
# print(std_deviations)