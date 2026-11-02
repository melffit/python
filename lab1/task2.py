password = input("введите ваш пароль: ")
if len(password) < 16 :
   print("пароль слишком короткий")
elif password.isalpha() or password.isdigit():
   print("слабый пароль")
else:
   print("надежный пароль")