# Student Name: Gordon Lam
# Student ID: 000892800
# Assignment: 4 - Classes (Individual)
# Responsible for the facility class


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






'''
# The lines are used to test the methods (you may ignore them)
print("Welcome to the AH Facility")
option = int(input("Please choose the Facilities\n 1 - Display Facilities list \n 2 - Add Facility\n 3 - Back to the Main Menu\n"))

if option == 1:
    facility.displayFacilities(facility.displayFacilities)

elif option == 2:
    facility.writeListOffacilitiesToFile(facility.writeListOffacilitiesToFile)

'''