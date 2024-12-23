
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score


def diabetes_processing():

    diabetes_dataset = pd.read_csv('diabetes_process.csv') 

    diabetes_dataset.head()

    # number of rows and Columns in this dataset
    diabetes_dataset.shape

    # getting the statistical measures of the data
    diabetes_dataset.describe()

    diabetes_dataset['Outcome'].value_counts()

    diabetes_dataset.groupby('Outcome').mean()

    # separating the data and labels
    X = diabetes_dataset.drop('Outcome', axis=1)
    Y = diabetes_dataset['Outcome']

    # print(X)
    # print(Y)

    scaler = StandardScaler()
    scaler.fit(X)

    standardized_data = scaler.transform(X)
    # print(standardized_data)

    X = standardized_data
    Y = diabetes_dataset['Outcome']

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)
    # print(X.shape, X_train.shape, X_test.shape)

    classifier = svm.SVC(kernel='linear')

    #training the support vector Machine Classifier
    classifier.fit(X_train, Y_train)

    # accuracy score on the training data
    X_train_prediction = classifier.predict(X_train)
    training_data_accuracy = accuracy_score(X_train_prediction, Y_train)

    # print('Accuracy score of the training data : ', training_data_accuracy)

    # accuracy score on the test data
    X_test_prediction = classifier.predict(X_test)
    test_data_accuracy = accuracy_score(X_test_prediction, Y_test)

    # print('Accuracy score of the test data : ', test_data_accuracy)

    return scaler, classifier

def check_diabetes(input_data):
    
    # # changing the input_data to numpy array
    # input_data_as_numpy_array = np.asarray(input_data)

    # # reshape the array as we are predicting for one instance
    # input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    # scaler, classifier = diabetes_processing()
    # # standardize the input data
    # std_data = scaler.transform(input_data_reshaped)
    # print(std_data)

    # prediction = classifier.predict(std_data)
    # print(prediction)

    prediction = 1
    return prediction
    # if (prediction == 0):
    #     print('The person is not diabetic')
    # else:
    #     print('The person is diabetic')


# input_data = (3,126,88,41,235,39.3,0.704,27)
# check_diabetes(input_data)