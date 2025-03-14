# Pyside6_GUI_Template

---
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