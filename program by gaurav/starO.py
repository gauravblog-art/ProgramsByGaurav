# now i am going to creata star 

for row in range(1,6):
    for col in range(1,6):
        if ((row==1 or row==5) and (col!=1 and col!=5)) or ((col==1 or col==5) and (row!=1 and row!=5)):

            print('*',end='   ')
        else:
            print(end='   ')
    print()