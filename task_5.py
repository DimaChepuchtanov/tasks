text = 'We’re always thinkinG of eternity as an idea that cannot be understood, soMething immense. But why must it be? What iF, Instead of all this, you suddenly find just a little room thereX, something like a village bath-house, grimy, and spiders in every corner, and that’s all eternity is. Sometimes, you know, I can’t help FeeLing that that’s what it is.'
cyphers = {'augustus':{'A':'B','B':'C','C':'D','D':'E','E':'F','F':'G','G':'H','H':'I','I':'J','J':'K','K':'L','L':'M','M':'N','N':'O','O':'P','P':'Q','Q':'R','R':'S','S':'T','T':'U','U':'V','V':'W','W':'X','X':'Y','Y':'Z','Z':'A'},
'enigmatic':{'A':'B','B':'V','C':'G','D':'Q','E':'K','F':'M','G':'N','H':'A','I':'D','J':'Z','K':'C','L':'W','M':'S','N':'E','O':'O','P':'Y','Q':'F','R':'J','S':'X','T':'H','U':'T','V':'L','W':'P','X':'U','Y':'I','Z':'R'},
'ochre':{'A':'V','B':'R','C':'A','D':'H','E':'E','F':'W','G':'N','H':'D','I':'U','J':'O','K':'Q','L':'Y','M':'S','N':'X','O':'F','P':'I','Q':'C','R':'Z','S':'G','T':'M','U':'J','V':'K','W':'L','X':'P','Y':'B','Z':'T'},
'ascorida':{'A':'U','B':'E','C':'J','D':'O','E':'B','F':'T','G':'P','H':'Z','I':'W','J':'C','K':'N','L':'S','M':'R','N':'K','O':'D','P':'G','Q':'V','R':'M','S':'L','T':'F','U':'A','V':'Q','W':'I','X':'Y','Y':'X','Z':'H'}
}
message = 'STOPNOW'
script = []
the_cypther = 0
for i in range(2,len(text)):
  if text[i] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" and text[i-2] not in ".!?":
    if text[i] =="I" and text[i-1]==" " and text[i+1]==" ":
      pass
    else:
      script.append(text[i])

for i in cyphers:
  ints = 0
  for j in cyphers[i]:
    if j == message[ints] and cyphers[i][j]==script[ints]:
      the_cypther = i
    if ints != len(script)-1:
      ints+=1
print(script)
print(the_cypther)
