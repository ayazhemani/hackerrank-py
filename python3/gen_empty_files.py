"""Create helper script to auto generate directory, py file, and test file

Attributes:
    DIR_PATH (string): Path to directory where current script resides
"""
import os

DIR_PATH = os.path.dirname(os.path.realpath(__file__))


def gen_empty_files(solutions):
    """Make directories and solution py/test files

    Args:
        solutions (string[]): String array of solution names

    Returns:
        string[][]: String array of successfully created files/folders
    """
    success = []
    for solution in solutions:
        url = solution if 'hackerrank.com' in solution else ''
        url = url.split('?')[0]
        solution = solution if url is '' else solution.split('/')[-2]
        solution = solution.split('/')[-1]
        solution = solution.replace('-', '_')

        solution_dir = os.path.join(DIR_PATH, solution)
        solution_py = os.path.join(solution_dir, solution.split('/')[-1] + '.py')
        test_py = os.path.join(solution_dir, 'test_' + solution.split('/')[-1] + '.py')

        temp_success = []
        if os.path.exists(solution_dir):
            temp_success.append('')
        else:
            os.makedirs(solution_dir)
            temp_success.append('Created folder: ' + solution_dir)

        # Create python solution file if it doesn't exist.
        if (os.path.exists(solution_py) and os.path.isfile(solution_py)):
            temp_success.append('')
        else:
            with open(solution_py, 'w') as f:
                f.writelines(["\'\'\' Solution for HackerRank challenge: ",
                    solution.replace('_',' ').title(),
                    "\n", url,
                    "\n\'\'\'",
                    "\n\ndef " + solution + "():",
                    "\n\t\'\'\'Description",
                    "\n\n\tArgs:",
                    "\n\t\tname (type): description",
                    "\n\n\tReturns:",
                    "\n\t\ttype: description",
                    "\n\t\'\'\'",
                    "\n\n\treturn",
                    "\n\n\ndef main():",
                    "\n\t\'\'\'Receives input from stdin, provides output to stdout.",
                    "\n\t\'\'\'",
                    "\n\ttemp = input()",
                    "\n\treturn",
                    "\n\nif __name__ == '__main__':",
                    "\n\tmain()\n"
                    ])
            temp_success.append(solution_py.split('/')[-1])

        # Create python test cases file if it doesn't exist.
        if (os.path.exists(test_py) and os.path.isfile(test_py)):
            temp_success.append('')
        else:
            with open(test_py, 'w') as f:
                f.writelines(["\'\'\' TDD Test Cases for ",
                    solution_py.split('/')[-1],
                    "\n", url,
                    "\n\'\'\'",
                    "\n\nimport unittest",
                    "\nfrom ", solution , " import ", solution,
                    "\n\nclass Test",
                    solution.replace('_',' ').title().replace(' ',''),
                    "(unittest.TestCase):",
                    "\n\t\'\'\'Description",
                    "\n\t\'\'\'",
                    "\n\n\tdef test_hackerrank_sample1(self):",
                    "\n\t\t\'\'\'Verify provided test case.",
                    "\n\t\t\'\'\'",
                    "\n\t\tresult = ", solution, "()",
                    "\n\t\tself.assertEqual(result, None)",
                    "\n\t\treturn",
                    "\n\n\tdef test_hackerrank_sample2(self):",
                    "\n\t\t\'\'\'Verify provided test case.",
                    "\n\t\t\'\'\'",
                    "\n\t\tresult = ", solution, "()",
                    "\n\t\tself.assertEqual(result, None)",
                    "\n\t\treturn",
                    "\n\nif __name__ == '__main__':",
                    "\n\tunittest.main(exit=False)\n"
                    ])
            temp_success.append(test_py.split('/')[-1])

        success.append(temp_success)
    return success

def main():
    """Receives input from stdin, provides output to stdout.
    """
    solutions = input().split(' ')
    for solution in gen_empty_files(solutions):
        print(solution[0])
        print(solution[1], end=' ')
        print(solution[2])

if __name__ == '__main__':
    main()
