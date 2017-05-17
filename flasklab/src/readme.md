关于 Flask
===

Flask是一个使用Python开发的基于Werkzeug的Web框架。

Flask非常适合于开发RESTful API，因为它具有以下特点：

* 使用Python进行开发，Python简洁易懂
* 容易上手
* 灵活
* 可以部署到不同的环境
* 支持RESTful请求分发

路由参数设定类型举例：

路由中还可以使用类型定义:

```Python
@app.route('/articles/<articleid>')
```

上面的路由可以替换成下面的例子：

```Python
@app.route('/articles/<int:articleid>')

@app.route('/articles/<float:articleid>')

@app.route('/articles/<path:articleid>')
```

默认的类型为字符串。

参考资料：

* [使用Flask实现RESTful API](http://www.jianshu.com/p/f3624eebff80)