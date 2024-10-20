def main():
    filename = input("Enter the filename: ")
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        lines = [line.rstrip() for line in lines]
        while True:
            print(f"\nThe file has {len(lines)} lines.")
            try:
                lineNumber = int(input("Enter a line number (0 to quit): "))
            except ValueError:
                print("Invald input. Please enter a valid number.")
                continue
            if lineNumber == 0:
                print("Exiting the program.")
                break
            if 1 <= lineNumber <= len(lines):
                print(f"Line {lineNumber}: {lines[lineNumber - 1]}")
            else:
                print(f"Invalid line number. Please enter a number between 1 and {len(lines)}.")
    except FileNotFoundError:
        print(f" Error: The file '{filename}' does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
if __name__ == "__main__":
    main()
