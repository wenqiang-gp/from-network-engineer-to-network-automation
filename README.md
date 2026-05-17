# 从网络工程师到网络自动化（From Network Engineer to Network Automation）

> 一个纯实战记录：从手工敲命令，到用 Python 自动化管理 Cisco 设备的全过程。

作者：文强（wenqiang-gp）

---

## 📖 项目背景

在日常网络运维中，我们大量重复做这些事情：

- 登录设备
- 配 IP
- 开接口
- 创建 VLAN
- 排错
- 保存配置

当设备数量变多时，这些操作会变得：

> **枯燥、低效、容易出错、不可复用**

于是我开始学习：

- Python
- Netmiko
- 网络自动化思维

并在 EVE-NG 实验环境中，真实还原生产网络拓扑，完成自动化配置。

本仓库完整记录这个学习与实战过程。

---

## 🧪 实验环境

| 项目 | 环境 |
|-----|------|
| 虚拟化 | VMware |
| Linux | Ubuntu |
| 网络模拟 | EVE-NG |
| 设备 | Cisco Router / Switch |
| 自动化工具 | Python + Netmiko |

拓扑结构：
    Net
     |
    R3
  /    \
SW1    SW2

---

## 🎯 第一个自动化目标

使用 Python 自动完成以下配置：

- SSH 登录 R3
- 进入配置模式
- 配置两个接口 IP
- no shutdown
- 保存配置

---

## 🧠 关键踩坑（非常重要）

在真实实验中遇到的典型问题：

### ❌ enable 报错 `Error in authentication`
原因：没有正确配置本地用户与特权级别

### ❌ `login local` 无法使用
原因：没有创建 `username admin privilege 15 secret`

---

## ✅ 最终正确的 Python 自动化脚本

```python
from netmiko import ConnectHandler

device = {
    "device_type": "cisco_ios",
    "host": "192.168.66.130",
    "username": "admin",
    "password": "Admin@123",
}

commands = [
    "interface e0/1",
    "ip address 192.168.10.1 255.255.255.0",
    "no shutdown",
    "interface e0/2",
    "ip address 192.168.20.1 255.255.255.0",
    "no shutdown",
]

with ConnectHandler(**device) as conn:
    output = conn.send_config_set(commands)
    print(output)
