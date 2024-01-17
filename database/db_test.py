"""
Database TEST module
"""
import os
import unittest

import box

from database.db import build_db


class DBTest(unittest.TestCase):
    """
    DBTest test suite
    """
    def test_build_db(self):
        """
        Test building of database
        """
        cfg = box.box_from_file("./config/config.yml", "yaml")
        build_db(config=cfg)
        self.assertTrue(os.path.exists("./vectorstore/db_faiss"))


if __name__ == "__main__":
    unittest.main()
