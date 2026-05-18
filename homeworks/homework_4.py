class Contact:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

    @classmethod
    def validate_phone_number(cls, phone_number):
        phone_number = str(phone_number)
        return len(phone_number) == 10 and phone_number.isdigit()


class ContactList:
    all_contacts = []

    @classmethod
    def add_contact(cls, name, phone_number):
        if not Contact.validate_phone_number(phone_number):
            raise ValueError(f"Not valid phone number: '{phone_number}'. It must contain 10 digits.")

        new_contact = Contact(name, phone_number)
        cls.all_contacts.append(new_contact)
        return new_contact


ContactList.add_contact("Amaliya", "7001234567")
ContactList.add_contact("Fatima", "7009876543")

for c in ContactList.all_contacts:
    print(f"{c.name}: {c.phone_number}")

ContactList.add_contact("Childe", "123")