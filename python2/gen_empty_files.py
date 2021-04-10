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
        temp_success = []
        if not os.path.exists(DIR_PATH + '/' + solution):
            os.makedirs(DIR_PATH + '/' + solution)
            temp_success.append('Created folder: ' + DIR_PATH + '/' + solution + '\n')
        # Create python solution file if it doesn't exist.
        try:
            pfile = open(DIR_PATH + '/' + solution +'/' + solution.split('/')[-1] + '.py', 'r')
        except IOError:
            pfile = open(DIR_PATH + '/' + solution +'/' + solution.split('/')[-1] + '.py', 'w')
            temp_success.append(pfile.name)
        # Create python test cases file if it doesn't exist.
        try:
            tfile = open(DIR_PATH + '/' + solution +'/' + 'test_' + solution.split('/')[-1] + '.py', 'r')
        except IOError:
            tfile = open(DIR_PATH + '/' + solution +'/' + 'test_' + solution.split('/')[-1] + '.py', 'w')
            temp_success.append(tfile.name)
        success.append(temp_success)
    return success

def main():
    """Receives input from stdin, provides output to stdout.
    """
    solutions = raw_input().split(' ')
    for solution in gen_empty_files(solutions):
        for files in solution:
            if files[-1] != '\n':
                print files.split('/')[-1],
            else:
                print files,
        print ''

if __name__ == '__main__':
    main()
