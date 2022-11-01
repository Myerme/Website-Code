<?php
require_once "Mail.php";

  $name = $_POST['Name'];
  $visitor_email = $_POST['Email'];
  $message = $_POST['Message'];

$from = "luke@lukeeland.com";
$to = "luke@lukeeland.com";
$subject = "Hi!";
$body = "Hi,\n\nHow are you?";

$host = "smtp.ionos.co.uk";
$port = "587";
$username = "luke@lukeeland.com";
$password = "kbH?u/.F+jE7%p2";

$headers = array ('From' => $from,
  'To' => $to,
  'Subject' => $subject);
$smtp = Mail::factory('smtp',
  array ('host' => $host,
    'port' => $port,
    'auth' => true,
    'username' => $username,
    'password' => $password));

$mail = $smtp->send($to, $headers, $message);

if (PEAR::isError($mail)) {
  echo("<p>" . $mail->getMessage() . "</p>");
 } else {
  echo("<p>Message successfully sent!</p>");
  

 }
?>