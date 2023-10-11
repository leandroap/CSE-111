# File: 04-Prove_sentences.py
# Author: Leandro Amaral Pereira
# Reference: https://byui-cse.github.io/cse111-course/lesson04/prove.html
import random

# Function to print some decorative elements
def print_elements(option): 
    break_line = "\n*****************************************************\n"
    header       = "*   Welcome to Prove Milestone: Writing Functions   *"
    footer       = "*                  Thank you! Bye.                  *"

    if option == "header":
        print(f"{break_line}{header}{break_line}")
    elif option == "footer":
        print(f"{break_line}{footer}{break_line}")

def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "some", "many".
    If quantity is 1, this function will return either "a",
    "one", or "the". Otherwise this function will return
    either "some", "many", or "the".

    Parameter
        quantity: an integer.
            If quantity is 1, this function will return a
            determiner for a single noun. Otherwise this
            function will return a determiner for a plural
            noun.
    Return: a randomly chosen determiner.
    """
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

def get_noun(quantity):
    """Return a randomly chosen noun.
    If quantity is 1, this function will
    return one of these ten single nouns:
        "bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"
    Otherwise, this function will return one of
    these ten plural nouns:
        "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"

    Parameter
        quantity: an integer that determines if
            the returned noun is single or plural.
    Return: a randomly chosen noun.
    """

    if quantity == 1:
        nouns = ["bird", "boy", "car", "cat", "child",
                  "dog", "girl", "man", "rabbit", "woman"]
    else:
        nouns = ["birds", "boys", "cars", "cats", "children",
                  "dogs", "girls", "men", "rabbits", "women"]

    # Randomly choose and return a noun.
    noun = random.choice(nouns)
    return noun

def get_verb(quantity, tense):
    """Return a randomly chosen verb. If tense is "past",
    this function will return one of these ten verbs:
        "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"
    If tense is "present" and quantity is 1, this
    function will return one of these ten verbs:
        "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and quantity is NOT 1,
    this function will return one of these ten verbs:
        "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"
    If tense is "future", this function will return one of
    these ten verbs:
        "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"

    Parameters
        quantity: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """

    if tense == "past":
        verbs = ["drank", "ate", "grew", "laughed", "thought",
                  "ran", "slept", "talked", "walked", "wrote"]
    elif tense == "present" and quantity == 1:
        verbs = ["drinks", "eats", "grows", "laughs", "thinks",
                  "runs", "sleeps", "talks", "walks", "writes"]
    elif tense == "present" and quantity != 1:
        verbs = ["drink", "eat", "grow", "laugh", "think",
                  "run", "sleep", "talk", "walk", "write"]
    elif tense == "future":
        verbs = ["will drink", "will eat", "will grow", "will laugh",
                  "will think", "will run", "will sleep", "will talk",
                   "will walk", "will write"]

    # Randomly choose and return a verb.
    verb = random.choice(verbs)
    return verb

def get_preposition():
    """Return a randomly chosen preposition
    from this list of prepositions:
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"

    Return: a randomly chosen preposition.
    """

    prepositions = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    
    # Randomly choose and return a preposition.
    return random.choice(prepositions)

def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed
    of three words: a preposition, a determiner, and a
    noun by calling the get_preposition, get_determiner,
    and get_noun functions.

    Parameter
        quantity: an integer that determines if the
            determiner and noun in the prepositional
            phrase returned from this function should
            be single or pluaral.
    Return: a prepositional phrase.
    """

    preposition = get_preposition()
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    adjective = get_adjective()

    # Build and return a prepositional phrase
    prepositional_phrase = f"{preposition} {determiner} {adjective} {noun}"
    return prepositional_phrase

def get_adjective():
    """Return a randomly chosen adjective
    from this list of adjectives:
            "beautiful", "brave", "clever", "colorful", "delicious",
            "energetic", "funny", "happy", "intelligent", "joyful",
            "kind", "lively", "mysterious", "playful", "quiet",
            "radiant", "strong", "red", "blue", "green",
            "gentle", "charming", "graceful", "fearless", "sincere",
            "vibrant", "creative", "thoughtful", "serene", "powerful",
            "orange", "yellow", "purple", "peaceful", "generous",
            "adventurous", "compassionate", "ambitious", "black", "white",
            "inspiring", "pink", "inventive", "elegant", "cheerful"

    Return: a randomly chosen adjective.
    """
    
    adjectives = [
        "beautiful", "brave", "clever", "colorful", "delicious",
        "energetic", "funny", "happy", "intelligent", "joyful",
        "kind", "lively", "mysterious", "playful", "quiet",
        "radiant", "strong", "red", "blue", "green",
        "gentle", "charming", "graceful", "fearless", "sincere",
        "vibrant", "creative", "thoughtful", "serene", "powerful",
        "orange", "yellow", "purple", "peaceful", "generous",
        "adventurous", "compassionate", "ambitious", "black", "white",
        "inspiring", "pink", "inventive", "elegant", "cheerful"]

    # Randomly choose and return a preposition.
    return random.choice(adjectives)

def make_sentence(quantity, tense):
    """Build and return a sentence with three words:
    a determiner, a noun, and a verb. The grammatical
    quantity of the determiner and noun will match the
    number in the quantity parameter. The grammatical
    quantity and tense of the verb will match the number
    and tense in the quantity and tense parameters.
    """

    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    prepositional_phrase = get_prepositional_phrase(quantity)
    adjective = get_adjective()

    # Build and return a sentence
    sentense = f"{determiner} {adjective} {noun} {verb} {prepositional_phrase}.".capitalize()
    return sentense

def main():
    print_elements("header")

    #Scenarios for Testing Procedure
    scenarios = [
        {"quantity" : 1, "verb_tense" : "past"},
        {"quantity" : 1, "verb_tense" : "present"},
        {"quantity" : 1, "verb_tense" : "future"},
        {"quantity" : 2, "verb_tense" : "past"},
        {"quantity" : 2, "verb_tense" : "present"},
        {"quantity" : 2, "verb_tense" : "future"}
    ]

    # Loops through the scenarios
    for step in scenarios:
        print(make_sentence(step.get("quantity"), step.get("verb_tense")))

    print_elements("footer")
# Start this program by calling the main function.
main()