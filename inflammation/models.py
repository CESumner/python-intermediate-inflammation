class Observation:
    def __init__(self, value, day):
        self.day = day
        self.value = value

    def __str__(self):
        return str(self.value)

class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

class Patient(Person):
    """A patient in an inflammation study."""
    def __init__(self, name):
        super().__init__(name)
        self.trial_group = None
        self.doctor = None
        self.observations = []

    def add_observation(self, value, day=None):
        if day is None:
            try:
                day = self.observations[-1].day + 1

            except IndexError:
                day = 0

        new_observation = Observation(value, day)

        self.observations.append(new_observation)
        return new_observation


class Doctor(Person):
    """A doctor in an inflammation study."""
    def __init__(self, name):
        super().__init__(name)
        self.patients = []

    def add_patient(self, Patient):
        self.patients.append(Patient)
        Patient.doctor = self.name

    @property
    def patient_list(self):
        return self.patients

    def __str__(self):
        return self.name

alice = Patient('Alice')
print(alice)

obs = alice.add_observation(3)
print(obs)

bob = Person('Bob')
print(bob)

DrSmith = Doctor("Dr Smith")
DrSmith.add_patient((alice))
patients = DrSmith.patient_list
for patient in patients:
    print(patient)