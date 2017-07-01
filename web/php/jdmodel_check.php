<?php
	echo "来查看这个爬虫的状态！</br>";
	echo "---------------------------------------------------------</br>";
	$scrapydip = $_COOKIE['mycookie_input03'];
	//$ip = "http://scrapydtest.t2.daoapp.io:61140/listjobs.json";
	exec("curl http://".$scrapydip.":61140/listjobs.json?project=jingdongModel",$out);
	echo $out[0];
?>
