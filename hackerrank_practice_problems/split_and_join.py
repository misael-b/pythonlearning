def split_and_join(line):
  # write your code here
  splitList = line.split(" ")
  return "-".join(splitList)

if __name__ == '__main__':
  line = input()
  result = split_and_join(line)
  print(result)