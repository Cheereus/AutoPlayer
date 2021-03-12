# AutoPlayer
A Qt Application which can automatically play video, PPT, word

基于 PyQt5 的多媒体自动播放图形化界面

## 主要功能

视频、PPT、Word、PDF 文件在自定义时段进行自动化播放：

* 队列播放：选择多个文件，在一定时段内循环播放

* 分时播放：选择多个文件，在不同时段内循环播放不同的文件

## 依赖

* PyQt5

* python-pptx

* 需要安装 K-Lite Codec Pack 作为视频播放器

## 运行

```shell
python Main.py
```

## 打包为 `exe` 文件

```shell
pyinstaller -F Main.py -i icon.ico -n AutoPlayer
```

