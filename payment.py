class Payment:
    def __init__(self,initialbill,guest_name):
        self.initialbill=initialbill
        self.finalbill=0
        self.totaltax=0
        self.guest_name=guest_name

    def tax_amount(self):
        tax_bracket=0.20
        totaltax=0.20*self.initialbill
        self.totaltax=totaltax
        return totaltax
    
    def final_amount(self):
        final_amount=self.initialbill + self.tax_amount()
        self.finalbill=final_amount
        return final_amount
    
    def get_final_bill(self):
        self.final_amount()
        print(f'Here is the final bill of customer {self.guest_name} \n')
        print(f'guest: {self.guest_name}')
        print(f'initial bill :{self.initialbill}')
        print(f'tax_amount: {self.totaltax}')
        print(f'total bill: {self.finalbill}')



