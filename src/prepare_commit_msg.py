"""Writes something into the commit msg"""
import sys


class CustomStdOut:
    """Output class"""
    def __init__(self):
        """Constructor"""
        self.old_stdout = sys.stdout

    def write(self, string):
        """Write a given string to console"""
        string = string.rstrip()
        if len(string) == 0:
            return
        self.old_stdout.write(string)


def main():
    """MAIN"""
    out = CustomStdOut()

    commit_msg_path = sys.argv.__getitem__(4)
    out.write(commit_msg_path + "\n")
    commit_msg_file = open(commit_msg_path, "w+")
    commit_msg_file.seek(0)
    string = commit_msg_file.read()
    out.write(string)
    commit_msg_file.seek(0)
    commit_msg_file.write("SHOULD BE THIS NOW")
    commit_msg_file.write("SHOULD BE THIS NOW")

    # out.write(str(sys.argv) + "\n")
    # out.write("SUCCESS\n")
    commit_msg_file.close()
    sys.exit(1)


if __name__ == '__main__':
    main()
