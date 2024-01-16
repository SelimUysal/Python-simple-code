key= ' '
ans =' '
def calculate(key,ans):
 i=count=0
 for c1 in key:
   if c1==ans[i]:
      count+=1
   i+=1   
 return count*10

def inp():
    global key
    key=input("Enter answer key: ")
    dict={}
    scores=[]
    sum=0
    for number in range(1,4):
        name=input("Enter name: ")
        last=input("Enter last name: ")
        answers=input("Enter answers: ")
        lst=[]
        lst.append(name)
        lst.append(last)
        score=calculate(key,answers)
        tup=tuple(lst)
        dict[tup]=score
        sum+=score
        scores.append(score)
    avg=sum/len(dict)
    return(dict,scores,avg)


d,s,av=inp()
print(d)

print("Average: ",av)
print("Students above average ")
for a in d.keys():
    if d[a]>=av:
      print("Name: ",a[1]+','+a[0][0]+'.',"Score: ",d[a])
      
st=input("Who are you searching for? ")
for a in d.keys():
    if st in a:
        print(a[0],a[1],"received ",d[a])




