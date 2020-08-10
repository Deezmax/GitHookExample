"""A package to check a given word if it is in a certain format"""
import re
import sys


def check_commit(word):
    """Checks a given word w if its in commit format"""
    result_regex = re.compile('(docs|feat|fix|refactor|style|test):\\s([a-z]|[A-Z]|\\s|[0-9]|\\.)+?')
    res = result_regex.match(word)
    return res


def check_branch(word):
    """Checks a given word w if its in branch format"""
    result_regex = re.compile('(feature|hotfixes|test|bug|refactor)/([a-z]|[A-Z]|[0-9])+')
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

    if len(message) == 0:
        sys.stdout.write("\nEMPTY MESSAGE")
        sys.exit(1)

    result = check_commit(message)

    if result is None:
        sys.exit(1)

    sys.stdout.write("Your commit-message was accepted\n")
    sys.exit(0)


if __name__ == '__main__':
    main()
