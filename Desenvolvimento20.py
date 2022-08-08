import pandas as pd

df = pd.read_csv("notas_alunos.csv")

media = (df["nota_1"] + df["nota_2"])/2
df["media"] = media

situacao = ''
df.loc[df["media"]  >= 7, "situacao"]   = "APROVADO"
df.loc[df["media"]  <  7 , "situacao"]  = "REPROVADO"
df.loc[df["faltas"] >= 5, "situacao"]   = "REPROVADO"
print(df.head(10))

maisFaltas = df["faltas"].max()
print("\nO maior número de faltas é:", maisFaltas)
mediaGeral = df["media"].median()
print("A média geral das notas dos alunos é:", mediaGeral)
maiorMedia = df["media"].max()
print("A maior média é:", maiorMedia)

df.to_csv("alunos_situacao.csv",index=False)

