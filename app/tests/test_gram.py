import unittest
from app.util.Gram import Gram

class GramTest(unittest.TestCase):
    """Docstring for GramTest. """

    def test_followingWordsOfPrevExist(self):
        """Getting tuple of (freq,currentWord) of existing prevGram
        :returns: TODO

        """
        obj = Gram(self.gramData, self.wordList)
        self.assertTupleEqual(tuple(obj.gen_bigram(3)), ((1, 8), (2, 3)))
        self.assertTupleEqual(tuple(obj.gen_bigram('3')), ((1, 8), (2, 3)))
    
    def test_sortByDesc(self):
        """ Sorting a list reserved 
        :return tupltrye
        """
        obj = Gram(self.gramData, self.wordList)
        unsortedList = obj.gen_bigram(2)
        sortedTuple = obj.sort(unsortedList)
        self.assertTupleEqual(sortedTuple, ((6, 7), (6, 0), (4, 5), (2, 6), (1, 4)))

    def test_sortByAsc(self):
        """ Sorting a list not reserved 
        :return tuple
        """
        obj = Gram(self.gramData, self.wordList)
        unsortedList = obj.gen_bigram(2)
        sortedTuple = obj.sort(unsortedList, reverse=False)
        self.assertTupleEqual(sortedTuple, ((1, 4),  (2, 6), (4, 5), (6, 0), (6, 7)))
    
    def test_getWordByIdStr(self):
        """Getting existing word from wordList by word Id (string)
        :returns: 
        """
        obj = Gram(self.gramData, self.wordList)
        self.assertEqual(obj.getWordFromId('2'), 'c')
        self.assertEqual(obj.getWordFromId(2), 'c')

    def test_nonExistingWordiByIdStr(self):
        """Getting None by non existing word from wordList (string id)
        :returns:  
        """
        obj = Gram(self.gramData, self.wordList)
        self.assertIsNone(obj.getWordFromId(99))

    def test_nonExistingWordiById(self):
        """Getting None of anon existing word from wordList
        :returns:  
        """
        obj = Gram(self.gramData, self.wordList)
        self.assertIsNone(obj.getWordFromId(99))

    def test_getWordId(self):
        """Getting existing index of word from wordList 
        :returns: 
        """
        obj = Gram(self.gramData, self.wordList)
        self.assertEqual(obj.getIndexOfWord('g'), 6)

    def test_nonExistingIdFromWord(self):
        """Getting non existing index of word from wordList
        :returns: 
        """
        obj = Gram(self.gramData, self.wordList)
        self.assertIsNone(obj.getIndexOfWord('non'))

    def test_getAllNextWordsByid(self):
        """Getting all following words given an existed previous word, sorting reverse
        :returns:

        """
        obj = Gram(self.gramData, self.wordList)
        self.assertTupleEqual(tuple(obj.gen_followingWordOf(2)), ('h', 'a', 'f', 'g', 'e'))
        self.assertTupleEqual(tuple(obj.gen_followingWordOf('2')), ('h', 'a', 'f', 'g', 'e'))
   
    def test_RaiseErrorEmptyPrevgramBygen_bigram(self):
        """Raise error on gen_bigram  for empty args
        :returns: 

        """
        obj = Gram(self.gramData, self.wordList)
        with self.assertRaises(ValueError):
            list(obj.gen_bigram(None))
        with self.assertRaises(ValueError):
            list(obj.gen_bigram(''))

    def test_raiseErrorWordExistNoBigram(self):
        """Raise error on gen_followingWordOf if word exist but no bigram
        :returns: 

        """
        obj = Gram(self.gramData, self.wordList)
        
        with self.assertRaises(ValueError):
            list(obj.gen_followingWordOf(obj.getIndexOfWord('j')))
        
    def setUp(self):
        self.gramData = [
                 [0,3,8,1],
                 [1,3,3,2],
                 [2,2,6,2],
                 [3,5,3,1],
                 [40,7,2,4],
                 [41,8,1,1],
                 [42,6,2,1],
                 [43,6,7,1],
                 [44,1,8,3],
                 [47,2,4,1],
                 [48,2,7,6],
                 [49,2,5,4],
                 [400,2,0,6]]
        self.wordList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i','j']
if __name__ == '__main__':
    unittest.main()
