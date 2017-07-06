<?php
	echo "来查看这个爬虫的状态！</br>";
	echo "---------------------------------------------------------</br>";
	$scdHost = $_COOKIE['mycookie_scdHost'];
	$scdPort = $_COOKIE['mycookie_scdPort'];
	//$ip = "http://scrapydtest.t2.daoapp.io:61031/listjobs.json";
	exec("curl http://".$scdHost.":".$scdPort."/listjobs.json?project=taobaoCrawler",$out);
	echo $out[0];
?>