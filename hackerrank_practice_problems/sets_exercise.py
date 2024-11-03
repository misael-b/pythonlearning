m = int(input())
mSet = set(input().split())
n = int(input())
nSet = set(input().split())

set1 = nSet.difference(mSet)
set2 = mSet.difference(nSet)

ansSet = set1.union(set2)
ansList = list(ansSet)
ansList = [int(x) for x in ansList]

ansList.sort()
for i in ansList:
    print(i)