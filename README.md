[TOC]
# python_automate_exercise
- "python自动化办公" 书籍的学习记录
### 20200106 学习ch8--目录信息
- os.path系列函数，可以获得文件目录信息，dir和base的区别；可以建立新的文件夹；判定文件/夹是否存在；读取文件夹大小
> 查看 ch8Files\\filePath.py\
### 20200108 学习 ch8--文件读写
- file对象的操作，基本方法
```
# 'r' 读模式 'w'覆盖写模式 'a' 附加写模式
.open()
.read()
.write()
.close()

```
### 20200108 学习 ch9--文件管理
- only copy pdf in a folder。 **shutil模块**，**send2trash**
- 批量修改文件名 
- 压缩文件夹到zip文件。  **zipfile模块**

### 20200113 学习 ch9 文件操作 
- 复制 shutil.copy('dir')
- 剪切 shutil.move('dir')
- 删除 os.unlink('dir')  或者 send2trash.send2trash()
### 20200114 学习 ch9 压缩文件
- zip对象 zipfile.ZipFile()

### 20200115-0117 学习debug方法
- Assertions 用来合理性检查，及早发现不合理的部分，并立刻中断程序
- Try and Expect 用来处理异常，而不中断程序
- logging  利用logging module 代替print() 函数，可以更方便地调试程序，而避免误删除print
- debugging tools 用来逐步执行程序，并检查变量变化
### 20200117 学习简单的爬虫
- webbrowser
- requests
- bs4
- selenium
