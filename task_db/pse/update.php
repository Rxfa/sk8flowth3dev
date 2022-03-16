<?php
include 'partdb.php';
if(isset($_GET['submitted'])){

    
	$partno = $_GET['partno'];
	$status = $_GET['status'];

	$pse = $_GET['pse'];

	$sql = "UPDATE `pars2` SET `status`='$status',`pse`='$pse' WHERE partno = '$partno'";
      $result = mysqli_query($db,$sql);
	
	  if($result){ 
		header("Location: index.php?record=Record $partno UPDATED w/o contact");
	        exit();
	
		}
        }

if(isset($_GET['contact'])){

    
	$partno = $_GET['partno'];
	$status = $_GET['status'];
	$contact = $_GET['contact'];
	$pse = $_GET['pse'];
	$sql = "UPDATE `pars2` SET `contact`='$contact',`status`='$status',`pse`='$pse' WHERE partno = '$partno'";
      $result = mysqli_query($db,$sql);

	
	  if($result){ 
		header("Location: index.php?record=Record $partno UPDATED w/ email contact");
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
    <button><a href="update.php">Update Items</a></button>
    <button><a href="add.php">Add Items</a></button>
    <button><a href="delete.php">Delete Items</a></button>
    <main>
        <div class="main-container">
            <h3> Login</h3>
            <form method="GET" action="update.php">
                <label for="partno">Part No</label>
                <input type="text" name="partno" />
               
                <label for="contact">Good Email for PD</label>
                <input type="text" name="contact" />
                <label for="status">Notes for you</label>
                <input type="text" name="status" />
                <label for="pse">PSE Summary</label>
                <input type="text" name="pse" />
                <button type="submit" name="submitted">Update Item</button>
            </form>
        </div>

    </main>
    <h3 style="color:red;"><?php if(isset($_GET['record'])){echo $_GET['record'];} ?> </h3>
    <h3 style="color:red;"><?php if(isset($addedalias)){echo $addedalias;}  ?> </h3>
    <!-- scripts go here -->

    <script src=""></script>
</body>
</html>