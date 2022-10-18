from http.server import HTTPServer, BaseHTTPRequestHandler
import requests
import time
import datetime
import json

##Convert the Bitcoin price from EUR to CZK
def currencyConvert(europrice):
    """The function collects the current exchange rate from EUR to CZK and returns the total value of BTC price in CZK"""
    url = f"https://api.apilayer.com/exchangerates_data/convert?to=czk&from=eur&amount={europrice}"
    payload = {}
    headers= {
        "apikey": "wlPasXa7c8FotEjZ53vs1A66dETfLTlu"
    }
    value_czk = requests.request("GET", url, headers = headers, data = payload)
    price_czk = value_czk.json()["result"]
    return price_czk
##Retreive data from coindesk API and dump the required fields to json format
def bitcoinPrice():
    """The function """
    btc_price_api = requests.get(url="https://api.coindesk.com/v1/bpi/currentprice.json")
    ts = time.time()
    data_euro = btc_price_api.json()["bpi"]["EUR"]["rate_float"]
    server_time = btc_price_api.json()["time"]["updated"]
    client_request_time=datetime.datetime.fromtimestamp(ts).utcnow().astimezone().strftime('%b %d, %Y %T UTC') ##Return current time and date in UTC timezone
    return json.dumps({
    "Crypto Currency": 'BTC',
    "EURO": data_euro,
    "CZK": currencyConvert(data_euro),
    "Server Time": server_time,
    "Client Request Time": client_request_time
    })
##HTTP Server class
class httpdServer(BaseHTTPRequestHandler):
    """Re-used some code from BaseHTTPRequestHandler to define the server response headers"""
    def _set_headers(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
    def _html(self):
        """Insert the json dump from bitcoinPrice() function and encode in utf8 format """
        content = bitcoinPrice()
        return content.encode("utf8")
    def do_GET(self):
        """Definition of GET Method which will reply with headers and page content to the request"""
        self._set_headers()
        self.wfile.write(self._html())
##Start the HTTP Server
def run(server_class=HTTPServer, handler_class=httpdServer, addr="0.0.0.0", port=8080):
    server_address = (addr, port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting httpd server on {addr}:{port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
