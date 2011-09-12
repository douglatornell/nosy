"""Unit tests for nosy.
"""
from __future__ import absolute_import
import os
from tempfile import NamedTemporaryFile
try:
    import unittest2 as unittest
except ImportError:
    import unittest


class TestNosy(unittest.TestCase):
    """Unit tests for Nosy.
    """
    def _get_target_class(self):
        from nosy.nosy import Nosy
        return Nosy


    def _make_one(self, *args, **kwargs):
        return self._get_target_class()(*args, **kwargs)


    def test_extra_paths_empty(self):
        """Zero checksum when extra_paths is empty
        """
        nosy = self._make_one()
        nosy.extra_paths = []
        nosy.paths = []  # backward compatibility for 1.0
        checksum = nosy._calc_extra_paths_checksum()
        self.assertEqual(checksum, 0)


    def test_extra_paths(self):
        """Non-zero checksum when extra_paths is not empty
        """
        nosy = self._make_one()
        tmp_file = NamedTemporaryFile()
        nosy.extra_paths = [tmp_file.name]
        nosy.paths = []  # backward compatibility for 1.0
        checksum = nosy._calc_extra_paths_checksum()
        self.assertNotEqual(checksum, 0)


    def test_extra_paths_checksum_changes(self):
        """Extra paths checksum changes when file is touched
        """
        nosy = self._make_one()
        tmp_file = NamedTemporaryFile()
        nosy.extra_paths = [tmp_file.name]
        nosy.paths = []  # backward compatibility for 1.0
        checksum1 = nosy._calc_extra_paths_checksum()
        tmp_file.write('foobar')
        tmp_file.flush()
        checksum2 = nosy._calc_extra_paths_checksum()
        self.assertNotEqual(checksum1, checksum2)


    def test_exclude_patterns_empty(self):
        """Empty exclusions set when exclude_patterns is empty
        """
        nosy = self._make_one()
        nosy.exclude_patterns = []
        exclusions = nosy._calc_exclusions('.')
        self.assertEqual(exclusions, set())
