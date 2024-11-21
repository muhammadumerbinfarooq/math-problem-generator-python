import random

def generate_problem(operation, difficulty):
    # Generate numbers based on difficulty level
    if difficulty == "Easy":
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
    elif difficulty == "Medium":
        num1 = random.randint(10, 50)
        num2 = random.randint(10, 50)
    else:  # Hard
        num1 = random.randint(50, 100)
        num2 = random.randint(50, 100)

    # Generate problem based on operation
    if operation == "Addition":
        problem = f"What is {num1} + {num2}? "
    elif operation == "Subtraction":
        problem = f"What is {num1} - {num2}? "
    elif operation == "Multiplication":
        problem = f"What is {num1} × {num2}? "
    else:  # Division
        problem = f"What is {num1} ÷ {num2}? "

    return problem

def main():
    print("Math Problem Generator")
    operation = input("Choose operation (Addition, Subtraction, Multiplication, Division): ")
    difficulty = input("Choose difficulty level (Easy, Medium, Hard): ")
    num_problems = int(input("Enter number of problems: "))

    for i in range(num_problems):
        problem = generate_problem(operation, difficulty)
        print(problem)

if __name__ == "__main__":
    main()
