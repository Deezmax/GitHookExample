"""A module to check a given word if it is in a certain format"""
import re
import sys


def check_branch(word):
    """Checks a given word w if its in branch format"""
    result_regex = re.compile('((feature|hotfixes|test|bug|refactor)/'
                              '([a-z]|[A-Z]|[0-9])+|master|develop)$')
    res = result_regex.match(word)
    return res


def main():
    """MAIN METHOD"""

    commit_msg_path = sys.argv.__getitem__(1)
    commit_msg_file = open(commit_msg_path, "r+")
    commit_msg_file.seek(0)
    message = commit_msg_file.read()
    commit_msg_file.seek(0)
    commit_msg_file.close()

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
    main()