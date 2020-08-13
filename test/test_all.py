"""Testing"""
import unittest
import os
import shutil
from src import check_branch
from src import check_regex
from src import check_file
from src import lint


def create_file(path, message):
    """Creates a file at current path with content message"""
    file = open(path, "x")
    file.write(message)
    file.close()


class MyTestCase(unittest.TestCase):
    """Class for test cases"""
    path: str

    def create_dir(self):
        """Creates a directory @ cwd/test/files"""
        self.path = os.getcwd()
        self.path += "/test/files"
        try:
            os.mkdir(self.path)
        except OSError:
            print("Failed @ %s" % self.path)

    def remove_dir(self):
        """Deletes the directory and everything in @ cwd/test/files"""
        try:
            shutil.rmtree(self.path)
        except OSError:
            print("Failed @ %s" % self.path)

    def test_checkbranch(self):
        """Tests the check_branch module"""
        self.create_dir()

        branch_path = self.path + "/HEAD"
        create_file(branch_path, "ref: refs/heads/feature/preMergeHook")

        with self.assertRaises(SystemExit) as sys_exit:
            check_branch.main(branch_path)
            self.assertEqual(sys_exit.exception.code, 0)

        branch_path += "1"
        create_file(branch_path, "ref: refs/heads/preMergeHook")

        with self.assertRaises(SystemExit) as sys_exit:
            check_branch.main(branch_path)
            self.assertEqual(sys_exit.exception.code, 1)

        self.remove_dir()

    def test_checkregex(self):
        """Tests the check_regex module"""
        self.create_dir()

        commit_path = self.path + "/COMMIT_EDITMSG"
        create_file(commit_path, "feat: DAS SOLLTE FUNKTIONIEREN")
        with self.assertRaises(SystemExit) as sys_exit:
            check_regex.main(commit_path)
            self.assertEqual(sys_exit.exception.code, 0)

        commit_path += "1"
        create_file(commit_path, "feature: DAS SOLLTE NICHT FUNKTIONIEREN")
        with self.assertRaises(SystemExit) as sys_exit:
            check_regex.main(commit_path)
            self.assertEqual(sys_exit.exception.code, 1)

        self.remove_dir()

    def test_checkfile(self):
        """Tests the check_file module"""

        file1 = "Test/Mehr/test/test/TestTest/alles_nice.py"
        file2 = "Nicht_Richtig.py"
        file3 = "auch_nicht_Richtig.py"
        file4 = "ebenfalls_nichT_riChtig.py"

        with self.assertRaises(SystemExit) as sys_exit:
            check_file.main(file1)
            self.assertEqual(sys_exit.exception.code, 0)

        with self.assertRaises(SystemExit) as sys_exit:
            check_file.main(file2)
            self.assertEqual(sys_exit.exception.code, 1)

        with self.assertRaises(SystemExit) as sys_exit:
            check_file.main(file3)
            self.assertEqual(sys_exit.exception.code, 1)

        with self.assertRaises(SystemExit) as sys_exit:
            check_file.main(file4)
            self.assertEqual(sys_exit.exception.code, 1)

    def test_lint(self):
        """Tests the lint module"""
        file1 = os.getcwd() + "/test/test_all.py"
        file2 = os.getcwd() + "/hooks/commit-msg"

        files = file1 + " " + file2

        with self.assertRaises(SystemExit) as sys_exit:
            lint.main(file1)
            self.assertEqual(sys_exit.exception.code, 0)

        with self.assertRaises(SystemExit) as sys_exit:
            lint.main(file2)
            self.assertEqual(sys_exit.exception.code, 0)

        with self.assertRaises(SystemExit) as sys_exit:
            lint.main(files)
            self.assertEqual(sys_exit.exception.code, 0)

    if __name__ == '__main__':
        unittest.main()
