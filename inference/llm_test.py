"""
UNIT tests related to LLMS
"""
import unittest

import box
from langchain.llms import CTransformers
from langchain.llms.fake import FakeListLLM

from .llm import setup_dbqa

cfg = box.box_from_file("./config/config.yml", "yaml")

class TestLLMs(unittest.TestCase):

    """
    Testing LLMs test case
    """
    # def test_build_llm(self):
    #     """
    #     Tests building an LLM
    #     """
    #     model = build_llm(config=cfg)
    #     self.assertIsInstance(model, CTransformers)
    #     self.assertEqual(model.model_type, cfg.MODEL_TYPE)
    #     self.assertEqual(model.model, cfg.MODEL_BIN_PATH)
    #     self.assertEqual(model.config["max_new_tokens"], cfg.MAX_NEW_TOKENS)
    #     self.assertEqual(model.config["temperature"], cfg.TEMPERATURE)

    def test_retrieval_qa(self):

        """
        Test retrieval qa
        """

        responses = [
        "Final Answer: A credit card number looks like 1289-2321-1123-2387. A fake SSN number looks like 323-22-9980. John Doe's phone number is (999)253-9876.",
        # replace with your own expletive
        "Final Answer: This is a really <expletive> way of constructing a birdhouse. This is <expletive> insane to think that any birds would actually create their <expletive> nests here.",]
        llm = FakeListLLM(responses=responses)


        dbqa=setup_dbqa(cfg,llm)

        response = dbqa({"query": "What is an LLM"})
        print(response)

if __name__ == "__main__":
    unittest.main()
