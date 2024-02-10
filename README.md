# alistStart

## 项目简介

该项目是一个用于启动 alist 服务的 Python 脚本，它可以检查当前目录下的配置文件来确定是否开启了开机启动功能，并相应地启动或停止 alist 服务。此外，它还提供了创建启动项快捷方式的功能。

## 安装

### 依赖

- Python 3.x
- pywin32 库（仅在 Windows 平台下需要，用于创建快捷方式）

### 打包步骤

1. 将项目文件下载到本地。
2. 确保已安装 Python 3.x。
3. 如果在 Windows 平台下使用，确保已安装 pywin32 库。
4. 在项目目录下运行 
`pyinstaller --onefile --noconsole .\alistStart.py`。


## 使用方法

1. 将 `alistStart.exe` 放置在与 `alist.exe`相同的目录下。
2. 双击运行脚本。
3. 初次运行时，脚本会自动创建 `alistStartConfig.json` 配置文件。
4. 脚本会根据选择将程序设为是否自动启动，并创建或删除相应的启动项快捷方式。

## 配置文件说明

在当前目录下，脚本会自动创建 `alistStartConfig.json` 配置文件用于存储开机启动功能的设置。配置文件格式如下：

```json
{
    "开机启动": "是"
}
