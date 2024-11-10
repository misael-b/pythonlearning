# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = input().split()
ans = ""
for i in range(1, int(n), 2):
    top = (".|."*i).center(int(m), "-")
    print(top)

print("WELCOME".center(int(m), "-"))

for i in range(int(n), 1, -2):
    bottom = (".|."*(i-2)).center(int(m), "-")
    print(bottom)