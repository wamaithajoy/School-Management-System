
class SchoolRecords:
    school="AkiraChix"
    def __init__(self,student_name,admission_number,email_address,phonenumber,year_of_birth) :
        self.student_name=student_name
        self.admission_number=admission_number
        self.email_address=email_address
        self.phonenumber=phonenumber
        self.year_of_birth=year_of_birth
        self.stream=['AdaLab','AnitaB','HopperLab']
        self.rooms=["Room10","Room14","Room16","Room18","Room22","Room26","Room32","Room36"]
        self.schoolfees=[]
        self.feebalance=[]


    def enrolling(self):
        return f"Hello {self.student_name} welcome to {self.school} your admission number is {self.admission_number} "

    def students_id(self):
        age=2022-self.year_of_birth
        print(f" Name: {self.student_name}\n Admission Number: {self.admission_number}\n Email Address: {self.email_address}\n Phone Number: {self.phonenumber}\n Students Age: {age} ")
    
        
    def school_fees(self,fees):
        self.fees=fees
        self.total_fees=50000
        if self.fees==self.total_fees:
            self.schoolfees.append(self.fees)
            return f"Hello {self.student_name} you have successfully paid  {self.total_fees}   "
        else:
            fee_balance=self.total_fees-self.fees
            self.feebalance.append(fee_balance)
            return f" Hello {self.student_name}  you have successfully paid {self.fees} and you fee balance is {fee_balance} "
    
    def fee_clearance(self,amount):
        total_amount=self.fees+amount
        if total_amount==self.total_fees:
            self.schoolfees.append(total_amount)
            return f" Hello {self.student_name} you have succesfully cleared your fee balance"
        else:
            pending_fee=self.total_fees-total_amount
            return f"Hello {self.student_name} you have succesfully managed to pay {amount} kindly clear the remaining balance which is {pending_fee} as soon as possible!"
    def student_marks(self):
        self.courses=["Python","Kotlin","Javascript","IOT","UI/UX Design"]
        self.student_marks=[]
        python=int(input("Enter your marks for Python: \n"))
        self.student_marks.append(python)
        kotlin=int(input("Enter your marks for Kotlin: \n"))
        self.student_marks.append(kotlin)
        javascript=int(input("Enter your marks for Javascript: \n"))
        self.student_marks.append(javascript)
        iot=int(input("Enter your marks for IOT: \n"))
        self.student_marks.append(iot)
        design=int(input("Enter your marks for UI/UX design: \n"))
        self.student_marks.append(design)
        grades=dict(zip(self.courses,self.student_marks))
        print(f" {self.student_name}: {grades} ")

    def grading_marks(self):
        sum=0
        for x in self.student_marks:
            sum+=x
            average=sum/len(self.student_marks)
            grade=average
        if grade>=90:
            print('A')
        elif grade>=70 and grade<90:
            print('B') 
        elif grade>=50 and grade<70:
            print('C')
        elif grade>=30 and grade<50:
            print('D')
        else:
            print("Are we in the same school!!")
                               





    
        