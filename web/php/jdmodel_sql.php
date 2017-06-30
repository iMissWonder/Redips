<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>爬取结果</title>
</head>

<body>
<center><table style="border:dotted;border-color:#F06">
<caption>来自Redips团队数据库：</caption>
<tr><th>店铺名</th><th>店铺所在地</th><th>店铺综合评分</th><th>店铺综合评分-与同行平均水平</th><th>商品满意度</th><th>商品满意度-与同行平均水平</th><th>服务满意度</th><th>服务满意度-与同行平均水平</th><th>物流速度满意度</th><th>物流速度满意度-与同行平均水平</th><th>商品描述满意度</th><th>商品描述满意度-与同行平均水平</th><th>退换货处理满意度</th><th>退换货处理满意度-与同行平均水平</th><th>售后处理时长</th><th>售后处理时长-与同行平均水平</th><th>交易纠纷率</th><th>交易纠纷率-与同行平均水平</th><th>退换货返修率</th><th>退换货返修率-与同行平均水平</th><th>店铺违法违规信息次数</th><th>
<?php
$conn=mysqli_connect('db2.daocloudinternal.io','user','user','jdmodel')or die("数据库连接失败");
//连接数据库

mysqli_select_db($conn, 'jdmodel') or die('选择数据库失败！');
mysqli_query("set names utf8");//设置编码格式

$sql="select * from jdmodelinfo";//设置查询指令

$result=mysqli_query($conn,$sql); //执行查询
while($row=mysqli_fetch_assoc($result))//将result结果集中查询结果取出一条
{
 echo"<tr><td>".$row["title"]."</td><td>".$row["location"]."</td><td>".$row["shopAveScore"]."</td><td>".$row["shopAveScore_comRate"]."</td><td>".$row["goodsContent"]."</td><td>".$row["goodsContent_comRate"]."</td><td>".$row["serveAttitude"]."</td><td>".$row["serveAttitude_comRate"]."</td><td>".$row["transSpeed"]."</td><td>".$row["transSpeed_comRate"]."</td><td>".$row["goodsDescribe"]."</td><td>".$row["goodsDescribe_cmRate"]."</td><td>".$row["backGoods"]."</td><td>".$row["backGoods_comRate"]."</td><td>".$row["aftersalesDealTime"]."</td><td>".$row["aftersalesDealTime_comRate"]."</td><td>".$row["dealDispute"]."</td><td>".$row["dealDispute_comRate"]."</td><td>".$row["backRepair"]."</td><td>".$row["backRepair_comRate"]."</td><td>".$row["violationTimes"]."</td><td>";

}
?>
</table>
<a href="index.html">返回</a>

</center>
</body>
</html>
