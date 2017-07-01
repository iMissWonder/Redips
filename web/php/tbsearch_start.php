<?php
$mysqlip = $_COOKIE['mycookie_input01'];
$redisip = $_COOKIE['mycookie_input02'];
$scrapydip = $_COOKIE['mycookie_input03'];
$search = $_COOKIE['mycookie_input04'];
//$ip="http://db2.daocloudinternal.io:61140/schedule.json";
exec("curl http://".$scrapydip.":61140/schedule.json -d project=taobaoSearch -d spider=taobaoSSpider -d setting=MYSQL_HOST=".$mysqlip." -d setting=REDIS_HOST=".$redisip." -d setting=TARGET=".$search,$out_redis);
echo "你打开了REDIS爬虫！！！底下是返回值！！！</br>";
echo "---------------------------------------------------------</br>";
$array_redis = $out_redis[0];
echo $array_redis."</br>";
$jobid_redis = substr($array_redis,27,32); //getjobid
echo "你的jobid:".$jobid_redis."</br>";
setcookie('mycookie_redis',$jobid_redis);

exec("curl http://".$scrapydip.":61140/schedule.json -d project=taobaoSearch -d spider=taobaoSProSpider -d setting=MYSQL_HOST=".$mysqlip." -d setting=REDIS_HOST=".$redisip,$out);
echo "你打开了爬虫！！！底下返回值！！！</br>";
echo "---------------------------------------------------------</br>";
$array = $out[0];
echo $array."</br>";
$jobid = substr($array,27,32); //getjobid
echo "你的jobid:".$jobid;
setcookie('mycookie',$jobid);

?>
