class Question:
    def __init__ (self, question, answer, points, category):
        self.question = question
        self.answer = answer
        self.points = points
        self.category = category

class TorF(Question):
    def __init__ (self, question, answer, points, category):
        super().__init__ (question, answer, points, category)

    def check_answer(self, input):
        if input.lower() == self.answer or input.lower() == self.answer[:1] :
            return self.points
        else:
            return 0

    def get_possible(self):
        return self.points

class choose1(Question):
    def __init__ (self, question, options, answer, points, category):
        super().__init__ (question, answer, points, category)
        self.options = options
 

    def check_answer(self, input):
        if input.upper() == self.answer:
            return self.points
        else:
            return 0
    
    def get_possible(self):
        return self.points

class choose2(Question):
    def __init__ (self, question, options, answer1, answer2, points, category):
        super().__init__ (question, options, points, category)
        self.options = options
        self.answer1 = answer1
        self.answer2 = answer2


    def check_answer(self, input1, input2):
        answers = [input1.upper(), input2.upper()]
        answers = list(set(answers)) #checks to see if entries are unique and puts them into another list based on unique values
        total_points = 0

        if len(answers) > 1:  #if more than one item in list then values are unique
            if answers[0] == self.answer1 or answers[0] == self.answer2:
                total_points += 1
            if answers[1] == self.answer1 or answers[1] == self.answer2:
                total_points += 1
        else:
            selection = str(answers[0])
            if selection == self.answer1 or selection == self.answer2:
                total_points += 1
            else:
                total_points = 0

        if total_points == 2:
            return self.points
        if total_points == 1:
            return 1
        else:
            return 0
    
    def get_possible(self):
        return self.points

# # class choose3():

#     def __init__ (self, question, options, answer1, answer2, answer3, points, category):
#         self.question = question
#         self.options = options
#         self.answer1 = answer1
#         self.answer2 = answer2
#         self.answer3 = answer3
#         self.points = points
#         self.category = category

#     def check_answer():
#         pass