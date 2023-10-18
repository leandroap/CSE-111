def main():

    introduction = "This program is an implementation of the Rosenberg\n"+ \
        "Self-Esteem Scale. This program will show you ten\n"+ \
        "statements that you could possibly apply to yourself.\n"+ \
        "Please rate how much you agree with each of the\n"+ \
        "statements by responding with one of these four letters:\n\n"+ \
        "D means you strongly disagree with the statement.\n"+ \
        "d means you disagree with the statement.\n"+ \
        "a means you agree with the statement.\n"+ \
        "A means you strongly agree with the statement.\n"
    
    print(introduction)
    
    statements = [
        {"number" : 1, "text" : "I feel that I am a person of worth, at least on an equal plane with others.", "is_positive" : True},
        {"number" : 2, "text" : "I feel that I have a number of good qualities.", "is_positive" : True},
        {"number" : 3, "text" : "All in all, I am inclined to feel that I am a failure.", "is_positive" : False},
        {"number" : 4, "text" : "I am able to do things as well as most other people.", "is_positive" : True},
        {"number" : 5, "text" : "I feel I do not have much to be proud of.", "is_positive" : False},
        {"number" : 6, "text" : "I take a positive attitude toward myself.", "is_positive" : True},
        {"number" : 7, "text" : "On the whole, I am satisfied with myself.", "is_positive" : True},
        {"number" : 8, "text" : "I wish I could have more respect for myself.", "is_positive" : False},
        {"number" : 9, "text" : "I certainly feel useless at times.", "is_positive" : False},
        {"number" :10, "text" : "At times I think I am no good at all.", "is_positive" : False}
    ]

    score = 0

    for statement in statements:
        print(f"{statement.get('number')}. {statement.get('text')}")
        answer = input("\tEnter D, d, a, or A: ")
        score = sum_score(answer, statement.get('is_positive'), score)

    print(f"\nYour score is {score}.")
    print("A score below 15 may indicate problematic low self-esteem.")

def compute_score(answer, is_positive):
    if is_positive:
        if answer == "D":
            point = 0
        elif answer == "d":
            point = 1
        elif answer == "a":
            point = 2
        elif answer == "A":
            point = 3
    else: 
        if answer == "D":
            point = 3
        elif answer == "d":
            point = 2
        elif answer == "a":
            point = 1
        elif answer == "A":
            point = 0
    return point

def sum_score(answer, is_positive, current_score):
    score = current_score + compute_score(answer, is_positive)
    return score

# If this file was executed like this:
# > python esteem.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()