import string
import hashlib
from zeep import Client, Settings
from zeep.wsse.username import UsernameToken

# Usage with WSDL
settings = Settings(strict=False)
wsdl = 'https://www.brenda-enzymes.org/soap/brenda.wsdl'
username = 'jbattista20@my.whitworth.edu'
password = hashlib.sha256('brendaPassword'.encode('utf-8')).hexdigest()
client = Client(wsdl, wsse=UsernameToken(username, password), settings=settings)
parameters = 'jbattista20@my.whitworth.edu,' + password + ',ecNumber*1.1.1.1#organism*Homo sapiens#'
#parameters = 'ecNumber*1.1.1.1#organism*Homo sapiens#'
resultString = client.service.getKmValue(parameters)
print(resultString)
