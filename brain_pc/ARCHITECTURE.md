brain_pc/
├── core/                   # 逻辑中枢（Agent 决策、API 调用）
├── vision/                 # ★ 视觉模块主阵地
│   ├── assets/             # 存放 ArUco 字典图片、标定用棋盘格图片
│   ├── calibration/        # 相机标定脚本（用于去除镜头畸变）
│   ├── detection/          # 目标检测与 ArUco 识别脚本
│   ├── mapping/            # 坐标变换与单应性矩阵算法
│   └── main_vision.py      # 视觉模块的主入口
├── requirements.txt        # 记录 Python 依赖库
└── config.yaml             # 存放相机参数、ArUco ID 等配置
