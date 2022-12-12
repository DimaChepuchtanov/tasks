Harry_Potter = '''
text: Mr and Mrs Dursley, of number four,
Privet Drive, were proud to say that they were perfectly normal, thank you very much.;
author: Author HP;
date of publication: 1345
'''
Faust = '''
text: Habe nun, ach! Philosophie,
Juristerei und Medizin.;
author: Author F;
date of publication: 1567
'''
Le_Petit_Prince = '''
text: La preuve que le petit prince a existé c'est qu'il était ravissant,
et qu'il voulait un mouton.;
author: Author LPP;
date of publication: 1435
'''
authors_and_works = {'Author One': {'book 1.1': [1987, '4,7']},
'Author Two': {'book 2.1': [1233, '0'], 'book 2.2': [1432, '4,4']},
'Author Three': {'book 3.1': [1234, '4,2'], 'book 3.2': [1999, '3,7']}}
import re
texts_words = []
book_authors = []
book_years = []
just = {}

titel = [Harry_Potter,Faust,Le_Petit_Prince] # Необходим для обходчика
for i in range(len(titel)):
  text = re.split("\ntext: |\nauthor: |\ndate of publication: ",titel[i])
  itme = re.split(", |; | ",text[1])
  just[len(itme)]={"author":text[2],"date":text[3]}
f = sorted(just.items(),reverse=True)
for i in f:
  texts_words.append(i[0])
  book_authors.append(i[1]["author"].replace(";",""))
  book_years.append(i[1]["date"].replace("\n",""))
  just = {}
  for i in authors_and_works:
    numbers = []
    for d in authors_and_works[i]:
      s = authors_and_works[i][d][1]
      ger = ""
      for sf in s:
        if sf == ",":
          ger+="."
        else:
          ger+=sf
          s = float(ger)
          numbers.append(s)
  just[i] = numbers

print(max(just,key=just.get))
print(texts_words)
print(book_authors)
print(book_years)
