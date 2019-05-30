endOfWord = "$"
def generateTrieFromWordsArray(words):
   root = {}
   for word in words:
      currentDict = root
      for letter in word:
         currentDict = currentDict.setdefault(letter, {})
      currentDict[endOfWord] = endOfWord
   return root


def isWordPresentInTrie(trie, word):
   currentDict = trie
   for letter in word:
      if letter in currentDict:
         currentDict = currentDict[letter]
      else: 
         return False
   return endOfWord in currentDict


w1 = raw_input()
t = generateTrieFromWordsArray([w1])
print t
q = int(raw_input())
for i in xrange(q):
    w2 = raw_input()
    print isWordPresentInTrie(t, w2)


