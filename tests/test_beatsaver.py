import unittest

from src.pybeatsaver import NotFoundException
from src.pybeatsaver.beatsaver import BeatSaver


class TestBeatSaver(unittest.TestCase):
    _valid_map_hash = "4bbdaa1004a00eeb9c8d9432640e1c7d490b46d9"
    _invalid_map_hash = "4BDAA104A00E32EB9CD941132640E1C7490B4932"
    _valid_map_key = "19487"
    _invalid_map_key = "153423234235"

    def setUp(self):
        self.beatsaver = BeatSaver()

    def test_get_map_by_hash_valid(self):
        map_detail = self.beatsaver.get_map_by_hash(self._valid_map_hash)
        self.assertEqual(map_detail.versions[0].hash, self._valid_map_hash)

    def test_get_map_by_hash_invalid(self):
        self.assertRaises(NotFoundException, self.beatsaver.get_map_by_hash, self._invalid_map_hash)

    def test_get_map_by_key(self):
        map_detail = self.beatsaver.get_map_by_key(self._valid_map_key)

        self.assertEqual(map_detail.versions[0].key, self._valid_map_key)

    def test_get_map_by_key_invalid(self):
        self.assertRaises(NotFoundException, self.beatsaver.get_map_by_key, self._invalid_map_key)
