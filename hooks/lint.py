"""Exec python programm to evaluate a given array with file names with pylinter"""
import os
import re
import sys
from pylint import epylint as lint

PYLINT_PASS_THRESHOLD = 9.5


def main():
    """Main method that is called on startup"""
    files = sys.argv[1].split(" ")

    sys.stdout.write("STAGED FILES:")
    sys.stdout.write("STAGED FILES:")
    sys.stdout.write(str(files))

    result = []

    for file in files:
        if not file.endswith(".py") or not os.path.exists(file):
            sys.stdout.write("\n Skipped file: %s" % file)
            continue

        (pylint_stdout, pylint_stderr) = lint.py_run(file, return_std=True)

        if str(pylint_stdout.getvalue()):
            sys.stdout.write('\n' + pylint_stdout.getvalue())
        elif not str(pylint_stdout.getvalue()):
            sys.stdout.write("\nFile %s has no warning or errors!" % file)
            sys.stdout.write('\n')

        result_regex = re.compile(r"Your code has been rated at ([\d.]+)/10")
        result.append(float(result_regex.findall(pylint_stdout.getvalue())[0]))
        sys.stdout.write('\n')

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
    main()
