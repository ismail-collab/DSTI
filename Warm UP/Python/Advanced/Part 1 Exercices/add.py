import sys

if len(sys.argv) != 3:
    print("Error: Please provide exactly two integer arguments.")

#if (type(sys.argv[1])!=int or type(sys.argv[1])!=int):
#    print("Erreur: Please Provide two integers ")

else:
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])

    
    result = num1 + num2
    print(result)

