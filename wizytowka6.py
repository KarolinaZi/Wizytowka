from faker import Faker
fake = Faker()

class BaseContact:
    def __init__(self, first_name, last_name, private_phone, email):
        self.first_name = first_name
        self.last_name = last_name
        self.private_phone = private_phone
        self.email = email
       # Variables
        #self.name_lenght = 0

    def __str__(self):
        return f'{self.first_name}, {self.last_name}, {self.private_phone}, {self.email}'    
    
    def contact(self):
            print(f'Wybieram numer {self.private_phone} i dzwonię do {self.first_name} {self.last_name}.')


    def label_lenght(func):    
        return func

    @label_lenght
    def name_len(self):
        self.name_lenght = len(self.first_name) + len(self.last_name) + 1
        print("Długość imienia i nazwiska to " + str(self.name_lenght) + " znaków.")
        return self.name_lenght


class BusinessContact(BaseContact):
    def __init__(self, job, company, business_phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.job = job
        self.company = company
        self.business_phone = business_phone
    def __str__(self):
        return f'{self.job}, {self.company}, {self.business_phone}'
    def contact(self):
        print(f'Wybieram numer służbowy {self.business_phone} i dzwonię do {self.first_name} {self.last_name}.')

def create_contacts(vc_type, vc_number):
    for i in range(vc_number):
        if vc_type == "basic":
            i = BaseContact(first_name = fake.first_name(), last_name = fake.last_name(), private_phone = fake.phone_number(), email=fake.ascii_company_email())
        elif vc_type == "business":
            i = BusinessContact(first_name = fake.first_name(), last_name = fake.last_name(), private_phone = None, business_phone = fake.phone_number(), company=fake.company(), job = fake.job(), email=fake.ascii_company_email())
        else:
            print('enter "basic" or "business" as visiting card type')
            exit(1)
        i.contact()
        i.name_len()

create_contacts("basic", 2)