# coding: utf-8
# In[122]:
import matplotlib
matplotlib.use('agg')
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os.path

# In[123]:

class EmployeeTurnover():        
    def importing_data(self):
        dataset = pd.read_csv('HR.csv')
        self.X = dataset.iloc[:,[0,1,2,3,4,5,7,9]].values
        self.Y = dataset.iloc[:,6].values 
        
        from sklearn.preprocessing import LabelEncoder
        labelencoder_X = LabelEncoder()
        self.X[:,7] = labelencoder_X.fit_transform(self.X[:,7])
        
    def splitting_and_feature_scaling(self):
        "Splitting the dataset into the Training set and Test set"
        from sklearn.cross_validation import train_test_split
        self.X_train, self.X_test, self.Y_train, self.Y_test = train_test_split(self.X, self.Y, test_size = 0.25, random_state = 0)

        "Feature Scaling"
        from sklearn.preprocessing import StandardScaler
        sc = StandardScaler()
        self.X_train = sc.fit_transform(self.X_train)
        self.X_test = sc.transform(self.X_test)
        
    def fitting_svm(self):
        "Fitting SVM to the Training set"
        from sklearn.svm import SVC
        classifier = SVC(C=10, kernel='rbf', gamma=0.5)
        classifier.fit(self.X_train, self.Y_train)
        return classifier
                
    def fitting_logistic_regression(self):
        "Fitting Logistic Regression to the Training set"
        from sklearn.linear_model import LogisticRegression
        classifier = LogisticRegression(random_state = 0)
        classifier.fit(self.X_train, self.Y_train)
        return classifier  
    
    def fitting_decision_tree(self):
        "Fitting Decision Tree Classifier to the Training set"
        from sklearn.tree import DecisionTreeClassifier
        classifier = DecisionTreeClassifier(criterion = 'entropy', random_state = 0, max_depth=3, min_samples_leaf=5)
        classifier.fit(self.X_train, self.Y_train)
        return classifier
    
    def fitting_random_forest(self):
        "Fitting Random Forest Classification to the Training set"
        from sklearn.ensemble import RandomForestClassifier
        classifier = RandomForestClassifier(n_estimators = 10, criterion = 'entropy', random_state = 0)
        classifier.fit(self.X_train, self.Y_train)
        return classifier
       
    def evaluate_on_test_data(self,model=None):
        "Predicting the Test set results"
        predictions = model.predict(self.X_test)
        
        "Calculating Accuracy"
        correct_classifications = 0
        for i in range(len(self.Y_test)) :
            if predictions[i] == self.Y_test[i] :
                correct_classifications += 1
        accuracy = 100*correct_classifications/len(self.Y_test)
        return accuracy

    
def visualize():
    "Comparing the different Algorithms"
    predict = EmployeeTurnover()
    predict.importing_data()
    predict.splitting_and_feature_scaling()
    svm_per = predict.evaluate_on_test_data(predict.fitting_svm())
    lr_per = predict.evaluate_on_test_data(predict.fitting_logistic_regression())
    dt_per = predict.evaluate_on_test_data(predict.fitting_decision_tree())
    rf_per = predict.evaluate_on_test_data(predict.fitting_random_forest())
    
    labels = ['SVM', 'Logistic Regression', 'Decision Tree', 'Random Forest']
    y_pos = np.arange(len(labels))
    values = [svm_per, lr_per, dt_per, rf_per]
    plt.bar(y_pos, values, width = 0.40, align='center', alpha=0.5)
    plt.xticks(y_pos, labels)
    plt.ylabel('Accuracy')
    plt.xlabel('Algorithms')
    plt.title('Algorithms Comparision')
	#if not os.path.isfile('../static/1.png'):
	plt.savefig('../static/1.png')
        
# In[124]:

if __name__=="__main__":
    visualize()

