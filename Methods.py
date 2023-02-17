def f(x):
    return 1 / (1 + x**2)


# function for finding the trapeze integral of the values
def find_trapeze(maximum, minimum, no):
    h = maximum - minimum / no
    integral = h / 2 * f(minimum) + f(maximum)
    for i in range(1, no):
        integral += h * f(minimum + (i * h))
    return integral


inputting = True
while inputting:
    function = input("Please write the coefficients of polynomial function: \n")
    try:
        list = function.split()
        string = "f(x) ="
        check = 0
        count = len(list) - 1
        for i in range(len(list)):
            cur_val = int(list[i])
            if check != 0:
                if cur_val >= 0:
                    string += "+"
                else:
                    cur_val = cur_val * -1
                    string += "-"
            if count > 1:
                string += f" {cur_val}x^{count} "
            elif count == 1:
                string += f" {cur_val}x "
            else:
                string += f" {cur_val}"
            count -= 1
            check += 1

        print("The function you've entered:")
        print(string)
        print("Please write the boundaries of integration:")
        a = input("a: ")
        b = input("b: ")
        try:
            if a == "0":
                a = 0
                b = float(b)
            elif b == "0":
                a = float(a)
                b = 0
            else:
                a = float(a)
                b = float(b)
            max = 0
            min = 0
            if a > b:
                max = a
                min = b
            else:
                max = b
                min = a

            trapeze_integral = find_trapeze(maximum=max, minimum=min, no=15)
            print("Integration by trapezoidal method:" + trapeze_integral)
        except:
            print("Please enter a number")
        inputting = False
    except:
        print("Please enter a valid input.")
