import re

regex_branch = "^(feature|hotfixes|test|bug|refactor)\/([a-z]|[A-Z]|[0-9])+$"
regex_commit = "^(docs|feat|fix|refactor|style|test)\:\s([a-z]|[A-Z]|\s|[0-9])+\.?$"


def check_for_regex(w, regex):
    """Checks a given word w if its regex"""
    result_regex = re.compile(regex)
    res = result_regex.match(w)
    return res


def main():
    """MAIN METHOD"""
    #TODO check for branch commit
    print(check_for_regex("feature/abc", regex_branch))


if __name__ == '__main__':
    main()
