<?php
$mysqlip = $_COOKIE['mycookie_input01'];
$redisip = $_COOKIE['mycookie_input02'];
$scrapydip = $_COOKIE['mycookie_input03'];
exec("curl http://".$scdHost.":".$scdPort."/schedule.json -d project=DoubanBookSpider -d spider=BookContentSpider -d setting=MYSQL_HOST=".$sqlHost." -d setting=REDIS_HOST=".$rdsHost." -d setting=MYSQL_USER=".$sqlUser." -d setting=MYSQL_PASSWD=".$sqlPwd." -d setting=REDIS_PORT=".$rdsPort." -d setting=REDIS_PASSWORD=".$rdsPwd,$out);
echo "你打开了爬虫！！！底下是返回值！！！</br>";
echo "---------------------------------------------------------</br>";
$array = $out[0];
echo $array."</br>";
$jobid = substr($array,27,32); //getjobid
echo "你的jobid:".$jobid;
setcookie('mycookie',$jobid);
?>


