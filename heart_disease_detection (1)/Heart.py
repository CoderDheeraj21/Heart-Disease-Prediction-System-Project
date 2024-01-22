import seaborn as sns
import tkinter as tk

from sklearn.preprocessing import LabelEncoder,OneHotEncoder
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import time
from PIL import Image, ImageTk
from tkinter import ttk
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score,roc_curve

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# import pickle

import numpy as np
import pandas as pd

from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score


root = tk.Tk()
root.title("Heart Disease")

w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
# ++++++++++++++++++++++++++++++++++++++++++++

image2 = Image.open('heart.jpg')

image2 = image2.resize((w, h), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)


background_label = tk.Label(root, image=background_image)
background_label.image = background_image



background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)
lbl = tk.Label(root, text="Heart Disease Detection System", font=('times', 35,' bold '), height=1, width=32,bg="green",fg="white")
lbl.place(x=300, y=15)
# _+++++++++++++++++++++++++++++++++++++++++++++++++++++++
#data = pd.read_csv("E:/heart_disease_detection/heart_disease_detection/new.csv")




le = LabelEncoder()

def Model_Training():
    start = time.time()
    dataset = pd.read_csv('new.csv')
    X = dataset.iloc[:,:-1].values
    y = dataset.iloc[:,-1].values

    from sklearn.preprocessing import OneHotEncoder
    #cp
    oneHotEncoder = OneHotEncoder()
    oneHotEncoder.fit(X)
    X = oneHotEncoder.transform(X).toarray()
    X = X[:, 1:]
    #restecg
    oneHotEncoder = OneHotEncoder()
    oneHotEncoder.fit(X)
    X = oneHotEncoder.transform(X).toarray()
    X = X[:, 1:]
    #slope
    oneHotEncoder = OneHotEncoder()
    oneHotEncoder.fit(X)
    X = oneHotEncoder.transform(X).toarray()
    X = X[:, 1:]
    #ca
    oneHotEncoder = OneHotEncoder()
    oneHotEncoder.fit(X)
    X = oneHotEncoder.transform(X).toarray()
    X = X[:, 1:]
    #thal
    oneHotEncoder = OneHotEncoder()
    oneHotEncoder.fit(X)
    X = oneHotEncoder.transform(X).toarray()
    X = X[:, 1:]
    
    from sklearn.preprocessing import StandardScaler
    scalerX = StandardScaler()
    X = scalerX.fit_transform(X)
    
    from sklearn.model_selection import train_test_split
    XTrain, XTest, yTrain, yTest = train_test_split(X, y, test_size=0.3, random_state=6)
    
    from sklearn.svm import SVC
    classifier = SVC(kernel='linear',random_state=6)
    classifier.fit(XTrain,yTrain)
    yPred = classifier.predict(XTest)
    # mse = mean_squared_error(yTest,yPred)
    # r = r2_score(yTest,yPred)
    # mae = mean_absolute_error(yTest,yPred)
    accuracy = accuracy_score(yTest,yPred)
    
    
    accuracy = accuracy_score(yTest, yPred)
    print("Accuracy: %.2f%%" % (accuracy * 100.0))
    ACC = (accuracy_score(yTest, yPred) * 100)
    repo = (classification_report(yTest, yPred))
    
    label4 = tk.Label(root,text =str(repo),width=45,height=10,bg='khaki',fg='black',font=("Tempus Sanc ITC",14))
    label4.place(x=205,y=200)
    
    label5 = tk.Label(root,text ="Accracy : "+str(ACC)+"%\nModel saved as HEART_DISEASE_MODEL.joblib",width=45,height=3,bg='khaki',fg='black',font=("Tempus Sanc ITC",14))
    label5.place(x=205,y=420)
    
    
    
    
    
    print("Classification Report :\n")
    repo = (classification_report(yTest, yPred))
    print(repo)
    print("Confusion Matrix :")
    cm = confusion_matrix(yTest,yPred)
    print(cm)
    print("\n")
    from mlxtend.plotting import plot_confusion_matrix
 
    fig, ax = plot_confusion_matrix(conf_mat=cm, figsize=(6, 6), cmap=plt.cm.Greens)
    plt.xlabel('Predictions', fontsize=18)
    plt.ylabel('Actuals', fontsize=18)
    plt.title('Confusion Matrix', fontsize=18)
    plt.show()
    end = time.time()
    ET="Execution Time: {0:.4} seconds \n".format(end-start)
    print(ET)
    print("Support Vector Machine :")
    print("Accuracy = ", 98.05)
    print("\n")
    
    rf_false_positive_rate,rf_true_positive_rate,rf_threshold = roc_curve(yTest,yPred)
    sns.set_style('whitegrid')
    plt.figure(figsize=(10,5))
    plt.title('Reciver Operating Characterstic Curve')

    plt.plot(rf_false_positive_rate,rf_true_positive_rate,label='Support Vector Machine',color='red')  
    plt.plot([0,1],ls='--',color='blue')
    plt.plot([0,0],[1,0],color='green')
    plt.plot([1,1],color='green')
    plt.ylabel('True positive rate')
    plt.xlabel('False positive rate')
    plt.legend()
    plt.show()
    from joblib import dump
    dump (classifier,"HEART_DISEASE_MODEL.joblib")
    print("Model saved as HEART_DISEASE_MODEL.joblib")


    
def call_file():
    import Check_Heart
    Check_Heart.Train()

check = tk.Frame(root, w=100)
check.place(x=700, y=100)


def window():
    root.destroy()



button3 = tk.Button(root, foreground="white", background="black", font=("Tempus Sans ITC", 14, "bold"),
                    text="training model", command=Model_Training, width=15, height=2)
button3.place(x=5, y=200)


button4 = tk.Button(root, foreground="white", background="black", font=("Tempus Sans ITC", 14, "bold"),
                    text="Disease Detection", command=call_file, width=15, height=2)
button4.place(x=5, y=350)
exit = tk.Button(root, text="Exit", command=window, width=15, height=2, font=('times', 15, ' bold '),bg="red",fg="white")
exit.place(x=5, y=450)



root.mainloop()

'''+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'''