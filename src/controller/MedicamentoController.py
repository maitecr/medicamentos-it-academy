import config.Database as db

import pandas as pd

class MedicamentoController(db.Database):
    def __init__(self):
        self._db = db.Database()


    def csv_to_database(self, file_path):
        _csv_to_df = pd.read_csv(file_path, 
                        quotechar='"',
                        delimiter=';',
                        encoding="ISO-8859-1", 
                        dtype=str,
                        low_memory=False
                        )

        _df_comma_to_dot = _csv_to_df.stack().str.replace(',', '.').unstack()
        _df_final = _df_comma_to_dot.fillna(value=0)

        _data = [tuple(row) for row in _df_final.itertuples(index=False, name=None)]

        self._db.insert_into_table(_data)