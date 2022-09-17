import pickle
import os


def store_dns(lookuptable):
    if os.path.isfile("lookuptable.pkl"):
        foo = pickle.load(open("lookuptable.pkl", "rb"))
        for i in lookuptable:
            if lookuptable[i] not in foo:
                foo[i] =  lookuptable[i]
        pickle.dump(foo, open('lookuptable.pkl', 'wb'))
    else:
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
