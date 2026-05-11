# Desktop-Agent: 基于大小脑协同架构的桌面智能体系统

[![Board](https://img.shields.io/badge/Hardware-ESP32--S3-orange)](https://www.espressif.com/)
[![LLM](https://img.shields.io/badge/Brain-DeepSeek--V3-blue)](https://www.deepseek.com/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

> **让桌面拥有“生命”：一种基于纯视觉降维打击与大模型驱动的桌面管理/开发辅助机器人。**

本项目旨在通过 **ESP32-S3 (小脑)** 与 **PC/算力平台 (大脑)** 的分布式协同，构建一个无需昂贵激光雷达、仅凭视觉即可实现高精度定位与逻辑推理的桌面级 AI Agent。

---

## 🛠️ 系统架构 (System Architecture)

系统采用“感知-决策-执行”的分层解耦设计，实现边缘侧的高实时性与云端的深度智能。

### 1. 小脑端 (Cerebellum: Edge Layer)
* **核心硬件**：ESP32-S3 系列 (支持 AI 扩展指令集)
* **职责**：
    * **实时交互**：离线语音唤醒引擎，毫秒级响应唤醒词。
    * **感知推流**：实时视频流采集与边缘推流。
    * **安全屏障**：硬件级防坠、防撞传感器融合，确保底层绝对安全。
    * **动作执行**：接收大脑指令，完成高精度底盘移动或云台指向。

### 2. 大脑端 (Cerebrum: Intel Layer)
* **核心环境**：Python 3.10+ / PyTorch / OpenCV
* **职责**：
    * **视觉中枢**：基于单应性变换（Homography）的 Mapless 定位，构建桌面 2D 绝对坐标系。
    * **多模态推理**：调用 DeepSeek 等多模态接口，将视觉场景转化为 Agent 决策指令。
    * **数据策略**：滚动缓冲（Rolling Buffer）机制，平衡实时算力负载与存储压力。

---

## 🚀 核心底层能力 (Core Capabilities)

### 📍 纯视觉空间映射 (Mapless Localization)
通过在桌面四角部署 **ArUco 标签**，利用线性代数中的单应性矩阵（Homography Matrix）将倾斜广角画面映射为标准的二维笛卡尔坐标系，实现毫米级的桌面绝对定位，实现对昂贵导航硬件的“降维打击”。

### 🎤 空间声场感知 (DOA & TDOA)
支持麦克风阵列的时间差（TDOA）算法。当用户呼唤机器人时，系统能捕捉声源方位并实现“转头”对准呼唤者，增强交互的自然感与沉浸感。

---

## 💡 顶层应用场景 (Use Cases)

### 3.1 方向 A：嵌入式 UI 视觉自动化纠错
* **场景描述**：充当开发者的“物理验证员”，解决代码生成与实际硬件表现不一致的问题。
* **业务逻辑**：摄像头监控外接屏幕 UI 表现，大脑提取图像特征并与预期代码逻辑比对。一旦发现渲染异常，自动截屏并生成详细报错报告，实现“开发-测试-报错-修复”的全自动闭环。

### 3.2 方向 B：桌面空间管理与“版本控制” (Desk Entropy Control)
* **核心概念**：**Desk Git（桌面版本管理）**。
* **业务逻辑**：
    * **Base Commit**：将整洁桌面记录为初始基准矩阵。
    * **Matrix Diff**：通过巡检识别物品的位移残差，精准识别异常位移。
    * **离座提醒**：当监控到用户起身离开时，结合 DeepSeek 生成自然语言，主动播报需归位的物品清单，抑制桌面熵增。

---

## 📦 技术栈 (Tech Stack)

* **固件开发**: C (ESP-IDF) / FreeRTOS
* **视觉处理**: OpenCV, ArUco Marker Detection, Homography Mapping
* **深度学习**: PyTorch (MLP/Neural Network), DeepSeek-V3 API
* **通信协议**: WebSocket / MQTT
* **工作流**: Vibe Coding (Claude Code / API Proxies)

