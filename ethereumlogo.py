# ethereum logo lol.

def pyramid(num): # 1 pyramid
    for i in range(0, num):

        for j in range(0, num-i):
            print(end=" ")
        
        for j in range(0, i+1):
            print(j, end=" ")
        
        
        
        print()
def pyramid_second(num): # pyramid reversed 
    num+=1
    for i in range(0, num):

        for j in range(0, i):
            print(end=" ")

        for j in range(num, i, -1):
            print(j, end=" ")

        print()
num = 6
pyramid(num)
pyramid_second(num)




#       0 
#      0 1 
#     0 1 2 
#    0 1 2 3 
#   0 1 2 3 4 
#  0 1 2 3 4 5 
# 7 6 5 4 3 2 1 
#  7 6 5 4 3 2 
#   7 6 5 4 3 
#    7 6 5 4 
#     7 6 5 
#      7 6 
#       7
