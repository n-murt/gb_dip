import pathlib
from collections import namedtuple

DIRSUBJECT = namedtuple('DIRSUBJECT', ['file_name', 'ext', 'flag', 'name_dir'])


def dir_info(path):
    path = pathlib.Path(path)
    new_list = []
    for file in path.iterdir():
        new_list.append(DIRSUBJECT(file.name, file.suffix, file.is_dir(), file.parent))
        return new_list


print(dir_info(r'C:\tmp'))
