# -*- coding: utf-8 -*-
from pyassets.file_group import FileGroup
from pyassets.exceptions import GroupNotFoundException, FilterNotSupportedException
from pyassets.meta_filter import MetaFilter
from pyassets.processor import Processor

class Manager(object):

    VERSION = 0.1

    def __init__(self, base_path, filters=[]):
        self.base_path = base_path
        self._groups = {}
        self._filters = filters

    def add_group(self, name, file_list=[], type=None):
        self._groups[name] = {
            "type": type,
            "obj": FileGroup(self.base_path, name, file_list)
        }
        return self

    def get_by_name(self, group_name):
        if not group_name in self._groups:
            raise GroupNotFoundException("Group {} not found in Manager instance.".format(group_name))

        return self._groups.get(group_name)["obj"]

    def get_by_type(self, type):
        for group in self._groups:
            if group.type is type:
                yield group


    def add_filter(self, filter):
        if not isinstance(filter, MetaFilter):
            raise FilterNotSupportedException("Please implement assets.MetaFilter class")
        self._filters.append(filter)


    def output_for_group(self, group_name):
        processor = Processor(filters=self._filters)
        return processor.proceess_group(self.get_by_name(group_name))
