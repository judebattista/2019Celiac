#!/usr/bin/perl -w
use SOAP::Lite;
use Digest::SHA qw(sha256_hex);

my $password = sha256_hex("brendaPassword");
#my $parameters = 'jbattista20@my.whitworth.edu,'.$password.",ecNumber*1.1.1.1#organism*Homo sapiens#";
my $parameters = 'jbattista20@my.whitworth.edu,'.$password.",ecNumber*3.4.21.107#";
$resultString = SOAP::Lite
-> uri('https://www.brenda-enzymes.org/soap')
-> proxy('https://www.brenda-enzymes.org/soap/brenda_server.php')
-> getKmValue($parameters)
-> result; 

open(RESULTS, ">results.raw") or die "Couldn't open file RESULTS.raw, $!";
#sysopen(RESULTS, "RESULTS.raw", O_RDWR);
print RESULTS $resultString;
close RESULTS;

print $resultString;
print "\n";
