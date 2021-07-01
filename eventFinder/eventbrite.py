import eventbrite

# initialize connection to api
api = eventbrite.Eventbrite('7CQIXFV4Y2P7URM6KC5D')
hello = eventbrite.client()
user = api.get_user()

print(user)
