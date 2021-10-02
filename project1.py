# The code and explanation of why I chose to write the code this way is provided below:

# First, to begin working on this project, the NLTK should be downloaded. We do this using the following code: 
import nltk
nltk.download()
from nltk.book import *

# Exercise 24
# This exercise asked to find special words in text6. We should then use [] to instruct Python to access the items. 
# Then, inside the brackets, we instruct Python to look at each word in the text using the expression (w for w in text6). 
# After that, we use the conditional if to specifiy the condition and write the function. In Question (A), for example, 
# we used the function w.endswith() and add 'ise' to it to specify the word-final letters. 
# Of course, the whole code has to be written inside the function print() so that we see the output in the Terminal. 
# I followed the same logic to write the code of the other questions in Exercise 24. 

# (a)
print([w for w in text6 if w.endswith('ise')])

# (b)
# Here, the code instruct python to look for words containing 'z'. 
print([w for w in text6 if 'z' in w])

# (c)
#Here, the code instruct python to look for words containing 'pt'. 
print([w for w in text6 if 'pt' in w])

# (d) 
# Here, the function w.istitle() is used to produce words with case characters and the word-initial letter is capital. 
print([w for w in text6 if w.istitle()])

# Exercise 25
# This exercise asked to define a variable "sent" consisting of a list of words, and print words with specific conditions.
# To define the variable, we use the assignment process where we use the "=" sign, followed by the list of items between []. 
# The following code defines the variable "sent".
sent = ['she', 'sells', 'sea', 'shells', 'by', 'the', 'sea', 'shore']

# Similar to the Exercise 24, we have to use the [] to insruct Python to access the items and specify the variable "sent".
# We then have to use the conditional if followed by the required function. 
# in (a), we use the function .startswith() to specify the word-initial sh.
# (a)
print([w for w in sent if w.startswith('sh')])

# (b)
# In (b), we use the function len() to specify the length > 4
print([w for w in sent if len(w) > 4])