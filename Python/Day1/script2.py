'''
Q. Write a program to prompt for a score bw 0.0 and 1.0. If the score is out of range, print an error msg. if the score 
is bw 0.0 to 1.0, print a grade using the following table:

    >= 0.9          A
    >= 0.8          B
    >= 0.7          C
    >= 0.6          D
    <  0.6          F

Run the program repeatedly to test the various different values for input.
'''

#!/usr/bin/python3


while True:

    a = (input("Enter a number: "))

    if(a>="0.9" and a<="1.0"):
        print("A")
    elif(a>="0.8" and a<="0.9"):
        print("B")
    elif(a>="0.7" and a<="0.8"):
        print("C")
    elif(a>="0.6" and a<="0.7"):
        print("D")
    elif(a<"0.6"):
        print("F")
    else:
        print("BAD SCORE")


