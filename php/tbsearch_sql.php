<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>爬取结果</title>
</head>

<body>
<center><table style="border:dotted;border-color:#F06">
<caption>来自Redips团队数据库：</caption>
<tr><th>商品名</th><th>商品链接</th><th>店铺名</th><th>商品价格</th><th>淘宝优惠价格</th><th>累计评论数</th><th>交易成功数</th><th>
<?php
$conn=mysqli_connect('192.168.199.218','user','user','tbsearch')or die("数据库连接失败");
//连接数据库

mysqli_select_db($conn, 'tbsearch') or die('选择数据库失败！');
mysqli_query("set names utf8");//设置编码格式

$sql="select * from tbsearchinfo";//设置查询指令

$result=mysqli_query($conn,$sql); //执行查询
while($row=mysqli_fetch_assoc($result))//将result结果集中查询结果取出一条
{
 echo"<tr><td>".$row["title"]."</td><td>".$row["link"]."</td><td>".$row["shop"]."</td><td>".$row["price"]."</td><td>".$row["taobaoPrice"]."</td><td>".$row["commentsNum"]."</td><td>".$row["dealDoneNum"]."</td><td>";
	
 
}
?>
</table>
<a href="index.html">返回</a>

</center>
</body>
</html>
