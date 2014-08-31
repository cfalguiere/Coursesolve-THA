import sys
import re
import csv
import math


def load_sentiments():
    afinnfile = open("AFINN-111.txt")
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    #print scores.items() # Print every (term, score) pair in the dictionary
    return scores;

def load_deal_terms():
    dealfile = open("deals.txt")
    scores = {} # initialize an empty dictionary
    for line in dealfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    #print scores.items() # Print every (term, score) pair in the dictionary
    return scores;

def load_event_terms():
    dealfile = open("deals.txt")
    scores = {} # initialize an empty dictionary
    for line in dealfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    #print scores.items() # Print every (term, score) pair in the dictionary
    return scores;

#firstpost_date,url,trackback_author_nick,content,score,trackback_permalink,trackback_author_url
def compute_tweet_info(tweetreader):
    tweets = []
    i = 0
    for row in tweetreader:
       #print len(row)
       #print row
       #print ', '.join(row)
       if (len(row) > 4):
            uri = row[1]
            author = row[2]
            content = row[3]
            #print content
            if i==0:
                tweet_info = ( uri, author, content, "opinion_score", "hashtag_score", "link_score" ,
                               "rt_score", "at_score", "deal_score" , "event_score", "emphasis_score" ,
                               "classification")
                tweets.append(tweet_info)
            else:
                tweet_info = ( uri, author, content)
                tweets.append(tweet_info)
            i = i + 1
    return tweets

def extract_words(sentence):
    words = sentence.split()
    return words


def parse_input(filename):
    csv.register_dialect('unixpwd', delimiter=',', quoting=csv.QUOTE_NONE)
    with open(filename, 'rb') as csvfile:
        tweetreader = csv.reader(csvfile, delimiter=',', quotechar='|',  dialect=csv.excel_tab)
        tweets = compute_tweet_info(tweetreader)
    csvfile.close()     
    return tweets

def compute_sentiment_score(sentiment_scores, words):
    score = 0
    for word in words:
        lword = word.lower()
        if lword in sentiment_scores:
            score = score + abs(sentiment_scores[lword])
    return score

def compute_hashtag_score(words):
    score = 0
    for word in words:
        if word.startswith("#"):
            score = score + 1
    return score

def compute_link_score(words):
    score = 0
    for word in words:
        if word.lower().startswith("http://"):
            score = score + 1
    return score

def compute_rt_score(words):
    score = 0
    for word in words:
        if word.startswith("RT"):
            score = score + 1
    return score

def compute_at_score(words):
    score = 0
    for word in words:
        if word.startswith("@"):
            score = score + 1
    return score

def compute_deal_score(deal_terms, words):
    score = 0
    for word in words:
        lword = word.lower()
        if lword in deal_terms:
            score = score + abs(deal_terms[lword])
    return score

def compute_event_score(event_terms, words):
    score = 0
    for word in words:
        lword = word.lower()
        if lword in event_terms:
            score = score + abs(event_terms[lword])
    return score

def compute_emphasis_score(words):
    score = 0
    for word in words:
        uword = word.upper()
        if uword == word:
            score = score + 1
        if "!" in word:
            score = score + 1
    return score

def tag_tweets(tweets, sentiment_scores, deal_terms, event_terms):
    i = 0
    for tweet in tweets:
        content = tweet[2]
        if content != "content":
            content_words = extract_words(content)
            sentiment_score = compute_sentiment_score(sentiment_scores, content_words)
            hashtag_score = compute_hashtag_score(content_words)
            link_score = compute_link_score(content_words)
            rt_score = compute_rt_score(content_words)
            at_score = compute_at_score(content_words)
            deal_score = compute_deal_score(deal_terms, content_words)
            event_score = compute_event_score(event_terms, content_words)
            emphasis_score = compute_emphasis_score( content_words)
            #print sentiment_score
            tweets[i] = tweet + (str(sentiment_score),str(hashtag_score),str(link_score),
                                 str(rt_score),str(at_score),str(deal_score),str(event_score),str(emphasis_score),
                                 "UNKNOWN")
        i = i + 1
    
def output_tweets(tweets, filename):
    with open(filename, 'wb') as f:
        for tweet in tweets:
            f.write(', '.join(tweet) + "\n")
    f.close()     
    
def main():
    input_file_name = sys.argv[1]
    sentiment_scores = load_sentiments()
    deal_scores = load_deal_terms()
    event_scores = load_event_terms()
    tweets =  parse_input(input_file_name)
    tag_tweets(tweets, sentiment_scores, deal_scores, event_scores)
    output_file_name = "processed/" + input_file_name.replace('/', '_').replace('.', '') + ".csv"
    output_tweets(tweets, output_file_name)
   
if __name__ == '__main__':
    main()
