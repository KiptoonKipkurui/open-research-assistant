"""
UNIT tests related to LLMS
"""
import unittest
import box
from langchain.llms import CTransformers

from .llm import build_llm


class TestLLMs(unittest.TestCase):

    """
    Testing LLMs test case
    """
    def test_build_llm(self):
        """
        Tests building an LLM
        """
        cfg = box.box_from_file("./config/config.yml", "yaml")

        llm = build_llm(cfg=cfg)
        self.assertIsInstance(llm, CTransformers)
        self.assertEqual(llm.model_type, cfg.MODEL_TYPE)
        self.assertEqual(llm.model, cfg.MODEL_BIN_PATH)
        self.assertEqual(llm.config["max_new_tokens"], cfg.MAX_NEW_TOKENS)
        self.assertEqual(llm.config["temperature"], cfg.TEMPERATURE)


if __name__ == "__main__":
    unittest.main()
