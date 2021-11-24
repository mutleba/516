# Exercise 18

# I first imported nltk and the Brown corpus to derive the text from. 
import nltk
from nltk.corpus import brown

# I then defined the text (text1).
text1 = brown.words(categories='religion')

# Then I created a function for automatically generating the most common bigrams in a text. 
def mostcommon50bigrams(text):
    # Inside the function, I first defined the bigrams I want to focus on within the text, usin the fucntion nltk.bigrams()
    bigrams = nltk.bigrams(text) 
    # Because I wanted to exclude the stopwords, I created a variable called (stopwords) to use in the next step within the frequency distribution. I specified the English stopwords from the corpus. 
    stopwords = nltk.corpus.stopwords.words('english')
    # In the frequency distribuition step, I made sure the first and second word in the bigrams are actual words, and I also used thre variable (stopwords) to exlude the stopwords.
    FreqDist = nltk.FreqDist(word for word in bigrams if word[0].isalpha() and word[1].isalpha() and word[0] not in stopwords and word[1] not in stopwords)
    return FreqDist.most_common(50)

print(mostcommon50bigrams(text1))

# Exercise 19
# To answer this question, I generally followed the same logic the book used to write the code. 
# First, I defined the frequency distribution with two pramaerers, genre and word.
cfd = nltk.ConditionalFreqDist(
        (genre, word)
        # Then I specified that all genres in the brown corpus would be used within the loop. 
        for genre in brown.categories()
        # And all words within all genres would be used.
        for word in brown.words(categories=genre))
# Then I defined the genres variable, which will subsequently used within the cfd,tabulate() function. 
genres = brown.categories()
# Then I defined a list of words I chose. The list of words was some wh-words. 
listofwhwords = ['what', 'who', 'whom', 'whose', 'which', 'when', 'where', 'why', 'whose']
# Then I used the cfd.tabulate() function with the two parameteres to produce the table and report the word frequency for all words based on the their occurance within each genre. 
print(cfd.tabulate(conditions=genres, samples=listofwhwords))
# The table does indeed show difference between genres in term of their use of the wh-words. 