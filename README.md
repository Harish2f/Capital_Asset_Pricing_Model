# Capital Asset Pricing Model (CAPM)

This is a Streamlit application that calculates the Capital Asset Pricing Model (CAPM) for a portfolio of stocks. CAPM is a financial model that determines the expected return of an investment based on its risk.

## Features

- Allows users to choose a selection of stocks from a predefined list.
- Calculates the beta values for each selected stock, representing their sensitivity to market movements.
- Normalizes and plots the stock prices over a specified number of years.
- Calculates the expected return of each stock using CAPM.
- Displays the results in a user-friendly format.

## How to Use

1. Clone this repository.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the application using `streamlit run app.py`.
4. Enter the number of years and select the desired stocks from the provided list.
5. The application will display the stock prices, normalized prices, calculated beta values, and expected returns using CAPM.

## Technologies Used

- Streamlit: For creating the interactive web application.
- Pandas: For data manipulation and analysis.
- yfinance: For retrieving stock data.
- Plotly: For visualizing the stock prices.

## Dependencies

- streamlit==0.89.0
- pandas==1.3.0
- yfinance==0.1.63
- plotly==5.1.0

## Disclaimer

This application provides a basic implementation of the CAPM model and should not be used as financial advice. The calculations are based on historical data and do not guarantee future performance. Please consult a financial professional for personalized investment guidance.

