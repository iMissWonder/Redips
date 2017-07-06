<?php
$sqlHost = $_POST['sqlHost'];
setcookie('mycookie_sqlHost',$sqlHost);
$sqlPort = $_POST['sqlPort'];
setcookie('mycookie_sqlPort',$sqlPort);
$sqlUser = $_POST['sqlUser'];
setcookie('mycookie_sqlUser',$sqlUser);
$sqlPwd = $_POST['sqlPwd'];
setcookie('mycookie_sqlPwd',$sqlPwd);

$rdsHost = $_POST['rdsHost'];
setcookie('mycookie_rdsHost',$rdsHost);
$rdsPort = $_POST['rdsPort'];
setcookie('mycookie_rdsPort',$rdsPort);
$rdsPwd = $_POST['rdsPwd'];
setcookie('mycookie_rdsPwd',$rdsPwd);

$scdHost = $_POST['scdHost'];
setcookie('mycookie_scdHost',$scdHost);
$scdPort = $_POST['scdPort'];
setcookie('mycookie_scdPort',$scdPort);

echo "键入成功！！！！！！！！！！！！！！！</br>";
echo "---------------------------------------------------------</br>";
echo "分别是：</br>";

echo $sqlHost."</br>";
echo "   ".$sqlPort."</br>";
echo "   ".$sqlUser."</br>";
echo "   ".$sqlPwd."</br>";

echo "   ".$rdsHost."</br>";
echo "   ".$rdsPort."</br>";
echo "   ".$rdsPwd."</br>";

echo "   ".$scdHost."</br>";
echo "   ".$scdPort;
?>
