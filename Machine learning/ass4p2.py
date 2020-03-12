import pandas as pd

data = pd.read_excel('olympicsports.xlsx')

data1 = pd.read_excel('olympicsport.xlsx')

#merged=pd.merge(data,data1)

katakutu = [data,data1]

kata = pd.concat(katakutu)

#print(merged)

print(kata)

#print(data)

#print (data1)