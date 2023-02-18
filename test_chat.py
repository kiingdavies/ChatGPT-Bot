import io
import unittest
from requests import patch
import chat

class TestChat(unittest.TestCase):
    def test_empty_input(self):
        result = chat.get_response("")
        self.assertEqual(result, "Error: Empty input")

    def test_unrecognized_input(self):
        result = chat.get_response("random input")
        self.assertEqual(result, "I don't understand")

    def test_recognized_input(self):
        result = chat.get_response("Hello")
        self.assertEqual(result, "Hi there!")

class TestChat(unittest.TestCase):
    # test cases for get_response function

    def test_empty_input(self):
        result = chat.get_response("")
        self.assertEqual(result, "Error: Empty input")

    def test_unrecognized_input(self):
        result = chat.get_response("random input")
        self.assertEqual(result, "I don't understand")

    def test_recognized_input(self):
        result = chat.get_response("Hello")
        self.assertEqual(result, "Hi there!")

    # test cases for chat_loop function

    def test_chat_loop_quit(self):
        user_inputs = ["quit"]
        expected_outputs = ["Goodbye!"]
        with patch('builtins.input', side_effect=user_inputs):
            with patch('sys.stdout', new_callable=io.StringIO) as fake_output:
                chat.chat_loop()
                self.assertEqual(fake_output.getvalue().strip(), expected_outputs[0])

    def test_chat_loop_recognized_input(self):
        user_inputs = ["random input", "Hello", "quit"]
        expected_outputs = ["I don't understand", "Hi there!", "Goodbye!"]
        with patch('builtins.input', side_effect=user_inputs):
            with patch('sys.stdout', new_callable=io.StringIO) as fake_output:
                chat.chat_loop()
                output = fake_output.getvalue().strip().split("\n")
                self.assertEqual(output, expected_outputs)
