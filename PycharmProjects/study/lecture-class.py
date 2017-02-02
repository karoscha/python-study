class Student:
    val1 = ''
    val2 = ''

    def __init__(self, name='pidch'):
        self.val1 = name

    def __init__(self, name='pidch', lover='karoscha'):
        self.val1 = name
        self.val2 = lover

    def studentInfo(self):
        print('name={}, lover={}'.format(self.val1, self.val2))

    def __del__(self):
        print('delete Stduent={}'.format(self.val1))


student1 = Student('karos')
student1.val2 = 'pidch'
student1.studentInfo()

student2 = Student()
student2.studentInfo()