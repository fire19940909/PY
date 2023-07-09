import time
from pynput.keyboard import Controller, Key
import tkinter as tk
import pygetwindow as gw

def simulate_keyboard_input():
    key = entry_key.get()
    press_count = int(entry_press_count.get())
    press_duration = float(entry_press_duration.get())
    interval = float(entry_interval.get())

    # 尋找指定視窗程式
    target_window = gw.getWindowsWithTitle(entry_window.get())
    if len(target_window) == 0:
        print("找不到指定的視窗程式")
        return

    # 取得目標視窗的處理程序
    handle = target_window[0].handle

    # 設定輸入結構體
    inputs = (INPUT * 2)()

    # 模擬按壓
    for _ in range(press_count):
        # 按下鍵位
        inputs[0].type = INPUT_KEYBOARD
        inputs[0].union = ctypes.pointer(KEYBDINPUT(key, 0, 0, 0, None))
        user32.SendInput(1, ctypes.pointer(inputs), ctypes.sizeof(INPUT))

        # 延遲一段時間
        time.sleep(press_duration)

        # 釋放鍵位
        inputs[1].type = INPUT_KEYBOARD
        inputs[1].union = ctypes.pointer(KEYBDINPUT(key, 0, KEYEVENTF_KEYUP, 0, None))
        user32.SendInput(1, ctypes.pointer(inputs[1]), ctypes.sizeof(INPUT))

        # 延遲按壓間隔
        time.sleep(interval)

# 建立視窗
window = tk.Tk()
window.title("模擬鍵盤訊號")
window.geometry("300x300")

# 視窗程式輸入框
label_window = tk.Label(window, text="視窗程式名稱：")
label_window.pack()
entry_window = tk.Entry(window)
entry_window.pack()

# 鍵位輸入框
label_key = tk.Label(window, text="鍵位：")
label_key.pack()
entry_key = tk.Entry(window)
entry_key.pack()

# 按壓次數輸入框
label_press_count = tk.Label(window, text="按壓次數：")
label_press_count.pack()
entry_press_count = tk.Entry(window)
entry_press_count.pack()

# 按壓時間輸入框
label_press_duration = tk.Label(window, text="每次按壓時間（秒）：")
label_press_duration.pack()
entry_press_duration = tk.Entry(window)
entry_press_duration.pack()

# 間隔時間輸入框
label_interval = tk.Label(window, text="每次按壓間隔（秒）：")
label_interval.pack()
entry_interval = tk.Entry(window)
entry_interval.pack()

# 模擬按鈕
button_simulate = tk.Button(window, text="模擬鍵盤訊號", command=simulate_keyboard_input)
button_simulate.pack()

# 啟動視窗主迴圈
window.mainloop()
