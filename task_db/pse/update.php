<?php
include 'partdb.php';
if(isset($_GET['submitted'])){
	$partno = $_GET['partno'];
	$alias = $_GET['alias'];
	$status = $_GET['status'];
	$psesign = $_GET['psesign'];
    //$sql2 = "INSERT INTO pars(partno, alias, name, lastname, email, tagline, reset) VALUES('$uname', '$pass', '$name', '$sname', '$email', '$tagline', '$status')";
	$sql = "INSERT INTO pars2(partno, alias, status, psesign) VALUES('$partno','$alias','$status','$psesign')";
      $result = mysqli_query($db,$sql);
      //$row = mysqli_fetch_array($result,MYSQLI_ASSOC);
	
	  if($result){ 
		header("Location: update.php?record=$partno added");
	        exit();
	
		}
        }

?>


<!doctype html>

<html lang="en">
<head>
    <title>Login THELAB</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, intial-scale=1">

    <link rel="stylesheet" href="">

</head>

<body>
  <button><a href="index.php">Home</a></button>
    <button><a href="psetest.php">List of Items</a></button>
    <button><a href="update.php">Add Items</a></button>
    <button><a href="fb.php">Update Items</a></button>
    <main>
        <div class="main-container">
            <h3> Login</h3>
            <form method="GET" action="update.php">
                <input type="text" name="partno" />
                <input type="text" name="alias" />
                <input type="text" name="status" />
                <input type="text" name="psesign" />
                <button type="submit" name="submitted">Add Item</button>
            </form>
        </div>

    </main>
    <h3 style="color:red;"><?php if(isset($_GET['record'])){echo $_GET['record'];} ?> </h3>
    <h3 style="color:red;"><?php if(isset($addedalias)){echo $addedalias;}  ?> </h3>
    <!-- scripts go here -->
    <script src=""></script>
</body>
</html>