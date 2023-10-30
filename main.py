import random
import os

def createDirectory(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print("Error: Failed to create the directory.")

def deleteAllFiles(filepath):
    if os.path.exists(filepath):
        for file in os.scandir(filepath):
            os.remove(file.path)
        return 'Cleared All Files'
    else:
        return 'Directory Not Found'

win = 0
now = 0
logSets = 0
Boxes = [1]
for i in range(1,100):
    Boxes.append(i+1)

n = int(input('Loops: '))
sets = int(input('Sets: '))

print(deleteAllFiles("./Logs/"))

for k in range(0,n):
    random.shuffle(Boxes)
    prisoner = 1
    now = 1
    cnt = 0

    while True:
        now = Boxes[now-1]
        cnt += 1

        if prisoner == now and cnt <= 50:
            prisoner += 1
            now = prisoner
            cnt = 0

            if prisoner == 101:
                win += 1
                break

        elif prisoner == now and cnt > 50:
            break

    f = open("./Logs/"+str(k+1)+".txt","w")
    for i in range(0, 100):
        f.write(str(Boxes[i]) + " ")
        if i % 10 == 0 and i != 0:
            f.write("\n")
    f.write('\n\n승리 수: '+str(win)+'회, 승률: '+str((win/(k+1)) * 100)+'%')
    f.close()

    if k % sets == 0 and k != 0:
        print(str(k)+'회차 완료. 승리 수: '+str(win)+'회, 승률: '+str((win/k) * 100)+'%')

print(str(n)+'회차 완료. 승리 수: '+str(win)+'회, 승률: '+str((win/n) * 100)+'%')
print('평균치와의 오차: '+str(31 - ((win/n)*100))+"%")
