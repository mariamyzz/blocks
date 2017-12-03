from __future__ import absolute_import, unicode_literals

import os, sys
import importlib.util

PATH = os.path.dirname(os.path.abspath(__file__))
PATH_TO_BLOCKS = os.path.join(PATH, 'templates/blocks')


def split_filename(file_name: str) -> tuple:
    return os.path.splitext(file_name)


def is_python_script(file_name: str) -> bool:
    _, extension = split_filename(file_name)
    return extension == '.py'


def find_py_files(path: str) -> list:
    py_files = []
    block_attrs = os.walk(path)
    for path_to_module, _, files in block_attrs:
        py_file = [_file for _file in files if is_python_script(_file)]        
        if py_file:
            py_files.append(
                (py_file[0], os.path.join(path_to_module))
            )
    return py_files


def make_class_name(snake_case: str) -> str:
    words = snake_case.split('_')
    capitalize_words = [word.capitalize() for word in words]
    capitalize_words.append('Block')
    return ''.join(capitalize_words)


def format_name(py_files: tuple) -> list:
    formatted_names = []
    for (full_name, path) in py_files:
        name, _ = split_filename(full_name)
        class_name = make_class_name(name)
        path_to_file = os.path.join(path, full_name)
        formatted_names.append(
            {
                'class_name': class_name, 
                'path_to_file': path_to_file
            }
        )
    return formatted_names


def register_imports(formated_names: list):
    for item in formated_names:
        spec = importlib.util.spec_from_file_location(
            item['class_name'], 
            item['path_to_file']
            )
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        # registering all classes
        globals()[item['class_name']] = getattr(module, item['class_name'])

# run registering
py_files = find_py_files(PATH_TO_BLOCKS)
formatted_names = format_name(py_files)
register_imports(formatted_names)