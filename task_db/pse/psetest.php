<?php

// Username is root
$user = 'root';
$password = '';

// Database name is gfg
$database = 'part';

// Server is localhost with
// port number 3308
$servername='localhost:3306';
$mysqli = new mysqli($servername, $user,
				$password, $database);

// Checking for connections
if ($mysqli->connect_error) {
	die('Connect Error (' .
	$mysqli->connect_errno . ') '.
	$mysqli->connect_error);
}

// SQL query to select data from database
$sql = "SELECT * FROM PARS2 ";
$result = $mysqli->query($sql);
$mysqli->close();
?>

<!DOCTYPE html>
<html lang="en">

<head>
	<meta charset="UTF-8">
	<title>PARS in DB</title>
	<!-- CSS FOR STYLING THE PAGE -->
	<style>
		table {
			margin: 0 auto;
			font-size: large;
			border: 1px solid black;
		}

		h1 {
			text-align: center;
			color: #006600;
			font-size: xx-large;
			font-family: 'Gill Sans', 'Gill Sans MT',
			' Calibri', 'Trebuchet MS', 'sans-serif';
		}

		td {
			background-color: #E4F5D4;
			border: 1px solid black;
		}

		th,
		td {
			font-weight: bold;
			border: 1px solid black;
			padding: 10px;
			text-align: center;
		}

		td {
			font-weight: lighter;
		}
	</style>
</head>

<body>
  <!-- nav bar -->
  <h2 style="color:blue;position:relative;top:5px;left:40%;">
<?php

   define('DB_SERVER', '127.0.0.1');
   define('DB_USERNAME', 'root');
   define('DB_PASSWORD', '');
   define('DB_DATABASE', 'part');
   $db = mysqli_connect(DB_SERVER,DB_USERNAME,DB_PASSWORD,DB_DATABASE);
  
   if($db){

  echo "Welcome to PART";
   }
   else{echo 'Error Connecting to PART';}

?>
</h2>
    <button><a href="index.php">Home</a></button>
    <button><a href="psetest.php">List of Items</a></button>
    <button><a href="update.php">Add Items</a></button>
    <button><a href="fb.php">Update Items</a></button>
	<section>
		<h1>PARS</h1>
		<!-- TABLE CONSTRUCTION-->
		<table>
			<tr>
				<th>No </th>
				<th>Alias </th>
				<th>Quick notes</th>
				<th>PSE Sig</th>
			</tr>
			<!-- PHP CODE TO FETCH DATA FROM ROWS-->
			<?php // LOOP TILL END OF DATA
				while($rows=$result->fetch_assoc())
				{
			?>
			<tr>
				<!--FETCHING DATA FROM EACH
					ROW OF EVERY COLUMN-->
				<td><?php echo $rows['partno'];?></td>
				<td><?php echo $rows['alias'];?></td>
				<td><?php echo $rows['status'];?></td>
				<td><?php echo $rows['psesign'];?></td>
			</tr>
			<?php
				}
			?>
		</table>
	</section>
</body>

</html>
