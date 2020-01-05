# HITWLAN-AutoLogin
哈工大校园网自动认证，Windows端

## 使用方法
用编辑器打开`login.py`，修改其中如下\*****字段为你的校园网用户名和密码
```python
userId = '******'
password = '******'
```
运行`login.cmd`，若显示
> ...
> 校园网登入成功！...
> ...

上网冲浪试试看，是不是认证成功了呢？

## 开机启动
用编辑器打开`login.cmd`，找到
```bash
REM 在当前目录运行python文件，可修改路径
cd %~sdp0
```
将`cd `后改成`login.py`所在的路径即可
然后把`login.cmd`移动至`C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp`
找不到？总之找到`开始菜单 > 程序 > 启动`文件夹放进去就行啦