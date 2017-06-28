<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>爬取结果</title>
</head>

<body>
<center><table style="border:dotted;border-color:#F06">
<caption>来自Redips团队数据库：</caption>
<tr><th>图书ID号</th><th>名称</th><th>作者</th><th>ISBN号</th><th>出版社</th><th>出版时间</th><th>价格</th><th>页数</th><th>翻译</th><th>读者数</th><th>封面图片链接</th><th>
<?php
$conn=mysqli_connect('192.168.199.218','user','user','douban')or die("数据库连接失败");
//连接数据库

mysqli_select_db($conn, 'douban') or die('选择数据库失败！');
mysqli_query("set names utf8");//设置编码格式

$sql="select * from doubaninfo";//设置查询指令

$result=mysqli_query($conn,$sql); //执行查询
while($row=mysqli_fetch_assoc($result))//将result结果集中查询结果取出一条
{
 echo"<tr><td>".$row["book_id"]."</td><td>".$row["title"]."</td><td>".$row["author"]."</td><td>".$row["isbn13"]."</td><td>".$row["publisher"]."</td><td>".$row["pubdate"]."</td><td>".$row["price"]."</td><td>".$row["pages"]."</td><td>".$row["translator"]."</td><td>".$row["lookcount"]."</td><td>".$row["image"]."</td><td>";
	
 
}
?>
</table>
<a href="index.html">返回</a>

</center>
</body>
</html>
