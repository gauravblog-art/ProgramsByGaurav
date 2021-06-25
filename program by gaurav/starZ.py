#  in this video we are create  print 

for row in range(1,5):
    for col in range(1,5):
        if (row==1 ==1 or row==4) or (row+col==5):
            print("*",end=' ')
        else:
            print(end='  ')

    print()