# 🐍 Data Cleaning Pipeline em Python
Este projeto Python tem como objetivo realizar um roteiro de tratamento de dados utilizando bibliotecas como pandas, numpy e outras ferramentas auxiliares. O código pode ser executado no PyCharm, seguindo um pipeline passo a passo para limpar, padronizar e preparar os dados para análise ou modelagem.

## 1. 📋 Leitura e Visualização Inicial
Leitura do DataFrame via pandas e impressão de todos os registros em uma linha (string) para análise mais clara.

## 2. 🔍 Análise Estrutural
Verificação dos tipos de dados com .info()

Verificação do tamanho do DataFrame com .shape

## 3. 🧮 Estatística Descritiva
Resumo estatístico com .describe()

Análise de distribuição, média, mediana, moda, etc.

## 4. 🧱 Verificação e Tratamento de Dados Ausentes
Verificação de valores nulos com .isnull().sum()

Exclusão de registros se necessário

## 5. 🔁 Conversão de Tipos de Dados
Conversão de colunas object para datetime, int, float etc.

## 6. ✏️ Normalização de Texto
Aplicação de padrões de formatação:

lower(), strip(), replace(), etc.

## 7. 🧬 Tratamento de Dados Duplicados
Identificação com .duplicated()

Remoção com .drop_duplicates()

## 8. 🧩 Tratamento de Outliers
Uso de medidas como IQR ou Z-Score

Remoção ou imputação dos outliers

## 9. 🏗️ Criação e Ajuste de Colunas
Colunas derivadas com apply() ou operações matemáticas

Ajuste de nomes e tipos

## 10. ⚠️ Verificação de Registros Inválidos
Identificação de inconsistências (ex: datas no futuro, negativos onde não deve haver)

Correção ou remoção dos registros

## 11. 💾 Salvamento dos Dados Tratados
Exportação para .csv.
