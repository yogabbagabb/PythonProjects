

class PaymentPlan ():

    def __init__(self,cost, months):
        self.netC = cost * (9.0/10)
        self.payment = (5.0/100) * cost  * (9.0/10)
        self.months = months
        self.interest = 0
        
    def updateMonth(self, month):
        if (month > self.months):
            SystemExit.exit("Done!")
        
        self.netC -= self.payment
        self.interest += self.netC * (12.0/100)/12.0
        self.principal = self.payment - self.interest
        
        self.displayMonth(month)
        
        
    def displayMonth(self, month):
    
        print ("Month",month,self.netC,self.interest,self.principal)
        self.updateMonth(month + 1)
        
        
    def displayTitle(self):
    
        print ("Net Cost, interest, and principal")
    
def main():
    one = PaymentPlan(1000,4)
    print one.netC
    one.displayTitle()
    one.updateMonth(1)
    
    
main()