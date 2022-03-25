import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
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

# df_grades = df_grades.drop(["_id", "CS210.Final", "CS210.HW1","CS210.HW2","CS210.Test1","CS210.Test2"], axis=1)
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
    while (max_acc < 51):
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
    print("Highest performing K is: ", K, "at", max_acc, "%")

    # Predicting on student
    X_test = student_df
    knn = KNeighborsClassifier(n_neighbors=K, p=2, n_jobs=-1)
    knn.fit(X_train, y_train)
    pred_k = knn.predict(X_test)
    res = "Predicted Grade: " + pred_k[0] + " --- Accuracy: " + "{:.2%}".format(max(accuracies))
    print(res)
    student_df[class_name] = pred_k[0]
    return res


def script():
    while (True):
        answer = int(input(
            "What would you like to do?\n1. Predict student's grade for CS210 prior to taking the class\n2. Predict next grade for student given CS210 grades\n3. Predict student's final CS210 grade given class grades\n4. Quit\n"))
        prompt_answer = prompt(answer)
        if prompt_answer == 0:
            break


def prompt(user_answer):
    if user_answer == 1:
        student_df = {}
        print("\nEnter 0 if not taken class yet.\n")
        student_df['CS101'] = [float(input("What grade did the student get in CS101? "))]
        student_df['CS102'] = [float(input("What grade did the student get in CS102? "))]
        student_df['CS140'] = [float(input("What grade did the student get in CS140? "))]
        student_df['MTH120'] = [float(input("What grade did the student get in MTH120? "))]
        student_df = pd.DataFrame.from_dict(student_df)
        pred_grades('Final Grade', student_df, df)
        return 1
    if user_answer == 2:
        student_df = {}
        print("\nEnter 0 if not taken assignment/test yet.\n")
        student_df['CS101'] = [float(input("What grade did the student get in CS101? "))]
        student_df['CS102'] = [float(input("What grade did the student get in CS102? "))]
        student_df['CS140'] = [float(input("What grade did the student get in CS140? "))]
        student_df['MTH120'] = [float(input("What grade did the student get in MTH120? "))]
        student_df['HW1'] = [float(input("What grade did the student get on HW1? "))]
        student_df['Test1'] = [float(input("What grade did the student get on Test1? "))]
        student_df['HW2'] = [float(input("What grade did the student get on HW2? "))]
        student_df['Test2'] = [float(input("What grade did the student get on Test2? "))]
        student_df['Final'] = [float(input("What grade did the student get on the Final? "))]

        student_df = {key: val for key, val in student_df.items() if val != 0.0}
        student_df = pd.DataFrame.from_dict(student_df)
        assignments_not_taken = []
        for i in student_df:
            if student_df[i][0] == 0:
                assignments_not_taken.append(i)

        assignment_drop_list = []
        for i in student_df:
            if i in assignments_not_taken[1:]:
                assignment_drop_list.append(i)
        student_df = student_df.drop(columns=assignment_drop_list)
        print(student_df)
        pred_grades(assignments_not_taken[0], student_df, df)
        return 1
    if user_answer == 3:
        student_df = {}
        print("\nEnter 0 if not taken assignment/test yet.\n")
        student_df['CS101'] = [float(input("What grade did the student get in CS101? "))]
        student_df['CS102'] = [float(input("What grade did the student get in CS102? "))]
        student_df['CS140'] = [float(input("What grade did the student get in CS140? "))]
        student_df['MTH120'] = [float(input("What grade did the student get in MTH120? "))]
        student_df['HW1'] = [float(input("What grade did the student get on HW1? "))]
        student_df['Test1'] = [float(input("What grade did the student get on Test1? "))]
        student_df['HW2'] = [float(input("What grade did the student get on HW2? "))]
        student_df['Test2'] = [float(input("What grade did the student get on Test2? "))]
        student_df['Final'] = [float(input("What grade did the student get on the Final? "))]

        student_df = {key: val for key, val in student_df.items() if val != 0.0}
        student_df = pd.DataFrame.from_dict(student_df)
        assignments_not_taken = []
        for i in student_df:
            if student_df[i][0] == 0:
                assignments_not_taken.append(i)

        assignment_drop_list = []
        for i in student_df:
            if i in assignments_not_taken:
                assignment_drop_list.append(i)
        student_df = student_df.drop(columns=assignment_drop_list)
        print(student_df)
        pred_grades('Final Grade', student_df, df)
        return 1
    if user_answer == 4:
        return 0
    else:
        return 0

# Django Calls
def pred_prior(grade1, grade2, grade3, grade4):
    student_df = {}
    student_df['CS101'] = [float(grade1)]
    student_df['CS102'] = [float(grade2)]
    student_df['CS140'] = [float(grade3)]
    student_df['MTH120'] = [float(grade4)]
    student_df = pd.DataFrame.from_dict(student_df)
    return pred_grades('Final Grade', student_df, df)

def pred_next(grade1,grade2,grade3,grade4,grade5,grade6,grade7,grade8,grade9):
    student_df = {}
    print("\nEnter 0 if not taken assignment/test yet.\n")
    student_df['CS101'] = [float(grade1)]
    student_df['CS102'] = [float(grade2)]
    student_df['CS140'] = [float(grade3)]
    student_df['MTH120'] = [float(grade4)]
    student_df['HW1'] = [float(grade5)]
    student_df['Test1'] = [float(grade6)]
    student_df['HW2'] = [float(grade7)]
    student_df['Test2'] = [float(grade8)]
    student_df['Final'] = [float(grade9)]

    student_df = {key: val for key, val in student_df.items() if val != 0.0}
    student_df = pd.DataFrame.from_dict(student_df)
    assignments_not_taken = []
    for i in student_df:
        if student_df[i][0] == 0:
            assignments_not_taken.append(i)

    assignment_drop_list = []
    for i in student_df:
        if i in assignments_not_taken[1:]:
            assignment_drop_list.append(i)
    student_df = student_df.drop(columns=assignment_drop_list)
    return pred_grades(assignments_not_taken[0], student_df, df)

def predict_final(grade1,grade2,grade3,grade4,grade5,grade6,grade7,grade8,grade9):
    student_df = {}
    student_df['CS101'] = [float(grade1)]
    student_df['CS102'] = [float(grade2)]
    student_df['CS140'] = [float(grade3)]
    student_df['MTH120'] = [float(grade4)]
    student_df['HW1'] = [float(grade5)]
    student_df['Test1'] = [float(grade6)]
    student_df['HW2'] = [float(grade7)]
    student_df['Test2'] = [float(grade8)]
    student_df['Final'] = [float(grade9)]

    student_df = {key: val for key, val in student_df.items() if val != 0.0}
    student_df = pd.DataFrame.from_dict(student_df)
    assignments_not_taken = []
    for i in student_df:
        if student_df[i][0] == 0:
            assignments_not_taken.append(i)

    assignment_drop_list = []
    for i in student_df:
        if i in assignments_not_taken:
            assignment_drop_list.append(i)
    student_df = student_df.drop(columns=assignment_drop_list)
    return pred_grades('Final Grade', student_df, df)