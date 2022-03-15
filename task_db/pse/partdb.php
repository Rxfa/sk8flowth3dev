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