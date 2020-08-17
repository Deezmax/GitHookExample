"""A module to check a given word if it is in a certain format"""
import re
import sys


def check_branch(word):
    """Checks a given word w if its in branch format"""
    result_regex = re.compile('((feature|hotfix|test|bug|refactor)/'
                              '([a-z]|[A-Z]|[0-9])+|master|develop|release)$')
    res = result_regex.match(word)
    return res


def main(path):
    """MAIN METHOD"""

    path = path
    current_branch = open(path, "r+")
    current_branch.seek(0)
    message = current_branch.read()
    current_branch.seek(0)
    current_branch.close()

    message = message.split("heads/")[1]

    if len(message) == 0:
        sys.stdout.write("\nEMPTY BRANCHNAME ?!")
        sys.exit(1)

    result = check_branch(message)

    if result is None:
        sys.stdout.write("\nYour branch naming is invalid")
        sys.exit(1)

    sys.stdout.write("Your branch name was accepted\n")
    sys.exit(0)


if __name__ == '__main__':
    main(sys.argv.__getitem__(1))
