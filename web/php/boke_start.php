<?php
$mysqlip = $_COOKIE['mycookie_input01'];
$redisip = $_COOKIE['mycookie_input02'];
$scrapydip = $_COOKIE['mycookie_input03'];
exec("curl http://".$scrapydip.":6800/schedule.json -d project=bodyExtract -d spider=bodyExtractIn -d setting=MYSQL_HOST=".$mysqlip." -d setting=REDIS_HOST=".$redisip,$out);
echo "你打开了爬虫！！！底下是返回值！！！</br>";
echo "---------------------------------------------------------</br>";
$array = $out[0];
echo $array."</br>";
$jobid = substr($array,27,32); //getjobid
echo "你的jobid:".$jobid;
setcookie('mycookie',$jobid);
?>

