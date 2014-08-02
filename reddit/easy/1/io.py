"""
create a program that will ask the users name, age, and reddit username.
have it tell them the information back, in the format:
your name is (blank), you are (blank) years old, and your username is (blank)
for extra credit, have the program log this information in a file to be accessed later.
"""


def main():
    name = input('What is your name? ')
    age = input('What is your age? ')
    username = input('What is your username? ')

    result = "Your name is {}, you are {} years old, and your username is {}.".\
        format(name, age, username)
    print(result)

if __name__ == "__main__":
    main()
