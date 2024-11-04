N = int(input())
arr = []
for i in range(0, N):
    command = input()
    if command == "print":
        print(arr)
    elif command == 'pop':
        arr.pop(-1)
    elif command == 'sort':
        arr.sort()
    elif command == 'reverse':
        arr.reverse()
    else:
        commandList = command.split()
        if commandList[0] == 'append':
            arr.append(int(commandList[1]))
        elif commandList[0] == 'remove':
            arr.remove(int(commandList[1]))
        else:
            arr.insert(int(commandList[1]), int(commandList[2]))