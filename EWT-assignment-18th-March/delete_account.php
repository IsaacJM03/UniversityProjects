<?php
session_start();
include "./db.php"; 

if (!isset($_SESSION["user_id"])) {
    header("Location: login.php");
    exit;
}

$id = $_SESSION["user_id"];

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Get profile picture
    $result = $conn->query("SELECT profile_picture FROM users WHERE id = $id");
    $user = $result->fetch_assoc();
    
    if ($user && $user["profile_picture"]) {
        unlink($user["profile_picture"]); 
    }

    $conn->query("DELETE FROM users WHERE id = $id");

    // Destroy session and redirect
    session_destroy();
    header("Location: register.php");
    exit;
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Delete Account</title>
    <link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
    <div class="container">
        <h2>Delete Account</h2>
        <p>Are you sure you want to delete your account? This action cannot be undone.</p>
        <form method="POST">
            <button type="submit" class="btn btn-danger">Yes, Delete My Account</button>
            <a href="dashboard.php" class="btn">Cancel</a>
        </form>
    </div>
</body>
</html>
