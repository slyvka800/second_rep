import re
import os


def main():
    log_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "access_log")
    regex = '\[(?:0[8-9]|10)\/Mar\/2004:(?:0[7-9]|10|11):(?:(?!10)[1-3][0-9]|40|41)' \
            ':(?:3[7-9]|4\d|5[0-2]) -0800] ".*" 200'
    counter = 0

    with open(log_file_path, "r") as file:
        for line in file:
            for _ in re.finditer(regex, line):
                counter += 1
    print(counter)


if __name__ == '__main__':
    main()
