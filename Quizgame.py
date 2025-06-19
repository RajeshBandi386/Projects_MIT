questions = [
    {
        "question": "What is the capital of France?",
        "options": ["London", "Paris", "Berlin", "Rome"],
        "answer": "Paris"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Venus"],
        "answer": "Mars"
    }
]

score = 0

print("Welcome to the Python Quiz Game!")

for q_data in questions:
    print(f"\nQuestion: {q_data['question']}")
    for i, option in enumerate(q_data['options']):
        print(f"{i+1}. {option}")

    user_answer = input("Enter the number of your choice: ")
    try:
        user_choice_index = int(user_answer) - 1
        if 0 <= user_choice_index < len(q_data['options']):
            if q_data['options'][user_choice_index] == q_data['answer']:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The correct answer was: {q_data['answer']}")
        else:
            print("Invalid choice. Please enter a valid number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

print(f"\nQuiz completed! Your final score is: {score}/{len(questions)}")