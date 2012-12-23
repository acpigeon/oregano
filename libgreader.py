from libgreader import GoogleReader, ClientAuthMethod

username = 'acpigeon'
password = 'Katana666'

ca = ClientAuthMethod(username, password)

reader = GoogleReader(ca)

info = reader.getUserInfo()
print info

x = reader.buildSubscriptionList()
if x == 'True': print("Subscription list built.")
else: print ("Something went wrong with building the subscription list.")

print("Printing feed objects...")
print reader.feeds

# reader.feeds is a list, so we can play around wtih individual objects
print reader.feeds[0]

# Each list item has some properties associated with it
print reader.feeds[0].id
print reader.feeds[0].title

# List comprehension for returning feed id
print [x.id for x in reader.feeds]

# List comprehension for returning feed title
print [x.title for x in reader.feeds]

# What are the other reader.feeds properties?


# This part gets a little unclear, I think it's related to the example feed specifically
echo_feed = [x for x in reader.feeds if "Echo" in x.title][0]

# Prints feed objects
print echo_feed.items

# Print title and url for each item in echo_feed
print [x.origin for x in echo_feed.items]

# Get a single post in dict form
article = [x.data for x in echo_feed.items][0]

# Print post content
print article['content']
