def my_function():
    a = 5
    return a
                    # ← only 1 blank line here
my_function()       # ← E305 error here


"""

def my_function():
    a = 5
    return a
                    # ← blank line 1
                    # ← blank line 2
print(my_function())

"""
