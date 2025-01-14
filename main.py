
def factorial(num):
    if num <0:
        print("Cant' Calculate Factorial ")
        return
    if num <=1:
        print("Factorial is ",1)
        return
    fac = 1
    for i in range(2, num+1):
        fac = fac * i
    print("The Factorial is",fac)
    return

factorial(5)    



