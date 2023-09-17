

print('Welcome to Elite 101 Chatbot')


# gets user inputs
name = input("what is your name? ")
age = input("how old are you ")
print("")

# uses user input to print information
print("Hello " +  name  + " !!!")
print("only " + age + " still got your whole life ahead of you")
print("")
day = str(input("how's your day "))
if (day == 'good'):
  print("im glad your day's going well")
  
else:
  print('well i hope i make it better')
  
choice = ""
print()
print('please choose following options. ')

while True:
  print("1. your favorite shoe brand")
  print("2. end chat")
  
  choice = (input('enter choice: '))

  choice = choice.strip()
  if (choice == '1'):
    brand = str(input('what is your favorite brand? '))
    if brand.lower()=='jordans' or brand.lower()=='js':
      print('wow i like jordans too')
      break
    else:
      print('oh thats a good choice for me my favorite is jordans')
      break
  elif (choice =='2'):
    exit('end')
    break
  else:
    print('please enter options 1-2')


 