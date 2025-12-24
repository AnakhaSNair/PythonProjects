str=input("enter a string:") 
ch=input("element to be searched:") 
count=0 
for i in range(0,len(str)): 
if(ch==str[i]): 
          count=count+1 
print(count)