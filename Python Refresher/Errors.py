def divide(dividend, divisor):
    ##This one catches math errors
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")
    return dividend/divisor

grades = []

print("Welcome to the average grade program")
##This one cares about the correctness of the data in context of the program
try:
    average = divide(sum(grades), len(grades))
    ##Can do this or the else statement
    ##print(f"The average grade is {average}")
except ZeroDivisionError as e:
    print(e)
    print("There are no grades yet!")
except ValueError:
    pass
else:
    print(f"The average grade is {average}")
finally:
    (print("Thank you!"))

