import twitter
# initialize api instance
twitter_api = twitter.Api(consumer_key='JJYU75IcScpLa2matMSINNEyK',
                        consumer_secret='X6qHl9uYdTLFWaP2uLZ5nZn7Fwl1UMaz6GD8WGBjozwFTcwQwW',
                        access_token_key='2611979148-neje28AYNoypNgKkXRUQlks5ElVrCMI9sbGpEJl',
                        access_token_secret='vuToj3yTjhODZW0VRp6E8j9VrqiOqaibUP7aUWXhG77Hl')

# test authentication
print(twitter_api.VerifyCredentials())


def buildTestSet(search_keyword):
    try:
        tweets_fetched = twitter_api.GetSearch(search_keyword, count=100)

        print("Fetched " + str(len(tweets_fetched)) + " tweets for the term " + search_keyword)

        return [{"text": status.text, "label": None} for status in tweets_fetched]
    except:
        print("Unfortunately, something went wrong..")
        return None

search_term = input("Enter a search keyword:")
testDataSet = buildTestSet(search_term)

print(testDataSet[0:4])