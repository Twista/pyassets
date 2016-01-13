# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod
from six import with_metaclass

class MetaFilter(with_metaclass(ABCMeta)):

    @abstractmethod
    def apply(self, file_content):
        pass
