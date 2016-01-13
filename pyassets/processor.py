# -*- coding: utf-8 -*-

class Processor():

    def __init__(self, filters=[]):
        self._filters = filters


    def proceess_group(self, group):
        output = ""
        for file in group:
            with(open(file, "r")) as f:
                file_out = f.read()
                for filter in self._filters:
                    file_out = filter.apply(file_out)

            output += file_out
        return output
