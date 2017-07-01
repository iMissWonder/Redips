<?php
	$jobid = $_COOKIE['mycookie'];
	$scrapyid = $_COOKIE['mycookie_input03'];
	echo "你的jobid的是".$jobid."</br>现在我们一起来停止它！！！下面是返回值：</br>";
	echo "---------------------------------------------------------</br>";
	//$ip = "http://db2.daocloudinternal.io:61031/cancel.json";
	exec("curl http://".$scrapyid.":61031/cancel.json -d project=JDSearch -d job=".$jobid,$out);
	echo "$out[0]";
?>
