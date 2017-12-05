import unittest

from guess import Guess
from hangman import Hangman


class TestGuess(unittest.TestCase):

    def setUp(self):
        self.g1 = Guess('default')
        self.g2 = Hangman()

    def testDisplayCurrent(self):
        self.assertEqual(self.g1.currentStatus, '_e_____')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ _ _ _ _ ')

        self.g1.guess('a')
        self.assertEqual(self.g1.currentStatus, '_e_a___')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a _ _ _ ')

        self.g1.guess('t')
        self.assertEqual(self.g1.currentStatus, '_e_a__t')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a _ _ t ')

        self.g1.guess('u')
        self.assertEqual(self.g1.currentStatus, '_e_au_t')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a u _ t ')

        self.g1.guess('f')
        self.assertEqual(self.g1.currentStatus, '_efau_t')
        self.assertEqual(self.g1.displayCurrent(), '_ e f a u _ t ')

        self.g1.guess('d')
        self.assertEqual(self.g1.currentStatus, 'defau_t')
        self.assertEqual(self.g1.displayCurrent(), 'd e f a u _ t ')

        self.g1.guess('l')
        self.assertEqual(self.g1.currentStatus, 'default')
        self.assertEqual(self.g1.displayCurrent(), 'd e f a u l t ')

    def testDisplayGuessed(self):
        self.assertEqual(self.g1.displayGuessed(), ' e n ')
        self.g1.guess('a')
        self.assertEqual(self.g1.displayGuessed(), ' a e n ')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t ')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t u ')
        self.g1.guess('d')
        self.assertEqual(self.g1.displayGuessed(), ' a d e n t u ')
        self.g1.guess('f')
        self.assertEqual(self.g1.displayGuessed(), ' a d e f n t u ')
        self.g1.guess('l')
        self.assertEqual(self.g1.displayGuessed(), ' a d e f l n t u ')

    def testGuess(self):
        self.assertEqual(self.g1.displayCurrent(), '_ _ _ _ _ _ _ ')
        self.assertEqual(self.g1.displayCurrent(), ' ')
        self.g1.guess('e')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ _ _ _ _ ')
        self.assertEqual(self.g1.displayCurrent(), ' e ')
        self.g1.guess('n')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ _ _ _ _ ')
        self.assertEqual(self.g1.displayGuessed(), ' e n ')
        self.g1.guess('a')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a _ _ _ ')
        self.assertEqual(self.g1.displayGuessed(), ' e n a ')
        self.g1.guess('s')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a _ _ _ ')
        self.assertEqual(self.g1.displayGuessed(), ' e n a s ')
        self.g1.guess('1')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a _ _ _ ')
        self.assertEqual(self.g1.displayGuessed(), ' e n a s ')
        self.g1.guess('?')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a _ _ _ ')
        self.assertEqual(self.g1.displayGuessed(), ' e n a s ')
        self.g1.guess('')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a _ _ _ ')
        self.assertEqual(self.g1.displayGuessed(), ' e n a s ')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a _ _ t ')
        self.assertEqual(self.g1.displayGuessed(), ' e n a s t ')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a u _ t ')
        self.assertEqual(self.g1.displayGuessed(), ' e n a s t u ')
        self.g1.guess('d')
        self.assertEqual(self.g1.displayCurrent(), 'd e _ a u _ t ')
        self.assertEqual(self.g1.displayGuessed(), ' e n a s t u d ')
        self.g1.guess('f')
        self.assertEqual(self.g1.displayCurrent(), 'd e f a u _ t ')
        self.assertEqual(self.g1.displayGuessed(), ' e n a s t u d f ')
        self.g1.guess('l')
        self.assertEqual(self.g1.displayCurrent(), 'd e f a u l t ')
        self.assertEqual(self.g1.displayGuessed(), ' e n a s t u d f l ')

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
