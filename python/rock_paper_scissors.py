
import random
actors = ['Rock', 'Paper', 'Scissor']
c, csp, cspup = 0, 0, 0
while c <5:
    ch = input("\nRock, Paper, Scissor ? : ")
    cpu = random.choice(actors)
    print('User:', ch, 'Cpu:', cpu)
    if ch == cpu:
        c = c + 1
    else:
        if (ch == 'Rock' and cpu == 'Paper') or (ch == 'Paper' and cpu == 'Scissor') or (ch == 'Scissor' and cpu == 'Rock'):
            cspup = cspup + 1
        else:
            csp = csp + 1
        c = c + 1
if csp > cspup:
    print("\nUser is the winner(%d - %d)" %(csp, cspup))
elif csp < cspup:
    print("\nCPU is the winner (%d - %d)" %(cspup, csp))
else:
    print("\nGame is Tie !")