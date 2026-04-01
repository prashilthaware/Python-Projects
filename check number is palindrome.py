num=int(input("Enter number:"))
num_str=str(num)

if (num_str==num_str[::-1]):
    print(f"{num} is palindrome")
else:
    print(f"{num} is not palindrome")