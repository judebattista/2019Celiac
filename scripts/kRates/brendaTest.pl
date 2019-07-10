#!/usr/bin/perl -w
use SOAP::Lite;
use Digest::SHA qw(sha256_hex);

# 32, 4, 107, 102

my $password = sha256_hex("brendaPassword");
#my $parameters = 'jbattista20@my.whitworth.edu,'.$password.",ecNumber*1.1.1.1#organism*Homo sapiens#";
my $parameters = 'jbattista20@my.whitworth.edu,'.$password.",ecNumber*3.4.21.32#";
$resultString = SOAP::Lite
-> uri('https://www.brenda-enzymes.org/soap')
-> proxy('https://www.brenda-enzymes.org/soap/brenda_server.php')
-> getKmValue($parameters)
-> result; 

my $outfile = ">km32.raw";
open(RESULTS, $outfile) or die "Couldn't open output file, $!";
#sysopen(RESULTS, "RESULTS.raw", O_RDWR);
print RESULTS $resultString;
close RESULTS;

print $resultString;
print "\n";
