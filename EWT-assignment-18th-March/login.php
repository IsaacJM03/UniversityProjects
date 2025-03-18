<?php
session_start();
include "./db.php";

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $email = trim($_POST["email"]);
    $password = trim($_POST["password"]);

    $stmt = $conn->prepare("SELECT id, username, password FROM users WHERE email = ?");
    $stmt->bind_param("s", $email);
    $stmt->execute();
    $stmt->store_result();
    $stmt->bind_result($id, $username, $hashed_password);
    $stmt->fetch();

    if ($stmt->num_rows > 0 && password_verify($password, $hashed_password)) {
        $_SESSION["user_id"] = $id;
        $_SESSION["username"] = $username;

        // Remember me functionality
        if (!empty($_POST["remember"])) {
            setcookie("user_email", $email, time() + (86400 * 30), "/");
            setcookie("user_pass", $password, time() + (86400 * 30), "/"); // 86400 seconds = 1 day
        }

        header("Location: dashboard.php");
        exit;
    } else {
        $error = "Invalid email or password.";
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
    <link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
    <div class="container">
        <h2>Login</h2>

        <?php if (isset($error)): ?>
            <p class="error"><?php echo $error; ?></p>
        <?php endif; ?>

        <form method="POST">
            <input type="email" name="email" value="<?php echo isset($_COOKIE['user_email']) ? $_COOKIE['user_email'] : ''; ?>" required placeholder="Email">
            <br /><br />
            <input type="password" name="password" value="<?php echo isset($_COOKIE['user_pass']) ? $_COOKIE['user_pass'] : ''; ?>" required placeholder="Password">
            <br /><br />
            
            <label>
                <input type="checkbox" name="remember" <?php echo isset($_COOKIE['user_email']) ? 'checked' : ''; ?>> Remember Me
            </label>
            <br /><br />

            <button type="submit" class="btn">Login</button>
        </form>

        <p>Don't have an account? <a href="register.php">Register here</a></p>
        <p>Forgot your password? <a href="forgot_password.php">Reset it here</a></p>
    </div>
</body>
</html>
