import pymongo
import pprint
import bson

client = pymongo.MongoClient("localhost",27017)
db = client.myCourseMentor
gradesColl = db.grades1
studentsColl = db.students



#check the students collection contents
def studentsList():     
    for item in studentsColl.find():
        print(item)

#check the grades collection contents
def gradesList():
    for elm in gradesColl.find().limit(10):
        print(elm)


#Launch first grade prediction for one student
##Get the results from user input assuming that results are from prediction code(Michael part)
#std = input("Enter the student ID: ")
#inp = input("Enter the predicted grades for CS210: ")
#print(std)
#print(inp)



##Launch the first grades' prediction for all the students
##Get the results from user input assuming that results are from prediction code(Michael part)
def FirstPredictionList():
    print("Enter the predicted grades for CS210: ")
    predictedList=[]
    for elm in studentsColl.find():
        print("For :",elm["Students"])
        inp =input()
        predictedList.append(inp)
        print(elm)
    #print(predictedList)
    return predictedList


##Insert the predicted grades into student database
def updatePredictions(name, aList):
    print("Insert the predicted grades for CS210: ")
    #print(predList)
    i=0
    if name=="OverallPred":
        print("name is ", name)
        for elm in studentsColl.find():
            studentsColl.find_one_and_update({"_id":bson.objectid.ObjectId(elm["_id"])},{"$set":{"CS210.OverallPred":aList[i]}})
            i+=1
    if name=="HW1":
        print("name is ", name)
        for elm in studentsColl.find():
            studentsColl.find_one_and_update({"_id":bson.objectid.ObjectId(elm["_id"])},{"$set":{"CS210.HW1":aList[i]}})
            i+=1
    if name=="HW2":
        print("name is ", name)
        for elm in studentsColl.find():
            studentsColl.find_one_and_update({"_id":bson.objectid.ObjectId(elm["_id"])},{"$set":{"CS210.HW2":aList[i]}})
            i+=1
    if name=="Test1":
        print("name is ", name)
        for elm in studentsColl.find():
            studentsColl.find_one_and_update({"_id":bson.objectid.ObjectId(elm["_id"])},{"$set":{"CS210.Test1":aList[i]}})
            i+=1
    if name=="Test2":
        for elm in studentsColl.find():
            studentsColl.find_one_and_update({"_id":bson.objectid.ObjectId(elm["_id"])},{"$set":{"CS210.Test2":aList[i]}})
            i+=1

##Insert the predicted grades into student database
def unsetPredictions():
    print("Insert the predicted grades for CS210: ")
   
    predictedList=[]
    i=0
    for elm in studentsColl.find():
        studentsColl.find_one_and_update({"_id":bson.objectid.ObjectId(elm["_id"])},{"$unset":{"CS210.OverallPred":""}})
        i+=1
    return predictedList

print()
print("Display database collections")

# List all the collections in 'sample_mflix':
collections = db.list_collection_names()
for collection in collections:
   print(collection)

print()
print()

print("Grab grades history to build a prediction model ")
print("######INCLUDE MICHAEL CODE")
print()
for elm in gradesColl.find():
    print(elm)

print()
print()

print("Grab the student list to predict their overal grades ")
print("######INCLUDE MICHAEL CODE")
print()
for elm in studentsColl.find():
    print(elm)

print()
print()

print("Assuming that we got the resulted prediction from Michael part")
print("Use fabricated prediction list")

predList=[85.3,78.3,88,89.8,47,99]
print("predicted list: ",predList)

print()

print("Add the overall prediction grades to the student collection")
updatePredictions("OverallPred", predList)
print()
for elm in studentsColl.find():
    print(elm)


print()
print()

print("Add the Homework1 grades(provided by the professors) to the student collection")
hmw1List=[75.3,98.2,88.8,65,79.8,92]
updatePredictions("HW1", hmw1List)
print("Update the overall prediction grades to the student collection")
updPredList = [75.3,88,91,89,75,92]
updatePredictions("OverallPred", updPredList)
for elm in studentsColl.find():
    print(elm)

print()
print()

print("Add the Test1 grades(provided by the professors) to the student collection")
hmw2List=[75.3,98.2,88.8,65,79.8,92]
updatePredictions("HW2",hmw2List)
print("Update the overall prediction grades to the student collection")
updPredList = [75.3,88,91,89,75,92]
updatePredictions("OverallPred", updPredList)
for elm in studentsColl.find():
    print(elm)

print()
print()

print("Add the Homework2 grades(provided by the professors) to the student collection")
test1List=[75.3,98.2,88.8,65,79.8,92]
updatePredictions("Test1",test1List)
print("Update the overall prediction grades to the student collection")
updPredList = [75.3,88,91,89,75,92]
updatePredictions("OverallPred", updPredList)
for elm in studentsColl.find():
    print(elm)

print()
print()

print("Add the Test2 grades(provided by the professors) to the student collection")
test2List=[75.3,98.2,88.8,65,79.8,92]
updatePredictions("Test2",test2List)
print("Update the overall prediction grades to the student collection")
updPredList = [75.3,88,91,89,75,92]
updatePredictions("OverallPred", updPredList)
for elm in studentsColl.find():
    print(elm)

print()
print()

print("Remove the predicted grades")
unsetPredictions()
for elm in studentsColl.find():
    print(elm)

print()
print()

print("Insert the overall grades to the students collection")
print("Insert this collection to the grades history for future prediction")
#unsetPredictions()



