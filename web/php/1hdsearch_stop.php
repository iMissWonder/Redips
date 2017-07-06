<?php	
	$jobid = $_COOKIE['mycookie'];
	$jobidIn = $_POST['jobYouIn'];
	$scdHost = $_COOKIE['mycookie_scdHost'];
	$scdPort = $_COOKIE['mycookie_scdPort'];
	
	if(empty($jobidIn)){
			echo "关闭最近一次开启的job</br>";
			echo "你的jobid的是".$jobid."</br>现在我们一起来停止它！！！下面是返回值：</br>";
			echo "---------------------------------------------------------</br>";
			//$ip = "http://scrapydtest.t2.daoapp.io:61031/cancel.json";
			exec("curl http://".$scdHost.":".$scdPort."/cancel.json -d project=yhdSearch -d job=".$jobid,$out);
			echo "$out[0]";
						  }
	else{
			echo "你的jobid的是".$jobidIn."</br>现在我们一起来停止它！！！下面是返回值：</br>";
			echo "---------------------------------------------------------</br>";
			//$ip = "http://scrapydtest.t2.daoapp.io:61031/cancel.json";
			exec("curl http://".$scdHost.":".$scdPort."/cancel.json -d project=yhdSearch -d job=".$jobidIn,$out);
			echo "$out[0]";
	    }
?>