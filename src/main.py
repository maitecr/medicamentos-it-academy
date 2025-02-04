import config.Database as db
import controller.MedicamentoController as contr

db_connect = db.Database()

db_connect.create_table()

controller = contr.MedicamentoController()

controller.create_from_csv('./data/TA_PRECO_MEDICAMENTO.csv')