from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        super().__init__(value)
        if not self.is_valid_phone(value):
            raise ValueError("Invalid phone number format")
        
    @staticmethod
    def is_valid_phone(value):
        return len(value) == 10 and value.isdigit()

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        
    def add_phone(self, phone):
        self.phones.append(Phone(phone))
        
    def remove_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)
                return
        raise ValueError(f"Phone number '{phone}' not found in record '{self.name.value}'")
    
    def edit_phone(self, old_phone, new_phone):
        for p in self.phones:
            if p.value == old_phone:
                p.value = new_phone
                return
        raise ValueError(f"Phone number '{old_phone}' not found in record '{self.name.value}'")
            
    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        raise ValueError(f"Phone number '{phone}' not found in record '{self.name.value}'")

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def __init__(self):
        self.records = {}
        
    def add_record(self, record):
        self.records[record.name.value] = record
        
    def delete(self, name):
        if name in self.records:
            del self.records[name]
        else:
            raise KeyError(f"Record '{name}' not found")
        
    def find(self, name):
        if name in self.records:
            return self.records[name]
        else:
            raise KeyError(f"Record '{name}' not found")
        
    def search_records(self, **kwargs):
        results = []
        for record in self.records.values():
            if all(getattr(record, field, None) == value for field, value in kwargs.items()):
                results.append(record)
        return results

# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
for name, record in book.records.items():
    print(record)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

# Видалення запису Jane
book.delete("Jane")        
    

