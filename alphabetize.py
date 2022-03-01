# This is a function for sorting a string by it's alphanumeric character constituents
def sort_alphanumeric(user_string):
    sorted_characters = sorted(user_string)
    user_string = "".join(sorted_characters)
    print(user_string)

def main():
    while(1):
        user_string = input("Enter a string to be sorted in order: ")
        sort_alphanumeric(user_string)

if __name__=="__main__":
    main()