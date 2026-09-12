##intiate the class
class employee:
    def __init__(self):
        print("started executing attributes/data")
        self.user_id=124
        self.salary=50000
        self.designation = "SDE"
        print("attributes/data have been initiated")

    def travel(self,destination):
        print("This travel function is called manually")
        print(f"Employee is now traveling to {destination}")


##Creating and obj/instance of the class
charli=employee()
# print(charli.salary)
# print(charli.id)
charli.travel("Bihar")
