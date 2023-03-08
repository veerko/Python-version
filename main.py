from version import Version

def main():
    a = Version("2.3")
    b = Version(major=2, minor=2)

    print("COMPARISON OPERATIONS")
    print(a, "==", b, "=", a == b)
    print(a, "!=", b, "=", a != b)
    print(a,  "<", b, "=", a  < b)
    print(a,  ">", b, "=", a  > b)
    print(a, ">=", b, "=", a >= b)
    print(a, "<=", b, "=", a <= b)

    print("BINARY OPERATIONS")
    print(a, "+", b, "=", a + b)
    print(a, "-", b, "=", a - b)

if __name__ == "__main__":
    main()