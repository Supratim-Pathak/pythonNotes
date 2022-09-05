class Mobile:
    def __init__(self):
        self.model = "Xiomi note 4"
    def getModel(self):
        print(self.model)

class MobileNoTo:
    def __init__(self, m):
        self.model = m
    def getModel(self):
        print(self.model)
        
# CREATING AN OBJECT

obj = Mobile()
print(obj.model)
obj.getModel()

obj2 = MobileNoTo('Samsung')
obj2.getModel()