import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix


dataset = pd.read_csv(r'C:\Users\Eddy Doering\Documents\Random Junk\Summer Job\Job\GENESIS10\Capstone\diabetic_data.csv')#, header="true")
df = dataset

df.drop(columns = ['encounter_id','patient_nbr', "weight", "medical_specialty"], inplace=True)
df = df[df.race!='?']
df = df[df.gender!='Unknown/Invalid']
df = df[df.payer_code!='?']

df = pd.get_dummies(df, columns= ["race","gender", "age", "admission_type_id", "discharge_disposition_id","admission_source_id",
                                          "payer_code", "diag_1", "diag_2", "diag_3","change","diabetesMed", "max_glu_serum","A1Cresult"], drop_first=True)
scale_mapper = {
    "No"    :0,
    "Down"  :1,
    "Steady":1,
    "Up"    :1
}
listMeds = [
       "metformin","repaglinide","nateglinide","chlorpropamide","glimepiride",
        "acetohexamide","glipizide","glyburide","tolbutamide","pioglitazone","rosiglitazone","acarbose","miglitol",
        "troglitazone","tolazamide","examide","citoglipton","insulin","glyburide-metformin","glipizide-metformin",
        "glimepiride-pioglitazone","metformin-rosiglitazone","metformin-pioglitazone"
        ]
df = pd.get_dummies(df, columns= listMeds, drop_first=True)
df.reset_index()

df[listMeds] = df[listMeds].replace(scale_mapper)

###########################################################################################
##################################### Split X/y ###########################################
###########################################################################################

X = df
y = X.readmitted
X.drop(columns = ['readmitted'], inplace=True)

y.replace(to_replace=['>30', '<30'], value='YES', inplace=True)

print(X.shape)

###########################################################################################
###################################### Train/Test Split ###################################
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.05, random_state=0)
leaf_size= 1
p= 1
n_neighbors=11
neigh = KNeighborsClassifier(n_neighbors=n_neighbors, leaf_size= leaf_size, p=p,n_jobs=4)
# neigh = KNeighborsClassifier()
neigh.fit(X_train, y_train)
y_pred = neigh.predict(X_test)
predSeries = pd.Series(y_pred)

###########################################################################################
####################################### Print Statements ##################################
###########################################################################################
print(neigh.score(X_test, y_test))                                                       ##
print(confusion_matrix(y_test, y_pred))                                                  ##
###########################################################################################
###########################################################################################


###########################################################################################
##################### For looping over multiple Medical Specialties #######################
###########################################################################################
# for i in listOfSpecalties:
#     print(i)
#     X = df[df.medical_specialty == i]
#     y = X.readmitted
#     X.drop(columns = ['readmitted','medical_specialty'], inplace=True)
#     #X = pd.DataFrame(X)
#     #y = pd.DataFrame(y)
#     # X.reset_index(inplace=True)
#     # y.reset_index(inplace=True)
#
#     y.replace(to_replace=['>30', '<30'], value='YES', inplace=True)
#
#     print(X.shape)
#     #print(X.head(5))
#     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)
#     # leaf_size= 5
#     # p= 1
#     # n_neighbors=10
#     # Score = 0.6030100334448161
#
#     leaf_size= 1
#     p= 1
#     n_neighbors=11
#     # Score = 0.6083612040133779
#     neigh = KNeighborsClassifier(n_neighbors=n_neighbors, leaf_size= leaf_size, p=p,n_jobs=4)
#
#     neigh.fit(X_train, y_train)
#     y_pred = neigh.predict(X_test)
#     predSeries = pd.Series(y_pred)
#     print(neigh.score(X_test, y_test))
#
#     print(confusion_matrix(y_test, y_pred))

########################################################################################################################
#### Hyperparameter Tuning #############################################################################################
########################################################################################################################

# leaf_size = [ 5,10,15,20,25,30,35,40,45,50]
# n_neighbors = [5,10,15,20,25,30]
# p=[1,2]
# leaf_size = list(range(1,50))
# n_neighbors = list(range(1,30))
# p=[1,2]
#
# #Convert to dictionary
# hyperparameters = dict(leaf_size=leaf_size, n_neighbors=n_neighbors, p=p)
#
# #Create new KNN object
# knn_2 = KNeighborsClassifier()
#
# #Use GridSearch
# clf = GridSearchCV(knn_2, hyperparameters, cv=3, verbose=3)
#
# #Fit the model
# best_model = clf.fit(X_test,y_test)
#
# #Print The value of best Hyperparameters
# print('Best leaf_size:', best_model.best_estimator_.get_params()['leaf_size'])
# print('Best p:', best_model.best_estimator_.get_params()['p'])
# print('Best n_neighbors:', best_model.best_estimator_.get_params()['n_neighbors'])