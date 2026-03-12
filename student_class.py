class Cmp142:
    
    def __init__(self, students,tables,gender,chairs):
        self.students = students
        self.tables = tables
        self.gender = gender
        self.chairs = chairs
    def lectures(self):
        print('I am ' + self.students)
    def seat(self):
        print(' The ' + self.students + 'is eating on the ' + self.chairs + ' and his laptop is on ' + self.tables)
    def wideboard(self):
        print('the '+ self.students + self.wideboard)
std_1= Cmp142('Baran ', 'seat2', 'Male', 'char2')  

std_1.lectures()
std_1.seat()
