class PatientNotFoundException(Exception):
    def __init__(self, patient_id):
        self.message = f"Patient with ID {patient_id} not found."
        super().__init__(self.message)