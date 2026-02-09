#!/usr/bin/perl
use strict;
use warnings;
use CGI ':standard';
use CGI::Carp qw(fatalsToBrowser);
print "Content-type:text/html\n\n";
print "<html>";
print "<head><title>Lab07c Result</title>";
print "<style>
body {font-family: Arial, sans-serif; background-color: #f5f8fc; color: #222;
text-align: center; margin-top: 50px;}
h2 {color: #0c5bd9;}
img {max-width: 400px; margin-top: 15px;}
a {color: #0c5bd9; text-decoration: none;}
a:hover {text-decoration: underline;}
</style>";
print "</head>";
print "<body>";
my $text = param('usertext') || '';
my $file = param('imagefile');
print "<h2>Results</h2>";
if ($file) {
my ($name) = $file =~ /([^\/\\]+)$/;
my $path = '/class-years/y2022/akatyara/public_html/uploads';
mkdir $path unless -d $path;
my $fullpath = "$path/$name";
if (open(my $out, '>', $fullpath)) {
binmode $out;
my $fh = upload('imagefile');
binmode $fh;
while (<$fh>) { print $out $_; }
close $out;
print "<p><b>Text Entered:</b></p>";
print "<p>$text</p>";
print "<p><b>Uploaded Image:</b></p>";
print "<img src=\"/~akatyara/uploads/$name\" alt=\"Uploaded Image\">";
}
else {
print "<p style='color:red;'>Error: cannot save the file.</p>";
}
}
else {
print "<p style='color:red;'>No image was selected.</p>";
}
print "<p><a href='../lab07c.html'>Back to form</a></p>";
print "</body></html>";
