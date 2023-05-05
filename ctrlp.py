# function CTRL+P to print on the printer

def ctrlp(list1):   
    list2 = []
    for t in list1:
        if t=="-":
            for y in range(1,2625):
                list2.append(y)
        elif "-" in t and len(t)>1:
            if t.index("-")==0:
                b = t[t.index("-")+1::]
                for y in range(1,int(b)+1):
                    list2.append(y)
            elif t.index("-")==len(t)-1:
                b = t[:t.index("-")]
                for x in range(int(b),2625):
                    list2.append(x)
            else:
            
                a,c = t.split("-")
                for y in range(int(a),int(c)+1):
                        list2.append(y)
        else:
            list2.append(t)
    return len(list2)

list1 = list(map(str,input().split(",")))
print(ctrlp(list1))
