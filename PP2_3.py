

def q1(): 
  #Write Assignment code here
  a = input("Input a word:")
  if a.endswith("y"):
    print("-ies")
  elif a.endswith("ey"):
    print("-eys")
  elif a.endswith("ife"):
    print("-ives")
  else:
    print("-s")
def q2(): 
  #Write Assignment code here
  num = input("Input a integer:")
  a = int(num)
  if a > 0:
    print(f"{a} is positive")
  else:
    print(f"{a} is negative")
    

#Do not alter the following code
#Comment out the following code when running your tests

q1()
q2()
