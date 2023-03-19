def Fib(n):
   fiblist=[0,1]
   x=0
   i=0
   while(i<n):
       x=fiblist[i]+fiblist[i+1]
       fiblist.append(x)
       i=i+1
   return fiblist
