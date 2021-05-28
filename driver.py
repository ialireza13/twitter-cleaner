from twitter_purge import delete_by_date, load_history_file
from datetime import datetime

history = load_history_file('tweet.js')

cutoff_date = datetime.fromisoformat('1970-05-01T00:00:01+03:30')

delete_by_date(history=history, cutoff_date=cutoff_date,
                min_retweet_threshold=0, min_like_threshold=0)
