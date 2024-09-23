#display name & age whose salary 60000-70000
li=[{'Name':'A','Age':26,'Salary':61000},
    {'Name':'B','Age':27,'Salary':66000},
    {'Name':'C','Age':31,'Salary':79000},
    {'Name':'D','Age':33,'Salary':70000},
    {'Name':'E','Age':28,'Salary':68000},
    {'Name':'F','Age':37,'Salary':88000},
    {'Name':'G','Age':38,'Salary':79000},
    {'Name':'H','Age':32,'Salary':70000}]
for i in li:
    if i['Salary']>=60000 and i['Salary']<=70000:
        print(i['Name'],i['Age'])
