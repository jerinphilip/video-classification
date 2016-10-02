from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import numpy as np

from pykernels.regular import GeneralizedHistogramIntersection

class SVM:
	def train(self,data,classes):
		print 'Training:'
		for clf, name in [(SVC(kernel=GeneralizedHistogramIntersection(), C=1000), 'pykernel')]:
			clf.fit(data, classes)
			print name
			print clf
			print

	def predict(self,p_data):
		print 'Predictions:'
		for clf, name in [(SVC(kernel=GeneralizedHistogramIntersection(), C=1000), 'pykernel')]:
			print name
			print clf
			print 'Predictions:', clf.predict(data)
			print 'Accuracy:', accuracy_score(clf.predict(data), classes)
			print
