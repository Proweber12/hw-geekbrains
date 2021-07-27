from abc import ABC, abstractmethod

class Warehouse:
    pass


class OfficeEquipment(ABC):
    def __init__(self,  company, name, quantity):
        self.company = company
        self.name = name
        self.quantity = quantity

    @abstractmethod
    def reception_office_equipment(self, company, name, quantity):
        pass


class Printer(OfficeEquipment):
    def __init__(self, company=None, name=None, quantity=None):
        super(Printer, self).__init__(company, name, quantity)

    @staticmethod
    def reception_office_equipment(company, name, quantity):
        return f'На склад поступило и было переданно в компанию {company} оргтехника: {name} в количестве {quantity} единиц(ы)' + '\n' + '-' * 100

    def print_text(self, text):
        print(text)


class Xerox(OfficeEquipment):
    def __init__(self, company=None, name=None, quantity=None):
        super(Xerox, self).__init__(company, name, quantity)

    @staticmethod
    def reception_office_equipment(company, name, quantity):
        return f'На склад поступило и было переданно в компанию {company} оргтехника: {name} в количестве {quantity} единиц(ы)' + '\n' + '-' * 100

    def photocopy_doc(self, document, photocopy):
        with open(document, 'r') as f_document:
            with open(photocopy, 'w') as f_photocopy:
                f_photocopy.write(f_document.read())


class Scanner(OfficeEquipment):
    def __init__(self, company=None, name=None, quantity=None):
        super(Scanner, self).__init__(company, name, quantity)

    @staticmethod
    def reception_office_equipment(company, name, quantity):
        return f'На склад поступило и было переданно в компанию {company} оргтехника: {name} в количестве {quantity} единиц(ы)' + '\n' + '-' * 100

    def scan(self, document):
        with open(document, 'r') as f_document:
            print(f_document.read())


printer = Printer()
xerox = Xerox()
scanner = Scanner()
print(printer.reception_office_equipment('Газпром', 'Принтер', 14))
print(xerox.reception_office_equipment('Shell', 'Ксерокс', 13))
print(scanner.reception_office_equipment('ВТБ', 'Сканнер', 24))
