import config.Database as db
import model.MedicamentoModel as model
import csv


class MedicamentoController(db.Database):
    def __init__(self):
        super().__init__()
        self._db = db.Database()
        self._medicamento_model = model.MedicamentoModel()


    def parse_decimal(self, value):
        if value is None or value.strip() == "" or not any(char.isdigit() for char in value):
            return None  

        try:
            return float(value.replace(',', '.'))
        except ValueError:
            return None 

    def parse_negative(self, value):
        if value is None or value.strip() == "" or not any(char.isdigit() for char in value):
            return None  

        try:
            # Remove espaços e verifica se o número está entre parênteses
            value = value.strip()
            if value.startswith('(') and value.endswith(')'):
                value = '-' + value[1:-1]  # Remove parênteses e adiciona o sinal negativo

            return float(value.replace(',', '.'))
        except ValueError:
            return None 

    def create_from_csv(self, file_path):
        with open(file_path, newline='', encoding="ISO-8859-1") as csvfile:
            reader = csv.reader(csvfile, delimiter=';', quotechar='"')
            next(reader)

            for row in reader:
                row[36] = self.parse_negative(row[36])

                column_numbers = [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 
                          23, 24, 25, 26, 27, 28, 29, 30, 31]
                
                for c in column_numbers:
                    row[c] = self.parse_decimal(row[c])
                
                self._medicamento_model.insert_into_table(*row)

    def get_product_by_name(self, product_name):
        _results = self._medicamento_model.select_by_product_name(product_name)

        for r in _results:
            print(r)

