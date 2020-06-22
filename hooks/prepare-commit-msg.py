import sys

class CustomStdOut:
    def __init__(self):
        self.old_stdout=sys.stdout

    def write(self, string):
        string = string.rstrip()
        if len(string) == 0 : return
        self.old_stdout.write(string)


def main():
    out = CustomStdOut()
    out.write(str(sys.argv) + "\n")
    out.write("SUCCESS\n")
    sys.exit(1)

if __name__ == '__main__':
    main()
