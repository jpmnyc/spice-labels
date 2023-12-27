# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def main():
    input = open("template.ps", "r")
    text = "".join(input.readlines())
    output = open("build/print.ps", "w")
    output.write(text)
    del output


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
