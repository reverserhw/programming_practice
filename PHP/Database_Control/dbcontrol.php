<!DOCTYPE html>
<html>
<head>
	<title> Local Control MySQL </title>
</head>
<body>
<form method="get">
	<table border="1">
		<tr>
			<th colspan="2"> MySQL Connect </th>
		</tr>
		<tr>
			<td> Your ID : </td>
			<td><input type="text" name="username"></td>
		</tr>
		<tr>
			<td> Your PW : </td>
			<td><input type="text" name="userpass"></td>
		</tr>
		<tr>
			<td> Database Name </td>
			<td><input type="text" name="database"></td>
		</tr>
		<tr>
			<th colspan="2"> MySQL Control </th>
		</tr>
		<tr>
			<td> MySQL Query </td>
			<td><input type="text" name="sql_command"></td>
		</tr>
		<tr>
			<td colspan="2"><b><center><input type="submit" value="send"></center></b></button></center></td>
		</tr>
	</table>
</form>
</body>
</html>

<?php
$hostname = "localhost";
$username = $_GET['username'];
$userpass = $_GET['userpass'];
$db_name = $_GET['database'];

if(!empty($hostname) && !empty($username) && !empty($userpass) && !empty($db_name)) {
	$dbconn = mysql_connect($hostname, $username, $userpass) or die("MySQL Connection Error!");
	mysql_select_db($db_name, $dbconn);
}

$mysql_command = $_GET['sql_command'];

if(!empty($mysql_command)) {
	$sql = $mysql_command;
	$result = mysql_query($sql);
	if($result) {
		echo "Done.<br>";
	} else {
		echo "MySQL Error!";
	}
}
?>
