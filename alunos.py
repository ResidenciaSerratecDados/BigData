import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1 - criação de dados
np.random.seed(42)
alunos = [f'Aluno {i+1:02d}' for i in range(50)]
disciplinas = ['Front-end', 'Back-end', 'Cibersegurança', 'Big Data', 'Java', 'Python','.NET', 'PHP', 'C#']

edados = {
    'nome_aluno': np.random.choice(alunos, size=200),
    'disciplina': np.random.choice(disciplinas, size=200),
    'nota1': np.random.randint(0, 11, size=200).round(1),
    'nota2': np.random.randint(0, 11, size=200).round(1),
    'nota3': np.random.randint(0, 11, size=200).round(1),
    'frequencia': np.random.randint(0, 101, size=200).round(1)
}
edados['media'] = ((edados['nota1'] + edados['nota2'] + edados['nota3']) / 3).round(1)
edados['situacao'] = np.where(edados['media'] >= 6, 'Aprovado', 'Reprovado')

# 2 - Criação do DataFrame
df_alunos = pd.DataFrame(edados)

# 3 - Exibição do DataFrame
print(df_alunos.head(50))

# 4 - Análise descritiva
def analise_descritiva(edados, nota):
  print(f"\n=== Análise Descritiva - {nota} ===")
  print(f"Média: {np.mean(edados):.4f}")
  print(f"Mediana: {np.median(edados):.4f}")
  print(f"Desvio Padrão: {np.std(edados):.4f}")
  print(f"Variância: {np.var(edados):.4f}")
  print(f"Valor Mínimo: {np.min(edados):.4f}")
  print(f"Valor Máximo: {np.max(edados):.4f}")

  q1, q2, q3 = np.percentile(edados, [25, 50, 75])
  iqr = q2 - q1
  limite_inferior = q1 - 1.5 * iqr
  limite_superior = q3 + 1.5 * iqr

  print("\n Medidas de Posição:")
  print(f"Q1 (25%): {q1:.4f}")
  print(f"Q2/Mediana (50%): {q2:.4f}")
  print(f"Q3 (75%): {q3:.4f}")
  print(f"IQR: {iqr:.4f}")

  print("\n Limites para Outliers:")
  print(f"Limite Inferior: {limite_inferior:.4f}")
  print(f"Limite Superior: {limite_superior:.4f}")

  outliers = [x for x in edados if x < limite_inferior or x > limite_superior]
  print(f"Outliers Detectados: {outliers}")

#aplicando análise descritiva
analise_descritiva(edados['nota1'], "Nota 1")
analise_descritiva(edados['nota2'], "Nota 2")
analise_descritiva(edados['nota3'], "Nota 3")
analise_descritiva(edados['frequencia'], "Frequência") # Also apply descriptive analysis to frequency
analise_descritiva(edados['media'], "Média") # Also apply descriptive analysis to mean

# 5 - Gráficos
#Boxplot Comparativo - retorno de quartis
plt.figure(figsize=(10, 6))
# Remove the non-numeric 'situacao' data from the boxplot input
box = plt.boxplot([edados['nota1'], edados['nota2'], edados['nota3'], edados['media']],
            # Adjust labels to match the data provided
            labels=["Nota1", "Nota2", "Nota3", "Média"],
            patch_artist=True,
            medianprops=dict(color='black'))

# Customização de cores
# Adjust colors list to match the number of boxplots
colors = ['lightgreen', 'lightblue', 'lavender', 'lightyellow']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

plt.title('Distribuição de Notas e Média', pad=20) # Update title for clarity
plt.ylabel('Valores') # Update ylabel
plt.xticks(rotation=45)
plt.xlabel('Métricas') # Update xlabel
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

#Boxplot Comparativo - retorno de quartis
plt.figure(figsize=(10, 6))
# Remove the non-numeric 'situacao' data from the boxplot input
box1 = plt.boxplot([ edados['frequencia']], # Removed edados['situacao']
            # Adjust labels to match the data provided
            labels=["Frequência"], # Adjusted labels
            patch_artist=True,
            medianprops=dict(color='black'))

# Customização de cores
# Adjust colors list to match the number of boxplots
colors = ['peachpuff'] # Adjusted colors list
for patch, color in zip(box1['boxes'], colors):
    patch.set_facecolor(color)

plt.title('Distribuição de Frequência', pad=20) # Update title for clarity
plt.ylabel('Valores') # Update ylabel
plt.xticks(rotation=45)
plt.xlabel('Métricas') # Update xlabel
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()