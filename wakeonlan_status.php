<html>
    <head>
        <meta http-equiv="Cache-Control" content="No-Cache"/>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
        <title>Forwarding Status</title>
        <style>
        html{font-size:100%; font-family:sans-serif; color:#666666;}
        body{margin-top:10%;}
        a{font-size:0.917rem; color:#8DB6CD; text-decoration:none;}
        table.csv_output{margin:0px auto; border:1px solid #FFFFFF; width:450px; border-collapse:collapse;}
            tr{background: #FFFFFF; height:25px; border-left:none; padding:3px 2px;}
            tr:nth-child(1){background: #0B6FA4; color: #FFFFFF; border-left:none; padding:3px 2px;}
            td:nth-child(1){text-align:center; font-weight:normal; min-width:10rem;}
            td:nth-child(2){text-align:center; font-weight:normal; min-width:15rem;}
            td:nth-child(3){text-align:center; font-weight:normal; min-width:10rem;}
        .footer{margin:0px auto; text-align:center; font-size:0.8rem;}
        </style>
    </head>
    <body>
    <table class="csv_output">
    <!-- Load CSV file -->
        <?php
        // File path as you python script location
                $file = fopen("/cav/file/path/python_script_location.csv","r") or die("Unable to open file!");
                while (($line = fgetcsv($file)) !== false) {
                    echo "<tr>";
                    foreach ($line as $cell) {echo "<td>" . htmlspecialchars($cell) . "</td>";}
                    echo "</tr>\n";}
                    fclose($file);
        ?>
    </table>
    <br>
    <div class="footer"><a href="https://github.com/Suzhou65/Python-Wake-on-LAN">Python-Wake-on-LAN</a></div>
    </body>
</html>