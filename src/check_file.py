"""A module to check a given word if it is in a certain format"""
import re
import sys


def check_filename(word):
    """Checks a given word w if its in filename format"""
    result_regex = re.compile('([a-z]+(_[a-z]+)*|__init__).py$')
    res = result_regex.match(word)
    return res


def main(allfiles):
    """Main function that executes on start"""
    files = allfiles.split(" ")

    sys.stdout.write("Checking these files for naming:")
    sys.stdout.write(str(files))

    errors = []

    for file in files:
        if not file.endswith(".py"):
            if file.find(" "):
                sys.stdout.write("\nThe file %s contains whitespace! Remove it" % file)
            else:
                sys.stdout.write("\nFile %s contains no whitespaces: " % file)
        else:
            split = file.rsplit("/")
            if len(split) < 0:
                sys.stderr.write("\nBIG FAT ERROR")
                sys.exit(1)

            word = split[len(split) - 1]

            result = check_filename(word)

            if result is None:
                sys.stdout.write("\n" + file + " is in wrong format!")
                errors.append(file)

    if len(errors) > 0:
        sys.stdout.write("\nRename your files and try again.")
        sys.exit(1)

    sys.exit(0)


if __name__ == '__main__':
    main(sys.argv[1])
