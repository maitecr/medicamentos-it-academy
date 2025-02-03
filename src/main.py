import config.Database as db
import controller.MedicamentoController as contr

db_connect = db.Database()

db_connect.create_table()

controller = contr.MedicamentoController()

controller.csv_to_database('./data/TA_PRECO_MEDICAMENTO.csv')