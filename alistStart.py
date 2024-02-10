import os
import json
import sys
import winshell

# 获取程序的绝对路径
program_path = sys.argv[0]
program_dir = os.path.dirname(program_path)

# 更改当前工作目录到程序所在目录
os.chdir(program_dir)

# 检查当前目录下是否存在alistStartConfig.json文件
config_file_path = os.path.join(program_dir, "alistStartConfig.json")
if not os.path.exists(config_file_path):
    # 如果文件不存在，则创建并添加默认选项
    with open(config_file_path, 'w', encoding='utf-8') as config_file:
        default_config = {
            "开机启动": "否"
        }
        json.dump(default_config, config_file, ensure_ascii=False, indent=4)

# 读取配置文件
with open(config_file_path, 'r', encoding='utf-8') as config_file:
    config = json.load(config_file)

# 输出配置信息（可选）
print("当前配置：", config)

# 根据配置决定命令
command = "alist.exe server"

if config.get("开机启动", "否") == "是":
    # 获取当前用户的启动文件夹路径
    startup_folder = winshell.startup()

    # 创建快捷方式
    shortcut_path = os.path.join(startup_folder, "alistStart.lnk")  # 快捷方式的路径
    target_exe_path = os.path.abspath(os.path.join(program_dir, "alistStart.exe"))  # alist.exe 的路径
    winshell.CreateShortcut(
        Path=shortcut_path,
        Target=target_exe_path,
        Description="Alist Server"  # 快捷方式的描述
    )

    print("已将快捷方式移动到启动文件夹:", startup_folder)
else:
    # 检查启动文件夹是否存在快捷方式，如果存在则删除
    startup_folder = winshell.startup()
    shortcut_path = os.path.join(startup_folder, "alistStart.lnk")
    if os.path.exists(shortcut_path):
        os.remove(shortcut_path)
        print("已删除启动文件夹中的快捷方式")
    else:
        print("启动文件夹中没有找到快捷方式")
    print("未启用开机启动")

# 执行命令
os.system(command)

input("按任意键退出...")
