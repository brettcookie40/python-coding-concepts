# This is
def alphabetize():
    val = input("Enter a string to be sorted in order: ")
    sorted_characters = sorted(val)
    val = "".join(sorted_characters)
    print(val)

def main():
    while(1):
        alphabetize()