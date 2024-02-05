#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    elements_printed = 0
    try:
        for i in range(x):
            print(my_list[i], end=" ")
            elements_printed += 1
    except IndexError:
        pass  # Ignore index errors if x is greater than the length of my_list
    finally:
        print()  # Print a new line after printing elements
        return elements_printed
# Example usage:
my_list = [1, 2, 'three', 4, 'five']
num_printed = safe_print_list(my_list, 3)
print(f"Number of elements printed: {num_printed}")
