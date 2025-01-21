import random

def calculation_game():
    print("Hello, what is your name?")
    name = input()
    print(f"{name.upper()}, good luck in the calculation game!")
    print("You have the option to choose the game length:")
    print("1. 5 questions")
    print("2. 10 questions")
    
    # Ask the user how many questions they want
    while True:
        game_choice = input("Choose 1 (5 questions) or 2 (10 questions): ")
        if game_choice not in ['1', '2']:
            print("Please choose either 1 or 2.")
        else:
            game_length = 5 if game_choice == '1' else 10
            break

    print(f"In this game, you will solve exactly {game_length} calculations using addition and subtraction.")

    correct_answers = 0  # To count correct answers
    
    for i in range(1, game_length + 1):  # Repeat based on the chosen game length
        # Randomly choose the operation (addition or subtraction)
        operation = random.choice(['+', '-'])
        
        # Generate a random question based on the operation
        if operation == '+':
            # Addition calculations up to 10
            number1 = random.randint(1, 10)
            number2 = random.randint(1, 10)
        else:
            # Subtraction calculations up to 10 (number1 must be greater than or equal to number2)
            number1 = random.randint(1, 10)
            number2 = random.randint(1, number1)  # To avoid negative results
        
        # Calculate the correct answer
        if operation == '+':
            correct_answer = number1 + number2
        else:
            correct_answer = number1 - number2
        
        # Ask the user for their answer
        while True:  # Loop until valid input is provided
            user_answer = input(f"Calculation {i}: What is {number1} {operation} {number2}? ")
            if user_answer.strip() == "":  # Check for empty input
                print("Please enter an answer!\n")
            else:
                try:
                    user_answer = int(user_answer)  # Try converting to integer
                    break  # If successful, exit the loop
                except ValueError:
                    print("Please enter a valid numeric value!\n")
        
        # Check if the answer is correct
        if user_answer == correct_answer:
            print("Correct answer! Well done!\n")
            correct_answers += 1  # If correct, increase the count of correct answers
        else:
            print(f"Wrong answer. The correct answer was {correct_answer}.\n")
    
    # At the end of the game, display the summary
    print(f"The game is over! You answered {correct_answers} questions correctly.\nThank you for playing, {name.upper()}!")

# Start the game
calculation_game()