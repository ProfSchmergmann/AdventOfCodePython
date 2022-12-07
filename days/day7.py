import numpy as np

from days.day import Day


class Directory:
    def __init__(self, name: str, parent):
        self.name = name
        self.parent = parent
        self.directories: list[Directory] = []
        self.files: list[File] = []

    def get_size(self):
        if len(self.files) == 0 and len(self.directories) == 0:
            return 0
        size = 0
        if len(self.files) != 0:
            size += np.sum([file.size for file in self.files])
        if len(self.directories) != 0:
            size += np.sum([d.get_size() for d in self.directories])
        return size

    def add_directory(self, directory):
        self.directories.append(directory)

    def add_file(self, file):
        self.files.append(file)

    def get_dir(self, dir_name: str):
        if self.name == dir_name:
            return self
        for sub in self.directories:
            if sub.name == dir_name:
                return sub
        for sub in self.directories:
            return sub.get_dir(dir_name)
        return 'NA'

    def __str__(self, indent=2):
        res = ''
        for i in range(indent):
            res += '  '
        res += f'- {self.name} (dir, size={self.get_size()})'
        if len(self.files) != 0:
            res += '\n'
            for i in range(len(self.files)):
                res += self.files[i].__str__(indent + 2)
                res += '\n'
        if len(self.directories) != 0:
            if len(self.files) == 0:
                res += '\n'
            for i in range(len(self.directories)):
                res += self.directories[i].__str__(indent + 2)
                res += '\n'
        return res


class File:
    def __init__(self, name: str, parent: Directory, size: int):
        self.name = name
        self.parent = parent,
        self.size = size

    def __str__(self, indent=2):
        res = ''
        for i in range(indent):
            res += '  '
        res += f'- {self.name} (file, size={self.size})'
        return res


def get_dir_from_data(lines: list[str]):
    if lines[0].startswith('$ cd /'):
        root = Directory('/', None)
    current_dir: Directory = root
    for i in range(1, len(lines)):
        if lines[i].startswith('$ ls'):
            continue
        elif lines[i].startswith('$ cd ..'):
            if current_dir.parent is not None:
                current_dir = current_dir.parent
        elif lines[i].startswith('$ cd'):
            dir_name = lines[i].split('cd')[1].replace('\n', '').strip()
            d = root.get_dir(dir_name)
            current_dir = d if d != 'NA' else Directory(dir_name, current_dir)
        else:
            if lines[i].startswith('dir'):
                dir_name = lines[i].split(' ')[1].replace('\n', '')
                current_dir.add_directory(Directory(dir_name, current_dir))
            else:
                size = int(lines[i].split(' ')[0])
                file_name = lines[i].split(' ')[1].replace('\n', '')
                current_dir.add_file(File(file_name, current_dir, size))
    return root


def get_dirs_with_max_size_rek(root_dir: Directory, max_size: int):
    dirs = []
    for d in root_dir.directories:
        if d.get_size() <= max_size:
            dirs.append(d)
        dirs += get_dirs_with_max_size_rek(d, max_size)
    return dirs


class Day7(Day):

    def __init__(self):
        super().__init__(7)

    def part_a(self):
        print(get_dir_from_data(self.get_lines_as_list()))
        print('__________________________________________________________________')
        print('\n'.join(d.__str__(2) for d in
                        get_dirs_with_max_size_rek(get_dir_from_data(self.get_lines_as_list()), 100_000)))
        return np.sum(
            [d.get_size() for d in get_dirs_with_max_size_rek(get_dir_from_data(self.get_lines_as_list()), 100_000)])

    def part_b(self):
        return ' '
