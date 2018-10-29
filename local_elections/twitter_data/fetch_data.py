import twint


def fetch_tweets(user, filename, search=None, since="2018-01-01", limit=1000):
    config = twint.Config()
    config.Username = user
    if search:
        config.Search = search
    config.Since = since
    config.Limit = limit
    config.Store_csv = True
    config.Custom = ["date", "time", "username", "tweet", "link", "likes", "retweets", "replies", "mentions", "hashtags"]
    config.Output = filename
    twint.run.Search(config)


for candidate in ['RozeckaPL', 'GoTracz', 'martalempart', 'MichalakJerzy', 'KatarzynaObara', 'SutrykJacek']:
    fetch_tweets(candidate, candidate.lower() + '.csv')
