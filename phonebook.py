class PhoneBook:
    def __init__(self):
        self.contact ={}
    def add_contact(self,name, number):
        self.contact[name.upper()] = number
        print(f"{name} Added to contacts")
    def remove_contact(self,name):
        if name.upper in self.contact:
            self.contact.pop(name.upper)
            print(f"{name} Deleted")
        else :
            print(f"Name not found")
        
    def search_contact(self, name):
        return self.contact.get(name.upper(),"Oops not found")
    
phone1 = PhoneBook()
phone1.add_contact("Kas", "123456789")
phone1.add_contact("Kao", "2345678901")
phone1.add_contact("Kago", "3456789012")
print(phone1.contact)

    
