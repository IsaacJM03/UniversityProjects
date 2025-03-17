<?php

// use mysqli and create database user_management
$host = "localhost";
$username = "root";
$password = "isaac2003";
$database = "mydatabase";

$conn = new mysqli($host, $username, $password, $database);

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
        name VARCHAR(50) NOT NULL,
        email VARCHAR(50) NOT NULL,
        password VARCHAR(255) NOT NULL,
        profile_picture VARCHAR(255) NOT NULL
    )");
    $createUserStmt->execute();
    $createUserStmt->close();

}

?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Management</title>
</head>
<body>
// create a form to collect username, email ,password(hashed), and profile picture(<=5MB) jpg,jpeg,png
<form>
    <input type="text" name="name" placeholder="Enter Username" required>
    <input type="email" name="email" placeholder="Enter Email" required>
    <input type="password" name="password" placeholder="Enter Password" required>
    <input type="file" name="profile_picture" required>
    <button type="submit">Register</button>
</form>

// sanitize data, use password_hash() and password_verify()

// use session checks

//save data to database

// login form(email and password)

// implement "remember me" feature

// maintain state using sessions

// logout destroys session

//user update form(name,email,password, profile picture)

// delete user button(delete user from database)

// remove the profile picture from database 

