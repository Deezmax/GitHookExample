"""Exec python programm to evaluate a given array with file names with pylinter"""
import os
import re
import sys
from pylint import epylint as lint

PYLINT_PASS_THRESHOLD = 9.5


def main(stagedfiles):
    """Main method that is called on startup"""
    sys.stdout.write(stagedfiles)
    files = stagedfiles.split(" ")

    sys.stdout.write("STAGED FILES:")
    sys.stdout.write(str(files))

    result = []
    errors = []

    for file in files:
        if not file.endswith(".py") or not os.path.exists(file) or file.find("__init__.py") >= 0:
            sys.stdout.write("\n Skipped file: %s" % file)
            continue

        (pylint_stdout, pylint_stderr) = lint.py_run(file, return_std=True)

        if str(pylint_stdout.getvalue()):
            sys.stdout.write('\n' + pylint_stdout.getvalue())
        elif not str(pylint_stdout.getvalue()):
            sys.stdout.write("\nFile %s has no warning or errors!" % file)
            sys.stdout.write('\n')

        regex = re.compile(r"Your code has been rated at ([\d.]+)/10")

        result_regex = regex.findall(pylint_stdout.getvalue())
        sys.stdout.write('\n')

        if len(result_regex) <= 0:
            errors.append(file)
            continue

        result.append(float(result_regex[0]))

    if len(result) == 0 and len(errors) == 0:
        sys.stdout.write("NO FILES TO CHECK FOUND exit..")
        sys.exit(0)

    if len(errors) > 0:
        sys.stdout.write("Please fix all errors to process")
        sys.exit(1)

    code_result = 0
    for value in result:
        code_result += value

    code_result /= len(result)

    sys.stdout.write("Overall code rating: %f" % code_result)

    if any([(res <= PYLINT_PASS_THRESHOLD) for res in result]):
        sys.stdout.write("git: commit failed, Pylint tests failed\n")
        sys.stdout.write("Every file needs to have a greater or equal "
                         "rating to %f \n" % PYLINT_PASS_THRESHOLD)
        sys.exit(1)

    sys.exit(0)


if __name__ == '__main__':
    main(sys.argv[1])
