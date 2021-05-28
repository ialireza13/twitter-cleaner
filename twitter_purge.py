import datetime
import tweepy
import json
from datetime import datetime, timedelta, timezone
from tqdm import tqdm
from time import sleep
from random import randint

def load_history_file(tweet_js_path):
    try:
        fp = open('tweet.js','r', encoding='UTF-8')
        myjson = json.load(fp)
        return myjson
    except:
        print('Error loading history file (tweet.js), maybe double check the path?')
        return {}


def delete_by_date(history, cutoff_date, min_retweet_threshold=0, min_like_threshold=0):
    try:
        from credentials import consumer_key, consumer_secret, access_token, access_token_secret
    except:
        print('Error reading credential file')
        return 0
    
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    
    idx_last = 2
    
    log_file = open('log_file_'+randint(1e5,9e5), 'w')

    for idx, tweet in tqdm(enumerate(history[(idx_last-2):])):
        
        if int(tweet['tweet']['favorite_count']) > min_like_threshold or int(tweet['tweet']['retweet_count']) > min_retweet_threshold:
            print(str(idx_last)+'  '+tweet['tweet']['id_str']+' excluded', file=log_file)
            idx_last += 1
            continue
        
        d = datetime.strptime(tweet['tweet']['created_at'], '%a %b %d    %H:%M:%S %z %Y')
        
        if d < cutoff_date:
            try:
                api.destroy_status(tweet['tweet']['id_str'])
            except tweepy.TweepError as e:
                if e.reason == '[{\'code\': 144, \'message\': \'No status found with that ID.\'}]':
                    print(str(idx_last)+'  '+tweet['tweet']['id_str']+' not found', file=log_file)
                    idx_last += 1
                    continue
                elif e.reason == '[{\'code\': 34, \'message\': \'Sorry, that page does not exist.\'}]':
                    print(str(idx_last)+'  '+tweet['tweet']['id_str']+' access error', file=log_file)
                    continue
                else:
                    while True:
                        api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
                        sleep(5)
                        try:
                            api.destroy_status(tweet['tweet']['id_str'])
                            break
                        except:
                            print(str(idx_last)+'  '+tweet['tweet']['id_str']+' retry failed with error '+e.reason, file=log_file)
            print(str(idx_last)+'  '+tweet['tweet']['id_str']+' deleted successfully', file=log_file)
        else: print(str(idx_last)+'  '+tweet['tweet']['id_str']+' date not included', file=log_file)
        idx_last += 1
