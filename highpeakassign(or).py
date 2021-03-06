print("Enter goodies and prices")
l=[]
j=0
#while(j<10):
#    l1=[str(i) for i in input().split(" ")]
#    l.append(l1)
#    j+=1
file1=open("in.text","a")
#l2=[]
for i in range(len(fie1)):
    l2=file1.seek(0)
for j in range(10):
    l2.append(int(l[j][1]))
l2.sort()
l3=[]
for i in range(4,8):
    p=l2[i]
    for j in range(len(l)):
        if l[j][1]==str(p):
            l3.append(l[j])
print("Number of employees: ",len(l3))
for i in range(len(l3)):
    print(l3[i][0]," ",l3[i][1])
    
#print("And the difference between the chosen goodie with highest price and the lowest price is " ,min)
    
file1.close();