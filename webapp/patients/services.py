import logging


# Contains patient related services
class PatientService:

    #Compare existing patientuid from data store
	#Return true if supplied patientuid already exist else return false
    def isduplicatepateint(patientuid):
        patientExist=False
        return patientExist