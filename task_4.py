heroes = {"Yui Kodai":["5$", 30, 25, 38, 31],
"Izuku Midoriya":["15$", 45, 40, 50, 42],
"Momo Yaoyorozu":["20$", 44, 42, 46, 39],
"Toshinori Yagi":["35$", 60, 59, 57, 63],
"Katsuki Bakugo":["30$", 50, 52, 54, 56],
"Tenya Ida":["20$", 60, 62, 64, 60],
"Anan Kurose":["30$", 40, 45, 42, 38],
"Tetsutetsu Tetsutetsu":["10$", 55, 55, 51, 45],
"Shoto Todoroki":["25$", 48, 50, 47, 52],
"Eijiro Kirishima":["15$", 42, 40, 45, 45],
"Yuga Aoyama":["15$", 25, 28, 20, 22],
"Shota Aizawa":["28$", 50, 51, 49, 50],
"Hizashi Yamada":["35$", 29, 28, 30, 31],
"Tsuyu Asui":["20$", 45, 44, 48, 46],
"Mashirao Ojiro":["17$", 32, 35, 38, 40],
"Ochaco Uraraka":["19$", 39, 35, 37, 40],
"Denki Kaminari":["15$", 30, 28, 25, 35],
"Fumikage Tokoyami":["20$", 34, 40, 40, 45],
"Mina Ashido":["21$", 35, 35, 32, 36],
"Emi Fukukado":["30$", 55, 56, 50, 55]}
staff = [' Aizawa ', ' Fukukado', 'Kur+ose', 'Yagi_', 'Yam ada']
intern = ['Aoyama ', 'Ashido0', 'As?ui', 'Ba!kugo', 'Ida5', 'Kam_inari', 'Kirishima', 'Kod_ai', 'Midoriya1', 'Ojiro', 'Tetsutetsu', 'Todoroki%', 'Tokoyami', 'Ur@araka', 'Yao3yorozu']
minimum_hours = (180, 125)
wagest = {}

free_mass = []
free_mass_2 = []
for i in staff:
  name = ""
  for j in i:
    if j not in "+-_!><?/\,.1234567890%$#@%^&*()№'":
      name+=j
  free_mass.append(name)
staff = free_mass

for i in intern:
  name = ""
  for j in i:
    if j not in "+-_!><?/\,.1234567890%$#@%^&*()№'":
      name+=j
  free_mass_2.append(name)
intern = free_mass_2

for i in heroes:
  pdrop = i.split(" ")
  count = 0
  price = ""
  if pdrop[1] in intern:
    price = heroes[i][0]
    count = heroes[i][1]+heroes[i][2]+heroes[i][3]+heroes[i][4]
    price_new = ""
    if count >= minimum_hours[1]:
      for proce in price:
        if proce != "$":
          price_new += proce
          price = int(price_new)
          price = round(price + (price*0.15))
          wagest[i] = [str(price)+"$",str(price*count)+"$",str(price*count)+"$"]
    else:
       for proce in price:
        if proce != "$":
              price_new += proce
              price = int(price_new)
              wagest[i] = ["standard not met, " +str(price)+"$",str(price*count)+"$"]
  else:
    price = heroes[i][0]
    count = heroes[i][1]+heroes[i][2]+heroes[i][3]+heroes[i][4]
    price_new = ""
    if count >= minimum_hours[0]:
      for proce in price:
        if proce != "$":
          price_new += proce
          price = int(price_new)
          price = round(price + (price*0.35))
          wagest[i] = [str(price)+"$",str(price*count)+"$",str(price*count)+"$"]
    else:
      for proce in price:
        if proce != "$":
          price_new += proce
          price = int(price_new)
          wagest[i] = ["standard not met, " +str(price)+"$",str(price*count)+"$"]
from pprint import pprint
pprint(wagest)
