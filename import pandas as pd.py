import pandas as pd
import random as random

db = pd.read_excel('artikeln.xlsx')
zahl= random.randint( 0, db.iloc[-1,0])
random_N=db.iloc[zahl,2]
print("was ist die Artikel von " + random_N)
input = input()
if input ==db.iloc[zahl,1]:
    print("wow du hast recht")
else:
  print("hahaha du bist dumm")    