### 库的安装
* selenium ： 模拟鼠标操作浏览器的库
* requests ： 发送请求的库
* Microsoftwebdriver ： 浏览器接口
* aiohttp： 之前的requests库是一个闭塞式的HTTP请求库，当发出指令后程序会一直等待服务器响应，
直到响应后才会进行下一步操作，这样很浪费时间，aiohttp就是个异步[^1]web服务的库，使用异步请求库抓取会更加高效。
> 异步处理：
异步的另外一种含义是计算机多线程的异步处理。与同步处理相对，异步处理不用阻
>塞当前线程来等待处理完成，而是允许后续操作，直至其它线程将处理完成，并回调通知此线程。
* aiodns: 加速dns解析
* cchardet： 字符编码检测库
> 下面是解析库
* lxml： 支持html和xml格式的解析，支持XPath的解析方式        

> xpath：XPath即为XML路径语言（XML Path Language），它是一种用来确定XML文档中某部分位置的语言。

* Beautiful Soup: 安装的适合是beautifulsoup4 这个库是基于lxml的html和xml解析库，在安装之前请确保lxml是否安装好了。
* pyquery 网页解析器，提供了jquery类似的语法来解析html文档，支持css选择器。
* tesserocr 验证码方面的问题。
