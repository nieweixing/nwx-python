# 类的定义

class Student:

    def __init__(self, name, score):
        self.name = name
        self.score = score
    
    def say_score(self):
        print("{0} 的分数是 {1}".format(self.name, self.score))

sl = Student("niewx", 60)
sl.say_score()