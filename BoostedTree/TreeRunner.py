# File created by Utkarsh Gupta
# Dated 20/02/2020

# Touched on 20/02/2020 by Utkarsh Gupta

# Execution of boosted tree

from TreeClassifier import treeClassifier


class TreeRunner():
    def __init__(self):
        self.tree = treeClassifier()
        self.tree.getParameterList(noOfTree=5, maxTreeDepth=7, learningRate=0.15, noOfBatchesPerLayer=30)
        self.tree.loadFiles()
        self.tree.generateFeatureColumn()
        self.tree.constructTree()
        self.tree.trainTree()
        self.tree.evaluateTree()
        self.tree.saveTreeModel()

    def predict(self, symptomList):
        self.tree.predictDisease(symptomList)

example = TreeRunner()
a = list()
for i in range(0, 131):
    a.append(0)
a[5] = 1
a[53] = 1
a[100] = 1
a[111] = 1
a[130] = 1
disease = example.predict(a)
print("You might have ", disease)
