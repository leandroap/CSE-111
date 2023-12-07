# File: fruit.py
# Author: Leandro Amaral Pereira
# Reference: https://byui-cse.github.io/cse111-course/lesson12/check.html

def main():

    try:
        # Create and print a list named fruit.
        fruit_list = ["pear", "banana", "apple", "mango"]
        print(f"original: {fruit_list}\n")

        fruit_list.reverse()
        print(f"reverse: {fruit_list}\n")

        fruit_list.append("orange")
        print(f"append orange: {fruit_list}\n")

        i = fruit_list.index("apple")
        fruit_list.insert(i, "cherry")
        print(f"insert cherry: {fruit_list}\n")

        fruit_list.remove("banana")
        print(f"remove banana: {fruit_list}\n")

        popped = fruit_list.pop()
        print(f"pop {popped}: {fruit_list}\n")

        fruit_list.sort()
        print(f"sorted: {fruit_list}\n")

        fruit_list.clear()
        print(f"cleared: {fruit_list}\n")
        
    except IndexError as index_err:
        print(type(index_err).__name__, index_err, sep=": ")

if __name__ == "__main__":
    main()