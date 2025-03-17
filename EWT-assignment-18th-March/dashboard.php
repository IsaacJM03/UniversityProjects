<?php
session_start();
if (!isset($_SESSION["user_id"])) {
    header("Location: login.php");
    exit;
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard</title>
    <link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
    <div class="dashboard">
        <h2>Welcome, <?php echo $_SESSION["username"]; ?>!</h2>
        <p>
            <a href="edit_profile.php" class="btn">Edit Profile</a>
        </p>
        <p>
            <a href="delete_account.php" class="btn btn-danger">Delete Account</a>
        </p>
        <p><a href="logout.php" class="logout-btn">Logout</a></p>
    </div>
</body>
</html>
