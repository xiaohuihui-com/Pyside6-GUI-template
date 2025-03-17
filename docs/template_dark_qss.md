
# QSS介绍

---
QSS（Qt Style Sheet）是一种用于定义Qt应用程序外观的样式表语言。

# 组件

---
- 全局
  - 设置所有QWidget的默认文本颜色和字体
  - 设置工具提示的样式
  - 设置应用背景的样式
- 左侧
  - 设置左侧菜单背景的样式
  - 设置顶部logo的样式
  - 设置左侧标题的样式
  - 设置左侧描述的样式
  - 设置左侧菜单框架的样式
- 顶部
  - 设置顶部菜单按钮的样式
  - 设置顶部菜单按钮悬停状态的样式
  - 设置顶部菜单按钮按压状态的样式
- 底部
  - 设置底部菜单按钮的样式
  - 设置底部菜单按钮悬停状态的样式
  - 设置底部菜单按钮按压状态的样式


- 工具提示
```qt style sheet
/* 设置工具提示的样式 */
QToolTip {
	color: #ffffff; /* 文本颜色为白色 */
	background-color: rgba(33, 37, 43, 180); /* 背景颜色为深灰色，带有透明度 */
	border: none; /* 去掉边框 */
	border-left: 2px solid rgb(255, 121, 198); /* 左侧边框为紫色 */
	text-align: left; /* 文本左对齐 */
	padding-left: 8px; /* 内左边距为8像素 */
	margin: 0px; /* 外边距为0 */
}
```
- 表格
```qt style sheet

/* 设置表格的样式 */
QTableWidget {
	background-color: transparent; /* 背景透明 */
	padding: 10px; /* 内边距为10像素 */
	border-radius: 5px; /* 圆角半径为5像素 */
	gridline-color: rgb(44, 49, 58); /* 网格线条颜色为深灰色 */
	border-bottom: 1px solid rgb(44, 49, 60); /* 下方边框为深灰色 */
}
/* 设置表格项的样式 */
QTableWidget::item{
	border-color: rgb(44, 49, 60); /* 单元格边框颜色为深灰色 */
	padding-left: 5px; /* 内左边距为5像素 */
	padding-right: 5px; /* 内右边距为5像素 */
	gridline-color: rgb(44, 49, 60); /* 网格线条颜色为深灰色 */
}
/* 设置选中的表格项的样式 */
QTableWidget::item:selected{
	background-color: rgb(189, 147, 249); /* 背景颜色为紫色 */
}
/* 设置表头部分的样式 */
QHeaderView::section{
	background-color: rgb(33, 37, 43); /* 背景颜色为深灰色 */
	max-width: 30px; /* 最大宽度为30像素 */
	border: 1px solid rgb(44, 49, 58); /* 边框为深灰色 */
	border-style: none; /* 去掉边框样式 */
    border-bottom: 1px solid rgb(44, 49, 60); /* 下方边框为深灰色 */
    border-right: 1px solid rgb(44, 49, 60); /* 右侧边框为深灰色 */
}
/* 设置水平表头的样式 */
QTableWidget::horizontalHeader {
	background-color: rgb(33, 37, 43); /* 背景颜色为深灰色 */
}
/* 设置水平表头部分的样式 */
QHeaderView::section:horizontal
{
    border: 1px solid rgb(33, 37, 43); /* 边框为深灰色 */
	background-color: rgb(33, 37, 43); /* 背景颜色为深灰色 */
	padding: 3px; /* 内边距为3像素 */
	border-top-left-radius: 7px; /* 左上圆角半径为7像素 */
    border-top-right-radius: 7px; /* 右上圆角半径为7像素 */
}
/* 设置垂直表头部分的样式 */
QHeaderView::section:vertical
{
    border: 1px solid rgb(44, 49, 60); /* 边框为深灰色 */
}
```
- 输入框
```qt style sheet

/* 设置输入框的样式 */
QLineEdit {
	background-color: rgb(33, 37, 43); /* 背景颜色为深灰色 */
	border-radius: 5px; /* 圆角半径为5像素 */
	border: 2px solid rgb(33, 37, 43); /* 边框为深灰色 */
	padding-left: 10px; /* 内左边距为10像素 */
	selection-color: rgb(255, 255, 255); /* 选中文本颜色为白色 */
	selection-background-color: rgb(255, 121, 198); /* 选中文本背景颜色为紫色 */
}
/* 设置输入框悬停状态的样式 */
QLineEdit:hover {
	border: 2px solid rgb(64, 71, 88); /* 边框颜色变为较亮的灰色 */
}
/* 设置输入框获取焦点状态的样式 */
QLineEdit:focus {
	border: 2px solid rgb(91, 101, 124); /* 边框颜色变为更深的灰色 */
}
```
- 多行文本编辑器
```qt style sheet

/* 设置多行文本编辑器的样式 */
QPlainTextEdit {
	background-color: rgb(27, 29, 35); /* 背景颜色为更深的灰色 */
	border-radius: 5px; /* 圆角半径为5像素 */
	padding: 10px; /* 内边距为10像素 */
	selection-color: rgb(255, 255, 255); /* 选中文本颜色为白色 */
	selection-background-color: rgb(255, 121, 198); /* 选中文本背景颜色为紫色 */
}
/* 设置多行文本编辑器垂直滚动条的样式 */
QPlainTextEdit  QScrollBar:vertical {
    width: 8px; /* 宽度为8像素 */
 }
/* 设置多行文本编辑器水平滚动条的样式 */
QPlainTextEdit  QScrollBar:horizontal {
    height: 8px; /* 高度为8像素 */
 }
/* 设置多行文本编辑器悬停状态的样式 */
QPlainTextEdit:hover {
	border: 2px solid rgb(64, 71, 88); /* 边框颜色变为较亮的灰色 */
}
/* 设置多行文本编辑器获取焦点状态的样式 */
QPlainTextEdit:focus {
	border: 2px solid rgb(91, 101, 124); /* 边框颜色变为更深的灰色 */
}
```
- 水平滚动条
```qt style sheet

/* 设置水平滚动条的样式 */
QScrollBar:horizontal {
    border: none; /* 去掉边框 */
    background: rgb(52, 59, 72); /* 背景颜色为深灰色 */
    height: 8px; /* 高度为8像素 */
    margin: 0px 21px 0 21px; /* 外边距为0像素，左右各21像素 */
	border-radius: 0px; /* 不带圆角 */
}
/* 设置水平滚动条手柄的样式 */
QScrollBar::handle:horizontal {
    background: rgb(189, 147, 249); /* 背景颜色为紫色 */
    min-width: 25px; /* 最小宽度为25像素 */
	border-radius: 4px /* 圆角半径为4像素 */
}
/* 设置水平滚动条增加按钮的样式 */
QScrollBar::add-line:horizontal {
    border: none; /* 去掉边框 */
    background: rgb(55, 63, 77); /* 背景颜色为深灰色 */
    width: 20px; /* 宽度为20像素 */
	border-top-right-radius: 4px; /* 右上圆角半径为4像素 */
    border-bottom-right-radius: 4px; /* 右下圆角半径为4像素 */
    subcontrol-position: right; /* 子控件位置在右侧 */
    subcontrol-origin: margin; /* 子控件原点在外边距 */
}
/* 设置水平滚动条减少按钮的样式 */
QScrollBar::sub-line:horizontal {
    border: none; /* 去掉边框 */
    background: rgb(55, 63, 77); /* 背景颜色为深灰色 */
    width: 20px; /* 宽度为20像素 */
	border-top-left-radius: 4px; /* 左上圆角半径为4像素 */
    border-bottom-left-radius: 4px; /* 左下圆角半径为4像素 */
    subcontrol-position: left; /* 子控件位置在左侧 */
    subcontrol-origin: margin; /* 子控件原点在外边距 */
}
/* 设置水平滚动条上下箭头的样式 */
QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal
{
     background: none; /* 背景透明 */
}
/* 设置水平滚动条增加和减少页面的样式 */
QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal
{
     background: none; /* 背景透明 */
}
```
- 垂直滚动条
```qt style sheet
/* 设置垂直滚动条的样式 */
 QScrollBar:vertical {
	border: none; /* 去掉边框 */
    background: rgb(52, 59, 72); /* 背景颜色为深灰色 */
    width: 8px; /* 宽度为8像素 */
    margin: 21px 0 21px 0; /* 外边距为21像素，上下各21像素 */
	border-radius: 0px; /* 不带圆角 */
 }
/* 设置垂直滚动条手柄的样式 */
 QScrollBar::handle:vertical {
	background: rgb(189, 147, 249); /* 背景颜色为紫色 */
    min-height: 25px; /* 最小高度为25像素 */
	border-radius: 4px /* 圆角半径为4像素 */
 }
/* 设置垂直滚动条增加按钮的样式 */
 QScrollBar::add-line:vertical {
     border: none; /* 去掉边框 */
    background: rgb(55, 63, 77); /* 背景颜色为深灰色 */
     height: 20px; /* 高度为20像素 */
	border-bottom-left-radius: 4px; /* 左下圆角半径为4像素 */
    border-bottom-right-radius: 4px; /* 右下圆角半径为4像素 */
     subcontrol-position: bottom; /* 子控件位置在下方 */
     subcontrol-origin: margin; /* 子控件原点在外边距 */
 }
/* 设置垂直滚动条减少按钮的样式 */
 QScrollBar::sub-line:vertical {
	border: none; /* 去掉边框 */
    background: rgb(55, 63, 77); /* 背景颜色为深灰色 */
     height: 20px; /* 高度为20像素 */
	border-top-left-radius: 4px; /* 左上圆角半径为4像素 */
    border-top-right-radius: 4px; /* 右上圆角半径为4像素 */
     subcontrol-position: top; /* 子控件位置在上方 */
     subcontrol-origin: margin; /* 子控件原点在外边距 */
 }
/* 设置垂直滚动条上下箭头的样式 */
 QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {
     background: none; /* 背景透明 */
 }

/* 设置垂直滚动条增加和减少页面的样式 */
 QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
     background: none; /* 背景透明 */
 }

```
- 复选框
```qt style sheet

/* 设置复选框指示器的样式 */
QCheckBox::indicator {
    border: 3px solid rgb(52, 59, 72); /* 边框为深灰色 */
	width: 15px; /* 宽度为15像素 */
	height: 15px; /* 高度为15像素 */
	border-radius: 10px; /* 圆角半径为10像素 */
    background: rgb(44, 49, 60); /* 背景颜色为更深的灰色 */
}
/* 设置复选框指示器悬停状态的样式 */
QCheckBox::indicator:hover {
    border: 3px solid rgb(58, 66, 81); /* 边框颜色变为更亮的灰色 */
}
/* 设置复选框指示器选中状态的样式 */
QCheckBox::indicator:checked {
    background: 3px solid rgb(52, 59, 72); /* 背景颜色为深灰色 */
	border: 3px solid rgb(52, 59, 72); /* 边框颜色为深灰色 */
	background-image: url(:/icons/icons/cil-check-alt.png); /* 使用勾选图标 */
}
```
- 单选按钮
```qt style sheet

/* 设置单选按钮指示器的样式 */
QRadioButton::indicator {
    border: 3px solid rgb(52, 59, 72); /* 边框为深灰色 */
	width: 15px; /* 宽度为15像素 */
	height: 15px; /* 高度为15像素 */
	border-radius: 7px; /* 圆角半径为7像素 */
    background: rgb(44, 49, 60); /* 背景颜色为更深的灰色 */
}
/* 设置单选按钮指示器悬停状态的样式 */
QRadioButton::indicator:hover {
    border: 3px solid rgb(58, 66, 81); /* 边框颜色变为更亮的灰色 */
}
/* 设置单选按钮指示器选中状态的样式 */
QRadioButton::indicator:checked {
    background: 3px solid rgb(189, 147, 249); /* 背景颜色为紫色 */
	border: 3px solid rgb(52, 59, 72); /* 边框颜色为深灰色 */
}
```

