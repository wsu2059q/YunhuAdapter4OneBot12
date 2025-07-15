# 云湖平台事件转换模块 (YunhuAdapter4OneBot12)

## 功能概述
本模块用于将云湖(即时通讯平台)的事件数据转换为标准的OneBot12格式。支持消息、通知等多种事件类型

## 安装方法
```bash
pip install yunhu2onebot12
```

## 使用方法
### 基本使用
```python
from yunhu2onebot12 import Converter

# 创建转换器实例
converter = Converter()

# 云湖平台原始事件数据
yunhu_event = {
    "version": "1.0",
    "header": {
        "eventId": "c192ccc83d5147f2859ca77bcfafc9f9",
        "eventType": "message.receive.normal",
        "eventTime": 1748613099002
    },
    "event": {
        # ... 事件数据 ...
    }
}

# 转换为OneBot12格式
onebot_event = converter.convert(yunhu_event)
```

## 支持的事件类型
| 云湖事件类型 | 
|-------------| 
| message.receive.normal | 
| message.receive.instruction | 
| bot.followed | 
| bot.unfollowed | 
| group.join | 
| group.leave | 
| button.report.inline | 
| bot.shortcut.menu | 

## 消息类型支持
支持以下内容类型的消息转换：
- 文本(text)
- 图片(image)
- 视频(video)
- 文件(file)
- 表单指令(form)

## 特殊字段处理
部分云湖特有字段会在转换后的OneBot事件中以`yunhu_`前缀的非标准字段形式保留：
- `yunhu_form`: 表单类型指令数据
- `yunhu_button`: 按钮相关数据
- `yunhu_menu`: 快捷菜单数据

## 错误处理
- 如果传入不支持的事件类型，方法会返回`None`
- 当事件数据格式错误时会抛出`ValueError`

## 注意事项
1. 使用 Python 3.7 及更高版本
2. 本模块仅处理事件格式转换，不包含网络通信功能
3. 云湖特有字段在OneBot12标准中可能不被其他组件识别
4. 表单消息/按钮/快捷菜单 事件是云湖平台特有功能，转换后会添加`yunhu_`前缀
