class WithoutIO:
    def __init__(self):
        self.v_membrane = -75

    def main(self):
        self.v_membrane += 30


class WithIO:
    def __init__(self):
        self.init_pot = -75

    def main(self):
        v_add = int(input("Enter the potential you want to add"))
        new_v = self.init_pot + v_add
        return new_v


class WithIOSpike:
    def __init__(self):
        self.init_pot = -75
        self.threshold = -65

    def main(self):
        v_add = int(input("Enter the potential you want to add"))
        new_v = self.init_pot + v_add
        if new_v >= self.threshold:
            return True
        else:
            return False


class WithCommand:
    def __init__(self):
        self.init_pot = int(input("Input the initial membrane potential"))
        self.threshold = int(input("Input the threshold value"))

    def main(self):
        v_add = int(input("Enter the potential you want to add"))
        new_v = self.init_pot + v_add
        if new_v >= self.threshold:
            return True
        else:
            return False


Neuron = WithIOSpike()
output=Neuron.main()
print(output)