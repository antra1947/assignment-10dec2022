#Solve these question on both Python and Javascript
 #1: Simple Number Triangle Pattern
#Pattern:
1  
#2 2  
#3 3 3  
#4 4 4 4 
#ans-

rows = 6

for num in range(rows):

    for i in range(num):

     print(num, end="") # print number

    # line after each row to display pattern correctly

    print("")



 #2: Inverted Pyramid of Numbers
#Pattern:
#1 1 1 1 1 
#2 2 2 2 
#3 3 3 
#4 4 
5

#ans-
rows = 5

b = 0

for i in range(rows, 0, -1):

    b += 1

    for j in range(1, i + 1):

        print(b, end='')

    print('\r')





3#Pattern:
1 
#1 2 
#1 2 3 
#1 2 3 4 
#1 2 3 4 5

#ans-
rows = 5

for row in range(1, rows+1):

    for column in range(1, row + 1):

        print(column, end='')

    print('')





 #4: Inverted Pyramid of Descending Numbers
#Pattern:
#5 5 5 5 5 
#4 4 4 4 
#3 3 3 
#2 2 
1

#ans
rows = 5

for i in range(rows, 0, -1):

    num = i

    for j in range(0, i):

        print(num, end='')

    print('\r')


 #5: Inverted Pyramid of the Same Digit
#Pattern
#5 5 5 5 5 
#5 5 5 5 
#5 5 5 
#5 5 
5
#ans
rows = 5

num = rows

for i in range(rows, 0, -1):

    for j in range(0, i):

        print(num, end='')

    print('\r')






  #6: Reverse Pyramid of Numbers
#Pattern:
1 
#2 1 
#3 2 1 
#4 3 2 1 
#5 4 3 2 1

#ans-
rows = 6

for row in range(1, rows):

    for column in range(row, 0, -1):

        print(column, end='')

    print('')



#7: Inverted Half Pyramid Number Pattern
#Pattern:
#0 1 2 3 4 5 
#0 1 2 3 4 
#0 1 2 3 
#0 1 2 
0# 1

#ans-
rows = 5

for i in range(rows, 0, -1):

    for j in range(0, i + 1):

        print(j, end="")

    print('\r')



 
 #8: Pyramid of Natural Numbers Less Than 10
#Pattern:
1 
#2 3 4 
#5 6 7 8 9


#ans-
currentNumber = 1

stop = 2

rows = 3 # Rows you want in your pattern

for i in range(rows):

    for column in range(1, stop):

        print(currentNumber, end='')

        currentNumber += 1

    print('')

    stop += 2

   
 #9: Reverse Pattern of Digits from 10 
#Pattern:
1
#3 2
#6 5 4
#10 9 8 7
 #ans-
start = 1

stop = 2

currentNumber = stop

for row in range(2, 6):

    for col in range(start, stop):

        currentNumber -= 1

        print(currentNumber, end='')

    print('')

    start = stop
    stop += row

    currentNumber = stop

 
 
 #10: Unique Pyramid Pattern of Digits
#Pattern:
1 
#1 2 1 
#1 2 3 2 1 
#1 2 3 4 3 2 1 
#1 2 3 4 5 4 3 2 1

#ans-
rows = 6

for i in range(1, rows + 1):

    for j in range (1,i-1):

        print(j, end='')
         
        for j in range(i-1,0,-1):

          print(j, end='')

    print()


 
 #11: Connected Inverted Pyramid Pattern of Numbers
#Pattern:
#5 4 3 2 1 1 2 3 4 5 
##5 4 3 2 2 3 4 5 
#5 4 3 3 4 5 
#5 4 4 5 
#5 5

#ans-
rows = 6

for i in range(0, rows):

 for j in range(rows-1,i,-1):

        print(j, ", end=")

for l in range(i):

        print('', end="")

for k in range(i + 1, rows):

        print(k, '', end='')

print('\n')






#12: Even Number Pyramid Pattern
#Pattern:
10 
#10 8 
#10 8 6 
#10 8 6 4 
#10 8 6 4 2
#ans-
rows = 5

LastEvenNumber = 2 * rows

evenNumber = LastEvenNumber

for i in range(1, rows+1):

    evenNumber = LastEvenNumber

    for j in range(i):

        print(evenNumber, end='')

        evenNumber -= 2

    print('\r')
  
 
 #13: Pyramid of Horizontal Tables
#Pattern:
0  
#0 1  
#0 2 4  
#0 3 6 9  
#0 4 8 12 16  
#0 5 10 15 20 25  
#0 6 12 18 24 30 36

#ans-
rows = 7

for i in range(0, rows):

    for j in range(0, i + 1):

        print(i * j, end='')

    print()





 #14: Pyramid Pattern of Alternate Numbers
#Pattern:
1 
#3 3 
#5 5 5 
#7 7 7 7 
#9 9 9 9 9

#ans-
rows = 5

i = 1

while i <= rows:

    j = 1

    while j <= i:

        print((i*2-1), end='')

        j = j + 1

    i = i + 1

    print()



 #15: Mirrored Pyramid (Right-angled Triangle) Pattern of Numbers
#Pattern:
  #         1 
   #      1 2 
  #    1 2 3 
   #1 2 3 4 
 #1 2 3 4 5
 #ans-
rows = 6

for row in range(1, rows):

    num = 1

    for j in range(rows, 0, -1):

        if j > row:

            print('', end='')

        else:

            print(num, end='')

            num += 1

    print("")
 
  
#Pattern #16: Equilateral Triangle with Stars (Asterisk Symbol)
#Pattern:
      #      *   
    #       * *   
     #     * * *   
      #   * * * *   
      ##  * * * * *   
      # * * * * * *   
     # * * * * * * *

     #ans-print(“Print equilateral triangle Pyramid using stars “)

size = 7

m = (2 * size)- 2

for i in range(0, size):

    for j in range(0, m):

        print(end='')

    m = m -1 # decrementing m after each loop

    for j in range(0, i + 1):
        print('Print equilateral triangle Pyramid using stars ')

size = 7

m = (2 * size)-2

for i in range(0, size):

    for j in range(0, m):

        print(end='')

    m = m-1 # decrementing m after each loop

    for j in range(0, i + 1):
        print('* ', end='')

    print('')

 
    
#Pattern #17: Downward Triangle Pattern of Stars
#Pattern:
 #       * * * * * * 
 #        * * * * * 
   ##       * * * * 
    #       * * * 
   #         * * 
    #         * 
    #ans-
    rows = 5

k = 2 * rows-2

for i in range(rows, -1, -1):

    for j in range(k, 0, -1):

        print(end='')

    k = k + 1
    for j in range(0, i + 1):

        print('*', end='')

    print('')
 
 
 
 
   #Pattern #18: Pyramid Pattern of Stars
#Pattern:
#* 
#* * 
#* * * 
#* * * * 
#* * * * *
#ans-

rows = 5

for i in range(0, rows):

    for j in range(0, i + 1):

        print('*', end='')

    print('\r')
