import twint


def fetch_tweets(filename, limit=100000):
    config = twint.Config()
    config.Search = "#antivax"
    config.Limit = limit
    config.Store_csv = True
    config.Output = filename
    twint.run.Search(config)


if __name__ == '__main__':
    fetch_tweets("antivax.csv")
