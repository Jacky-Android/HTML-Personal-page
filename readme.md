# 个人网页导航实现
体验地址：📫[地址]📫(http://218.244.150.75/)
```
pip install flask
```

# 先上HTML代码

```html

<!DOCTYPE html>
<html lang="zh-CN">

<head>
    <meta charset=utf-8>
    <meta name=apple-mobile-web-app-title content=Hsury>
    <meta name=application-name content=Hsury>
    <meta name=msapplication-TileColor content=#2d89ef>
    <meta name=theme-color content=#ffffff>
    <meta name=viewport content="width=device-width, initial-scale=1.0">
    <link rel="icon" href="./blog.ico" type="image/x-icon">
    <link rel="shortcut icon" href="./blog.ico" type="image/x-icon">
    <link rel=manifest href=/site.webmanifest>
    <link rel=mask-icon href=/safari-pinned-tab.svg color=#5bbad5>
    <title>Liusiyong</title>
    <script src="js/jquery.min.js"></script>
    <link rel="stylesheet" href="css/semantic.min.css">
    <style>
        * {
            color: #fff;
            font-family: "Microsoft YaHei";
            font-size: 8px;
            font-weight: lighter;
            text-align: center;
        }
        
        body {
            background: #3cd5ff;
            background: -webkit-linear-gradient(to right, #ff00c8, #3cd5ff);
            background: linear-gradient(to right, #ff00c8, #3cd5ff);
        }
        
        h1 {
            font-size: 75px;
            margin: 3.5vw 0 0
        }
        
        h2 {
            font-size: 24px;
            margin: .8vw
        }
        
        footer {
            font-weight: normal;
            line-height: 18px;
            margin: .8vw 0 .4vw;
            position: relative
        }
        
        .btn {
            border: 1px solid;
            cursor: pointer;
            display: inline-block;
            font-size: 16px;
            font-weight: 400;
            line-height: 45px;
            margin: 0 32px 1em;
            max-width: 160px;
            overflow: hidden;
            position: relative;
            text-decoration: none;
            vertical-align: middle;
            width: 100%;
        }
        
        .btn:after {
            background: #fff;
            content: "";
            height: 155px;
            left: -75px;
            opacity: .2;
            position: absolute;
            top: -50px;
            -webkit-transform: rotate(35deg);
            -ms-transform: rotate(35deg);
            transform: rotate(35deg);
            -webkit-transition: all 550ms cubic-bezier(0.19, 1, 0.22, 1);
            transition: all 550ms cubic-bezier(0.19, 1, 0.22, 1);
            width: 50px;
            z-index: -10
        }
        
        .btn:hover:after {
            left: 120%;
            -webkit-transition: all 550ms cubic-bezier(0.19, 1, 0.22, 1);
            transition: all 550ms cubic-bezier(0.19, 1, 0.22, 1)
        }
    </style>
    <style>
        input:focus {
            border: 2px solid rgb(62, 88, 206);
        }
        
        input {
            text-indent: 11px;
            padding-left: 11px;
            font-size: 16px;
        }
    </style>
    <!--input初始状态-->
    <style class="input/css">
        .input {
            width: 40%;
            height: 45px;
            vertical-align: top;
            box-sizing: border-box;
            border: 2px solid rgb(207, 205, 205);
            border-right: 2px solid rgb(62, 88, 206);
            border-bottom-left-radius: 10px;
            border-top-left-radius: 10px;
            outline: none;
            margin: 0;
            display: inline-block;
            background: url(camera.png) no-repeat 0 0;
            background-position: 565px 7px;
            background-size: 28px;
            padding-right: 49px;
            padding-top: 10px;
            padding-bottom: 10px;
            line-height: 16px;
        }
    </style>
    <!--button初始状态-->
    <style class="button/css">
        .button {
            height: 45px;
            width: 130px;
            vertical-align: middle;
            text-indent: -8px;
            padding-left: -8px;
            background-color: rgb(62, 88, 206);
            color: white;
            font-size: 18px;
            outline: none;
            border: none;
            border-bottom-right-radius: 10px;
            border-top-right-radius: 10px;
            margin: 0;
            padding: 0;
        }
    </style>

</head>
<h1>dyc's page</h1>
<h2>个人网页导航</h2>
<div style="font-size: 0px;">
    <div align="center">

        <form method="GET" action="https://www.baidu.com/s?wd=hello%20world" id="wd">
            <input type="text" class="input" name="wd" id="s-input" />
            <input type="submit" class="button" href="javascript:wd.submit()" value="搜索一下" />
        </form>

    </div>
</div>
<br>
<a href="https://blog.csdn.net/qq_43997786" target=_blank class="btn">blog</a>
<a href="https://space.bilibili.com/391099187?from=search&seid=10292981058346091712" target=_blank class=btn>Bilibili</a>
<a href="https://github.com/Jacky-Android" target=_blank class=btn>GitHub</a>
<a href="https://www.ghxi.com/" target=_blank class=btn>果核软件</a>
<a href="https://music.ghpym.com/" target=_blank class=btn>果核音乐</a>
<br>
<a href="https://www.cn-ki.net/" target=_ blank class=btn>iData</a>
<a href="https://www.dalipan.com/#/" target=_ blank class=btn>百度网盘爬虫</a>
<a href="http://flysheep.ys168.com/" target=_ blank class=btn>单机游戏分享</a>
<a href="https://www.douban.com/" target=_ blank class=btn>豆瓣</a>
<a href="https://www.zhihu.com/topic/19550228/hot" target=_ blank class=btn>知乎热榜</a>
<a href="https://www.githubs.cn/" target=_ blank class=btn>github china</a>
<br>
<a href="https://www.google.com/" target=_ blank class=btn>google</a>
<a href="https://gaoxx.com/" target=_ blank class=btn>巴法文库下载</a>
<a href="https://xbeibeix.com/api/bilibili/" target=_ blank class=btn>哔哩哔哩解析</a>
<a href="https://musicder.com/?ref=p" target=_ blank class=btn>音乐download</a>
<a href="https://www.meiju5.com/" target=_ blank class=btn>美剧网</a>
<footer>&hearts;<br>欢迎来到我的主页<br>一起学习HTML吧<br>&hearts;<br>Copyright &copy; 1999-
    <script>
        document.write(new Date().getFullYear())
    </script> by auther liusiyong </footer>
</body>

</html>
```
## 用flask封装后
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210421221438439.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzOTk3Nzg2,size_16,color_FFFFFF,t_70)

