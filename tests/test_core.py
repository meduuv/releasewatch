import unittest
from releasewatch import compare

class ReleaseWatchTests(unittest.TestCase):
    def test_compare(self):
        self.assertEqual(compare(["1.0", "1.1"], ["1.1", "1.2"]), {"added": ["1.2"], "removed": ["1.0"]})

if __name__ == "__main__":
    unittest.main()
