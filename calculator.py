import colorama
from colorama import Fore, Style
colorama.init(autoreset=True)

print(f"\n\t\t\t\t{Fore.GREEN}{Style.BRIGHT}Simple Calculator\n\n")
print(f"{Fore.GREEN}{Style.BRIGHT}[1]Enter add to add \n[2]Enter subtract to subtract \n[3]Enter multiply to multiply \n[4]Enter divide to divide \n[5]Enter exit to exit\n")

while True:
    try:
        user_choice = input(f"{Fore.RED}{Style.BRIGHT}Enter Your choice : ")

        if user_choice == "add":
            first_num = int(input(f"\n{Fore.GREEN}{Style.BRIGHT}Enter the first number : "))
            second_num = int(input(f"{Fore.GREEN}{Style.BRIGHT}Enter the second number : "))
            answer = print(f"{Fore.GREEN}{Style.BRIGHT}{first_num} + {second_num} = ", first_num + second_num)
            
        elif user_choice == "subtract":
            first_num = int(input(f"\n{Fore.GREEN}{Style.BRIGHT}Enter the first number : "))
            second_num = int(input(f"{Fore.GREEN}{Style.BRIGHT}Enter the second number : "))
            answer = print(f"{Fore.GREEN}{Style.BRIGHT}{first_num} - {second_num} = ", first_num - second_num)
            
        elif user_choice == "multiply":
            first_num = int(input(f"\n{Fore.GREEN}{Style.BRIGHT}Enter the first number : "))
            second_num = int(input(f"{Fore.GREEN}{Style.BRIGHT}Enter the second number : "))
            answer = print(f"{Fore.GREEN}{Style.BRIGHT}{first_num} * {second_num} = ", first_num * second_num)
            
        elif user_choice == "divide":
            first_num = int(input(f"\n{Fore.GREEN}{Style.BRIGHT}Enter the first number : "))
            second_num = int(input(f"{Fore.GREEN}{Style.BRIGHT}Enter the second number : "))
            answer = print(f"{Fore.GREEN}{Style.BRIGHT}{first_num} / {second_num} = ", first_num / second_num)
            
        elif user_choice == "exit":
            print(f"\n\t\t\t\tBYEEEEEEEEEEEEEEEE")
            break
    except:
        print(f"{Fore.RED}{Style.BRIGHT}\nInvalid Choice! Try Again")