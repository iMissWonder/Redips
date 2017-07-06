<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>爬取结果</title>
</head>

<body>
<center><table style="border:dotted;border-color:#F06">
<caption>来自Redips团队数据库：</caption>
<tr><th>商品名</th><th>商品价格</th><th>商品链接</th><th>目录</th><th>商品ID</th><th>图片链接</th><th>
<?php
$sqlHost = $_COOKIE['mycookie_sqlHost'];
$sqlUser = $_COOKIE['mycookie_sqlUser'];
$sqlPwd = $_COOKIE['mycookie_sqlPwd'];
$sqlPort = $_COOKIE['mycookie_sqlPort'];

$conn=mysqli_connect($sqlHost,$sqlUser,$sqlPwd,'1hdall',$sqlPort)or die("数据库连接失败");
//连接数据库

mysqli_select_db($conn, '1hdall') or die('选择数据库失败！');
mysqli_query("set names utf8");//设置编码格式

$sql="select * from 1hdallinfo";//设置查询指令

$result=mysqli_query($conn,$sql); //执行查询
while($row=mysqli_fetch_assoc($result))//将result结果集中查询结果取出一条
{
 echo"<tr><td>".$row["title"]."</td><td>".$row["currentPrice"]."</td><td>".$row["link"]."</td><td>".$row["category"]."</td><td>".$row["productId"]."</td><td>".$row["imgLink"]."</td><td>";


}
?>
</table>
<a href="index.html">返回</a>

</center>
</body>
</html>
