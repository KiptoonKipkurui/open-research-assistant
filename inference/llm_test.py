import unittest
import box
import os
from langchain.llms import CTransformers

from llm import build_llm,set_qa_prompt,setup_dbqa
class TestLLMs(unittest.TestCase):
    def test_build_llm(self):
        cfg=box.box_from_file("./config/config.yml","yaml")

        llm=build_llm(cfg=cfg)
        self.assertIsInstance(llm,CTransformers)
        self.assertEqual( llm.model_type,cfg.MODEL_TYPE)
        self.assertEqual( llm.model,cfg.MODEL_BIN_PATH)
        self.assertEqual( llm.config["max_new_tokens"],cfg.MAX_NEW_TOKENS)
        self.assertEqual( llm.config["temperature"],cfg.TEMPERATURE)
if __name__=="__main__":
    unittest.main()