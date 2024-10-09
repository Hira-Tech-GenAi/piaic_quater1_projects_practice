"""This program counts the number of times each number appears in a list. It uses a dictionary to keep track of the information.

An example run of the program looks like this (user input is in blue):

Enter a number: 3 Enter a number: 4 Enter a number: 3 Enter a number: 6 Enter a number: 4 Enter a number: 3 Enter a number: 12 Enter a number: 3 appears 3 times. 4 appears 2 times. 6 appears 1 times. 12 appears 1 times."""

from colorama import Fore, Style
def get_user_numbers()->list:

    user_numbers: list = []
    while True:
        user_input: str = input(Fore.BLUE + "Enter a number: " + Style.RESET_ALL)
        
        #? If the user enters a blank line, break out of the loop and stop asking for input
        if user_input == "":
            break
        
        # ?convert the user input to an integer and add it to the list
        num = int(user_input)
        user_numbers.append(num)
    
    return user_numbers

def count_nums(num_lst)->dict:
    """
    Create an empty dictionary.
    Loop over the list of numbers. 
    If the number is not in the dictionary, add it as a key with a value of 1.
    If the number is in the dictionary, increment its value by 1.
    """
    num_dict: dict = {}
    for num in num_lst:
        if num not in num_dict:
            num_dict[num] = 1
        else:
            num_dict[num] += 1
    
    return num_dict


def print_counts(num_dict) -> None:
    """
    Loop over the dictionary and print out each key and its value.
    """
    for num in num_dict:
        print(str(num) + " appears " + str(num_dict[num]) + " times.")


def main() -> None:
    
    user_numbers: list = get_user_numbers()
    num_dict: dict = count_nums(user_numbers)
    print_counts(num_dict)


#? Python boilerplate.
if __name__ == '__main__':
    main()