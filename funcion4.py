import re

def sacar_hashtags(string):
    ret = []
    s=''
    hashtag = False
    for char in string:
        if char=='#':
            hashtag = True
            if s:
                ret.append(s)
                s=''           
            continue

        # take only the prefix of the hastag in case contain one of this chars (like on:  '#happy,but i..' it will takes only 'happy'  )
        if hashtag and char in [' ','.',',','(',')',':','{','}','\n'] and s:
            ret.append(s)
            s=''
            hashtag=False 

        if hashtag:
            s+=char

    if s:
        ret.append(s)

    return ret


def funcion4(tweets):
  hashtags = {}
  for tweet in tweets:
    for hashtag in sacar_hashtags(tweet['content']):
      if hashtag not in hashtags.keys():
        hashtags[hashtag] = 1
      else:
        hashtags[hashtag] += 1
  top = [k for k, v in sorted(hashtags.items(), key=lambda item: item[1],reverse=True)]
  return top[0:10]