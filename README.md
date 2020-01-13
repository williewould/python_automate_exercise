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

### 20200114 学习 ch9 文件操作 
- 复制 shutil.copy('dir')
- 剪切 shutil.move('dir')
- 删除 os.unlink('dir')  或者 send2trash.send2trash()