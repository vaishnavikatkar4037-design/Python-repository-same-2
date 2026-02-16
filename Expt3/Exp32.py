def simple_interest(principal,rate,time):
  si = (principal*rate*time)/100
  return si
# taking input from the user
p = float(input("enter principal amount:"))
r = float(input("enter rate of intrest:"))
t = float(input("enter time(in years):"))

# function call

interest = simple_interest(p,r,t)
print("simple interest is:",interest)
