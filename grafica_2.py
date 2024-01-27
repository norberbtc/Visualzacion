import pandas as pd
import matplotlib.pyplot as plt

# Cargar el dataset
data = {
    'id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    'materia': ['Matemáticas', 'Historia', 'Ciencias', 'Lenguaje', 'Matemáticas', 'Historia', 'Ciencias', 'Lenguaje', 'Matemáticas', 'Historia', 'Ciencias', 'Lenguaje', 'Matemáticas', 'Historia', 'Ciencias', 'Lenguaje', 'Matemáticas', 'Historia', 'Ciencias', 'Lenguaje'],
    'nota': [80, 65, 90, 75, 95, 70, 85, 60, 78, 82, 93, 68, 73, 88, 77, 50, 92, 63, 85, 79],
    'aprobado': ['Sí', 'No', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'No', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'No', 'Sí', 'No', 'Sí', 'Sí']
}

df = pd.DataFrame(data)

# Graficar la distribución de notas con un boxplot
plt.figure(figsize=(8, 6))
plt.boxplot(df['nota'])
plt.title('Distribución de Notas')
plt.xlabel('Materia')

plt.ylabel('Nota')
plt.show()

# Graficar la distribución de aprobados con un pie chart
aprobados = df['aprobado'].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(aprobados, labels=aprobados.index, autopct='%1.1f%%', startangle=90, colors=['green', 'red'])
plt.title('Proporción de Estudiantes Aprobados y No Aprobados')
plt.show()
