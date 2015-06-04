class Gram(object):
    """Gram class
    :TODO error handling, look aat set for wordList (performance? )
    :bigram: list [0]=id,[1]=prevgram,[2]=currentword,[3]=freq
    # """
    def __init__(self, gramData, wordList=None):
        self.gramData = gramData
        self.wordList = wordList
    
    def gen_bigram(self, prevGram):
        """gen_bigram: Generate frequency and the current word
        of bigram with "prevGram"

        :prevGram: previous word in int
        :returns: Generator tulip with freq, following word

        """
        if not prevGram:
            raise ValueError('prevGram %s:',prevGram)

        if type(prevGram) is not int:
            prevGram = int(prevGram)
        return ((row[3], row[2]) for row in self.gramData if row[1] == prevGram )
 
    
    def sort(self, listOfTuple, reverse=True):
        """
        :listOfTuple: TODO
        :reverse: default true
        :returns:  tulp

        """
        return tuple(sorted(listOfTuple, reverse=reverse))
    
    def getWordFromId(self, wordId):
        """getWordFromId: Getting word with wordId stored in wordList.

        :wordId: int
        :returns: string / None
        """
        try:
            return self.wordList[int(wordId)]
        except(IndexError):
            return None

    def getIndexOfWord(self, word):
        """getIndexOfWord: Getting index of word

        :word: string
        :returns: int/None
        """
        if not word:
            raise ValueError('invalid type:',prevGram)
        if str(word) in self.wordList:
            return self.wordList.index(str(word))
        else:
            return None

    def gen_followingWordOf(self,  prevGram):
        """gen_followingWordOf, Generate following word
           of giving previous word (prevGram)

        :prevGram: int
        :returns: generator string
        
        """
        getFollowingWords = self.gen_bigram(prevGram)
        sortWords = self.sort(getFollowingWords)
        retreiveWords = [currentWord for (freq, currentWord) in sortWords]
        idToWords = tuple(map(self.getWordFromId, retreiveWords))
        return (followingWord for followingWord in idToWords)
