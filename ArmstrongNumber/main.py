# Armstrong Number
# samples:
# 371 = 3^3 + 7^3 + 1^3
# 9474 = 9^4 + 4^4 + 7^4 + 4^4


state = True
while state:
  number = input('Enter a number ==> ')
  if not number.isnumeric():
      sate = True
      print('Invalid number try again')
  else:
    state = False
length = len(number)
result = 0
for i in number:
  result += int(i)**length  
if result == int(number):
    print(f"{number} is an n-Armstrong Number")
else:
    print(f"{number} is not an n-Armstrong Number")