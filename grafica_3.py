import pandas as pd
import plotly.express as px

# Cargar el dataset
data = {
    'id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    'materia': ['Matemáticas', 'Historia', 'Ciencias', 'Lenguaje', 'Matemáticas', 'Historia', 'Ciencias', 'Lenguaje', 'Matemáticas', 'Historia', 'Ciencias', 'Lenguaje', 'Matemáticas', 'Historia', 'Ciencias', 'Lenguaje', 'Matemáticas', 'Historia', 'Ciencias', 'Lenguaje'],
    'nota': [80, 65, 90, 75, 95, 70, 85, 60, 78, 82, 93, 68, 73, 88, 77, 50, 92, 63, 85, 79],
    'aprobado': ['Sí', 'No', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'No', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'No', 'Sí', 'No', 'Sí', 'Sí']
}

df = pd.DataFrame(data)

# Graficar la distribución de notas con un boxplot
fig_boxplot = px.box(df, x='materia', y='nota', color='aprobado', points='all', title='Distribución de Notas', labels={'nota': 'Nota'})
fig_boxplot.update_layout(xaxis_title='Materia', yaxis_title='Nota')

# Graficar la distribución de aprobados con un pie chart
fig_piechart = px.pie(df, names='aprobado', title='Proporción de Estudiantes Aprobados y No Aprobados')

# Mostrar las gráficas
fig_boxplot.show()
fig_piechart.show()
