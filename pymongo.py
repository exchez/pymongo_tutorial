# start the mongodb with the CLI command "mongod"
# you may get an error that the data path folder doesn't exist
# use mongod --dbpath /usr/local/mongodb-data to set the new directory for your data. dir must exist before command can be run

from pymongo import MongoClient
client = MongoClient()

db = client['test-database']

# create a collection called posts
posts = db.posts # or use posts = db['posts']


# a record in your collection starts as a python dictionary
post = {"author": "Mike",
          "text": "My first blog post!",
          "tags": ["mongodb", "python", "pymongo"],
          "date": datetime.datetime.utcnow()}

# insert your post into the posts collection
posts.insert_one(post)

# now that you've added this record, the collection and record are created and you can check the collection in your db
db.list_collection_names()

# grab a random record with
posts.find_one()

# get get one by attribute
posts.find_one({'author': 'Mike'})

# insert more than one record
new_posts = [{"author": "Mike",
                "text": "Another post!",
                "tags": ["bulk", "insert"],
                "date": datetime.datetime(2009, 11, 12, 11, 14)},
             {"author": "Eliot",
               "title": "MongoDB is fun",
                "text": "and pretty easy too!",
                "date": datetime.datetime(2009, 11, 10, 10, 45)}]
posts.insert_many(new_posts)

# get all the records
for post in posts.find(): # .find() will return a cursor object which can be iterated thru
    print(post)

# find many by attribute
for post in posts.find({"author": "Mike"}):
    print(post)

# count numbers of records in your collection
posts.count_documents({})

# count by attribute
posts.count_documents({"author": "Mike"})

# you can create your own unique index
# mongodb will not insert another record with the same User_id as another record
db.profiles.create_index([('user_id', pymongo.ASCENDING)], unique=True)

