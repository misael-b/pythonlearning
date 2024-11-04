def swap_case(s):
  ans = ""
  for letter in s:
      if letter.isupper():
          ans += letter.lower()
      elif letter.islower():
          ans+= letter.upper()
      else:
          ans += letter

  return ans

if __name__ == '__main__':
  s = input()
  result = swap_case(s)
  print(result)