if __name__ == '__main__':
  n = int(input())
  student_marks = {}
  for _ in range(n):
      name, *line = input().split()
      scores = list(map(float, line))
      student_marks[name] = scores
  query_name = input()
  scores = student_marks[query_name]
  sumOfScores = 0
  for testResult in scores:
      sumOfScores += testResult
  average = sumOfScores/len(scores)
  formatted_number = "%.2f" % average
  print(formatted_number)