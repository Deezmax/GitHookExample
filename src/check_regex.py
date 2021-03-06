"""A module to check a given word if it is in a certain format"""
import re
import sys
import os


def check_commit(word):
    """Checks a given word w if its in commit format"""
    result_regex = re.compile('(docs|feat|fix|refactor|style|test)'
                              ':\\s([a-z]|[A-Z]|\\s|[0-9]|[\\W]|_)+?$')
    res = result_regex.match(word)
    return res


def main(commit_msg_path):
    """MAIN METHOD"""

    if not os.path.exists(commit_msg_path):
        sys.stdout.write("Path %s not found." % commit_msg_path)
        exit(1)
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
    main(sys.argv.__getitem__(1))
