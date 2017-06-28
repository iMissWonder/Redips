<?php
$input01 = $_POST['input01'];
setcookie('mycookie_input01',$input01);
$input02 = $_POST['input02'];
setcookie('mycookie_input02',$input02);
$input03 = $_POST['input03'];
setcookie('mycookie_input03',$input03);
echo "键入成功！！！！！！！！！！！！！！！</br>";
echo "---------------------------------------------------------</br>";
echo "分别是：</br>";
echo $input01."</br>";
echo "   ".$input02."</br>";
echo "   ".$input03;

?> 
