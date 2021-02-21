import matplotlib.pyplot as plt

class graph:
    def __init__ (self, list1 = None, list2 = None):
        if list1 is None:
            list1 = []
        self.list1 = list1
        if list2 is None:
            list2 = []
        self.list2 = list2

    def plotting (self):
        plt.ylim(0, 5)
        plt.xlim(0,5)
        plt.plot(self.list1, label = 'calculated value')
        plt.legend()
        plt.plot(self.list2, label = 'ideal value')
        plt.legend()
        plt.title('Leucocyte Count')
        plt.show()
        


calc = [2.5, 4, 3.1, 2.9, 3.3]
ideal = [3, 3, 3, 3, 3]
obj = graph(calc, ideal)
obj.plotting()



