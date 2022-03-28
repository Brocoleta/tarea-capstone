
import bisect
class KeyWrapper:
    def __init__(self, iterable, key):
        self.it = iterable
        self.key = key

    def __getitem__(self, i):
        return self.key(self.it[i])

    def __len__(self):
        return len(self.it)

    def insert(self, index, item):
        print('asked to insert %s at index%d' % (item, index))
        self.it.insert(index, {"time":item})






def funcion1(tweets):
  maxRetweet = tweets[0:10]
  maxRetweet.sort(key=lambda x:x['retweetCount'])
  
  
  
  for tweet in tweets[10::]:
    if tweet['retweetCount'] > maxRetweet[9]['retweetCount'] or maxRetweet[9]['retweetCount']=='null':
      
      maxRetweetIndex = bisect.bisect_left(KeyWrapper(maxRetweet, key=lambda t: t["retweetCount"]),tweet['retweetCount'])
      maxRetweet.insert(maxRetweetIndex, tweet)
      maxRetweet = maxRetweet[1::]

  
  content = []
  for tweet in maxRetweet[::-1]:
    content.append(tweet['content'])
  return content
