# import json
# import os
# import unittest
# from fakeredis import FakeServer, FakeStrictRedis
# from fastapi.testclient import TestClient
# from hashlib import md5
# from main import app, db

# import unittest
# from fastapi.testclient import TestClient
# import json

# class TestProcessPDFEndpoint(unittest.TestCase):
#     def setUp(self):
#         self.client = TestClient(app)
#         self.test_pdf_data = b"Test PDF Data"
#         self.fake_server = FakeServer()
#         self.fake_redis = FakeStrictRedis(server=self.fake_server)

#     def tearDown(self):
#         # Clean up any files or data created during the tests
#         # Stop the fake Redis server
#         pass

#     def test_process_pdf(self):
#         response = self.client.post("/process_pdf", data=self.test_pdf_data)
#         self.assertEqual(response.status_code, 200)
#         self.assertIn("key", response.json())

#     def test_process_existing_pdf(self):
#         key = md5(self.test_pdf_data).hexdigest()
#         db[key] = self.test_pdf_data

#         response = self.client.post("/process_pdf", data=self.test_pdf_data)
#         self.assertEqual(response.status_code, 200)
#         self.assertIn("key", response.json())


# class TestDownloadPDFEndpoint(unittest.TestCase):
#     def setUp(self):
#         self.client = TestClient(app)
#         self.test_url = "https://raft.github.io/raft.pdf"

#     def tearDown(self):
#         # Clean up any files or data created during the tests
#         key = md5(str(self.test_url).encode("utf-8")).hexdigest()
#         file_name = f"./data/{key}.pdf"
#         if os.path.exists(file_name):
#             os.remove(file_name)
#         if db.get(key)is not None:
#             db.delete(key)

#     def test_download_pdf(self):
#         payload = {"url": self.test_url}
#         response = self.client.post("/download_pdf", data=json.dumps(payload))
#         self.assertEqual(response.status_code, 200)
#         self.assertIn("key", response.json())


# class TestReplyEndpoint(unittest.TestCase):
#     def setUp(self):
#         self.client = TestClient(app)
#         self.test_query = "What is the meaning of life?"

#     def tearDown(self):
#         # Clean up any data or resources created during the tests
#         pass

#     def test_reply(self):
#         payload = {"query": self.test_query}
#         response = self.client.post("/reply", data=json.dumps(payload))
#         self.assertEqual(response.status_code, 200)
#         result_data = response.json()

#         # Check if the response contains the expected keys
#         self.assertIn("answer", result_data)
#         self.assertIn("sources", result_data)

#         # Check if the "answer" is a non-empty string
#         self.assertIsInstance(result_data["answer"], str)
#         self.assertTrue(result_data["answer"].strip())

#         # Check if "sources" is a list and contains at least one source
#         self.assertIsInstance(result_data["sources"], list)
#         self.assertTrue(result_data["sources"])

#         # Check if each source in "sources" is a valid LLMSource
#         for source in result_data["sources"]:
#             self.assertIsInstance(source, dict)
#             self.assertIn("text", source)
#             self.assertIn("page", source)


# if __name__ == '__main__':
#     unittest.main()

