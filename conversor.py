def txt_to_bin(txt):
    return ''.join('{0:08b}'.format(ord(x), 'b') for x in txt)

def bin_to_txt(bin):
    return ''.join(chr(int(bin[i:i+8], 2)) for i in range(0, len(bin), 8))

def txt_to_bytes(txt):
    return [ord(i) for i in txt]

def bytes_to_txt(bytes):
    return ''.join(chr(i) for i in bytes)

def main():
    while True:
        print("""
        1. Text to binary
        2. Binary to text
        3. Text to bytes
        4. Bytes to text
        5. Exit
        """)
        choice = int(input("Enter your choice: "))
        if choice == 1:
            txt = input("Enter a text: ")
            print(txt_to_bin(txt))
            input("Press enter to continue...")
        elif choice == 2:
            bin = input("Enter a binary: ")
            print(bin_to_txt(bin))
            input("Press enter to continue...")
        elif choice == 3:
            txt = input("Enter a text: ")
            for i in txt_to_bytes(txt):
                print(i)
            input("Press enter to continue...")
        elif choice == 4:
            bytes = input("Enter a bytes: ")
            bytes = bytes.split(",")
            print(bytes_to_txt(bytes))
            input("Press enter to continue...")
        elif choice == 5:
            break
        else:
            print("Invalid choice")
            input("Press enter to continue...")

if __name__ == "__main__":
    main()