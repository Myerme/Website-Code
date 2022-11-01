<?php

$host_name = 'db5009816141.hosting-data.io';
  $database = 'dbs8321056';
  $user_name = 'dbu1498706';
  $password = 'elandLuke2002';

  $conn = new mysqli($host_name, $user_name, $password, $database);

// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

$name = $_POST['Name'];
$visitor_email = $_POST['Email'];
$message = $_POST['Message'];

$sql = "INSERT INTO myguests (Name, Email, Message)
VALUES (\"$name\", \"$visitor_email\", \"$message\")";

if ($conn->query($sql) === TRUE) {
  echo "New record created successfully";
} else {
  echo "Error: " . $sql . "<br>" . $conn->error;
}

$conn->close();
?>