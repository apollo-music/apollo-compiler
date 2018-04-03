import os


def run_tests():
    dirs = os.listdir()
    for dir in dirs:
        if os.path.isdir(dir):
            os.system('python3 ' + dir + '/test_' + dir + '.py')


if __name__ == '__main__':
    run_tests()
