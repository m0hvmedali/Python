class Student :
    def __init__(self,name,sub):
        self.StudentName = name
        self.StudentSub = sub
        
    def SaveData(self,name,sub):
        Data = {'Name':self.StudentName,'sub':self.StudentSub}
        return Data
        print(Data)

class Test :
    ...
    p = 'mohamed is my name'

# NOTE: can you called object is a instance meaning نموذج from your class you are defined
