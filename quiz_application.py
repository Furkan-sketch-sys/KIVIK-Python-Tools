class Question() :
    def __init__(self , question , choice , answer):
        self.question = question
        self.choice = choice
        self.answer = answer


    def check_answer(self , user_answer) :
        return self.answer.upper() == user_answer.upper() 
    


class Quiz() :
    def __init__(self , question):
        self.question = question
        self.score = 0
        self.question_index = 0

    def get_question(self) :
        return self.question[self.question_index]
    

    def display_question(self) :
        question = self.get_question()
        print(f"\n--- Question {self.question_index + 1} / {len(self.question)}---")
        print(question.question)
        

        for choice in question.choice :
            print(f"-{choice}")

        user_answer = input("\n Please tell everyone your answer : ")


        if question.check_answer(user_answer) :
            print("True")
            self.score += 10

        else :
            print("\n Wrong Answer! Please try again.")


        self.question_index += 1


    def show_score(self) :
        print("\n" + "=" * 30)
        print("Quiz has been completed.")
        print(f"Total_score : {self.score} / {len(self.question) * 10}")
        print("=" * 30)



q1 = Question("TSK'nin acilimi nedir?" , [" A) Türk Silahli Kuvvetleri" , "B) Türk Hava Kuvvetleri " , "C) Türk Deniz Kuvvetleri" , "D) Özel Kuvvetler Komutanliği"] , "A")
q2 = Question("Ethan has 5 pencil in his hand . If he gives his 2 pencil to his friend - Matt- , how many does he have left in his hand?" , ["A ) 5" , "B ) 4" , "C ) 1" , "D ) 3"] , "D")
q3 = Question("The year : 2008 , Emma who is a child 10 years old wants to calculate her age in 2001. What's her age in 2001?" , ["A ) 5" ,"B) 3" , "C ) 10" , " D ) 6" ] , "B")

questions = (q1 , q2 , q3)
quiz = Quiz(questions)

while quiz.question_index < len(quiz.question) :
    quiz.display_question()

quiz.show_score()
