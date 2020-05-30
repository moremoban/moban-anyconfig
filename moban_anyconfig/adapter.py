import anyconfig
from moban.externals.file_system import open_file, path_splitext


def loads(file_name):
    _, extension = path_splitext(file_name)
    with open_file(file_name) as any_format_file:
        content = anyconfig.loads(any_format_file.read(), ac_parser=extension[1:])
    print(content)
    return content
