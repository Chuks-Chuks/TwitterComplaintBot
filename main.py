from Speed import Speed
from Twitter import Twitter


internet_test = Speed()
results = internet_test.run_test()
twitter = Twitter()

if float(results[0]) < 100:
    message = f'@zzoommplc. Currently, I have a ' \
              f'download speed of {results[0]} Mbps and upload speed of {results[1]} Mbps. This falls short of the ' \
              f'download' \
              f'speed that was promised.'
    twitter.tweet(message)
