import numpy
from lightfm.datasets import fetch_movielens #importing sub modules since we don't need the whole package.
                                             #the movielens is a CSV file that contains 100k movie ratings from 1k users on 1700 movies.
from lightfm import LightFM

#fetch data and format it
data = fetch_movielens(min_rating=4.0)
    #only collecting movies with a rating of 4.0 or higher.

#print training and testing data
print(repr(data['train']))
print(repr(data['test']))

#creating a model
model = LightFM(loss="warp")

#train model
model.fit(data['train'], epochs=30, num_threads=2)

def sample_recommendation(model, data, user_ids):
    #get number of users and movies in training data
    n_users, n_items = data['train'].shape

    #generate recommendations for all of the users we input.
    for user_id in user_ids:
        #movies they already like
        known_positives = data['item_labels'][data['train'].tocsr()[user_id].indices]

        #generate the recommendations and store them in a variable using the predict method.
        scores = model.predict(user_id, numpy.arange(n_items))

        #rank them in order of most liked to least liked
        top_items = data['item_labels'][numpy.argsort(-scores)]

        #print the results
        print("User %s" % user_id)
        print("    Known Positives:")
        for x in known_positives[:3]:
            print("       %s" % x)

        print("     Recommend:")
        for x in top_items[:3]:
            print("         %s" % x)


sample_recommendation(model, data, [3,25,450])