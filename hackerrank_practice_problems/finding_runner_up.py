if __name__ == '__main__':
  def maxNumber(array, maxNum):
      for score in array:
          if score > maxNum:
              maxNum = score
      return int(maxNum)

  n = int(input())
  arr = list(map(int, input().split()))
  maxNum = maxNumber(arr, -200)
  ans = -200
  for x in arr:
      if x > ans and x < maxNum:
          ans = x
  print(ans)