from asyncio.windows_events import NULL
import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score
from sklearn.multioutput import MultiOutputRegressor
from math import isnan
import pprint
file = pd.read_csv("./data/CS210Prereqs.csv")
file2 = pd.read_csv("./data/CS210Final.csv")

df_grades = pd.DataFrame(file)
df_in_class = pd.DataFrame(file2)
for i in df_in_class:
    if i != "Students":
        df_in_class[i] = df_in_class[i] * 100

for j in df_grades:
    if j != "Students":
        df_grades[j] = df_grades[j] * 100

df = df_grades.merge(df_in_class, how='inner', on='Students')


def grades_df_to_dict(grades_df):
    grades_df = grades_df.dropna(axis=1)
    grades_dict = grades_df.to_dict('records')

    return grades_dict[0]


def pred_grades(class_name, student_df, df):
    knn = KNeighborsClassifier()
    temp_df = df
    drop_list = []
    for i in temp_df:
        if i not in student_df.columns and i != class_name:
            drop_list.append(i)
    if class_name in student_df.columns:
        student_df = student_df.drop(columns=class_name)
    temp_df = temp_df.drop(drop_list, axis=1)
    X = temp_df.drop([class_name], axis=1)
    X = X.astype('float')
    y = temp_df[class_name]
    for i in range(len(y)):
        if y[i] > 90:
            y[i] = 'A'
        elif y[i] > 80:
            y[i] = 'B'
        elif y[i] > 70:
            y[i] = 'C'
        elif y[i] > 60:
            y[i] = 'D'
        else:
            y[i] = 'F'

    max_acc = 0
    while max_acc < 70:
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)
        k_range = range(1, len(X_train))
        accuracies = []
        for k in k_range:
            knn = KNeighborsClassifier(n_neighbors=k, p=2, n_jobs=-1)
            knn.fit(X_train, y_train)
            pred_k = knn.predict(X_test)
            accuracies.append(1 - (np.mean(pred_k != y_test)))

        # This is our K
        K = np.argmax(accuracies) + 1
        max_acc = max(accuracies) * 100

    # plt.plot(k_range, accuracies, color='blue', linestyle='dashed',
    #          marker='o', markerfacecolor='red', markersize=10)
    # plt.title("Accuracy vs. K Value")
    # plt.xlabel("Value of K for KNN")
    # plt.ylabel("Accuracy")
    # plt.show()

    print("Highest performing K is: ", K, "at", max_acc, "%")

    # Predicting on student
    X_test = student_df
    knn = KNeighborsClassifier(n_neighbors=K, p=2, n_jobs=-1)
    knn.fit(X_train, y_train)
    pred_k = knn.predict(X_test)
    res = "Predicted a grade of a " + pred_k[0] + " for " + class_name + " with an accuracy of " + " {:.2%}".format(max(accuracies)) + "\n"
    print(res)
    student_df[class_name] = pred_k[0]

    return res


def script():
    while True:
        answer = int(input(
            "What would you like to do?\n1. Predict student's grade for CS210 prior to taking the class\n2. Predict "
            "next grade for student given CS210 grades\n3. Predict student's final CS210 grade given CS210 grades so "
            "far\n4. "
            "Quit\n"))
        prompt_answer = prompt(answer)
        if prompt_answer == 0:
            break


