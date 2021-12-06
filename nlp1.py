from textblob import TextBlob
from textblob.blob import Word

text = "Today is a beautiful day. Tommorow looks like bad weather."

blob=TextBlob(text)

# print(blob.sentences)
# print(blob.words)
# print(blob.tags)
#print(blob.noun_phrases)

# print(round(blob.sentiment.polarity,3))
# print(round(blob.sentiment.subjectivity,3))


# for i in blob.sentences:
#     print(i,round(i.sentiment.polarity,3))





from textblob.sentiments import NaiveBayesAnalyzer

blob = TextBlob(text, analyzer=NaiveBayesAnalyzer())


# for sentences in blob.sentences:
#     print(sentences.sentiment)

