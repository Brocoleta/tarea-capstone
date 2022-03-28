

def funcion2(tweets):
  usuarios = {}

  for tweet in tweets:
    if tweet['user']['username'] not in usuarios.keys():
      usuarios[tweet['user']['username']] = 1
    else:
      usuarios[tweet['user']['username']] += 1
  top = [k for k, v in sorted(usuarios.items(), key=lambda item: item[1],reverse=True)]
  return top[0:10]