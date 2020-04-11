class CallHandler:

  def __init__(self,employees):
    """ employees has a list of freshers,
        only one technical lead and only one product manager """
    
    self.freshers = []

    # sort employees first
    for employee in employees:
      if employee.getRank() == 0: # fresher
        self.freshers.append(employee)
      elif employee.getRank() == 1: # technical lead
        self.tl = employee
      else:
        self.pm = employee
        

  def getCallHandler(self):
    """ associates an employee to an incoming call,
      returns an employee instance to answer, and
      False if nobody is available"""
    person = self.getAvailableFresher()

    if not person: # if a fresher is not available
      if not self.tl.availability(): # if TL is not available
        if not self.pm.availability(): # if PM is not available
          return False
        else: # if PM is available
          return self.pm
      else: # if TL is available
        return self.tl

    # a fresher is available to answer the call
    return person

  def getAvailableFresher(self):
    """ finds an available to answer the call employee """
    for employee in self.freshers:
      if employee.availability():
        return employee

    return False

class Employee:

  def __init__(self,rank,name): # more information can be added later
    """ rank = 1 for Fresher, 2 for technical lead, 3 for product manager """
    self.available = True # False when not available to answer a call
    self.rank = rank
    self.name = name

  def availability(self): # available to answer the call?
    """ returns True if available, and False otherwise """
    return self.available

  def getRank(self):
    return self.rank

  def getName(self):
    return self.name

  def __str__(self):
    name = self.name
    if self.rank == 0:
      return self.name + ", fresher"
    elif self.rank == 1:
      return self.name + ", technical lead"
    else:
      return self.name + ", product manager"

#### --------------   TESTING ------------------
# only PM is available
employees = [Employee(0,"Alex"),Employee(1,"Mike"),Employee(0,"Alice"),Employee(0,"Frank"),Employee(2,"Ian")]
employees[0].available = False
employees[1].available = False
employees[2].available = False
employees[3].available = False
c1 = CallHandler(employees)
print("available to answer the call:",c1.getCallHandler())


# Alice, fresher is available
employees2 = [Employee(0,"Alex"),Employee(1,"Mike"),Employee(0,"Alice"),Employee(0,"Frank"),Employee(2,"Ian")]
employees2[0].available = False
employees2[1].available = False

c2 = CallHandler(employees2)
print("available to answer the call:",c2.getCallHandler())
