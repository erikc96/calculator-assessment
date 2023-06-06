from src.calculator import Calculator

def main():
    calc = Calculator()
    print(calc.current)
    while True:
        try:
            command = input('> ')
            if command == 'q':
                break
            result = calc.input(command)
            print(result)
        except Exception as e:
            print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
