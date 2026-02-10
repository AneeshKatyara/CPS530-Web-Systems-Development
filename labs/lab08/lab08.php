<?php
//Problem 1
$hour = date("H");
if($hour >= 5 && $hour < 12){
$greet = "Good morning";
$bg = "morning.jpg";
$color = "black";
}
else if($hour >= 12 && $hour < 17){
$greet = "Good afternoon";
$bg = "afternoon.jpg";
$color = "black";
}
else if($hour >= 17 && $hour < 21){
$greet = "Good evening";
$bg = "evening.jpg";
$color = "white";
}
else{
$greet = "Good night";
$bg = "night.jpg";
$color = "white";
}
//Problem 3
$fav_image = "";
if(isset($_POST["fav_image"])){
$fav_image = $_POST["fav_image"];
setcookie("fav_image", $fav_image, time() + 48*60*60);
}
else if(isset($_COOKIE["fav_image"])){
$fav_image = $_COOKIE["fav_image"];
}
?>
<html>
<head>
<title>Lab 8</title>
</head>
<body style="font-family:sans-serif;">
<h2>Problem 1</h2>
<div style="width:700px; height:320px; margin-left:auto; margin-right:auto;
background-image:url('<?php echo $bg; ?>');
background-size:cover; background-position:center; text-align:center;">
<h1 style="color:<?php echo $color; ?>; padding-top:130px;">
<?php echo $greet; ?>
</h1>
</div>
<hr>
<h2>Problem 2</h2>
<form method="post">
Rows (3 to 12):
<input type="text" name="rows">
<br><br>
Columns (3 to 12):
<input type="text" name="cols">
<br><br>
<input type="submit" value="Create Table">
</form>
<?php
if(isset($_POST["rows"]) && isset($_POST["cols"])){
$r = $_POST["rows"];
$c = $_POST["cols"];
if(!is_numeric($r) || !is_numeric($c)){
echo "<p>Please enter numbers only.</p>";
}
else if($r < 3 || $r > 12 || $c < 3 || $c > 12){
echo "<p>Both numbers must be between 3 and 12.</p>";
}
else{
echo "<table border='1' cellpadding='10'
style='border-collapse:collapse; margin-top:10px;
margin-left:auto; margin-right:auto;'>";
for($i = 1; $i <= $r; $i++){
echo "<tr>";
for($j = 1; $j <= $c; $j++){
echo "<td style='width:40px; height:40px; text-align:center;'>";
echo ($i * $j);
echo "</td>";
}
echo "</tr>";
}
echo "</table>";
}
}
?>
<hr>
<h2>Problem 3</h2>
<?php
if($fav_image == ""){
echo "<p>you have not picked a favourite image yet.</p>";
}
else{
echo "<p>Your favourite image:</p>";
echo "<img src='".$fav_image.
"'
style='display:block; margin:10px auto; border:5px solid blue;
max-width:100%; height:auto;'>";
}
?>
<p>Select your favourite image</p>
<form method="post">
<input type="radio" name="fav_image" value="astro1.jpg"> Image 1<br>
<input type="radio" name="fav_image" value="astro2.jpg"> Image 2<br>
<input type="radio" name="fav_image" value="astro3.jpg"> Image 3<br>
<input type="radio" name="fav_image" value="astro4.jpg"> Image 4<br>
<input type="radio" name="fav_image" value="astro5.jpg"> Image 5<br>
<br>
<input type="submit" value="Save favourite image">
</form>
</body>
</html>
