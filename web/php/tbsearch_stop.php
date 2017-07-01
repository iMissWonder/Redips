<?php
	$jobid_redis = $_COOKIE['mycookie_redis'];
	$jobid = $_COOKIE['mycookie'];
	$scrapyid = $_COOKIE['mycookie_input03'];
	echo "你的jobid的是".$jobid_redis."</br>现在我们一起来停止它！！！下面是返回值：</br>";
	echo "---------------------------------------------------------</br>";
	//$ip = "http://db2.daocloudinternal.io:61140/cancel.json";
	exec("curl http://".$scrapyid.":61140/cancel.json -d project=taobaoSearch -d job=".$jobid_redis,$out_redis);
	echo "$out_redis[0]</br>";
	echo "你的jobid的是".$jobid."</br>现在我们一起来停止它！！！下面是返回值：</br>";
	echo "---------------------------------------------------------</br>";
	//$ip = "http://db2.daocloudinternal.io:61140/cancel.json";
	exec("curl http://".$scrapyid.":61140/cancel.json -d project=taobaoSearch -d job=".$jobid,$out);
	echo "$out[0]";
?>
