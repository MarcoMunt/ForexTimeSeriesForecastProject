# Forex Time Series Forecast Project

## Overview
This project aims to forecast time series data in the Forex market, specifically focusing on XAUUSD (Gold to US Dollar) exchange rates. It utilizes a Dockerized environment for ease of deployment and execution.

### Forex and XAUUSD
Forex, or Foreign Exchange Market, is where currencies are traded globally. XAUUSD represents the exchange rate between gold (XAU) and the US dollar (USD). It is one of the most widely traded currency pairs in the Forex market, with gold being a popular asset for investors seeking stability and diversification.

## Installation and Execution
To run the project, follow these simple steps:

### 1. Install Docker
- Docker allows for containerization of applications, ensuring consistency across different environments.
- Install Docker from [Docker's official website](https://www.docker.com/get-started).

### 2. Clone the Repository
```bash
git clone https://github.com/your/repository.git
cd ForexTimeSeriesForecastProject
```

### 3. Build the Docker Image
```bash
docker build -t forex-forecast .
```

### 4. Run the Docker Container
```bash
docker run -d -p 5000:5000 forex-forecast
```

### 5. Send Data for Prediction
- Use the provided curl command to send 12-week candles data to the prediction endpoint.
- Ensure the data contains open, high, low, close, volume, and spread information for each candle.
- Example:
```bash
curl -X POST -H 'Content-Type: application/json' -d '{"data": [1728.56,1755.46,1719.25,1745.14,695664.0,5.0,1743.80,1745.43,1721.63,1732.70,605314.0,5.0,1731.17,1732.84,1677.86,1729.49,491085.0,5.0,1728.66,1758.66,1721.25,1743.46,513577.0,5.0,1742.71,1783.79,1723.70,1776.67,542195.0,5.0,1775.67,1797.88,1763.53,1776.48,532590.0,5.0,1775.48,1789.98,1756.19,1768.97,494178.0,0.0,1766.81,1843.30,1766.04,1830.85,521847.0,0.0,1833.04,1845.93,1808.77,1842.56,606858.0,0.0,1843.52,1890.09,1843.52,1881.74,643808.0,0.0,1881.41,1912.74,1872.71,1903.18,629466.0,0.0,1903.74,1916.58,1855.50,1891.51,558035.0,0.0]}' http://localhost:5000/predict
```

### 6. Interpret the Prediction
 - The prediction endpoint will respond with the forecast for the next candle (Open, High, Low,CLose) based on the provided data.

#### 6.1 Next Candle Information
The next candle in the history of XAUUSD using the example provided in the curl command is as follows:
- Open: 1890.19
- High: 1903.67
- Low: 1869.84
- Close: 1876.16

