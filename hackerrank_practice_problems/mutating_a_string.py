def mutate_string(string, position, character):
  firstHalf = string[:position]
  lastHalf = string[position+1:]
  return firstHalf + character + lastHalf

if __name__ == '__main__':
  s = input()
  i, c = input().split()
  s_new = mutate_string(s, int(i), c)
  print(s_new)