class credit_card:
  """A consumer credit card"""

  def __init__(self,customer,bank,acnt,limit):
    self.customer = customer
    self.bank = bank
    self.acnt = acnt
    self.limit = limit
    self.balance = 0 

  def get_customer(self):
    return self.customer

  def get_bank(self):
    return self.bank

  def get_acnt(self):
    return self.acnt   

  def get_limit(self):
    return self.limit

  def get_balance(self):
    return self.balance

  def charge(self,price):
    """Charge given price to the card , assuming sufficient balance 
    Return True if charge was processed , False if charge is denied"""

    if price+self.balance > self.limit:
      return False
    else:
      return True

  def make_payment(self,amount):
    self.amount = amount
    """Process customer payment that reduces the balance"""
    self.balance = self.balance-amount


class PredatoryCreditCard(credit_card):
  def __init__(self,customer,bank,acnt,limit,apr):
    super.__init_(customer,bank,acnt,limit)
    self.apr = apr
  def charge(self, price):
    success  = super().charge(price) #call inherit method
    if not success:
      self.balance+=5 #assess penality
    return success

  def process_month(self):
    """Acess monthly interset on outstanding balance"""
    if self.balance>0:
      #if positive balance convert APR to monthly multiplication factor
      monthly_factor = pow(1+self.apr , 1/12)
      self.balance*=monthly_factor


if __name__ == '__main__':
  wallet = []
  wallet.append(credit_card("john joe","union bank of india","5000,000",500))
  wallet.append(credit_card("peter","Bank of britian","4000,000",2500))
  wallet.append(credit_card("garvee","Bank of Ameria","6000,000",5000))

  for val in range(1,7):
    wallet[0].charge(val)
    wallet[1].charge(2*val)
    wallet[2].charge(3*val)
  #get the details of individual account information

  for c in range(len(wallet)):
    print("customer=" , wallet[c].get_customer())
    print("Bank=" , wallet[c].get_bank())
    print("Account=" , wallet[c].get_acnt())
    print("Limit=" , wallet[c].get_limit())
    print("Blanace=" , wallet[c].get_balance())
    while wallet[c].get_balance() > 100:
      wallet[c].make_payment(100)
      print("New balance =",wallet[c].get_balance()) 
    print("\n**********************************************\n")



