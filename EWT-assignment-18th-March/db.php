<?php
$host = "localhost";
$user = "root";  // Change if necessary
$pass = "isaac2003";      // Change if necessary
$dbname = "user_management";

$conn = new mysqli($host, $user, $pass, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: ". $conn->connect_error);
} else {
    $stmt = $conn->prepare("CREATE DATABASE IF NOT EXISTS user_management");
    $stmt->execute();
    $stmt->close();
    $conn->select_db("user_management");

    // create table users  -- done
    $createUserStmt = $conn->prepare("CREATE TABLE IF NOT EXISTS users (
        id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(50) NOT NULL,
        email VARCHAR(50) NOT NULL,
        password VARCHAR(255) NOT NULL,
        profile_picture VARCHAR(255) NOT NULL,
        reset_token VARCHAR(100) DEFAULT NULL,
        reset_token_expiry DATETIME DEFAULT NULL
    )");
    $createUserStmt->execute();
    $createUserStmt->close();

}
?>

