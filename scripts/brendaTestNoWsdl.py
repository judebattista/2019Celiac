import string
import hashlib

# Usage with WSDL
endpointUrl = 'https://www.brenda-enzymes.org/soap/brenda_server.php'
password = hashlib.sha256('brendaPassword'.encode('UTF-8')).hexdigest()
parameters = 'jbattista20@my.whitworth.edu,' + password + ',ecNumber*1.1.1.1#organism*Homo sapiens#'
client=SOAPProxy(endpointUrl)
resultString = client.getKmValue(parameters)
print(resultString)

