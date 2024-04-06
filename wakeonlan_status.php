<!DOCTYPE html>
<html lang="en">
    <head>
        <!-- META -->
        <meta http-equiv="Cache-Control" content="max-age=600"/>
        <meta http-equiv="Content-Type" content="text/html" charset="utf-8"/>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name="robots" content="noindex,nofollow">
        <!-- Style, 20240405 -->
        <style>
        @media all{
            body{background:#FFFFFF;color:#24292E;font-family:sans-serif;font-size:100%;font-weight:400;margin-top:2rem;}
            h1{font-size:1.12rem;font-weight:600;margin:0 0 1.125rem;line-height:1.1;}
            h2{font-size:1.06rem;font-weight:600;color:#028090;margin:1.125 0.25 0.25 0.25rem;line-height:1.1;}
            a{font-size:0.917rem;text-decoration:none;color:#3399CC;}
            small{font-size:0.85rem;font-weight:600;}
            a small{font-size:0.75rem;color:#777777;margin-top:-0.3em;display:block;font-weight:600;}
            strong{color:#222222;font-weight:600;}
            .wrapper{max-width:73.75rem;margin:0 auto;}
            header{width:16.875rem;float:left;position:fixed;}
            header ul{list-style:none;width:16.875rem;height:2.5rem;padding:0;background:#F4F4F4;border-radius:0.313rem;border:0.063rem solid #E0E0E0;}
            header li{width:5.563rem;height:2.5rem;float:left;border-right:0.063rem solid #E0E0E0;}
            header ul a{height:2.125rem;padding-top:0.375rem;display:block;font-size:0.88rem;color:#999999;font-weight:600;line-height:1;text-align:center;}
            header ul li + li + li{width:5.563rem;border-right:none;}
            header ul a strong{font-size:0.875rem;color:#222222;font-weight:600;display:block;}
            footer{width:16.875rem;float:left;position:fixed;bottom:3.125rem;font-size:0.85rem;}
            section{width:51.875rem;float:right;padding-bottom:3.125rem;}
            .failed{margin:0px auto;text-align:center;font-size:1rem;font-weight:700;color:#028090;padding:1rem;}
            table{margin:0px auto;border:0.063rem solid #FFFFFF;width:100%;border-collapse:collapse;}
            table tr{background:#FFFFFF;height:1.563rem;border-left:none;padding:0.188rem 0.125rem;}
            table tr:nth-child(1){background:#028090;color:#FFFFFF;border-left:none;padding:0.188rem 0.125rem;}
            table td{padding:0.5rem;}
            .authorization{text-align:center;margin-top:10rem;}
            .authorization form.login{margin:0px auto;}
            input[type="password"]{
                border:0.125rem #028090 solid;border-radius:0.25rem;width:18rem;text-align:center;font-size:1.12rem;}
            input[type='submit']{
                border:0.125rem #3399CC solid;border-radius:0.25rem;width:18.5rem;text-align:center;font-size:1.12rem;margin-top:1rem;color:#F4F4F4;background:#3399CC;}
        }@media print,screen and (min-width:1280px){
            header{padding-right:11.25rem;}
        }@media print,screen and (max-width:1136px){
            .wrapper{width:auto;margin:0;}
            header,section,footer{float:none;position:static;width:auto;}
            header{padding-right:20rem;}
            section{border:0.063rem solid #E5E5E5;border-width:0.063rem 0;padding:1.25rem 0;margin:0 0 1.25rem;}
            header a small{display:inline;}
            header ul{position:absolute;right:3.125rem;top:3.25rem;}
        }@media print,screen and (max-width:960px){
            body{word-wrap:break-word;font-size:1rem;line-height:1.2rem;}
            header{padding:0;}
            header ul,header p.view{position:static;}
            table{margin:0px auto;border:0.063rem solid #FFFFFF;width:95%;border-collapse:collapse;}}
        </style>
        <!-- Favicon -->
        <link rel="icon" type="image/png" href="/favicon.png" sizes="32x32" />
        <link rel="alternate icon" type="image/x-icon" href="/favicon.ico" sizes="128x128" />
        <link rel="alternate icon" type="image/webp" href="/favicon.webp" sizes="128x128" />
        <link rel="apple-touch-icon" type="image/png" href="/apple-touch-icon.png" sizes="180x180" />
        <!-- Title -->
        <title>Forwarding Status</title>
    </head>
    <body>
        <div class="wrapper">
            <header>
                <h1>Wake-on-LAN</h1>
                <p>Forwarding Status</p>
                <ul>
                    <li><a href="javascript:history.back()">Previous<strong>Pages</strong></a></li>
                    <li><a href="javascript:window.location.reload()">Refresh<strong>Pages</strong></a></li>
                    <li><a href="https://github.com/Suzhou65/Python-Wake-on-LAN" target="_self">Source<strong>Code</strong></a></li>
                </ul>
            </header>
            <section>
            <!--Section Frame Start-->
            <?php
            // Hash password
            $hash = '$Put_Your_Hashed_Password_at_Here';
            $verify = password_verify($_POST["password"],$hash);
            // Authorization Action
            if(isset($_POST["submit"])){
                //Authorization
                if($verify){
                    // Authorization Succeeded
                    // Header
                    echo "<h2>Forwarding System Status</h2>";
                    // Table
                    if ($file = fopen("/file_path/wakeonlan.forward_status.csv","r")){
                        // Table, Forwarding Record
                        echo '<table class="forwarding">';
                        while (($line = fgetcsv($file)) !== false){
                            // Thead 
                            echo "<tr>";
                            foreach ($line as $cell) {echo"<td>".htmlspecialchars($cell)."</td>";}
                            echo "</tr>\n";}
                            fclose($file);
                        echo "</table>";
                        }else{
                            // Unable Open File
                            echo "<table><tr>";
                            echo "<td>Unable to open database file.</td>";
                            echo "</tr></table>";}
                    // Header
                    echo "<br>";
                    echo "<h2>Forwarding Record</h2>";
                    // Table
                    if ($file = fopen("/file_path/wakeonlan.mac_address.csv","r")){
                        // Table, Forwarding Record
                        echo '<table class="forwarding">';
                        while (($line = fgetcsv($file)) !== false){
                            // Thead 
                            echo "<tr>";
                            foreach ($line as $cell) {echo"<td>".htmlspecialchars($cell)."</td>";}
                            echo "</tr>\n";}
                            fclose($file);
                        echo "</table>";
                        }else{
                            // Unable Open File
                            echo "<table><tr>";
                            echo "<td>Unable to open database file.</td>";
                            echo "</tr></table>";}
                }else{
                    // Incorrect Password
                    echo '<div class="authorization"><div class="failed">';
                    echo "Authorization Failed.";
                    echo "</div></div>";}
                }else{
                // Authorization Form
                ?>
                <div class="authorization">
                    <form method="post" name="login">
                        <input type="password" name="password"/><br>
                        <input type="submit" name="submit" value="Access"/>
                    </form>
                </div>
            <?php
            }
            ?>
            <!-- PHP Section End -->
            </section>
            <!--Section Frame end-->
            <footer>
            <p>Demonstration from <a href="https://github.com/" target="_self">GitHub</a> .<br>
                    <small>Develop, written by <a href="https://github.com/Suzhou65" target="_self">Suzhou65</a> .</small></p>
            </footer>
        </div>
        <!--Main Frame end-->
    </body>
</html>
