<?php
include("config.php");

$filename = "data.txt";

if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST["content"])) {
    $name = $_POST["name"];
    $email = $_POST["email"];
    
    $upload_dir = "uploads/";
    $file_path = $upload_dir.basename(($_FILES["file"]["name"]));

    if (move_uploaded_file($_FILES["file"]["tmp_name"], $file_path)) {
        $stmt = $conn->prepare("INSERT INTO users(name,email,filename) VALUES (?,?,?)");
        $stmt->bind_param("sss", $name, $email,$file_path);
        $stmt->execute();
        $stmt->close();
    }
}
// read file contents
$file_content = file_exists($filename) ? file_get_contents($filename) :"No data yet";

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>File handling and Upload</title>
</head>
<body>
    <h2>Write to File</h2>
    <form method="post">
        <textarea name="content" required></textarea>
        <button type="submit">Save</button>
    </form>

    <h3>File Content:</h3>
    <pre><?php echo htmlspecialchars($file_content); ?></pre>

    <h2>Upload File & Store Data</h2>
    <form method="post" enctype="multipart/form-data">
        <input type="text" name="name" placeholder="Enter Name" required>
        <input type="email" name="email" placeholder="Enter Email" required>
        <button type="submit">Upload</button>
    </form>

    <h2>Uploaded Users</h2>
    <table border="1">
        <tr>
            <th>Name</th>
            <th>Email</th>
            <th>File</th>
        </tr>
        <?php 
        $result = $conn->query("SELECT * FROM users");
        while ($row = $result->fetch_assoc()) {
            echo "<tr>
                    <td>{$row['name']}</td>
                    <td>{$row['email']}</td>
                    <td><a href='{$row['filename']}>Download</a></td>
                </tr>
            ";
        }
        ?>
    </table>
</body>
</html>