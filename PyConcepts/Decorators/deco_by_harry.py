# you decorate the existing function as you cannot change the functionality of an existing function
# often used to add functionality to existing functions such as logging, memoization and access control
# it returns a new function that modifies the behavior of the original function

# defining decorator function, it takes a function as an argument
def greet(func):
    def m_func():
        print("Good morning..")
        func()
        print("Thank you for using this func")

    return m_func  # Return the function itself, not its result


@greet  # decorating hello function, it is same as calling greet(hello)()
def hello():
    print("hello world!!")


hello()

# greet(hello)()

print("=============================")


# case when arguments are there

def greet_1(func):
    def m_func(*args, **kwargs):
        print('Good Morning')
        returv_val = func(*args, **kwargs)
        print("We are done.Thanks!!")
        return returv_val

    return m_func


# @greet
@greet_1
def add(a, b):
    print(a + b)
    return b


add(3, 4)
res = add(5, 9)
print(res)
