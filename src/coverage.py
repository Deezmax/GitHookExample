"""Coverage analysis"""
import sys
import re

coverage_threshold: int = 75


def main(report):
    """Main function"""
    if not report:
        sys.stdout.write("Report is empty. Completion with error.")
        sys.exit(1)

    regex = re.compile(r"TOTAL\s+([\d]+)\s+([\d]+)\s+([\d]+)%")
    result = regex.findall(report)

    if len(result) <= 0:
        sys.stdout.write("Something bad happend")
        sys.exit(1)

    if int(result[0][2]) <= coverage_threshold:
        sys.stdout.write("Your code coverage is below the threshold of %d" % coverage_threshold)
        sys.exit(1)

    sys.stdout.write("Your total code coverage is %s" % result[0][2])
    sys.exit(0)


if __name__ == '__main__':
    main(sys.argv[1])
