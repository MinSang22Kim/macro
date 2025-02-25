import pyautogui
import tkinter as tk
import threading
import time
import random

pyautogui.PAUSE = 0  # PyAutoGUI의 기본 딜레이 제거

# 10분에 500번 클릭하는 매크로

# 화면 중앙에 창 위치 계산
def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")

# 사용자에게 클릭할 위치를 선택받아 반환
def select_click_position():
    print("매크로 시작할 위치 좌표를 선택하세요...")
    time.sleep(2)
    position = pyautogui.position()  # 마우스 위치 가져오기
    print(f"선택된 좌표: {position}")
    return position

# 선택된 위치를 반복적으로 클릭
def run_macro(click_position, interval=0.002, stop_event=None):
    print("매크로 실행 중... 마우스를 화면 모서리로 이동하면 종료됩니다.")
    screen_width, screen_height = pyautogui.size()

    while not stop_event.is_set():
        # 랜덤 위치 생성
        random_x = click_position[0] + random.randint(-30, 30)  # X축으로 ±30 픽셀
        random_y = click_position[1] + random.randint(-30, 30)  # Y축으로 ±30 픽셀

        # 현재 마우스 위치 확인
        mouse_x, mouse_y = pyautogui.position()
        if mouse_x in (0, screen_width - 1) or mouse_y in (0, screen_height - 1):
            print("마우스가 화면 모서리에 위치했습니다. 매크로를 종료합니다.")
            stop_event.set()
            break

        # 클릭 실행
        pyautogui.click(x=random_x, y=random_y)

        # 랜덤 딜레이 추가
        random_delay = interval + random.uniform(-0.0005, 0.0005)
        time.sleep(random_delay)

# 매크로 시작 및 재설정 버튼을 띄우는 팝업창
def show_start_and_reset_buttons(callback_start, callback_reset):
    root = tk.Tk()
    root.title("매크로 설정")
    center_window(root, 300, 150)  # 중앙 배치

    root.geometry("400x100") # 너비 400, 높이 200

    label = tk.Label(root, text="원하는 작업을 선택하세요.")
    label.pack(pady=10)

    button_frame = tk.Frame(root)
    button_frame.pack(pady=10)

    start_button = tk.Button(button_frame, text="시작!", command=lambda: (callback_start(), root.destroy()))
    start_button.grid(row=0, column=0, padx=10)

    reset_button = tk.Button(button_frame, text="재설정", command=lambda: (callback_reset(), root.destroy()))
    reset_button.grid(row=0, column=1, padx=10)

    root.mainloop()

if __name__ == "__main__":
    # 전역 변수로 클릭 위치 선언
    click_position = select_click_position()

    # 종료 이벤트 생성
    stop_event = threading.Event()

    while True:
        # 매크로 실행 준비 (시작 및 재설정 버튼)
        def start_macro():
            print("매크로 시작 버튼 클릭됨.")
            macro_thread = threading.Thread(target=run_macro, args=(click_position, 0.005, stop_event))
            macro_thread.start()
            macro_thread.join()
            print("매크로가 종료되었습니다.")

        def reset_macro():
            global click_position
            click_position = select_click_position()
            print("클릭 위치가 재설정되었습니다.")

        show_start_and_reset_buttons(start_macro, reset_macro)

        if stop_event.is_set():
            break
