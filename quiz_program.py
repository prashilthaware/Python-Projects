# Define a dictionary with questions, options, and answers
quiz_questions = {
    "What is the capital of France?": {
        "A": "Berlin",
        "B": "Paris",
        "C": "London",
        "D": "Rome",
        "Answer": "B"
    },
    "Which planet is the largest in our solar system?": {
        "A": "Earth",
        "B": "Saturn",
        "C": "Jupiter",
        "D": "Uranus",
        "Answer": "C"
    },
    "Who painted the famous painting 'The Starry Night'?": {
        "A": "Leonardo da Vinci",
        "B": "Vincent van Gogh",
        "C": "Pablo Picasso",
        "D": "Claude Monet",
        "Answer": "B"
    },
    "What is the chemical symbol for gold?": {
        "A": "Ag",
        "B": "Au",
        "C": "Hg",
        "D": "Pb",
        "Answer": "B"
    },
    "Which musician is known as the 'King of Rock and Roll'?": {
        "A": "Elvis Presley",
        "B": "Chuck Berry",
        "C": "Little Richard",
        "D": "Jerry Lee Lewis",
        "Answer": "A"
    },
    "What is the largest living species of lizard?": {
        "A": "Komodo dragon",
        "B": "Saltwater crocodile",
        "C": "Black mamba",
        "D": "African elephant",
        "Answer": "A"
    },
    "Who wrote the famous novel 'To Kill a Mockingbird'?": {
        "A": "F. Scott Fitzgerald",
        "B": "Harper Lee",
        "C": "Jane Austen",
        "D": "J.K. Rowling",
        "Answer": "B"
    },
    "What is the smallest country in the world, both in terms of population and land area?": {
        "A": "Vatican City",
        "B": "Monaco",
        "C": "Nauru",
        "D": "Tuvalu",
        "Answer": "A"
    },
    "Which artist created the famous sculpture 'David'?": {
        "A": "Michelangelo",
        "B": "Leonardo da Vinci",
        "C": "Raphael",
        "D": "Donatello",
        "Answer": "A"
    }
}

def quiz_program():
    score = 0
    for question, options in quiz_questions.items():
        print(question)
        for option, value in options.items():
            if option != "Answer":
                print(f"{option}: {value}")
        answer = input("Enter your answer (A, B, C, D): ")
        if answer.upper() == options["Answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Sorry, the correct answer is {options['Answer']}.")
    print(f"\nQuiz finished! Your final score is {score} out of {len(quiz_questions)}.")

def main():
    print("Welcome to the Quiz Program!")
    play_again = "yes"
    while play_again.lower() == "yes":
        quiz_program()
        play_again = input("Would you like to play again? (yes/no): ")
    print("Thanks for playing!")

if __name__ == "__main__":
    main()