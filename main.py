print('Welcome to Elite 101 Chatbot')
print()
# gets user inputs
name = input("what is your name? ")
print()
age = input("how old are you ")
print("")

# uses user input to print information
print("Hello " +  name  + " !!!")
print()
print("only " + age + " still got your whole life ahead of you")
print("")
day = str(input("how's your day? "))
print()
if (day == 'good'):
  print("im glad your day's going well")
else:
  print('well i hope i make it better')
  
choice = ""
print()
print('please choose following options. ')

while True:
  print("1. your favorite shoe brand.")
  print("2. what's your favorite phone brand.")
  print("3. if you play games what's your preferred console.")
  print("4. end chat")
  
  choice = (input('enter choice: '))

  choice = choice.strip()
  if (choice == '1'):
    brand = str(input('what is your favorite brand? '))
    if brand.lower()=='jordans' or brand.lower()=='js'or brand.lower()=='jordan':
      print()
      print('wow i like jordans too!!!')
      print()
    else:
      print()
      print('oh thats a good choice for me my favorite is jordans')
      print()
  elif (choice =='2'):
    phone = str(input("what's your favorite phone brand. "))
    if phone.lower()=='samsung':
      print()
      print('wow!!! I like samsung too')
      print()
    else:
      print()
      print('dang really for me its samsung')
      print()
  elif (choice =='3'):
    game = str(input("if you play games what's your preferred console. "))
    if game.lower()=='xbox':
      print()
      print('crazy thats also my favorite console!!!')
      print()
    else:
      print()
      print('not a bad choice for me its xbox')
      print()
  elif (choice =='4'):
    exit('end')
      
    break
  else:
    print('please enter options 1-4')


 