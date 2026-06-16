try:
 num=int(input("enter a number:"))
 result=10/num
except valueerror:
  print("error:invalid input! please enter a valid number:")
except zerodivisionerror:
  print("error:division by zerz!")
else:
  print("result:",result)
