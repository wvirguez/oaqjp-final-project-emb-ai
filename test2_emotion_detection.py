from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        # Rest case for positive sentiment
        text = 'I think I am having fun'
        result_1 = emotion_detector(text)
        self.assertEqual(result_1['label'], 'SENT_POSITIVE')

if __name__ == "__main__":
    unittest.main()  