# -*- coding: utf-8 -*-

import os
import argparse
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument('-b',
                    '--bin',
                    required=True,
                    help='path of executable clang-format')
parser.add_argument('-dir',
                    '--directory',
                    required=True,
                    help='the target directory to be formatted')

types = ['.h', '.cpp', '.cu', '.cuh', '.hpp', '.cc']
processes = []


def format_file(cmd, path):
    cmd = cmd + path
    processes.append(subprocess.Popen(cmd, shell=True))


def format_dir(cmd, root):
    dirs = os.listdir(root)
    if len(dirs) == 0:
        return 0

    for dir in dirs:
        path = os.path.join(root, dir)
        if os.path.isdir(path):
            format_dir(cmd, path)
        else:
            for suffix in types:
                if path.endswith(suffix):
                    format_file(cmd, path)


def main(cmd, dir):
    if not cmd or cmd.find('clang-format') < 0:
        print('Invalid clang-format path!')
        return -1

    cmd += ' -style=file -i -fallback-style=none '

    if os.path.isdir(dir):
        format_dir(cmd, dir)

    for p in processes:
        p.wait()


if __name__ == "__main__":
    args = parser.parse_args()
    main(args.bin, args.directory)