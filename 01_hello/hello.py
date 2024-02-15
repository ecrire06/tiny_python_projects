#!/usr/bin/env python3
"""
만든이: 준하 <https://junchive.kr>
이메일: juneha2002@gmail.com
목적: 인사하기
"""

import argparse


def get_args():
    """Get the command-line arguments"""

    parser = argparse.ArgumentParser(description='인사하기')
    parser.add_argument('-n',
                        '--name',
                        metavar='name',
                        default='World',
                        help='이름을 입력하세요')
    return parser.parse_args()


def main():
    """First Step Is Half of The Journey"""

    args = get_args()
    print('Hello, ' + args.name + '!')


if __name__ == '__main__':
    main()
