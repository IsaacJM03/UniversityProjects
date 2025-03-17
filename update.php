<?php

$host = "localhost";
$username = "root";
$password = "isaac2003";
$database = "mydatabase";

$conn = new mysqli($host, $username, $password, $database);
$name = $_POST["name"];
$email = $_POST["email"];
$password = password_hash($_POST["password"], PASSWORD_DEFAULT);
$profile_picture = "uploads/".basename($_FILES["profile_picture"]["name"]);
if ($conn->connect_error) {
    die("Connection failed: ". $conn->connect_error);
} else {
    $stmt = $conn->prepare("UPDATE users SET name=?, email=?, password=?, profile_picture=? WHERE id=?");
    $stmt->bind_param("ssssi", $name, $email, $password, $profile_picture, $id);
}
// update user details