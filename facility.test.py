# Student Name: Gordon Lam
# Student ID: 000892800
# Assignment: 4 - Classes (Individual)
# Section responsible in the group project: facility class


class facility:
    #Constructor
    def __init__(self,FacilityName):
        self.FacilityName = FacilityName

    #Method
    def addFacility(self):
        pass

    def displayFacilities(self):
        FacilitiesFile=open("facilities.txt","r")
        fList = FacilitiesFile.read()
        print(fList)
        FacilitiesFile.close()
    
    def writeListOffacilitiesToFile(self):
        New_facility=facility(input("Enter new facility: "))
        appendFile=open('facilities.txt','a')
        appendFile.write("\n")
        appendFile.write(str(New_facility.FacilityName))
        appendFile.close()