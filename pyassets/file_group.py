# -*- coding: utf-8 -*-
from os import path

class FileGroup(object):

    def __init__(self, base_path, name, files=[]):
        self._base_path = base_path
        self._name = name
        self._files = files
        print("files are", self._files)

    def add(self, file):
        # todo: add possibility to add whole list
        self._files.append(file)
        return self

    def remove(self, file):
        self._files.remove(file)
        return self

    def get_files(self):
        return list(self.__iter__())

    def __iter__(self):
        for file in self._files:
            yield path.join(self._base_path, file)