def prompt(user_answer):
    if user_answer == 1:
        classes_and_assignments = ['CS101', 'CS102', 'CS140', "MTH120"]
        student_df = {}
        print("\nHit 'ENTER' if not taken class yet.\n")
        answer = " "
        option_number = 0
        while answer != "" and option_number < len(classes_and_assignments):
            answer = input("What grade did the student get for " + classes_and_assignments[option_number] + "? ")
            if answer != "":
                student_df[classes_and_assignments[option_number]] = float(answer)
                option_number += 1
        student_df = pd.DataFrame.from_dict([student_df])
        print(student_df)
        print("Predicting for: Final Grade \n")
        pred_grades('Final Grade', student_df, df)
        return 1
    if user_answer == 2 or user_answer == 3:
        classes_and_assignments = ['CS101', 'CS102', 'CS140', "MTH120", "HW1", "Test1", "HW2", "Test2", "Final"]
        student_df = {}
        print("\nHit 'ENTER' if not taken assignment/test yet.\n")
        answer = " "
        option_number = 0
        while answer != "" and option_number < len(classes_and_assignments):
            answer = input("What grade did the student get for " + classes_and_assignments[option_number] + "? ")
            if answer != "":
                student_df[classes_and_assignments[option_number]] = float(answer)
                option_number += 1

        student_df = pd.DataFrame.from_dict([student_df])
        print(student_df)
        if user_answer == 2 and option_number != len(classes_and_assignments):
            print("Predicting for: " + classes_and_assignments[option_number] + "\n")
            pred_grades(classes_and_assignments[option_number], student_df, df)
        elif user_answer == 3 or option_number == len(classes_and_assignments):
            if option_number == len(classes_and_assignments):
                print("All assignments, tests, and prerequisites have been taken.")
            print("Predicting for: Final Grade \n")
            pred_grades('Final Grade', student_df, df)
        return 1
    if user_answer == 4:
        return 0
    else:
        return 0


# Django Stuff
def pred_prior(grade1, grade2, grade3, grade4):
    student_df = {}
    student_df['CS101'] = [float(grade1)]
    student_df['CS102'] = [float(grade2)]
    student_df['CS140'] = [float(grade3)]
    student_df['MTH120'] = [float(grade4)]
    student_df = pd.DataFrame.from_dict(student_df)
    return pred_grades('Final Grade', student_df, df)

def pred_next(grade1,grade2,grade3,grade4,grade5,grade6,grade7,grade8,grade9):
    classes_and_assignments = ['CS101', 'CS102', 'CS140', "MTH120", "HW1", "Test1", "HW2", "Test2", "Final"]
    student_df = {}
    print("\nEnter nothing if not taken assignment/test yet.\n")
    if (grade1 != ''):
        student_df['CS101'] = [float(grade1)]
    if (grade2 != ''):
        student_df['CS102'] = [float(grade2)]
    if (grade3 != ''):
        student_df['CS140'] = [float(grade3)]
    if (grade4 != ''):
        student_df['MTH120'] = [float(grade4)]
    if (grade5 != ''):
        student_df['HW1'] = [float(grade5)]
    if (grade6 != ''):
        student_df['Test1'] = [float(grade6)]
    if (grade7 != ''):
        student_df['HW2'] = [float(grade7)]
    if (grade8 != ''):
        student_df['Test2'] = [float(grade8)]
    if (grade9 != ''):
        student_df['Final'] = [float(grade9)]

    index = 0
    for value in student_df.values():
        if value != '':
            index += 1
        else:
            break

    student_df = pd.DataFrame.from_dict(student_df)
    return pred_grades(classes_and_assignments[index], student_df, df)

def predict_final(grade1,grade2,grade3,grade4,grade5,grade6,grade7,grade8,grade9):
    classes_and_assignments = ['CS101', 'CS102', 'CS140', "MTH120", "HW1", "Test1", "HW2", "Test2", "Final"]
    student_df = {}
    if (grade1 != ''):
        student_df['CS101'] = [float(grade1)]
    if (grade2 != ''):
        student_df['CS102'] = [float(grade2)]
    if (grade3 != ''):
        student_df['CS140'] = [float(grade3)]
    if (grade4 != ''):
        student_df['MTH120'] = [float(grade4)]
    if (grade5 != ''):
        student_df['HW1'] = [float(grade5)]
    if (grade6 != ''):
        student_df['Test1'] = [float(grade6)]
    if (grade7 != ''):
        student_df['HW2'] = [float(grade7)]
    if (grade8 != ''):
        student_df['Test2'] = [float(grade8)]
    if (grade9 != ''):
        student_df['Final'] = [float(grade9)]
    
    student_df = pd.DataFrame.from_dict(student_df)
    return pred_grades('Final Grade', student_df, df)