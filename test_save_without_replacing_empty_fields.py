import unittest
import tempfile
from os import path
from lxml import etree

from mailmerge import MailMerge
from tests.utils import EtreeMixin


class SaveWithoutReplacingAllFieldsTest(EtreeMixin, unittest.TestCase):
    def test(self):
        with MailMerge(path.join(path.dirname(__file__), 'test_save_without_replacing_empty_fields.docx')) as document:
            self.assertEqual(document.get_merge_fields(),
                             set(['foo', 'bar', 'gak']))

            document.merge(foo='one', gak='three')

            with tempfile.TemporaryFile() as outfile:
                document.write(outfile, erase_empty_fields = False)
                
                with MailMerge(outfile) as output:
                    self.assertEqual(document.get_merge_fields(),
                             set(['bar']))

            
