import pandas as pd

# data = {
#     'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
#     'gender': ['female', 'male', 'male', 'male', 'female'],
#     'department': ['HR', 'Engineering', 'Marketing', 'Engineering', 'HR']
# }
# df = pd.DataFrame(data)
# df['gender'] = df['gender'].astype('category')
# df['department'] = df['department'].astype('category')
# print(df['department'].cat.categories)
# df['department'] = df['department'].cat.add_categories(['Finance'])
# print(df['department'].cat.categories)
# print(df)

import pandas as pd
import random

students = ['Алексей', 'Мария', 'Иван', 'Ольга', 'Дмитрий', 'Елена', 'Сергей', 'Наталья', 'Андрей', 'Анна']
subjects = ['Математика', 'Физика', 'Химия', 'История', 'Литература']
grades = {subject: [random.randint(2, 5) for _ in range(10)] for subject in subjects}
df = pd.DataFrame(grades, index=students)

mean_grades = df.mean()
print("Средняя оценка:")
print(mean_grades)
print()

median_grades = df.median()
print("Медианная оценка:")
print(median_grades)
print()

Q1_math = df['Математика'].quantile(0.25)
Q3_math = df['Математика'].quantile(0.75)
print(f"Q1 для оценок по математике: {Q1_math}")
print(f"Q3 для оценок по математике: {Q3_math}")

IQR_math = Q3_math - Q1_math
print(f"IQR по математике: {IQR_math}")
print()

std_deviation = df.std()
print("Стандартное отклонение:")
print(std_deviation)
