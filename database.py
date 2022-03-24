#from xxlimited import new
import pymongo
import pprint
import bson
from passlib.hash import pbkdf2_sha256
from passlib.hash import scram


uri='mongodb+srv://ouafa:123@cluster0.nvxgi.mongodb.net/MycourseMentor?retryWrites=true&w=majority'
client = pymongo.MongoClient(uri)
db = client.MycourseMentor

gradesColl = db.gradesReport
studentsColl = db.students
usersColl = db.users

#check the students collection content
def studentsList():     
    for item in studentsColl.find():
        print(item)

#check the grades collection content
def gradesList():
    for elm in gradesColl.find().limit(10):
        print(elm)

#check the users collection content
def usersList():
    for elm in usersColl.find().limit(10):
        print(elm)

#Create a new user
def createUser(stdID, userName,pwd,fullname):
    hashpswd=scram.hash(pwd)
    doc={
        "Student_ID": stdID,
        "username": userName,
        "full_name": fullname,
        "hashed_password": hashpswd,
    }
    usersColl.insert_one(doc)

#Authenticate a user
def authenticateUser(userName,pwd):
    hashpswd=scram.hash(pwd)
    #search for user
    #for elm in usersColl.find():
    for elm in usersColl.find({"username":userName}):
        print(elm)
        print("element found")
        if scram.verify(pwd,elm["hashed_password"]) == True:
            print("successfully login")
            break
        else:
            print("wrong username or password!!!")
        
#Change the password
def updateUser(userName,pwd):
    hashpswd=scram.hash(pwd)
    newpwd=""
    oldpwd=""
    # stat = False
    # newDoc={}
    # for elm in usersColl.find({"username":userName}):
    #     #usersColl.find_one({"username":userName})
    #     print(elm)
    #     if scram.verify(pwd,elm["hashed_password"]) == True:
    #         stat=True
    #         newDoc=elm
    #         print("Enter the old password")
    #         input(oldpwd)
    #         if scram.verify(pwd,elm["hashed_password"]) == True:
    #             print("Enter a new password")
    #             input(newpwd)
    #             newHashedPwd=scram.hash(newpwd)
    #             usersColl.update_one({"userName":userName},{"$set":{"hashed_password":newHashedPwd}})
    #     else:
    #         print("wrong password, please try again")
        

    print("Enter the old password")
    input(oldpwd)
    print("Enter a new password")
    input(newpwd)
    oldHashedPwd=scram.hash(oldpwd)
    newHashedPwd=scram.hash(newpwd)
    print(oldHashedPwd)
    print(newHashedPwd)
    print()
    for elm in usersColl.find():
        usersColl.find_one_and_update({"username":userName, "hashed_password": oldHashedPwd},{"$set":{"hashed_password":newHashedPwd}})
        print("updating!!!!!!!!!!!!!!!!!!")

    for elm in usersColl.find({"username":userName,"hashed_password":newHashedPwd}):
        print("elemnt updated")
    for elm in usersColl.find({"username":userName,"hashed_password":newHashedPwd}):
        print("elemnt updated")

    # if stat==True:
    #     print("Enter the old password")
    #     input(oldpwd)
    #     if scram.verify(pwd,elm["hashed_password"]) == True:
    #         print("Enter a new password")
    #         input(newpwd)
    #         newHashedPwd=scram.hash(newpwd)
    #         #for elm in usersColl.find():
    #         if usersColl.find_one_and_update({"userName":userName},{"$set":{"hashed_password":newHashedPwd}})
    #     else:
    #         print("wrong password, please try again")


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
#def updatePredictions(name, aList):
def updatePredictions(stdID, name, grade,tag):
    print("Insert the predicted grades for CS210: ")
    #print(predList)
    i=0
    if name=="HW1":
        print("update the grade of ", name)
        for elm in studentsColl.find():
            #studentsColl.find_one_and_update({"_id":bson.objectid.ObjectId(elm["_id"])},{"$set":{"CS210.HW1":aList[i]}})
            #i+=1
            studentsColl.find_one_and_update({"Students":stdID},{"$set":{"CS210.HW1.grade":grade,"CS210.HW1.tags":tag}})
    if name=="HW2":
        print("update the grade of ", name)
        for elm in studentsColl.find():
            #studentsColl.find_one_and_update({"_id":bson.objectid.ObjectId(elm["_id"])},{"$set":{"CS210.HW2":aList[i]}})
            #i+=1
            studentsColl.find_one_and_update({"Students":stdID},{"$set":{"CS210.HW2.grade":grade,"CS210.HW2.tags":tag}})
    if name=="Test1":
        print("update the grade of ", name)
        for elm in studentsColl.find():
            #studentsColl.find_one_and_update({"_id":bson.objectid.ObjectId(elm["_id"])},{"$set":{"CS210.Test1":aList[i]}})
            #i+=1
            studentsColl.find_one_and_update({"Students":stdID},{"$set":{"CS210.Test1.grade":grade,"CS210.Test1.tags":tag}})
    if name=="Test2":
        for elm in studentsColl.find():
            #studentsColl.find_one_and_update({"_id":bson.objectid.ObjectId(elm["_id"])},{"$set":{"CS210.Test2":aList[i]}})
            #i+=1
            studentsColl.find_one_and_update({"Students":stdID},{"$set":{"CS210.Test2.grade":grade,"CS210.Test2.tags":tag}})
    if name=="Final":
        print("update the grade of ", name)
        for elm in studentsColl.find():
            #studentsColl.find_one_and_update({"_id":bson.objectid.ObjectId(elm["_id"])},{"$set":{"CS210.Final":aList[i]}})
            #i+=1
            studentsColl.find_one_and_update({"Students":stdID},{"$set":{"CS210.Final.grade":grade,"CS210.Final.tags":tag}})
    if name=="FinalGrade":
        print("update the grade of ", name)
        for elm in studentsColl.find():
            #studentsColl.find_one_and_update({"_id":bson.objectid.ObjectId(elm["_id"])},{"$set":{"CS210.FinalGrade":aList[i]}})
            #i+=1
            studentsColl.find_one_and_update({"Students":stdID},{"$set":{"CS210.FinalGrade.grade":grade,"CS210.FinalGrade.tags":tag}})

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
#print("Display database collections")

