import stocklist
import stockdataservice


stock_list = stocklist.StockListFromEastMoney()
stocks = stock_list.fetch_stock_list()
dataservice = stockdataservice.StockDataService()
dataservice.delete_stock()
dataservice.add_stock(stocks)
stock = dataservice.query_stock_by_code('600001')
print(stock)

