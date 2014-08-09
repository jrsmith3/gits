# -*- coding: utf-8 -*-
import os
import unittest
import gittool

test_dir_root = os.path.dirname(os.path.realpath(__file__))

class MethodsReturnType(unittest.TestCase):
    """
    Tests output types of the methods.
    """
    def test_list_tl_subdirs(self):
        """
        list_tl_subdirs should return a list.
        """
        self.assertIsInstance(gittool.list_tl_subdirs(test_dir_root), list)
