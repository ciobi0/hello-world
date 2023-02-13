def bad_fun(n):
    return 1 / n
 
try:
    bad_fun(0)
except ArithmeticError:
    print("What happened? An exception was raised!")
 
print("THE END.")