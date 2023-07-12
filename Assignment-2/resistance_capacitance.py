class circuit:


    def __init__(self,voltage,current):

        self.voltage=voltage

        self.current= current


    def resistance(self):

        return self.voltage/ self.current

    def capacitance(self):

        return self.voltage/(self.current * 2 * 3.14159265359 )


a= circuit(20,9)


r=a.resistance()

c= a.capacitance()

print(f"resistance is {r} ohms and capacitance is {c} f.")
