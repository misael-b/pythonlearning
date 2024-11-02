if __name__ == '__main__':
  studentScores = []
  scores = []
  ans = []
  for _ in range(int(input())):
      name = input()
      score = float(input())
      scores.append(score)
      studentScores.append([name, score])

  scores2 = list(set(scores))
  scores2.sort()
  secondLowestScore = scores2[1]
  for student in studentScores:
      if student[1] == secondLowestScore:
          ans.append(student[0])

  ans.sort()
  for answer in ans:
      print(answer)