import string
import random

def gen_pass(length):
    if length < 1:
        return "Password should be of at least 1 length"
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")
    length = int(input("Enter the desired length of password: "))
    if length <= 0:
        print("The length should be a positive integer.")
    else:
        password = gen_pass(length)
        print(f"Generated Password: {password}")
if __name__ == "__main__":
    main()

    
            
