# ForexTimeSeriesForecastProject

Just run the dockerfile and send 12 week candles data
(open,high,low,close,volume and spread) of XAUUSD to http://localhost:5000/predict as a POST

The data bellow is an example of request with real life data from XAUUSD candles:

curl -X POST -H 'Content-Type: application/json' -d '{"data": [1728.56,1755.46,1719.25,1745.14,695664.0,5.0,1743.80,1745.43,1721.63,1732.70,605314.0,5.0,1731.17,1732.84,1677.86,1729.49,491085.0,5.0,1728.66,1758.66,1721.25,1743.46,513577.0,5.0,1742.71,1783.79,1723.70,1776.67,542195.0,5.0,1775.67,1797.88,1763.53,1776.48,532590.0,5.0,1775.48,1789.98,1756.19,1768.97,494178.0,0.0,1766.81,1843.30,1766.04,1830.85,521847.0,0.0,1833.04,1845.93,1808.77,1842.56,606858.0,0.0,1843.52,1890.09,1843.52,1881.74,643808.0,0.0,1881.41,1912.74,1872.71,1903.18,629466.0,0.0,1903.74,1916.58,1855.50,1891.51,558035.0,0.0]}' http://localhost:5000/predict

The next candle in the history of XAUUSD is bellow:
1890.19(open)	1903.67(high) 	1869.84(low)	1876.16(close)