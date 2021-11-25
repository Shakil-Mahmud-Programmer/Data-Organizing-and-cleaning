import pandas as pd

#first dataset

df=pd.read_excel('Data/data.xlsx')
profit=list()
price=list()
meter=list()
city=list()

i=0

while i< len(df['profit']):
    profit.append(df['profit'].loc[i])
    i=i+1
    price.append(df['profit'].loc[i])
    i=i+1
    meter.append(df['profit'].loc[i])
    i=i+1
    city.append(df['profit'].loc[i])
    i=i+1

data=pd.DataFrame({'profit':profit ,'price in million': price ,'square meter': meter ,'city': city })

loc=0
for i in data.duplicated().values:
    if i==True:
        print(loc)
    loc=loc+1

loc=0
for i in data.isnull().values:
    for j in i:
        if j == "True":
            print(loc)
    loc=loc+1

data.to_excel('clean data/cleaned data.xlsx')

#second dataset

df=pd.read_excel('Data/heart.xlsx')

age=list()
sex=list()
chest_pain_type=list()
Resting_BP=list()
cholesterol=list()
FastingBS=list()
RestingECG=list()
MaxHR=list()
ExerciseAngina=list()
Oldpeak=list()

i=0
while i< len(df['age']):
    age.append(df['age'].loc[i])
    i=i+1
    sex.append(df['age'].loc[i])
    i=i+1
    chest_pain_type.append(df['age'].loc[i])
    i=i+1
    Resting_BP.append(df['age'].loc[i])
    i=i+1
    cholesterol.append(df['age'].loc[i])
    i = i + 1
    FastingBS.append(df['age'].loc[i])
    i = i + 1
    RestingECG.append(df['age'].loc[i])
    i = i + 1
    MaxHR.append(df['age'].loc[i])
    i = i + 1
    ExerciseAngina.append(df['age'].loc[i])
    i = i + 1
    Oldpeak.append(df['age'].loc[i])
    i = i + 1

data=pd.DataFrame({'age':age, 'sex':sex, 'chest pain type':chest_pain_type,	'Resting BP':Resting_BP, 'cholesterol': cholesterol, 'FastingBS':FastingBS, 'RestingECG':RestingECG, 'MaxHR':MaxHR, 'ExerciseAngina':ExerciseAngina, 'Oldpeak': Oldpeak})

loc=0
for i in data.duplicated().values:
    if i==True:
        print(loc)
    loc=loc+1

loc=0
for i in data.isnull().values:
    for j in i:
        if j == "True":
            print(loc)
    loc=loc+1

data.to_excel('clean data/cleaned heart.xlsx')
print('done !')





