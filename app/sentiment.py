from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
sid = SentimentIntensityAnalyzer()
message_text = '''It is a really amazing movie.'''
print(message_text)
scores = sid.polarity_scores(message_text)
print(scores)