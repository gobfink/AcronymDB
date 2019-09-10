<h1>Hello ASSETT!</h1>
<h3>This is a test of the Acronym DB...</h3>
<h4>Attempting MySQL connection from php...</h4>

<?php 
  $conn = new mysqli("db", "root", "example", "acronym");
  if ($conn->connect_error) {
    die("ERROR: Unable to connect: " . $conn->connect_error);
  }

  echo 'Connected to the database.<br>';

  $result = $conn->query("SELECT * FROM tbl_User");

  echo "Number of Users: $result->num_rows";

  $result->close();

  $conn->close();

?>
