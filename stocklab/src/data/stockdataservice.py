import stockmodel
import stockdal


class StockDataService:
    def __init__(self, db_name='stocklab.sqlite'):
        self.stock_db = stockdal.StockSQLiteDB(db_name)
        self.table_stock = 'stock'

    def delete_stock(self, code=''):
        self.stock_db.delete_from_table(self.table_stock, filters='CODE='+code)

    def add_stock(self, stock_list):
        self.stock_db.insert_to_table(self.table_stock, stock_list)

    def query_stock_by_code(self, code=''):
        return self.stock_db.get_data_scal_item(self.table_stock, filters='CODE='+code)