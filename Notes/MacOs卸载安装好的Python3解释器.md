# MacOs卸载安装好的Python3解释器

## 准备工作

1. 查看已经安装好的python3解释器的版本
   - `python3 --version`

2. 查看已经安装好的python3解释器的安装路径
   - `which python3`
     - `/Library/Frameworks/Python.framework/Versions/3.10/bin/python3`

## 开始卸载

1. 卸载/删除python3的框架
   - 通过`/Library/Frameworks/Python.framework/Versions/` 进一步确认要卸载的python3解释器版本
   - 卸载/删除命令: `sudo rm -rf /Library/Frameworks/Python.framework/Versions/3.10`
   - 通过:`ls /Library/Frameworks/Python.framework/Versions` 命令查看python3框架是否删除
2. 卸载/删除python3应用目录

   - 应用目录: `/Applications`
   - 进入到到应用目录: `cd /Applications`
   - 查看应用目录内容: `ls`
   - 卸载/删除Python3应用目录: `sudo rm -rf Python 3.10` (可按下tab键进行补全)
   - 查看应用目录内容: `ls` (确认是否已经删除)
   - 查看launchpad中的Python3的IDLE是否已经消失

3. 删除 `/usr/local/bin `目录下指向的Python3(Python 3.10)
   - 进入到 `/usr/local/bin`:  `cd /usr/local/bin`
   - 查看应用目录内容: `ls`
   - 卸载/删除Python3.10相关的文件和链接 (需要自行确认) : 
     - 方案一: `sudo rm -rf python3*`
     - 方案二: `rm python3*`