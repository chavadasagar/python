def reverse_str(string):
    reverse_string = ""
    for x in string:
        reverse_string = x + reverse_string;

    return reverse_string

string = input("Enter String :")

print(reverse_str(string))
