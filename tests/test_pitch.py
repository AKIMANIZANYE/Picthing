import unittest
from app.models import Pitch

class PitchModelTest(unittest.TestCase):

    def setUp(self):
        self.new_pitch = Pitch(pitch = 'Where does sad music get its sadness from? And whom should you ask—a composer or a cognitive psychologist?', category_id = 1, user_id=1)


    def test_instance(self):
        self.assertTrue(isinstance(self.new_pitch, Pitch))

    def test_save_comment(self):
        self.new_pitch.save_pitch()
        self.assertTrue(len(Pitch.query.all())>0)