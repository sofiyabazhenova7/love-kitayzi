import csv
m=[]
def data():
    with open('data.csv') as f: #принимает файл за переменную
        reader = csv.reader(f, delimiter=';')
        
        for row in reader:
            s=row[0]
            asci=[ord(c) for c in s]
            print(sum(asci)/len(asci))
            m.append(sum(asci)/len(asci))
data()
print(sum(m)/len(m))
#asci=[ord(c) for c in s]
#print(sum(asci)/len(asci))