Suggest-bigram
==============
Suggest-bgram is a python library which suggests following words of a given word.

# Example
This example contains only dutch words.

- Suggested word of 'ik'  ('I' in english)
````
    bg = loadDataFromPickle('./dataset/bigram_nl')
    wl = loadDataFromPickle('./dataset/words_nl')
    obj = Gram(bg,wl);
    getFollowingWords = obj.gen_followingWordOf(obj.getIndexOfWord('Ik'))
    print(tuple(getFollowingWords))
Returns:
('heb', 'ben', 'denk', 'wil', 'weet', 'kan', 'hoop', 'was', 'geef', 'doe', 'vind', 'had', 'zal', 'zoek', 'voel', 'verwacht', 'moet', 'zou', 'zie', 'wilde', 'werk', 'probeerde',......)
````
- Suggested word of 'can'  ('can' in english)
````
    getFollowingWords = obj.gen_followingWordOf(obj.getIndexOfWord('kan'))
    print(tuple(getFollowingWords))
Returns:

['je', 'ik', 'worden', 'het', 'de', 'ook', 'hij', 'nu', 'er', 'een', 'zijn', 'u', 'niet', 'dat', 'zich', 'wel', 'nog', 'iedereen', 'gaan', 'die',....]

````
Licence
=======
[MIT](https://github.com/eronde/suggest-bigram/blob/master/LICENSE)
