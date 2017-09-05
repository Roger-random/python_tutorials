import urllib.request
from html.parser import HTMLParser

temperature_server_addr = 'http://192.168.10.98'

class TemperatureParser(HTMLParser):
  def handle_starttag(self, tag, attrs):
    print("Starting a tag:", tag)

with urllib.request.urlopen(temperature_server_addr) as response:
  html = response.read()

parser = TemperatureParser()
parser.feed(str(html))