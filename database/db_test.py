import unittest
import box
import os
from db import build_db 
class DBTest(unittest.TestCase):
    def test_build_db(self):
        cfg=box.box_from_file("./config/config.yml","yaml")
        build_db(cfg=cfg)
        self.assertTrue(os.path.exists("vectorstore/db_faiss"))


if __name__=="__main__":
    unittest.main()