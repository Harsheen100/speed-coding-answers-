#question 1 
def isPossible(str, n): 
      
    
    l = len(str) 
  
   
    if (l >= n): 
        return True
      
    return False
  

str = input("enter a string")
n = len(str)
  
if(isPossible(str, n)): 
    print("1") 
else:
    print("0")

#question 2
def multiply(num1, num2): 
    len1 = len(num1) 
    len2 = len(num2) 
    if len1 == 0 or len2 == 0: 
        return "0"
  
 
    result = [0] * (len1 + len2) 

    i_n1 = 0
    i_n2 = 0

    for i in range(len1 - 1, -1, -1): 
        carry = 0
        n1 = ord(num1[i]) - 48

        i_n2 = 0
  

        for j in range(len2 - 1, -1, -1): 
 
            n2 = ord(num2[j]) - 48
      
            summ = n1 * n2 + result[i_n1 + i_n2] + carry 
  

            carry = summ // 10
  
         
            result[i_n1 + i_n2] = summ % 10
  
            i_n2 += 1
  
       
        if (carry > 0): 
            result[i_n1 + i_n2] += carry 
  
        i_n1 += 1
          
    
    i = len(result) - 1
    while (i >= 0 and result[i] == 0): 
        i -= 1
  
  
    if (i == -1): 
        return "0"
   
    s = "" 
    while (i >= 0): 
        s += chr(result[i] + 48) 
        i -= 1
  
    return s 
  

str1 = input("enter string")
str2 = input("enter the second string ")
  
if((str1[0] == '-' or str2[0] == '-') and 
   (str1[0] != '-' or str2[0] != '-')): 
    print("-", end = '') 
  
  
if(str1[0] == '-' and str2[0] != '-'): 
    str1 = str1[1:] 
elif(str1[0] != '-' and str2[0] == '-'): 
    str2 = str2[1:] 
elif(str1[0] == '-' and str2[0] == '-'): 
    str1 = str1[1:] 
    str2 = str2[1:] 
print(multiply(str1, str2))


#question 3

def ispalindrome(x): 
	ans, temp = 0, x 
	while temp > 0: 
		ans = 10 * ans + temp % 10
		temp = temp // 10
	return ans == x 


def SuperPalindromes(L, R): 
	
	L, R = int(L), int(R) 

	
	LIMIT = 10

	ans = 0

	
	for i in range(LIMIT): 
		s = str(i) 
		p = s + s[-2::-1] 
		p_sq = int(p) ** 2
		if p_sq > R: 
			break
		if p_sq >= L and ispalindrome(p_sq): 
			ans = ans + 1

	 
	for i in range(LIMIT): 
		s = str(i) 
		p = s + s[::-1] ' 
		p_sq = int(p) ** 2
		if p_sq > R: 
			break
		if p_sq >= L and ispalindrome(p_sq): 
			ans = ans + 1

	
	return ans 

L = input("enter starting of the range ")
R = input("enter seconf number ")


print("{"+SperPalindromes(L, R)+"}") 



#question 4
  
def isPrime( n ): 
	
	
	if n <= 1: 
		return False
	
	
	for i in range(2, n): 
		if n % i == 0: 
			return False
	
	return True


def isEmirp( n): 
	
	
	n = int(n) 
	if isPrime(n) == False: 
		return 0
		
		
	rev = 0
	while n != 0: 
		d = n % 10
		rev = rev * 10 + d 
		n = int(n / 10) 
		
	
	return isPrime(rev) 


n = int(input("enter a number"))
if isEmirp(n): 
	print("1") 
else: 
	print("0") 
	

#question 5

def gcd(x, y):
    gcd = 1
    
    if x % y == 0:
        return y
    
    for k in range(int(y / 2), 0, -1):
        if x % k == 0 and y % k == 0:
            gcd = k
            break  
    return gcd
x=int(input())
y=int(input())
print(gcd(x,y))

#question 6
#question 7
#question 8
def term(n) : 
    
    ans = 0
    for i in range(1,n+1) : 
        ans = (i**2)-1  
       
    return ans 
  
  

n = int(input("enter the last value"))
print(term(n))

#question 9
filename = input("Input the Filename: ")
count =0
for i in filename :
    if i==".":
        count = count +1

if count == 1:
    f_extns = filename.split(".")
    print (repr(f_extns[-1]))
else:
    print("Not a file name ")

#question 10

import math 


def check(n) : 

	
	count_digits = len(str(n)) 
	
	sum = 0  
	x = n 
	while (x!=0) : 

		
		r = x % 10
		
		
		sum = (int) (sum + math.pow(r, count_digits)) 
		count_digits = count_digits - 1
		x = x/10
		
	
	if sum == n : 
		return 1
	else : 
		return 0
		

n = int(input())
if (check(n) == 1) : 
	print ("1")
else : 
	print ("0")

 

    


  