# # List all the collections in 'sample_mflix':
# collections = db.list_collection_names()
# for collection in collections:
#    print(collection)

# print()
# print()

# print("Grab grades history to build a prediction model ")
# print("######INCLUDE MICHAEL CODE")
# print()
# for elm in gradesColl.find():
#     print(elm)

# print()
# print()

# print("Grab the student list to predict their overal grades ")
# print("######INCLUDE MICHAEL CODE")
# print()
# for elm in studentsColl.find():
#     print(elm)

# print()
# print()

# print("Assuming that we got the resulted prediction from Michael part")
# print("Use fabricated prediction list")

# predList=[85.3,78.3,88,89.8,47,99]
# print("predicted list: ",predList)

# print()

# print("Add the overall prediction grades to the student collection")
# updatePredictions("OverallPred", predList)
# print()
# for elm in studentsColl.find():
#     print(elm)


# print()
# print()

# print("Add the Homework1 grades(provided by the professors) to the student collection")
# hmw1List=[75.3,98.2,88.8,65,79.8,92]
# updatePredictions("HW1", hmw1List)
# print("Update the overall prediction grades to the student collection")
# updPredList = [75.3,88,91,89,75,92]
# updatePredictions("OverallPred", updPredList)
# for elm in studentsColl.find():
#     print(elm)

# print()
# print()

# print("Add the Test1 grades(provided by the professors) to the student collection")
# hmw2List=[75.3,98.2,88.8,65,79.8,92]
# updatePredictions("HW2",hmw2List)
# print("Update the overall prediction grades to the student collection")
# updPredList = [75.3,88,91,89,75,92]
# updatePredictions("OverallPred", updPredList)
# for elm in studentsColl.find():
#     print(elm)

# print()
# print()

# print("Add the Homework2 grades(provided by the professors) to the student collection")
# test1List=[75.3,98.2,88.8,65,79.8,92]
# updatePredictions("Test1",test1List)
# print("Update the overall prediction grades to the student collection")
# updPredList = [75.3,88,91,89,75,92]
# updatePredictions("OverallPred", updPredList)
# for elm in studentsColl.find():
#     print(elm)

# print()
# print()

# print("Add the Test2 grades(provided by the professors) to the student collection")
# test2List=[75.3,98.2,88.8,65,79.8,92]
# updatePredictions("Test2",test2List)
# print("Update the overall prediction grades to the student collection")
# updPredList = [75.3,88,91,89,75,92]
# updatePredictions("OverallPred", updPredList)
# for elm in studentsColl.find():
#     print(elm)

#print()
#print()

#print("Remove the predicted grades")
#unsetPredictions()
#for elm in studentsColl.find():
 #   print(elm)

#print()
#print()

#print("Insert the overall grades to the students collection")
#print("Insert this collection to the grades history for future prediction")
##unsetPredictions()

# print("list of users")
# for elm in usersColl.find():
#      print(elm)

#print("Add a new user")
#createUser("Student1","std1", "mycourseMentor123", "test one")
# createUser("Student1","std2", "mycourseMentor234", "test one")
# createUser("Student2","std3", "mycourseMentor345", "test two")
# createUser("Student3","std4", "mycourseMentor456", "test three")
# createUser("Student4","std5", "mycourseMentor567", "test four")
# createUser("Student5","std6", "mycourseMentor678", "test five")
# createUser("Student6","std7", "mycourseMentor789", "test six")

#print()
#print("list of students")
#for elm in studentsColl.find():
     #print(elm)

print()
print()
print("user login authentication")
authenticateUser("std1","mycourseMentor123")
# print()
# print()
# authenticateUser("std2","mycourseMentor234")
# print()
# print()
# authenticateUser("std3","mycourseMentor345")
# print()
# print()
# authenticateUser("std4","mycourseMentor456")
# print()
# print()
# authenticateUser("std5","mycourseMentor567")
# print()
# print()
# authenticateUser("std6","mycourseMentor678")
# print()
# print()
# authenticateUser("std7","mycourseMentor789")
# print()
# print()
# ##try wrong username and/or password
# authenticateUser("std1","mycourseMentor789")
# print()
# print()

print()
print()
print("user login password change")
#updateUser("std1","mycourseMentor123")


print()
print()
print("user login authentication")
authenticateUser("std1","mycourseMentor123")

#hashhh= scram.hash("mycourseMentor123")
#print(hashhh)
#updatePredictions("Student1","HW1",100.00)
