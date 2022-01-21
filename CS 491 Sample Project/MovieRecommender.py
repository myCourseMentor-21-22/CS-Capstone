from surprise import SVD
from surprise import Dataset
#from surprise.model_selection import cross_validate
from surprise.model_selection import train_test_split
from surprise import accuracy

data = Dataset.load_builtin('ml-100k')

trainset, testset = train_test_split(data, test_size=.25)

algo = SVD()

algo.fit(trainset)
predictions = algo.test(testset)


uid = str(200)
iid = str(302)

pred = algo.predict(uid, iid)
#pred = algo.predict(uid, iid, r_ui=4)

pred = (str(pred)).split(" ")
print("With the parameters the prediction rating is " + pred[25])

accuracy.rmse(predictions, verbose=True)
#cross_validate(algo, data, measures= ['RMSE', 'MAE'], cv=5, verbose=True)

