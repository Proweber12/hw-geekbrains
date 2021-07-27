class Warehouse:
    pass


class OfficeEquipment(Warehouse):
    def __init__(self, format: str):
        self.format = format


class Printer(OfficeEquipment):
    def print_text(self, text):
        print(text)


class Xerox(OfficeEquipment):
    def photocopy_doc(self, document, photocopy):
        with open(document, 'r') as f_document:
            with open(photocopy, 'w') as f_photocopy:
                f_photocopy.write(f_document.read())


class Scanner(OfficeEquipment):
    def scan(self, document):
        with open(document, 'r') as f_document:
            print(f_document.read())


a = Scanner("A4")
a.scan("text.txt")
