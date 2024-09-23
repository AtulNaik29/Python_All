# di={'Name':'A','Age':26,'Salary':67000}
# for k,v in di.items():
#     print(k,v)

li=[{'Name':'A','Age':26,'Salary':67000},
    {'Name':'B','Age':27,'Salary':88000},
    {'Name':'C','Age':31,'Salary':79000},
    {'Name':'D','Age':33,'Salary':70000}]
# for i in li:
#         for k,v in i.items():
#             print(k,v)

#display details whose age <30
for i in li:
        if i['Age']>30:
            print(i['Name'],i['Salary'])

            