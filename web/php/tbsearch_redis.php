<?php
$sqlHost = $_COOKIE['mycookie_sqlHost'];
$sqlUser = $_COOKIE['mycookie_sqlUser'];
$sqlPwd = $_COOKIE['mycookie_sqlPwd'];
$rdsHost = $_COOKIE['mycookie_rdsHost'];
$rdsPort = $_COOKIE['mycookie_rdsPort'];
$rdsPwd = $_COOKIE['mycookie_rdsPwd'];
$scdHost = $_COOKIE['mycookie_scdHost'];
$scdPort = $_COOKIE['mycookie_scdPort'];
$keyWd = $_COOKIE['mycookie_keyWd'];
exec("curl http://".$scdHost.":".$scdPort."/schedule.json -d project=taobaoSearch -d spider=taobaoSSpider -d setting=MYSQL_HOST=".$sqlHost." -d setting=REDIS_HOST=".$rdsHost." -d setting=MYSQL_USER=".$sqlUser." -d setting=MYSQL_PASSWD=".$sqlPwd." -d setting=REDIS_PORT=".$rdsPort." -d setting=REDIS_PASSWORD=".$rdsPwd." -d setting=TARGET=".$keyWd,$out);
echo "你打开了REDIS爬虫！！！底下是返回值！！！</br>";
echo "---------------------------------------------------------</br>";
$array = $out[0];
echo $array."</br>";
$jobid = substr($array,27,32); //getjobid
echo "你的jobid:".$jobid;
setcookie('mycookie',$jobid);
?>
