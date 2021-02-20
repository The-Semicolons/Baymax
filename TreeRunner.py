# File created by Utkarsh Gupta
# Dated 20/02/2020

# Touched on 20/02/2020 by Utkarsh Gupta

# Execution of boosted tree

import TreeClassifier


class TreeRunner:
    def __init__(self):
        self.tree = TreeClassifier.treeClassifier()
        self.tree.getParameterList(noOfTree=5, maxTreeDepth=7, learningRate=0.15, noOfBatchesPerLayer=30)
        self.tree.loadFiles()
        self.tree.generateFeatureColumn()
        self.tree.constructTree()
        self.tree.trainTree()
        self.tree.evaluateTree()
        self.tree.saveTreeModel()

    def predict(self, symptomList):
        return self.tree.predictDisease(symptomList)
