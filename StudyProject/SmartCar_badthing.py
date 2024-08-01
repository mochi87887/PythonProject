# https://makecode.microbit.org/#editor
# 2024/7/30 協助修改智能行走車程式碼


# 初始化距離感測器和馬達
# 初始化左、右和中的距離感測器
sonarbit.sonarbit_distance(Distance_Unit.DISTANCE_UNIT_MM, DigitalPin.P0) # 左
sonarbit.sonarbit_distance(Distance_Unit.DISTANCE_UNIT_MM, DigitalPin.P8) # 右
sonarbit.sonarbit_distance(Distance_Unit.DISTANCE_UNIT_MM, DigitalPin.P15) # 中
# 停止所有馬達
wuKong.stop_all_motor()
# 初始化距離變數
DIS_left = 0
DIS_right = 0
DIS_mid = 0

# 定義中間檢測函數
def mid_detect():
    global DIS_left, DIS_right, DIS_mid
    # 讀取左、右和中的距離，並將其轉換為公分
    DIS_left = sonarbit.sonarbit_distance(Distance_Unit.DISTANCE_UNIT_MM, DigitalPin.P0) / 10
    DIS_right = sonarbit.sonarbit_distance(Distance_Unit.DISTANCE_UNIT_MM, DigitalPin.P8) / 10
    DIS_mid = sonarbit.sonarbit_distance(Distance_Unit.DISTANCE_UNIT_MM, DigitalPin.P15) / 10
    # 暫停1秒
    basic.pause(1000)

    # 顯示 "straight" 並設置馬達速度為20
    OLED12864_I2C.show_string(0, 1, "straight", 1)
    wuKong.set_all_motor(20, 20)
    
    # 如果左邊距離小於右邊且小於10公分
    if DIS_left < DIS_right and DIS_left < 10:
        # 停止所有馬達，顯示 "RIGHT"，並設置右轉
        wuKong.stop_all_motor()
        OLED12864_I2C.show_string(0, 0, "RIGHT", 1)
        wuKong.set_all_motor(30, 0)
        # 暫停3秒
        basic.pause(3000)
    
    # 如果右邊距離小於左邊且小於10公分
    elif DIS_left > DIS_right and DIS_right < 10:
        # 停止所有馬達，顯示 "LEFT"，並設置左轉
        wuKong.stop_all_motor()
        OLED12864_I2C.show_string(0, 0, "LEFT", 1)
        wuKong.set_all_motor(0, 30)
        # 暫停3秒
        basic.pause(3000)
    
    # 否則，保持直行
    else:
        # 停止所有馬達，顯示 "straight"，並設置馬達速度為20
        wuKong.stop_all_motor()
        OLED12864_I2C.show_string(0, 1, "straight", 1)
        wuKong.set_all_motor(20, 20)
        
    # 清除顯示
    OLED12864_I2C.clear()

# 設置 mid_detect 函數為永久執行
basic.forever(mid_detect)