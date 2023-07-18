# edge-starter
针对**n2n**的边缘节点linux启动服务

---

## 安装准备
首先需要在系统内安装**n2n**，并且配置开启**n2n**服务，相关介绍直接看[n2n github项目](https://github.com/ntop/n2n)

系统必须有python3环境，pip以及setuptools

## 安装
直接clone该仓库，选取你所需要的版本，执行
```shell
sudo python setup.py install
```
即可完成安装

## 使用
在使用之前需要对配置文件进行修改，配置文件一般位于 ***/usr/etc/start-edge/config.json*** ，配置选项很简单，直接编辑即可，代码中会自动生成随机的tap设备mac地址，之前碰到n2n的tap设备mac地址与上报不符导致网络无法连通，通过手动指定后可解决，不知新版本是否解决。

配置完成后通过
```shell
sudo systemctl start start-edge.service
```
可启动服务，如果需要开机启动，则执行
```shell
sudo systemctl enable start-edge.service
```
即可
