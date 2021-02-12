import unittest
import speech_recognition as sr

import main as main

class TestVoiceRecognition(unittest.TestCase):

    def test_voice_recognition(self):
        r = sr.Recognizer()
        audio = r.listen(source)
        self.assertNotNull(audio)

    def test_input(self):
        pass

    if __name__ == "__main__":
        unittest.main()