#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#    Project: Fable Input Output
#             https://github.com/kif/fabio
#
#    Copyright (C) European Synchrotron Radiation Facility, Grenoble, France
#
#    Principal author:       Jérôme Kieffer (Jerome.Kieffer@ESRF.eu)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
"""
# Unit tests

# builds on stuff from ImageD11.test.testpeaksearch
28/11/2014
"""
from __future__ import print_function, with_statement, division, absolute_import
import unittest
import sys
import os

try:
    from .utilstest import UtilsTest
except (ValueError, SystemError):
    from utilstest import UtilsTest

logger = UtilsTest.get_logger(__file__)
fabio = sys.modules["fabio"]
import shutil


class TestHeaderNotSingleton(unittest.TestCase):

    def setUp(self):
        """
        download images
        """
        self.file1 = UtilsTest.getimage("mb_LP_1_001.img.bz2")[:-4]

    def testheader(self):
        file2 = self.file1.replace("mb_LP_1_001.img", "mb_LP_1_002.img")
        self.assertTrue(os.path.exists(self.file1))
        if not os.path.exists(file2):
            shutil.copy(self.file1, file2)
        image1 = fabio.open(self.file1)
        image2 = fabio.open(file2)
        abs_norm = lambda fn: os.path.normcase(os.path.abspath(fn))
        self.assertEqual(abs_norm(image1.header['filename']), abs_norm(self.file1))
        self.assertEqual(abs_norm(image2.header['filename']), abs_norm(file2))
        self.assertNotEqual(image1.header['filename'], image2.header['filename'])

    def tearDown(self):
        unittest.TestCase.tearDown(self)
        self.file1 = None


def test_suite_all_header():
    testSuite = unittest.TestSuite()
    testSuite.addTest(TestHeaderNotSingleton("testheader"))
    return testSuite


if __name__ == '__main__':
    mysuite = test_suite_all_header()
    runner = unittest.TextTestRunner()
    runner.run(mysuite)
