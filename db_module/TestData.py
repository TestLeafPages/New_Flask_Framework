class TestData:

    def __init__(self, **kwargs):
        self.fname = kwargs['fname']
        self.lname = kwargs['lname']
        self.email = kwargs['email']
        self.pwd = kwargs['pwd']


data = TestData(fname= '1', lname='2', email='3', pwd='4')

print(data.fname)


