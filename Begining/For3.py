# display the name & salary whose sub:python

li=[{'Name':'A','Age':26,'Salary':61000,'Sub':['Python','Java','c']},
    {'Name':'B','Age':27,'Salary':66000,'Sub':['Ruby','Java','c']},
    {'Name':'C','Age':31,'Salary':79000,'Sub':['c#','Java','c']},
    {'Name':'D','Age':33,'Salary':70000,'Sub':['Python','Java','c++']},
    {'Name':'E','Age':28,'Salary':68000,'Sub':['Python','Java','c#']},
    {'Name':'F','Age':37,'Salary':88000,'Sub':['SQL','Java','c']},
    {'Name':'G','Age':38,'Salary':79000,'Sub':['c++','Java','c']},
    {'Name':'H','Age':32,'Salary':70000,'Sub':['HTML','Java','c']}]
for i in li:
    if 'Python' in i['Sub']:
        print(i['Name'],i['Age'],i['Salary'])