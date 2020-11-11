from matplotlib import pyplot as plt
from sklearn import datasets
iris_datasets = datasets.load_iris()

plt.figure(figsize=(16,9))
data = iris_datasets['data']
classflower = iris_datasets['target_names']
feature_names = iris_datasets['feature_names']
target = iris_datasets['target']
plt.scatter(data[2][target == 0],data[3][target == 0],marker='o',label=classflower[0])
plt.scatter(data[2][target == 1],data[3][target == 1],marker='x',label=classflower[1])
plt.scatter(data[2][target == 2],data[3][target == 2],marker='*',label=classflower[2])
plt.ylabel([feature_names['3']])
plt.xlabel([feature_names['2']])
plt.title('Iris Data')
plt.show()

