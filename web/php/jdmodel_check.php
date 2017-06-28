<?php
	echo "来查看这个爬虫的状态！</br>";
	echo "---------------------------------------------------------</br>";
	$scrapydip = $_COOKIE['mycookie_input03'];
	//$ip = "http://192.168.199.203:6800/listjobs.json";
	exec("curl http://".$scrapydip.":6800/listjobs.json?project=jingdongModel",$out);
	echo $out[0];
?>
