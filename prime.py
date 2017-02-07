def prime_numbers(n):
	PrimeList=[]
	if not instance(n,int):
		return 'only integers are allowed'
	elif n<=0:
		return 'only positive prime numbers greater than are required'
	elif n==1:
		return 'not a prime number'
	else:
 		for x in range(2,n+1):
 			isPrime=True
      for y in range(2,x):
     		if (x%y==0):
          isPrime==0:
            	break
       if isPrime
          PrimeList.append(x)    
    		else:
        		print(n)