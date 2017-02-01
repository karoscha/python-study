class Student:
    val1 = ''
    val2 = ''

    def studentInfo(self):
        print('name={}, lover={}'.format(self.val1, self.val2))


student1 = Student()

student1.val1 = 'karoscha'
student1.val2 = 'pidch'

student1.studentInfo()
