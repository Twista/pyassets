# -*- coding: utf-8 -*-
from pyassets.meta_filter import MetaFilter

class DummyFilter(MetaFilter):

    def apply(self, file_content):
        print("fc", file_content)
        return file_content
