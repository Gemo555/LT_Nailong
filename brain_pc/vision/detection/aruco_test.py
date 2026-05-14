import cv2
import numpy as np

def main():
    # 1. 打开本地摄像头 (0通常代表电脑自带摄像头)
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("❌ 无法打开摄像头，请检查摄像头是否被其他程序占用！")
        return

    print("✅ 摄像头已就绪！请将手机屏幕上的 ArUco 标签对准镜头。")
    print("👉 按下英文小写 'q' 键可关闭窗口。")

    # 2. 准备 ArUco 字典和检测器 (适配最新版 OpenCV 语法)
    dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)
    parameters = cv2.aruco.DetectorParameters()
    detector = cv2.aruco.ArucoDetector(dictionary, parameters)

    # 3. 进入视觉流死循环
    last_ids = set()

    while True:
        # 逐帧读取画面
        ret, frame = cap.read()
        if not ret:
            print("⚠️ 无法获取画面帧")
            break

        # 核心检测：找出画面里的所有 ArUco 标签
        corners, ids, rejected = detector.detectMarkers(frame)
        current_ids = set(ids.flatten()) if ids is not None else set()

        if ids is not None:
            # 1. 先画官方的绿框
            cv2.aruco.drawDetectedMarkers(frame, corners, ids)

            # 2. 遍历每一个检测到的标签，计算并画出中心点
            for marker_corners in corners:
                # marker_corners 的形状是 (1, 4, 2)
                # 我们取 [0] 得到那 4 个点的数组 (4, 2)
                points = marker_corners[0]

                # 计算 4 个点的平均值
                # np.mean(points, axis=0) 会分别计算 x 列和 y 列的平均值
                center = np.mean(points, axis=0)
                cx, cy = int(center[0]), int(center[1])

                # 3. 在中心点画一个红色的实心圆
                # 参数：画布, (x, y), 半径, 颜色(BGR), -1表示实心
                cv2.circle(frame, (cx, cy), 2, (0, 0, 255), -1)
                
                # 可选：在中心点旁边显示一下坐标数值
                #cv2.putText(frame, f"({cx},{cy})", (cx + 10, cy), 
                #cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)  

        # 如果检测到了标签变更，就在画面上画出绿框和 ID
        if current_ids != last_ids:
            if len(current_ids) > 0:
                print(f"✨ 检测到标签变化，当前看到: {list(current_ids)}")
            else:
                print("💨 目标丢失：当前画面无有效标签")    
            
            last_ids = current_ids


        # 显示实时画面
        cv2.imshow("TwinMind-Desk: Vision Test", frame)

        # 监听键盘，按下 'q' 键退出
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("🛑 视觉测试已手动退出。")
            break

    # 释放资源
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()