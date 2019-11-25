def reverse_int(int_str):
    str_int=""
    for i in range(len(int_str)):
        str_int+=int_str(len(int_str)-1-i);
    return str_int

def main():
    input1=input("num  >>");

    print(reverse_int(input1))

main()