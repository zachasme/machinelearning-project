from sklearn.metrics import confusion_matrix
from sklearn import svm, datasets
from sklearn.cross_validation import train_test_split

import pylab as pl

x_true = [0,1,1,1,0,1,0,1,1,0,1,0,0,0,1,0,1,0,0,0,1,1,0,0,1,0,1,0,1,0,0,1,1,1,1,1,1
,1,1,1,0,0,1,1,1,0,1,1,0,0,1,1,1,0,0,1,1,0,1,0,0,1,0,1,1,0,1,0,1,0,0,0,0,0
,1,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,1,1,0,0,1,1,1,1,0,0,1,0,1,1,0,1,1,0,1,1,1
,0,0,1,1,1,1,0,0,1,0,1,0,1,0,0,0,1,1,0,1,0,1,1,0,0,0,1,1,0,1,0,1,0,1,1,1,0
,1,1,1,1,0,0,1,1,0,1,1,0,0,0,0,0,0,1,1,0,1,0,0,0,0,1,1,1,0,1,0,1,1,0,1,0,0
,1,0,0,0,0,1,0,1,0,0,0,0,1,0,1]

x_pred = [2,1,1,2,1,2,1,0,1,1,2,1,1,1,2,1,2,1,1,1,2,2,0,2,0,1,2,1,1,1,1,2,0,1,1,1,2
,0,0,1,1,2,0,2,1,2,1,0,1,1,1,2,1,1,1,0,2,1,2,1,1,1,1,0,0,1,2,1,2,1,1,0,1,1
,2,1,1,0,2,2,2,2,0,1,0,1,1,1,1,2,0,1,1,1,2,2,0,0,1,2,2,1,2,2,1,0,0,1,0,2,2
,1,1,2,2,1,2,1,1,2,2,1,1,1,1,1,1,2,2,1,0,1,0,2,2,1,1,2,1,1,1,1,0,1,2,2,0,1
,0,0,2,0,1,1,0,2,1,0,2,1,1,2,1,1,1,2,0,1,0,1,1,1,1,0,2,2,1,2,1,1,1,0,0,1,1
,2,2,1,1,1,2,1,0,1,1,1,1,0,2,0]

cm = confusion_matrix(x_pred, x_true)

print(cm)

# Show confusion matrix in a separate window
pl.matshow(cm)
pl.title('Confusion matrix')
pl.colorbar()
pl.xlabel('True label')
pl.ylabel('Predicted label')
pl.show()


x_pred = [1,1,0,1,1,1,1,0,1,1,1,1,1,1,1,0,1,1,0,1,1,1,0,1,2,1,1,0,0,0,0,1,1,1,1,1,1
,0,0,0,0,1,1,1,1,1,1,0,1,0,1,1,1,1,1,0,1,0,1,1,1,0,0,0,0,1,1,1,1,0,1,0,1,0
,1,1,1,1,1,1,1,1,0,1,0,0,0,1,0,1,0,1,1,1,1,1,0,0,1,1,1,1,1,1,0,0,1,1,0,1,1
,1,1,1,1,0,1,1,1,1,1,1,1,1,0,1,1,1,1,0,0,0,0,1,1,1,1,1,0,1,1,1,1,0,1,1,1,0
,0,0,1,1,1,1,0,1,1,0,1,0,0,1,1,1,1,1,0,0,0,1,1,0,0,1,1,1,1,1,0,1,0,0,0,1,1
,1,1,1,1,1,1,1,0,1,1,1,1,1,1,0]

cm = confusion_matrix(x_pred, x_true)

print(cm)

pl.matshow(cm)
pl.title('Confusion matrix')
pl.colorbar()
pl.xlabel('True label')
pl.ylabel('Predicted label')
pl.show()