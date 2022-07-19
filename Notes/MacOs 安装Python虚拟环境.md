## MacOs 安装Python虚拟环境

### 1  安装环境依赖

1. `pip install virtualenv`

2. `pip install virtualenvwrapper`

3. 可使用国内镜像源加速 `pip install -i https://pypi.mirrors.ustc.edu.cn/simple 包名`

### 2 更新系统环境变量

**-zsh 终端下** 控制台输入

` which virtualenvwrapper.sh` 找到文件所在地址 

`/Library/Frameworks/Python.framework/Versions/3.10/bin/virtualenvwrapper.sh`

输入 `which python3` 找到python3地址

`/Library/Frameworks/Python.framework/Versions/3.10/bin/python3`

输入命令`open .zshrc`打开隐藏文件.zshrc 在文件中输入

```bash
# Setting PATH for Python 3.10
PATH="/Library/Frameworks/Python.framework/Versions/3.10/bin:${PATH}"
export PATH

# Setting virtualenv PATH for Python 3.10
export WORKON_HOME='~/.virtualenv'
export VIRTUALENVWRAPPER_SCRIPT=/Library/Frameworks/Python.framework/Versions/3.10/bin/virtualenvwrapper.sh
export VIRTUALENVWRAPPER_PYTHON=/Library/Frameworks/Python.framework/Versions/3.10/bin/python3
export VIRTUALENVWRAPPER_VIRTUALENV=/Library/Frameworks/Python.framework/Versions/3.10/bin/virtualenv
source /Library/Frameworks/Python.framework/Versions/3.10/bin/virtualenvwrapper.sh
```

保存文件回到控制台 输入 `source .zshrc`

此时配置文件已经更新完毕 输入 ``

这时虚拟环境已经创建完毕

### 3 虚拟环境相关命令

1. `mkvirtualenv -p python3 虚拟环境名称(自定义)`
2. `workon`  命令:列出虚拟环境列表
3. `workon 虚拟环境名称`  切换到某个虚拟环境
4. `deactivate`  退出虚拟环境
5. `rmvirtualenv 虚拟环境名称` 删除虚拟环境

### 4 使用`requeirments.txt`打包安装环境依赖(迁移环境)

- 导出环境依赖
  - `pip freeze > requeirments.txt`

- 使用导出的文件迁移环境
  - `pip install -r requeirments.txt`
