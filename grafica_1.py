import numpy as np
import matplotlib.pyplot as plt

# Datos sintéticos
rng = np.random.default_rng(42)

matematicas = rng.integers(50, 100, 20)
ciencias = rng.integers(40, 95, 20)
literatura = rng.integers(60, 100, 20)

errores_matematicas = rng.uniform(2, 5, 2)
errores_matematicas = [min(errores_matematicas), max(errores_matematicas)]

errores_ciencias = rng.uniform(1, 4, 2)
errores_ciencias = [min(errores_ciencias), max(errores_ciencias)]

errores_literatura = rng.uniform(3, 6, 2)
errores_literatura = [min(errores_literatura), max(errores_literatura)]

# Gráfico de dispersión
plt.figure(figsize=(8, 6))
plt.scatter(matematicas, ciencias, label='Estudiantes')
plt.title('Relación entre Calificaciones de Matemáticas y Ciencias')
plt.xlabel('Calificaciones de Matemáticas')
plt.ylabel('Calificaciones de Ciencias')
plt.legend()
plt.grid(True)
plt.show()

# Gráfico de barras de error
materias = ['Matemáticas', 'Ciencias', 'Literatura']
calificaciones = [matematicas.mean(), ciencias.mean(), literatura.mean()]
errores = [errores_matematicas, errores_ciencias, errores_literatura]

plt.figure(figsize=(8, 6))
plt.bar(materias, calificaciones, yerr=np.transpose(errores), capsize=5, color=['blue', 'green', 'orange'])
plt.title('Calificaciones Promedio con Barras de Error')
plt.xlabel('Materias')
plt.ylabel('Calificaciones Promedio')
plt.grid(axis='y')
plt.show()

# Histograma
plt.figure(figsize=(8, 6))
plt.hist(matematicas, bins=10, color='purple', edgecolor='black')
plt.title('Distribución de Calificaciones de Matemáticas')
plt.xlabel('Calificaciones')
plt.ylabel('Frecuencia')
plt.grid(axis='y')
plt.show()
