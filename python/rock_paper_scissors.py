
import random
actors = ['Rock', 'Paper', 'Scissor']
c, cp, cpup = 0, 0, 0
while c <5:
    ch = input("\nRock, Paper, Scissor ? : ")
    cpu = random.choice(actors)
    print('User:', ch, 'Cpu:', cpu)
    if ch == cpu:
        c = c + 1
    else:
        if (ch == 'Rock' and cpu == 'Paper') or (ch == 'Paper' and cpu == 'Scissor') or (ch == 'Scissor' and cpu == 'Rock'):
            cpup = cpup + 1
        else:
            cp = cp + 1
        c = c + 1
if cp > cpup:
    print("\nThe winner is user(%d - %d)" %(cp, cpup))
elif cp < cpup:
    print("\nThe winner is cpu (%d - %d)" %(cpup, cp))
else:
    print("\nTie game !")