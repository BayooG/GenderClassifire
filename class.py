import time
from sklearn import tree
	
X = [[150,45,37],[190,80,43],[175,60,39],
     [177,75,44],[180,76,43],[167,70,39],
     [166,66,38],[207,85,45],[164,55,38],
     [170,69,45],[165,53,37],[170,80,40]]

y = ['female','male','female',
     'male'  ,'male','female',
     'female','male','female',
     'male','female', 'male']

test_X = [[172,85,39], [151,44,37], [200,70,39],
		     [180,71,38], [182,79,44], [170,69,43]]

test_y = [['male'], ['female'], ['female'],
		     ['female'],['male'],['male']]


def main():
	start_time = time.time()
	clf =tree.DecisionTreeClassifier()
	clf = clf.fit(X,y)
	count = 0
	for i in range(len(test_X)):
		if str(clf.predict([test_X[i]]))!=str(test_y[i]):
			count= count+1

	print('acc = '+str(1-(count/len(test_X	))))
	print('time of execution : %s seconds ' % (time.time() - start_time))
	


if __name__ == '__main__':
	main()
