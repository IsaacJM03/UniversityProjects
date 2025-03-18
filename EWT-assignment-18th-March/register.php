<?php
session_start();
include "./db.php";

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $username = trim($_POST["username"]);
    $email = trim($_POST["email"]);
    $password = $_POST["password"];
    $profile_picture = null;

    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        die("Invalid email format.");
    }

    $hashed_password = password_hash($password, PASSWORD_BCRYPT);

    if (!empty($_FILES["profile_picture"]["name"])) {
        $allowed_types = ["image/jpg", "image/jpeg", "image/png"];
        $file_type = $_FILES["profile_picture"]["type"];
        $file_size = $_FILES["profile_picture"]["size"];

        if (!in_array($file_type, $allowed_types) || $file_size > 5 * 1024 * 1024) {
            die("Invalid file type or size exceeded (max 5MB).");
        }

        $profile_picture = "uploads/" . basename($_FILES["profile_picture"]["name"]);
        move_uploaded_file($_FILES["profile_picture"]["tmp_name"], $profile_picture);
    }

    $stmt = $conn->prepare("INSERT INTO users (username, email, password, profile_picture) VALUES (?, ?, ?, ?)");
    $stmt->bind_param("ssss", $username, $email, $hashed_password, $profile_picture);

    if ($stmt->execute()) {
        echo "Registration successful. <a href='login.php'>Login</a>";
    } else {
        echo "Error: " . $stmt->error;
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Register</title>
    <link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
    <div class="container">
        <h2>Register</h2>
        
        <form method="POST" enctype="multipart/form-data">
            <input type="text" name="username" required placeholder="Username">
            <br /><br />
            <input type="email" name="email" required placeholder="Email">
            <br /><br />
            <input type="password" name="password" required placeholder="Password">
            <br /><br />
            <input type="file" name="profile_picture" accept="image/*">
            <br /><br />
            <button type="submit" class="btn">Register</button>
        </form>

        <p>Already have an account? <a href="login.php">Login here</a></p>
    </div>
</body>
</html>
