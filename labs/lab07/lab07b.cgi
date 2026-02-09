#!/usr/bin/perl
use strict;
use warnings;
use CGI ':standard';
print "Content-type:text/html\n\n";
print "<html>";
print "<head><title>Reservation Results</title>";
print "<style>
body {
font-family: Arial, sans-serif;
background-color: #f5f8fc;
color: #222;
max-width: 700px;
margin: 40px auto;
padding: 20px;
}
h2 {
text-align: center;
color: #0c5bd9;
}
h3 {
color: #0c5bd9;
margin-top: 30px;
}
ul {
background: #ffffff;
padding: 15px 25px;
border-radius: 10px;
box-shadow: 0 2px 6px rgba(0,0,0,0.1);
}
li { margin: 6px 0; }
.error { color: red; font-weight: bold; }
a {
display: inline-block;
margin-top: 20px;
text-decoration: none;
color: #0c5bd9;
}
a:hover { text-decoration: underline; }
</style>";
print "</head>";
print "<body>";
my $fname = param('fname') || '';
my $lname = param('lname') || '';
my $street = param('street') || '';
my $city = param('city') || '';
my $postal = param('postal') || '';
my $province = param('province') || '';
my $phone = param('phone') || '';
my $email = param('email') || '';
my $payment = param('payment') || '';
my @errors;
push @errors, "First name is required." if $fname eq '';
push @errors, "Last name is required." if $lname eq '';
push @errors, "Street is required." if $street eq '';
push @errors, "City is required." if $city eq '';
push @errors, "Postal code must be in format L0L 0L0."
unless $postal =~ /^[A-Za-z]\d[A-Za-z] \d[A-Za-z]\d$/;
push @errors, "Phone number must be 10 digits."
unless $phone =~ /^\d{10}$/;
push @errors, "Invalid email address."
unless $email =~ /^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$/;
push @errors, "Province must be selected." if $province eq '';
push @errors, "Payment method must be selected." if $payment eq '';
print "<h2>Results</h2>";
if (@errors) {
print "<h3 style='color:red;'>Input Errors:</h3><ul>";
foreach my $err (@errors) {
print "<li>$err</li>";
}
print "</ul>";
print "<p><a href='../lab07b.html'>Return to the form</a></p>";
}
else {
print "<h3>Reservation Confirmation</h3>";
print "<p>Thank you, <b>$fname $lname</b>!</p>";
print "<p>Your reservation details are:</p>";
print "<ul>";
print "<li>Address: $street, $city, $province, $postal</li>";
print "<li>Phone: $phone</li>";
print "<li>Email: $email</li>";
print "<li>Payment Method: $payment</li>";
print "</ul>";
print "<p>Your Bed & Breakfast reservation has been successfully recorded.</p>";
}
print end_html();
