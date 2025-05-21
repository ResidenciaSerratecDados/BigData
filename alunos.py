import pandas as pd
import numpy as np

# 1 - criação de dados
np.random.seed(42)
alunos = [f'Aluno {i+1:02d}' for i in range(50)]
disciplinas = ['Front-end', 'Back-end', 'Cibersegurança', 'Big Data', 'Java', 'Python','.NET', 'PHP', 'C#']  

dados = {
    'nome_aluno': np.random.choice(alunos, size=200),
    'disciplina': np.random.choice(disciplinas, size=200),
    'nota1': np.random.randint(0, 11, size=200).round(1),
    'nota2': np.random.randint(0, 11, size=200).round(1),  
    'nota3': np.random.randint(0, 11, size=200).round(1),  
    'frequencia': np.random.randint(0, 101, size=200).round(1)
}
dados['media'] = ((dados['nota1'] + dados['nota2'] + dados['nota3']) / 3).round(1)
dados['situacao'] = np.where(dados['media'] >= 7, 'Aprovado', 'Reprovado')
dados['situacao'] = np.where(dados['frequencia'] < 75, 'Reprovado', dados['situacao'])

# 2 - Criação do DataFrame
df_alunos = pd.DataFrame(dados)

# 3 - Exibição do DataFrame
print(df_alunos.head(50))