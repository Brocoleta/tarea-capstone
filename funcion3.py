def funcion3(tweets):
  fechas = {}

  for tweet in tweets:
    if tweet['date'].split('T')[0] not in fechas.keys():
      fechas[tweet['date'].split('T')[0]] = 1
    else:
      fechas[tweet['date'].split('T')[0]] += 1
  top = [k for k, v in sorted(fechas.items(), key=lambda item: item[1],reverse=True)]
  return top[0:10]