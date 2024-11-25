import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt


# Fetch historical stock data
def fetch_stock_data(ticker, start_date, end_date):
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    return stock_data


# Calculate simple moving averages
def calculate_sma(data, window):
    return data['Close'].rolling(window=window).mean()


# Generate buy and sell signals based on SMA
def generate_signals(data, short_window, long_window):
    signals = pd.DataFrame(index=data.index)
    signals['price'] = data['Close']
    signals['short_sma'] = calculate_sma(data, short_window)
    signals['long_sma'] = calculate_sma(data, long_window)
    signals['signal'] = 0.0
    signals['signal'][short_window:] = np.where(
        signals['short_sma'][short_window:] > signals['long_sma'][short_window:], 1.0, 0.0)
    signals['positions'] = signals['signal'].diff()
    return signals


# Plot the stock data and signals
def plot_signals(data, signals):
    plt.figure(figsize=(14, 7))
    plt.plot(data['Close'], label='Close Price')
    plt.plot(signals['short_sma'], label=f'Short SMA ({short_window} days)')
    plt.plot(signals['long_sma'], label=f'Long SMA ({long_window} days)')
    plt.plot(signals[signals['positions'] == 1.0].index,
             signals['short_sma'][signals['positions'] == 1.0],
             '^', markersize=10, color='g', lw=0, label='Buy Signal')
    plt.plot(signals[signals['positions'] == -1.0].index,
             signals['short_sma'][signals['positions'] == -1.0],
             'v', markersize=10, color='r', lw=0, label='Sell Signal')
    plt.title(f'{ticker} Trading Signals')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.show()


# Main function
if __name__ == "__main__":
    ticker = 'AAPL'  # Example ticker symbol (Apple Inc.)
    start_date = '2020-01-01'
    end_date = '2024-11-25'
    short_window = 40
    long_window = 100

    # Fetch and process stock data
    stock_data = fetch_stock_data(ticker, start_date, end_date)
    signals = generate_signals(stock_data, short_window, long_window)

    # Plot signals
    plot_signals(stock_data, signals)
