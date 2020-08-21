dict2={'0':'Zero','1':'One','2':'Two','3':'Three','4':'Four','5':'Five','6':'Six','7':'Seven','8':'Eight','9':'Nine'}
dict1={'1':'Ten','2':'Twenty','3':'Thirty','4':'Fourty','5':'Fivety','6':'Sixty','7':'Seventy','8':'Eightty','9':'Ninety'}
dict3={'1':'One-Hundred','2':'Two Hundred','3':'Three Hundred','4':'Four Hundred','5':'Five Hundred','6':'Six Hundred','7':'Seven Hundred','8':'Eight Hundred','9':'Nine Hundred'}
dict4={'10':'Ten','11':'Eleven','12':"Twelve",'13':'Thirteen','14':"Fourteen",'15':'Fiveteen','16':'Sixteen','17':'siventeen','18':'Eighteen','19':'Nineteen'}
string1=""
string2=""
number=list(input("Enter any number(0-999):"))
i=0
k=1
t=2
if(len(number)==1):
    search_key=number[i]
    string1=string1+(dict2[search_key])+" "
elif(len(number)==2):
    if(number[i]=='0'):
        print("Invalid Number")
        print("[You are not supposed to give 'Zero' at first]")
    elif(number[i]=='1'):
        string2=string2+'1'
        if(number[k]=='1','2','3','4','5','6','7','8','9'):
            string2=string2+number[k]
            string1=string1+(dict4[string2])
    elif(number[i]!='1'):
        search_key2=number[i]
        string1=string1+(dict1[search_key2])+" "
        if(number[k]!='0'):
            search_key2=number[k]
            string1=string1+(dict2[search_key2])+" "
elif(len(number)==3):
    if(number[i]=='0'):
        print("Invalid Number")
        print("[You are not supposed to give 'zero' at first]")
    else:
        search_key3=number[i]
        string1=string1+(dict3[search_key3])+" "
        if(number[k]=='1'):
            string2=string2+'1'
            if(number[t]=='1','2','3','4','5','6','7','8','9'):
                string2=string2+number[t]
                string1=string1+"And "+(dict4[string2])
        elif(number[k]!=None):
            if(number[k]=='0'):
                if(number[t]=='0'):
                    string1=string1+" "
                else:
                    search_key=number[t]
                    string1=string1+"And "+(dict2[search_key])
            elif(number[t]!=None):
                string1=string1+"And "
                search_key2=number[k]
                string1=string1+(dict1[search_key2])+" "
                if(number[t]!='0'):
                    search_key2=number[t]
                    string1=string1+(dict2[search_key2])
else:
    print("Greater than 1000 Not Available")
print(string1)
    
