if __name__ == '__main__':
  s = input()
  hasAlphaNum = False
  hasNumber = False
  hasAlpha = False
  hasLowercase = False
  hasUppercase = False
  for letter in s:
      if letter.isalnum():
          hasAlphaNum = True
      if letter.isnumeric():
          hasNumber = True
      if letter.isalpha():
          hasAlpha = True
      if letter.islower():
          hasLowercase = True
      if letter.isupper():
          hasUppercase = True
      if hasNumber and hasUppercase and hasLowercase and hasAlpha and hasAlphaNum:
          break

  print(hasAlphaNum)
  print(hasAlpha)
  print(hasNumber)
  print(hasLowercase)
  print(hasUppercase)