<?php
//1) Usage with WSDL (for extracting the URL of the endpoint)

#phpinfo();

$client = new SoapClient("https://www.brenda-enzymes.org/soap/brenda.wsdl", array("trace" => 1));
$password = hash("sha256","brendaPassword");
$parameters = "jbattista20@my.whitworth.edu,".$password.",ecNumber*1.1.1.1#organism*Homo sapiens#";
$resultString=$client->getKmValue($parameters);
print($resultString);
?>
