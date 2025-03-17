<?php
session_start();
session_destroy();
header("Location: login.php");
exit;
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Logging Out</title>
    <link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
    <div class="container">
        <h2>You have been logged out successfully.</h2>
        <p>Redirecting to login page...</p>
    </div>
</body>
</html>

