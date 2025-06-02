import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Carregar os dados
praticar = pd.read_csv('treino.csv')
teste = pd.read_csv('teste.csv')

# Verificar as primeiras linhas de 'praticar'
print(praticar.head())

# Separando as variáveis independentes (X) e dependente (y) para treino
X_p = praticar.drop(columns=['id', 'target'])  
y_t = praticar['target']

# Definindo o modelo de árvore de decisão
M = DecisionTreeClassifier(random_state=42)

# Treinando o modelo
M.fit(X_p, y_t)

# Preparando os dados de teste, removendo a coluna 'id'
X_teste = teste.drop(columns=['id'])

# Fazendo as previsões
y_pred = M.predict(X_teste)

# Criando um DataFrame para armazenar as previsões
result = pd.DataFrame({
    'id': teste['id'],  
    'target': y_pred   
})

# Salvando o DataFrame em um arquivo CSV
result.to_csv('predicoes.csv', index=False)

# Carregando e exibindo as previsões
predicoes = pd.read_csv('predicoes.csv')
print("Previsões:""\n", predicoes.head())
