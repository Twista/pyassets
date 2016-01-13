# -*- coding: utf-8 -*-
from pyassets.meta_filter import MetaFilter
import coffeescript


class CoffeeScriptFilter(MetaFilter):

    def apply(self, file_content):
        return coffeescript.compile(file_content)
