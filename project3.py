# First, I imported regular expressions.
import re
# Second, I assigned a variable named "string" to a text file containing the text I want to change. 
string = open('string.txt').read()
# Replacing "nce" with "nse"
# In a variable named "string", using the function re.sub(), I instructed python to replace any  literal string "nce" at the end of the word "\b" with literal "nse".
# I of course had to add the variable string and the flags=re.M to use the multiple line feature, in case the text had multiple lines. 
string = re.sub(r'nce\b', r'nse', string, flags=re.M)
# Replacing "ise" with "ize"
# The following part was a bit tricky, and Kate kindly helped me a bit with it. 
# Similar to the last part, I used the function re.sub(). I used capture groups rather than literal strings. 
# The first capture group contained word-initial boundary+the first part of the word before the letter i. I used the letter i to focus on a single letter, rather than using *, which would capture the whole word. 
# The second capture group contained the letter s which I want to change to z. 
# The third capture group contained potential word-final strings, which I divided using "|". Then, I used \b to indicate the word-final boundary. 
# Next, I then used r'' first containing \ to indicate a capture group (not a literal string) and I included the first capture group, followed by the letter z followed by the third capture group.
# I of course had to include the variable name anf the flags. 
string = re.sub(r'(\w+i)(s)(e|ing|ed|es|ation|ations)\b', r'\1z\3', string, flags=re.M)
# To produce a file containing the changed text, I used the foolowing code. 
with open("corrected_text.txt", 'a+') as output:
    for changed_text in string:
        output.write(changed_text)