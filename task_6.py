import pandas

df = pandas.read_csv("https://raw.githubusercontent.com/ksegorov/python_homework/main/var2/df.csv ")

df_two = pandas.read_csv("https://raw.githubusercontent.com/ksegorov/python_homework/main/var2/grades.csv")

print(df)
df_new = pandas.merge(df,df_two)


indexs = []
for index, row in df_new.iterrows ():
  for i in row:
    if i == "Nan" or i == "-":
      if index not in indexs:
        indexs.append(index)

df_new.drop(labels = indexs,axis = 0,inplace=True)
df_new.reset_index(drop=True,inplace=True)


df_new = df_new[df_new["is_Commercial"] == "No"]
df_new[['Student_ID', 'Grade']] = df_new[['Student_ID', 'Grade']].astype(int)


df_news = df_new.sort_values(by='Student_ID', ascending=False)
df_news.reset_index(drop=True,inplace=True)

value = df_news.loc[1, 'Grade']
print(df_new)
print(value)
