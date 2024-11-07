def count_substring(string, sub_string):
  counter = 0
  if sub_string in string:
      for i in range(0, len(string)):
          if string[i:i+len(sub_string)] == sub_string:
              counter = counter+1
  else:
      return 0
  return counter

if __name__ == '__main__':
  string = input().strip()
  sub_string = input().strip()

  count = count_substring(string, sub_string)
  print(count)