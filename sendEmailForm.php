<!DOCTYPE html>
<html>
<body>



<form method="post" name="myemailform" action="sendMail.php">

Enter Name:	<input type="text" name="name">

Enter Email Address:	<input type="text" name="email">

Enter Message:	<textarea name="message"></textarea>

<input type="submit" value="Send Form">
</form>

<?php
  $name = $_POST['name'];
  $visitor_email = $_POST['email'];
  $message = $_POST['message'];

  $to = $visitor_email;

  $headers = "From: testForm@lukeeland.com \r\n";

  $headers .= "Reply-To:  \r\n";
  
  $email_subject = "TBC";

  $email_body = "Email Body";

  mail($to,$email_subject,$email_body,$headers);
?>




</body>
</html>
