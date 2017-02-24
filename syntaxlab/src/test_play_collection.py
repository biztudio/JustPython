import unittest
import play_collection


class TestCollection(unittest.TestCase):
    def test_normalize_name(self):
        self.raw_names = ['sTevEn lOBs', 'coCo lee', 'biLL W clinTON', 'ciRAlI Clinton']
        normalized_names = play_collection.get_normalize_names(self.raw_names)
        self.assertEqual(normalized_names, ['Steven Lobs', 'Coco Lee', 'Bill W Clinton', 'Cirali Clinton'])


    def test_normalize_name(self):
        self.raw_names = ['JAck zhaNG', 'robin zhAng', 'biLL W clinTON', 'ciRAlI Clinton']
        normalized_names = play_collection.get_normalize_names(self.raw_names)
        grouped_names = play_collection.get_names_group(normalized_names)
        self.assertEqual(grouped_names, {'Clinton': {'Cirali Clinton', 'Bill W Clinton'}, 'Zhang': {'Robin Zhang', 'Jack Zhang'}})