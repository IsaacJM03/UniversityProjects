<?php
session_start();
include "./db.php";

if (!isset($_SESSION["user_id"])) {
    header("Location: login.php");
    exit;
}

$id = $_SESSION["user_id"];
$message = "";

//current user data
$result = $conn->query("SELECT username, email,profile_picture FROM users WHERE id = $id");
$user = $result->fetch_assoc();

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $username = trim($_POST["username"]);
    $email = trim($_POST["email"]);

    if (!empty($_FILES["profile_picture"]["name"])) {
        $allowed_types = ["image/jpg", "image/jpeg", "image/png"];
        $file_type = $_FILES["profile_picture"]["type"];
        $file_size = $_FILES["profile_picture"]["size"];

        if (!in_array($file_type, $allowed_types) || $file_size > 5 * 1024 * 1024) {
            die("Invalid file type or size exceeded (max 5MB).");
        }

        $profile_picture = "uploads/" . basename($_FILES["profile_picture"]["name"]);
        move_uploaded_file($_FILES["profile_picture"]["tmp_name"], $profile_picture);
    } else {
        $profile_picture = $user['profile_picture'];
    }

    $stmt = $conn->prepare("UPDATE users SET username = ?, email = ?, profile_picture = ? WHERE id = ?");
    $stmt->bind_param("sssi", $username, $email,$profile_picture, $id);
    if ($stmt->execute()) {
        $message = "Profile updated successfully!";
        $_SESSION["username"] = $username; // Update session data
    } else {
        $message = "Error updating profile.";
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Edit Profile</title>
    <link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
    <div class="container">
        <h2>Edit Profile</h2>
        
        <?php if ($message): ?>
            <p class="message"><?php echo $message; ?></p>
        <?php endif; ?>

        <form method="POST" enctype="multipart/form-data">
            <input type="text" name="username" value="<?php echo htmlspecialchars($user['username']); ?>" required placeholder="New Username">
            <input type="email" name="email" value="<?php echo htmlspecialchars($user['email']); ?>" required placeholder="New Email">
            <input type="file" name="profile_picture" value="<?php echo $user['profile_picture']; ?>" accept="image/*" placeholder="Profile Picture" >
            <button type="submit" class="btn">Update</button>
        </form>

        <a href="dashboard.php" class="btn btn-secondary">Back to Dashboard</a>
    </div>
</body>
</html>
