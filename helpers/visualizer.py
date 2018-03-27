import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import numpy as np

def input_data_chart(data):
	labels = ['data' + str(i) for i in range(1,len(data)+1)]
	y_pos = np.arange(len(labels))
	plt.bar(y_pos, data, width = 0.40, align='center', alpha=0.5)
	plt.xticks(y_pos, data)
	plt.ylabel('Intensity')
	plt.xlabel('Parameters')
	plt.title('Input Data')
	plt.savefig('static/input_data.png')
	
def confusion_matrix():
	pass
	
def accuracy_ratio():
	pass
	
## plot the importances ##
def feature_importances(classifier):
	importances = classifier.feature_importances_
	feat_names = ['','','','','','','']
	indices = np.argsort(importances)[::-1]
	plt.figure(figsize=(12,6))
	plt.title("Feature importances by DecisionTreeClassifier")
	plt.bar(range(len(indices)), importances[indices], color='lightblue',  align="center")
	plt.step(range(len(indices)), np.cumsum(importances[indices]), where='mid', label='Cumulative')
	plt.xticks(range(len(indices)), feat_names[indices], rotation='vertical',fontsize=14)
	plt.xlim([-1, len(indices)])
	plt.savefig('static/feature_importances.png')
