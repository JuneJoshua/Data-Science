import matplotlib.pyplot as plt
from sklearn import datasets
iris = datasets.load_iris()

predictors = iris.data[:, 0:2]
outcomes = iris.target
plt.plot(predictors[outcomes==0][:,0], predictors[outcomes==0][:, 1], "ro")
plt.plot(predictors[outcomes==1][:,0], predictors[outcomes==2][:, 1], "go")
plt.plot(predictors[outcomes==2][:,0], predictors[outcomes==2][:, 1], "bo")
plt.savefig("iris.pdf")

