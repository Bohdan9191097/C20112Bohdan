import requests
import yfinance as yf


def get_yfinance_price(symbol):
    try:
        stock = yf.Ticker(symbol)
        price = stock.history(period="1d")['Close'].iloc[-1]  # Остання закриваюча ціна
        return price
    except Exception as e:
        print(f"Помилка отримання даних для {symbol}: {e}")
        return None


def get_binance_price(symbol):
    url = f'https://api.binance.com/api/v3/ticker/price?symbol={symbol}'
    response = requests.get(url)
    data = response.json()
    return float(data['price'])
def main():
    stock_symbols = ['AAPL', 'TSLA', 'MSFT', 'SPY', 'NVDA', 'AMZN', 'GOOGL', 'META']
    crypto_symbols = ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'XRPUSDT']
    stock_prices = {}
    crypto_prices = {}
    # цены акций
    for symbol in stock_symbols:
        stock_prices[symbol] = get_yfinance_price(symbol)
        if stock_prices[symbol] is not None:
            print(f"Ціна акцій {symbol} в доларах: {stock_prices[symbol]:.2f}")
        else:
            print(f"Не вдалося отримати ціну для {symbol}")
    # цены крипты
    for symbol in crypto_symbols:
        crypto_prices[symbol] = get_binance_price(symbol)
        print(f"Ціна {symbol[:-4]} в доларах: {crypto_prices[symbol]}")

    monthly_income = float(input("Введіть ваш місячний дохід в доларах: "))
    investment_percentage = float(input("Введіть відсоток вашого доходу, який ви хочете інвестувати (наприклад, 10 для 10%): "))
    investment_amount = (investment_percentage / 100) * monthly_income
    periods = {
        'День': 1,
        'Тиждень': 7,
        'Місяць': 30,
        'Рік': 365
    }

    for period, days in periods.items():
        period_investment_amount = (investment_amount / 30) * days
        print(f"\nІнвестиції за {period}: ${period_investment_amount:.2f}")

        for symbol in stock_symbols:
            if stock_prices[symbol] is not None:
                shares = period_investment_amount / stock_prices[symbol]
                print(f"Ви можете купити {shares:.2f} акцій {symbol} за {period_investment_amount:.2f} доларів")

        for symbol in crypto_symbols:
            coins = period_investment_amount / crypto_prices[symbol]
            print(f"Ви можете купити {coins:.6f} {symbol[:-4]} за {period_investment_amount:.2f} доларів")

if __name__ == "__main__":
    main()
