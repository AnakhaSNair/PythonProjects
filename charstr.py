str=input("enter a string:") 
free={} 
for i in str: 
      if i in free: 
free[i]+=1 
      else: 
           free[i]=1 
print(free) 