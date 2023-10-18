# File: esteem_LAP.py
# Author: Leandro Amaral Pereira
# Reference: https://byui-cse.github.io/cse111-course/lesson06/teach.html

def main():

    introduction_text = "This program is an implementation of the Rosenberg\n" +\
        "Self-Esteem Scale. This program will show you tenn\n" +\
        "statements that you could possibly apply to yourself.\n" +\
        "Please rate how much you agree with each of the\n" +\
        "statements by responding with one of these four letters:\n\n" +\
        "D means you strongly disagree with the statement.\n" +\
        "d means you disagree with the statement.\n" +\
        "a means you agree with the statement.\n" +\
        "A means you strongly agree with the statement.\n"

    statements = [
        {"number" : 1, "text": "I feel that I am a person of worth, at least on an equal plane with others.", "positive" : True},
        {"number" : 2, "text": "I feel that I have a number of good qualities.", "positive" : True},
        {"number" : 3, "text": "All in all, I am inclined to feel that I am a failure.", "positive" : False},
        {"number" : 4, "text": "I am able to do things as well as most other people.", "positive" : True},
        {"number" : 5, "text": "I feel I do not have much to be proud of.", "positive" : False},
        {"number" : 6, "text": "I take a positive attitude toward myself.", "positive" : True},
        {"number" : 7, "text": "On the whole, I am satisfied with myself.", "positive" : True},
        {"number" : 8, "text": "I wish I could have more respect for myself.", "positive" : False},
        {"number" : 9, "text": "I certainly feel useless at times.", "positive" : False},
        {"number" :10, "text": "At times I think I am no good at all.", "positive" : False}
    ]

    score = 0
    
    print(introduction_text)

    for statement in statements:
        print(f"{statement.get('number')}. {statement.get('text')}")
        typed_answer = input("\tEnter D, d, a, or A: ")

        score = compute_score(typed_answer, statement.get('positive'), score)

    print(f"\nYour score is {score}.")
    print("A score below 15 may indicate problematic low self-esteem.")

def compute_score(answer, is_positive, current_score):
    score = current_score + score_answer(answer, is_positive)

    return score

def score_answer(answer, is_positive):
    if is_positive:
        match answer:
            case 'D': return 0
            case 'd': return 1
            case 'a': return 2
            case 'A': return 3
    else:
        match answer:
            case 'D': return 3
            case 'd': return 2
            case 'a': return 1
            case 'A': return 0

# If this file was executed like this:
# > python example.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()
