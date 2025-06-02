## 1 - COLETA DE DADOS

# 1.1 - Importar a Biblioteca
import pandas as pd
from scipy import stats

# 1.2 - Ler o arquivo
df = pd.read_csv('clientes2.csv')

## 2 - ANÁLISE EXPLORATÓRIA DOS DADOS

# 2.1 - Verificar os registros e aparecer toda a informação na mesma linha (string).
print(df.head().to_string()) # primeiros registros

print(df.tail().to_string()) # últimos registros

# 2.2 - Verificar os tamanhos e tipos
print('\nTotal de Linha e Colunas: ', df.shape) # linhas e colunas

print('\nTipagem: \n', df.dtypes) # tipos de dados

print(df.info()) #Visão geral dos dados

# 2.3 - Checar valores nulos
print('\nValores nulos: \n', df.isnull().sum()) #total de nulos por coluna.
print('\nTotal de valores nulos: ', df.isnull().sum().sum() ) #Mostra o total geral de valores nulos

# 2.4 - Estatística Descritiva:
print('\nEstatistica do df: \n', df.describe()) #Valores de média, mediana, desvio padrão e quartis
print('\nFrequência de valores: \n', df['estado'].value_counts()) #Frequência de cada valor da coluna

## 3 - LIMPEZA DOS DADOS

# 3.1 - Verificar e Tratar Valores Ausentes
  # Axis = 1-coluna, 0-linha
  # Inplace = True --> Modifica o objeto original (df), sem precisar atribuir o resultado a uma nova variável.
df.drop('pais', axis=1, inplace=True) # remove a coluna pais do df
df.drop(2, axis=0, inplace=True) #remova a linha de índice 2 do df

# 3.2 - Converter tipos de dados
df['idade'] = df['idade'].astype(int) #converter para número inteiro

df['data_corrigida'] = pd.to_datetime(df['data'], format='%d/%m/%Y', errors='coerce') #Converter texto para formato de data.

print('Tipagem',df.dtypes)

# 3.3 - Normalizar os campos de texto (definir um padrão para todos)
df['nome'] = df['nome'].str.title() # str.title - primeira letra maiúscula
df['endereco'] = df['endereco'].str.lower() # lower- letra minuscula para tudo
df['estado'] = df['estado'].str.upper() #upper- tudo maiúscula

# 3.4 - Tratar dados duplicados
print('Qtd registros atual:', df.shape[0]) #0 - linhas
df.drop_duplicates() # remover as linhas duplicadas
df.drop_duplicates(subset='cpf', inplace=True) # selecionar um coluna específica
print('Qtd de registros removendo as duplicadas:', len(df)) # len também mostra o número de linhas

# 3.5 - Tratar valores nulos(ausentes)
# Possui diferentes forma de tratar os valores nulos, tratar segundo a demanda.

print('Valores nulos: \n', df.isnull().sum()) # Mostra os valores por coluna
print('Qtd total de valores nulos: ', df.isnull().sum().sum()) #Mostra o total geral de valores nulos

df_dropna =df.dropna() # Remover valores nulos
print('Qtd total de registros nulas com dropna: ', df_dropna.isnull().sum().sum())
#ou
df_dropna4 =df.dropna(thresh=4) # Exige pelo menos 4 valores não nulos para manter a linha.
print('Qtd total de registros nulas com dropna4:', df_dropna4.isnull().sum().sum())
#ou
df = df.dropna(subset=['cpf']) # Remover registro com CPF nulo.
print('Qtd total de registros nulos contendo CPF: ', df.isnull().sum().sum() )

df_fillna = df.fillna(0) # Substituir valores nulos por 0
print('Qtd total de registros nulas com fillna: ', df_fillna.isnull().sum().sum())
#ou
df.fillna({'estado': 'Desconhecido'}, inplace=True) #Substitui os valores nulos na coluna 'estado' por 'Desconhecido'.
#ou
df['endereco'] = df['endereco'].fillna('Endereço não informado') #Preenche os valores nulos apenas na coluna 'endereco' com 'Endereço não informado'.
#ou
df['idade_corrigida'] = df['idade'].fillna(df['idade'].mean()) # Substitui os valores nulos pela média (mean) das idades.

# 3.6 - Tratar Outliers

# Visualizar outliers com Z-score (desvio padrão)
z_scores  = stats.zscore(df['idade'])
outliers_z = df[z_scores >=2]
print('Outliers pelo Z-score:\n', outliers_z)

# Visualizar outliers com IQR
Q1 = df['idade'].quantile(0.25)
Q3 = df['idade'].quantile(0.75)
IQR = Q3 - Q1

limite_baixo = Q1 - 1.5 * IQR # 1.5 é o número padrão utilizado na estatistica
limite_alto = Q3 + 1.5 * IQR
# pode definir números para os limites também : limite_baixo = 1 e limite_alto = 100

print('Limites IQR: ', limite_alto, limite_baixo)

df = df[(df['idade']>= limite_baixo) & (df['idade']<= limite_alto)]
print('Limites IQR: \n', df)

# 3.7 - Criar ou Ajustar Colunas

df['ano'] = df['data_corrigida'].dt.year #Criar coluna a partir de outra coluna
df['faixa etaria'] = pd.cut(df['idade'], bins=[0,18,60,100], labels=['jovem', 'adulto', 'idoso']) #criar coluna com faixas

# 3.8 - Mascarar dados pessoais
df['cpf'] = df['cpf'].apply(lambda cpf: f'{cpf[:3]}.***.***-{cpf[-2:]}')

print(df.head().to_string())

# 3.8 - Verificar registros inválidos

df['endereco'] = df ['endereco'].apply(lambda x:'Endereço inválido' if len(x.split('\n')) < 3 else x) #split é dividir por cada /
print('Qte de registros com endereço inválido: ', (df['endereco'] == 'Endereço inválido').sum())

df['nome'] = df['nome'].apply(lambda x:'Nome inválido' if isinstance(x,str) and len(x)> 50 else x) # isinstance: verifica se o valor x é um texto
print('Qte de registros com nome inválido: ', (df['nome'] == 'nome inválido').sum())

# 3.8 - Salvar Df
df.to_csv('clientes_limpeza.csv', index=False)
