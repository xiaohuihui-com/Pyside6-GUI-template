# Pyside6_GUI_Template

---
## 模板介绍
- 模板基于PySide6框架，实现了MVC架构，并使用PyQtDesigner设计了用户界面。
- 模板提供了一种快速开发GUI应用的方式，并支持多种主题切换。
- 模板提供了多种主题切换功能，包括浅色和深色两种模式。

## 模板目录结构
```shell
Pyside6-template
├── config # 应用配置相关文件
│   └── config.py  
├── controllers # MVC 中的控制器组件
│   └── controller_main.py
├── models # MVC 中的模型组件，处理数据逻辑
├── resources # UI 资源，如图标、图片、主题样式等
│   ├── icons
│   ├── images
│   ├── svgs
│   ├── themes
│   ├── resources.qrc
│   └── resources_rc.py
├── ui # 用户界面文件
│   ├── ui_components
│   │   ├── animations.py
│   │   └── ui_setup.py
│   ├── ui_designs
│   │   ├── login.ui
│   │   ├── main.ui
│   │   ├── ui_login.py
│   │   └── ui_main.py
├── views # MVC 中的视图组件，用户界面文件
│   ├── widgets
│   │   ├── login_window.py
│   │   └── main_window.py
│   └── view_main.py
├── README.md
├── app.py
└── requirements.txt
```

## 项目部署

1. 拉取项目模板代码：
```shell
git clone https://kkgithub.com/xiaohuihui-com/Pyside6-GUI-template.git
```
2. 安装依赖：
```shell
cd Pyside6-GUI-template
pip install -r requirements.txt
```
3. 运行项目：
```shell
python app.py
```
4. 打包项目：
```shell
# linux
sh nuitka_linux_standalone.sh
# windows
sh nuitka_windows_standalone.sh
```
