<?php
//2) Usage without WSDL
$endpointData = array("location" => "https://www.brenda-enzymes.org/soap/brenda_server.php", "uri" => "");
$clientWithoutWSDL = new SOAPClient(null, $endpointData);
$password = hash("sha256","brendaPassword");
$parameters = "jbattista20@my.whitworth.edu,".$password.",ecNumber*1.1.1.1#organism*Homo sapiens#";
#$resultString=  $clientWithoutWSDL->getKmValue(array("j.doe@example.edu","myPassword","ecNumber*1.1.1.1#organism*Homo sapiens#"));
#$resultString=  $clientWithoutWSDL->getKmValue(array("jbattista20@my.whitworth.edu","brendaPassword","ecNumber*1.1.1.1#organism*Homo sapiens#"));
#$resultString=  $clientWithoutWSDL->getKmValue(array("jbattista20@my.whitworth.edu",$password,"ecNumber*1.1.1.1#organism*Homo sapiens#"));
$resultString=  $clientWithoutWSDL->getKmValue($parameters);
print $resultString;
?>
