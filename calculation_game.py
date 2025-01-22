import random

def get_user_name():
    print("Hello, what is your name?")
    return input("Enter your name: ")

def choose_game_length():
    print("You have the option to choose the game length:")
    print("1. 5 questions")
    print("2. 10 questions")
    while True:
        game_choice = input("Choose 1 for 5 questions or 2 for 10 questions: ")
        if game_choice in ['1', '2']:
            return 5 if game_choice == '1' else 10
        print("Please choose either 1 or 2.")

def generate_question():
    operation = random.choice(['+', '-'])
    if operation == '+':
        number1 = random.randint(1, 10)
        number2 = random.randint(1, 10)
        correct_answer = number1 + number2
    else:
        number1 = random.randint(1, 10)
        number2 = random.randint(1, number1)
        correct_answer = number1 - number2
    return number1, operation, number2, correct_answer

def get_user_answer(question):
    while True:
        user_answer = input(question)
        if user_answer.strip():
            try:
                return int(user_answer)
            except ValueError:
                print("Please enter a valid numeric value!\n")
        else:
            print("Please enter an answer!\n")

def calculation_game(name, game_length):
    correct_answers = 0
    for i in range(1, game_length + 1):
        number1, operation, number2, correct_answer = generate_question()
        user_answer = get_user_answer(f"Calculation {i}: What is {number1} {operation} {number2}? ")
        if user_answer == correct_answer:
            print("Correct answer! Well done!\n")
            correct_answers += 1
        else:
            print(f"Wrong answer. The correct answer was {correct_answer}.\n")
    print(f"The game is over! You answered {correct_answers} questions correctly.")
    print(f"Thank you for playing, {name.upper()}!")

def main():
    name = get_user_name()
    print(f"{name.upper()}, good luck in the calculation game!")
    game_length = choose_game_length()
    calculation_game(name, game_length)

if __name__ == "__main__":
    main()