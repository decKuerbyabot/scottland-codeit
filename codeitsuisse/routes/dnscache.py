import pickle


def store_dns(lookuptable):
    pickle.dump(lookuptable, open('lookuptable.pkl', 'wb'))


def simulate_query(cache_size, logs):
    cache ={}
    res = []
    lookuptable = pickle.load(open('lookuptable.pkl', 'rb'))
    for domain in logs:
        if domain not in cache:
            if domain in lookuptable:
                res.append({'status':'cache miss', 'ipAddress':lookuptable[domain]})
                if len(cache) >= cache_size:
                    cache.pop(list(cache.keys())[0])
                cache[domain] = lookuptable[domain]
            else:
                res.append({'status': 'invalid', 'ipAddress': 'null'})

        else:
            res.append({'status': 'cache hit', 'ipAddress': lookuptable[domain]})
            del cache[domain]
            cache[domain] = lookuptable[domain]
    return res


# store_dns( {
#     'google.com': '1.2.3.4',
#     'amazon.com': '2.3.4.5',
#     'yahoo.com': '3.4.5.6',
#     'bing.com': '4.5.6.7',
#     'facebook.com': '5.6.7.8',
#     'instagram.com': '6.7.8.9'
#   })

print(simulate_query(3,
  [
    'google.com',
    'google.com',
    'amazon.com',
    'instagram.com',
    'google.com',
    'bing.com',
    'instagram.com',
    'burger.com'
  ]))