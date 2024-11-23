from datetime import date
from typing import Dict


class Stock:
    def __init__(self, name: str, prices: Dict[date, float]) -> None:
        """
        Initialize the stock with a name and a dictionary of prices.

        :param name: Name of the stock.
        :param prices: Dictionary with dates as keys and prices as values.
        """
        self.name = name
        self.prices = prices

    def Price(self, query_date: date) -> float:
        """
        Get the stock price for a specific date.

        :param query_date: The date for which the price is needed.
        :return: Price of the stock on the given date.
        """
        return self.prices.get(query_date, 0.0)

    def UpdatePrice(self, date: date, price: float) -> None:
        """
        Update the stock price for a specific date.

        :param date: The date for which the price is being updated.
        :param price: The new price for the stock on that date.
        """
        self.prices[date] = price


class Portfolio:
    def __init__(self) -> None:
        """
        Initialize an empty portfolio.
        """
        self.stocks: Dict[str, Stock | int] = {}

    def AddStock(self, stock: Stock, quantity: int) -> None:
        """
        Add a stock to the portfolio.

        :param stock: The Stock object to add.
        :param quantity: Number of shares of the stock.
        """
        if stock.name in self.stocks:
            self.stocks[stock.name]['quantity'] += quantity
        else:
            self.stocks[stock.name] = {'stock': stock, 'quantity': quantity}

    def _PortfolioValue(self, query_date: date) -> float:
        """
        Calculate the total value of the portfolio on a specific date.

        :param query_date: The date for which the value is needed.
        :return: The total value of the portfolio on the given date.
        """
        total_value = 0.0
        for stock_data in self.stocks.values():
            stock = stock_data['stock']
            quantity = stock_data['quantity']
            total_value += stock.Price(query_date) * quantity
        return total_value

    def Profit(self, start_date: date, end_date: date) -> float:
        """
        Calculate the portfolio's profit between two dates.

        :param start_date: The start date.
        :param end_date: The end date.
        :return: The total profit of the portfolio between the two dates.
        """
        start_value = self._PortfolioValue(start_date)
        end_value = self._PortfolioValue(end_date)
        return end_value - start_value

    def AnnualizedReturn(self, start_date: date, end_date: date) -> float:
        """
        Calculate the annualized return of the portfolio between two dates.

        :param start_date: The start date.
        :param end_date: The end date.
        :return: The annualized return as a float.
        """
        start_value = self._PortfolioValue(start_date)
        end_value = self._PortfolioValue(end_date)

        return ((end_value - start_value)/start_value)*100


if __name__ == "__main__":
    stock_a = Stock("StockA", {
        date(2024, 1, 1): 100,
        date(2024, 1, 31): 110
    })
    stock_b = Stock("StockB", {
        date(2024, 1, 1): 200,
        date(2024, 1, 31): 190
    })
    portfolio = Portfolio()
    portfolio.AddStock(stock_a, 10)
    portfolio.AddStock(stock_b, 5)

    profit = portfolio.Profit(date(2024, 1, 1), date(2024, 1, 31))
    print(f"Portfolio profit between 2024-01-01 - 2024-01-31: ${profit:.2f}")
    annualized = portfolio.AnnualizedReturn(
        date(2024, 1, 1), date(2024, 1, 31))
    print(
        f"Annualized between 2024-01-01 - 2024-01-31: {annualized:.2f}%")
