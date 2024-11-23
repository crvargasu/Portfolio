import unittest
from datetime import date
# Adjust the import based on your file structure
from main import Stock, Portfolio


class TestStock(unittest.TestCase):
    def test_price_on_existing_date(self):
        stock = Stock("TestStock", {date(2024, 1, 1): 100.0})
        self.assertEqual(stock.Price(date(2024, 1, 1)), 100.0)

    def test_price_on_non_existing_date(self):
        stock = Stock("TestStock", {date(2024, 1, 1): 100.0})
        self.assertEqual(stock.Price(date(2024, 1, 2)), 0.0)

    def test_update_price(self):
        stock = Stock("TestStock", {date(2024, 1, 1): 100.0})
        stock.UpdatePrice(date(2024, 1, 1), 120.0)
        self.assertEqual(stock.Price(date(2024, 1, 1)), 120.0)


class TestPortfolio(unittest.TestCase):
    def setUp(self):
        self.stock_a = Stock("StockA", {
            date(2024, 1, 1): 100,
            date(2024, 1, 31): 110
        })
        self.stock_b = Stock("StockB", {
            date(2024, 1, 1): 200,
            date(2024, 1, 31): 190
        })
        self.portfolio = Portfolio()
        self.portfolio.AddStock(self.stock_a, 10)
        self.portfolio.AddStock(self.stock_b, 5)

    def test_add_stock(self):
        stock_c = Stock("StockC", {date(2024, 1, 1): 50})
        self.portfolio.AddStock(stock_c, 8)
        self.assertIn("StockC", self.portfolio.stocks)
        self.assertEqual(self.portfolio.stocks["StockC"]["quantity"], 8)

    def test_portfolio_value(self):
        value = self.portfolio._PortfolioValue(date(2024, 1, 1))
        expected_value = (100 * 10) + (200 * 5)  # StockA * 10 + StockB * 5
        self.assertEqual(value, expected_value)

    def test_profit(self):
        profit = self.portfolio.Profit(date(2024, 1, 1), date(2024, 1, 31))
        expected_profit = ((110 * 10) + (190 * 5)) - ((100 * 10) + (200 * 5))
        self.assertEqual(profit, expected_profit)

    def test_annualized_return(self):
        annualized = self.portfolio.AnnualizedReturn(
            date(2024, 1, 1), date(2024, 1, 31)
        )
        start_value = (100 * 10) + (200 * 5)
        end_value = (110 * 10) + (190 * 5)
        expected_return = ((end_value - start_value) / start_value) * 100
        self.assertAlmostEqual(annualized, expected_return, places=2)


if __name__ == "__main__":
    unittest.main()
