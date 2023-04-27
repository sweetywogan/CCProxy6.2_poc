import argparse
import random
import string

def generate_random_string(length):
    """
    生成一个指定长度的随机字符串
    """
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

def calculate_offset(string, substrings):
    """
    计算子字符串在字符串中对应的偏移量
    """
    offset = 0
    for s in substrings:
        idx = string.find(s)
        print(f"idx:",idx)
        if idx != -1:
            offset += idx

    return offset

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate a random string and calculate offset of given substrings.')
    parser.add_argument('-l', '--length', type=int, help='length of the generated string')
    parser.add_argument('-s', '--substrings', nargs='+', help='list of substrings to calculate offset')
    args = parser.parse_args()

    if args.length:
        string = generate_random_string(args.length)
        with open('cal.txt', 'w') as f:
            f.write(string)
        print(f'Generated random string: {string}')  

    if args.substrings:
        with open('cal.txt', 'r') as f:
            string = f.read()
        offset = calculate_offset(string, args.substrings)
        print(f'Calculated offset: {offset}')
