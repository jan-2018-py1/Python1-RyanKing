class Patient(object):
    def __init__(self, patient_id, name, allergies):
        self.patient_id = patient_id
        self.name = name
        self.allergies = allergies
        self.bed = None

class Hospital(object):
    def __init__(self, name, capacity):
        self.patients = []
        self.name = name
        self.capacity = capacity

    def admit(self, patient):
        if len(self.patients) < self.capacity:
            patient.bed = len(self.patients) + 1
            self.patients.append(patient)
            print "Admission complete."
            return self
        else:
            print "Hospital full, admission not possible."
            return self

    def discharge(self, patient):
        if patient in self.patients:
            idx = patient.bed - 1
            patient.bed = None
            self.patients.pop(idx)
            print "Patient discharged."
            return self
        else:
            print "Patient not found"
            return self

patient1 = Patient(1, "Ryan", "None")
patient2 = Patient(5, "Bob", "None")
patient3 = Patient(3, "John", "None")
patient4 = Patient(4, "Mark", "None")

hospital1 = Hospital("First Hospital", 3)
hospital1.admit(patient1).admit(patient2).admit(patient3).admit(patient4)
# for pat in hospital1.patients:   # testing admit method
#     print pat.name, pat.bed
hospital1.discharge(patient2)
# for pat in hospital1.patients:   # testing discharge method
#     print pat.name, pat.bed
