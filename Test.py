class PeerMentor:
    pay_rate = 13

    def __init__(self, name, email, working_hours=0):
        self.name = name
        self.email = email
        self.working_hours = working_hours

    def run_discussion(self, hours):
        self.working_hours += hours

    def weekly_pay(self):
        return pay_rate * self.working_hours


abishanka = PeerMentor("Abishanka", "osc32@ufl.edu", 4)
print(abishanka.weekly_pay())
