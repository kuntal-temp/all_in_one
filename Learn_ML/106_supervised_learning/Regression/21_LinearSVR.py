'''
LinearSVR is same as kernal(Linear) in svm
'''

from sklearn.svm import LinearSVR

reg = LinearSVR()
reg.fit(x, y)
