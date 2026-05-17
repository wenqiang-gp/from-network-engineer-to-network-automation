# 从传统网络工程师到网络自动化的真实踩坑记录

本仓库完整记录了一个传统网络运维工程师，从 0 开始学习 **网络自动化（Python + Netmiko + EVE-NG + Cisco）** 的真实全过程。

没有跳步骤，没有“理所当然”，全部是**真实报错、真实踩坑、真实解决**。

如果你是以下人群，这个仓库会非常有帮助：

- 正在学习 CCNA / CCNP，不知道如何结合自动化
- 会 Python，但不会连接真实网络设备
- 会网络设备，但不会 Python
- 正在从传统网工向自动化网工转型

---

## 实验环境

- VMware Workstation
- Ubuntu 24.04 LTS
- EVE-NG
- Cisco IOL L3 镜像
- Python venv 虚拟环境
- Netmiko

---

## 学到的核心能力

- VMware NAT / vmnet8 / pnet8 原理打通
- Ubuntu / EVE / Cisco 三者网络互通
- Cisco SSH、AAA、VTY、login local 的真实配置
- Python venv 正确使用（解决 externally-managed-environment）
- 使用 Netmiko 自动化配置真实路由器
- 理解 `send_config_set` 的工作原理
- 接口 IP overlap 的经典错误
- 用 EVE 日志验证 Python 推送配置

---

## 目录

| 文件 | 内容 |
|-----|------|
| 01-环境准备.md | VMware、Ubuntu、EVE 网络打通全过程 |
| 02-EVE搭建与SSH打通.md | Cisco SSH、AAA、VTY 配置与踩坑 |
| 03-Ubuntu+Python+venv踩坑.md | Python 环境与 Netmiko 安装全过程 |
| push_vlan.py | 第一个真正成功推送配置的脚本 |

---

## 最终效果

在 Ubuntu 中执行：

```bash
python push_vlan.py
