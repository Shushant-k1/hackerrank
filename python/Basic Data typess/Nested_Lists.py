nam=[]

if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        a=[name,score]
        nam.append(a)
nam.sort(key=lambda x: (x[1] ,x[0]), reverse=False)
mi=nam[0][1]
b=[]
for i in range(1,len(nam)):
    if nam[i][1]!=mi:
        b.append(nam[i])
        
mi=b[0][1]
for i in range(len(b)):
    if b[i][1]==mi:
        print(b[i][0])
    else:
        break
