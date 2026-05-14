```text
edge_esp32/
├── lib/                        # 存放独立封装的组件
│   ├── motor_control/          # 运动底座封装工作区
│   │   ├── motor.h             # 声明对外暴露的接口（如 Motor_Init）
│   │   └── motor.c             # 具体的 PWM 驱动代码和私有逻辑
│   │
│   └── ir_sensor/              # 红外传感器封装工作区
│       ├── ir_sensor.h         # 声明对外暴露的接口
│       └── ir_sensor.c         # 具体的 GPIO 配置和硬件中断函数
│
├── include/                    # 全局配置区：存放整个工程的公共头文件
│   └── pin_config.h            # ★ 极其重要：全量引脚分配表
│
├── src/                        # 调度中心：主业务逻辑
│   └── main.c                  # 在这里引入 motor.h 和 ir_sensor.h
│
└── platformio.ini              # 编译配置文件edge_esp32/
