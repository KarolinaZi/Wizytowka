from faker import Faker
fake = Faker()

class BaseContact:
    def __init__(self, first_name, last_name, private_phone, email):
        self.first_name = first_name
        self.last_name = last_name
        self.private_phone = private_phone
        self.email = email


    def __str__(self):
        return f'{self.first_name}, {self.last_name}, {self.private_phone}, {self.email}'    
    
    def contact(self):
            print(f'Wybieram numer {self.private_phone} i dzwonię do {self.first_name} {self.last_name}. Liczba znaków: {self.label_lenght}')

    @property
    def label_lenght(self):
        return len(f'{self.first_name} {self.last_name}')


class BusinessContact(BaseContact):
    def __init__(self, job, company, business_phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.job = job
        self.company = company
        self.business_phone = business_phone
    def __str__(self):
        return f'{self.job}, {self.company}, {self.business_phone}'
    def contact(self):
        print(f'Wybieram numer służbowy {self.business_phone} i dzwonię do {self.first_name} {self.last_name}. Liczba znaków: {self.label_lenght}')

def create_contacts(vc_type, vc_number):
    for person in range(vc_number):
        if vc_type == "basic":
            person = BaseContact(first_name = fake.first_name(), last_name = fake.last_name(), private_phone = fake.phone_number(), email=fake.ascii_company_email())
        elif vc_type == "business":
            person = BusinessContact(first_name = fake.first_name(), last_name = fake.last_name(), private_phone = None, business_phone = fake.phone_number(), company=fake.company(), job = fake.job(), email=fake.ascii_company_email())
        else:
            print('enter "basic" or "business" as visiting card type')
            exit(1)
        person.contact()


create_contacts("basic",3)