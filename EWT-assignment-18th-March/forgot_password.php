<?php
use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;
include "./db.php";
require 'vendor/autoload.php';

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $email = trim($_POST["email"]);

    $stmt = $conn->prepare("SELECT id FROM users WHERE email = ?");
    $stmt->bind_param("s", $email);
    $stmt->execute();
    $stmt->store_result();

    if ($stmt->num_rows > 0) {
        $token = bin2hex(random_bytes(50));
        $stmt = $conn->prepare("UPDATE users SET reset_token = ?, reset_token_expiry = DATE_ADD(NOW(), INTERVAL 1 HOUR) WHERE email = ?");
        $stmt->bind_param("ss", $token, $email);
        $stmt->execute();

        $reset_link = "http://localhost:8000/reset_password.php?token=" . $token;

        $mail = new PHPMailer(true);
        try {
            //SMTP Server settings
            $mail->isSMTP();
            $mail->Host = 'smtp.gmail.com';
            $mail->SMTPAuth = true;
            $mail->Username = 'mwesigwaisaac40@gmail.com';
            $mail->Password = 'kodd oory jmhe dhcd';
            $mail->SMTPSecure = 'ssl';
            $mail->Port = 465;
            $mail->SMTPOptions = array(
                'ssl' => array(
                    'verify_peer' => false,
                    'verify_peer_name' => false,
                    'allow_self_signed' => true
                )
            );
            //Recipients
            $mail->setFrom('mwesigwaisaac40@gmail.com', 'Mailer');
            $mail->addAddress($email);

            //Content
            $mail->isHTML(true);
            $mail->Subject = 'Password Reset Request';
            $mail->Body    = 'Click the following link to reset your password: <a href="' . $reset_link . '">' . $reset_link . '</a>';

            $mail->send();
            print('A password reset link has been sent to your email.');
            header("Location: login.php");
            exit;
        } catch (Exception $e) {
            die("Message could not be sent. Mailer Error: {$mail->ErrorInfo}");
        }
    } else {
        print("No account found with that email.");
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Forgot Password</title>
    <link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
    <div class="container">
        <h2>Forgot Password</h2>
        <form method="POST">
            <input type="email" name="email" required placeholder="Enter your email">
            <br /><br />
            <button type="submit" class="btn">Submit</button>
        </form>
    </div>
</body>
</html>