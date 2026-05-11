edge_esp32/
├── lib/                        # 核心阵地：存放你们各自独立封装的组件
│   ├── motor_control/          # 同学 A 的工作区：运动底座封装
│   │   ├── motor.h             # 声明对外暴露的接口（如 Motor_Init, Motor_Forward）
│   │   └── motor.c             # 具体的 PWM 驱动代码和私有逻辑
│   │
│   └── ir_sensor/              # 同学 B 的工作区：红外传感器封装
│       ├── ir_sensor.h         # 声明对外暴露的接口（如 IR_Init, 状态读取或中断声明）
│       └── ir_sensor.c         # 具体的 GPIO 配置和硬件中断函数
│
├── include/                    # 全局配置区：存放整个工程的公共头文件
│   └── pin_config.h            # ★ 极其重要：全量引脚分配表
│
├── src/                        # 调度中心：主业务逻辑
│   └── main.c                  # 在这里引入 motor.h 和 ir_sensor.h，将两者联动
│
└── platformio.ini              # 编译配置文件 (如果你们使用 VS Code + PlatformIO)