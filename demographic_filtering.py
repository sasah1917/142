import pandas as pd

# crie um dataframe usando o arquivo final.csv
df = pd.read_csv('C:/Users/sarah/Desktop/Curso programação/byjus/Python/PRO_1-1_C142_AtividadeDoAluno1-main/final.csv')

# classificação de dataframe: em relação à coluna weighted_rating em ordem crescente
df = df.sort_values('weighted_rating' , ascending = False)

# dataframe final
output = df[['original_title' , 'poster_link' , 'runtime', 'release_date' , 'weighted_rating' ]].head(20)
