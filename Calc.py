
def Check():
    while True:
        args = input("--> Enter 2 numbers separated by space: ").split()
        if len(args) != 2:
            print("Incorrect number of arguments")
        else:
            try:
                return [float(arg) for arg in args]
            except ValueError:
                print("Error: Arguments must be numbers")

def Add(nums):
    return nums[0] + nums[1]

def Subtract(nums):
    return abs(nums[0] - nums[1])

def Multiply(nums):
    return nums[0] * nums[1]

def Divide(nums):
    try:
        return nums[0] / nums[1]
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")         

def Power(nums):
    return nums[0] ** nums[1]

def Modulos(nums):
    return nums[0] % nums[1]

#Checks if a number is prime.
def is_prime(n):
    flag = True
    if n < 2:
        flag = False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            flag =  False
    if flag: 
        print(n, "Is a prime number")
    else:
        print(n, "Is NOT a prime number")

#Checks if a number is odd or even.
def is_odd_even(n):
    print( n, "Is an Odd number" if n % 2 else "Is an Even number")

#Checks if a number is divisible by five without a remainder.
def is_div_by_five(n):
    print( n, "Is NOT dividsible by 5" if n % 5 else "Is dividsible by 5")

#Function to display menu and get user choice
def display_menu():
    print("\nMenu:\n------")
    print("a. Add")
    print("b. Subtract")
    print("c. Multiply")
    print("d. Divide")
    print("e. Power of")
    print("f. Modulos")
    print("g. Exit\n------")
    return input("\n--> Choose an option: ")

def main():
    res = 0
    while True:
        choice = display_menu()
        flag = True    
        match choice:
            case "a" | "add" | "Add":
                res = Add(Check())
            case "b" | "subtract" | "Subtract":
                res = Subtract(Check())
            case "c" | "multiply" | "Multiply":
                res = Multiply(Check())
            case "d" | "divide" | "Divide":
                res = Divide(Check())
                if res == None: flag = False
            case "e" | "power" | "Power":
                res = Power(Check())
            case "f" | "modulos" | "Modulos":
                res = Modulos(Check())
            case "g" | "exit" | "Exit":
                print("Exiting...")
                break
            case _:
                flag = False
                print("\nInvalid Input, Enter again")   

        if flag:    
            print(res)
            is_prime(int(res))
            is_odd_even(int(res))
            is_div_by_five(int(res))


if __name__ == "__main__":
    main()


    