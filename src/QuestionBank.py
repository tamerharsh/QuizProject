
class SimpleQuestionBank:
    def __init__(self) -> None:
        pass
    def AddQuestion(self,question_id,question,option_a,option_b,option_c,option_d,correct_ans):
        self.question_id=question_id
        self.question=question
        match correct_ans:
            case 'a':self.correct_ans=self.options[self.option_a]
            case 'b':self.correct_ans=self.options[self.option_b]
            case 'c':self.correct_ans=self.options[self.option_c]
            case 'd':self.correct_ans=self.options[self.option_d]         
        self.options={self.option_a:option_a,self.option_b:option_b,self.option_c:option_c,self.option_d:option_d}
        self.question_bank={self.question_id,[self.question,self.options,self.correct_ans]}
    
    def DeleteQuestion(self,question_id):
        if(self.question_bank[question_id]):
            self.question_bank.remove(question_id)
            print("Deleted Question exists with ID=",self.question_id)
        else:
            print("Id=",self.question_id,"not found")
        
class DefineGame:
    def __init__(self) -> None:
        pass
                
        
            
        
        
    
