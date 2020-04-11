# BCC Student "Class"

class BCC_student:

    def __init__(self, name, gpa, creds, sems):
        self.name = name
        self.gpa = gpa
        self.creds = creds
        self.sems = sems # number of semesters

    def howManyCreds(self):
        return self.creds

    def whatsMyName(self):
        return self.name

    def hasGraduated(self, creds_needed):
        return self.creds >= creds_needed

    def avgCredsPerSemester(self):
        avg = self.creds / self.sems
        return avg
        
