import random
import os

print 'Rules:'
print 'Rock blunts scissors'
print 'Paper covers rock'
print 'Scissors cut paper'

testVar = raw_input("Select one Rock(r), Paper(p) , Scissor(s): ")
if testVar == "r" or testVar == "p" or testVar == "s":
    print(testVar)
else:
    print 'Invalid Input'
    os._exit(0)

list1=['r','p','s']
cpu = random.randint(0,2)
print(list1[cpu])

if testVar == list1[cpu]:
    print 'Draw'
elif testVar == 'r' and list1[cpu] == 's':
    print 'User Won'
elif testVar == 'r' and list1[cpu] == 'p':
    print 'Cpu Won'
elif testVar == 'p' and list1[cpu] == 'r':
    print 'User Won'    
elif testVar == 'p' and list1[cpu] == 's':
    print 'Cpu Won'
elif testVar == 's' and list1[cpu] == 'r':
    print 'Cpu Won'
elif testVar == 's' and list1[cpu] == 'p':
    print 'User Won'

elif list1[cpu] == 'r' and testVar == 's':
    print 'User Won'
elif list1[cpu] == 'r' and testVar == 'p':
    print 'Cpu Won'
elif list1[cpu] == 'p' and testVar == 'r':
    print 'User Won'    
elif list1[cpu] == 'p' and testVar == 's':
    print 'Cpu Won'
elif list1[cpu] == 's' and testVar == 'r':
    print 'Cpu Won'
else:
    print 'User Won'

os._exit(0)
