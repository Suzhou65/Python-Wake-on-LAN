<html>
    <head>
        <!-- META -->
        <meta http-equiv="Cache-Control" content="No-Cache"/>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
        <!-- Style -->
        <style>
            html{font-size:100%; font-family:sans-serif; color:#666666;}
            body{margin-top:10%;}
            a{font-size:0.917rem; color:#8DB6CD; text-decoration:none;}
            .fail{margin:0px auto; text-align:center; font-size:1rem; color:#FF5733; font-weight:bold; padding:1rem;}
            .footer{margin:0px auto; text-align:center; font-size:0.8rem; padding:1rem;}
            .banner{margin-top:0.5rem; margin-bottom:1rem; margin:0px auto; text-align:center; font-size:1.5rem; color:#05668D; font-weight:600; padding:0.5rem;}
            /*Table*/
            table.csv_output{margin:0px auto; border:1px solid #FFFFFF; width:80%; border-collapse:collapse;}
                tr{background:#FFFFFF; height:25px; border-left:none; padding:3px 2px;}
                /*Header*/
                tr:nth-child(1){background:#0B6FA4; color:#FFFFFF; border-left:none; padding:3px 2px;}
                /*Column*/
                td{padding:0.3rem;}
                td:nth-child(1){text-align:center; min-width:20rem;}
                td:nth-child(2){text-align:center; min-width:18rem;}
        </style>
        <!-- Title -->
        <title>Forwarding Status</title>
    </head>
    <!-- Body -->
    <body>
        <div class="banner">Monitor Status</div>
        <table class="csv_output">
            <!-- php block -->
            <?php
            header("refresh:600");
            // Load monitor status
            // File path as you python script location
            if ($file = fopen("/python_script_data/path/status_program.csv","r")){
                while (($line = fgetcsv($file)) !== false){
                    echo "<tr>";
                    foreach ($line as $cell) {echo "<td>" . htmlspecialchars($cell) . "</td>";}
                    echo "</tr>\n";}
                    fclose($file);
                }else{
                    // If unable open file
                    echo '<div class="fail">';
                    echo "Unable to open file.";
                    echo "</div>";}
            ?>
            <!-- php block -->
        </table>
        <br>
        <div class="banner">Forwarding Status</div>
        <table class="csv_output">
            <!-- php block -->
            <?php
            header("refresh:600");
            // Load forwarding record
            // File path as you python script location
            if ($file = fopen("/python_script_data/path/wakeup_record.csv","r")){
                while (($line = fgetcsv($file)) !== false){
                    echo "<tr>";
                    foreach ($line as $cell) {echo "<td>" . htmlspecialchars($cell) . "</td>";}
                    echo "</tr>\n";}
                    fclose($file);
                }else{
                    // If unable open file
                    echo '<div class="fail">';
                    echo "Unable to open monitoring file.";
                    echo "</div>";}
            ?>
            <!-- php block -->
        </table>
        <br>
        <div class="footer">
            <a href="https://github.com/Suzhou65/Python-Wake-on-LAN">Python-Wake-on-LAN</a>
        </div>
    </body>
</html>