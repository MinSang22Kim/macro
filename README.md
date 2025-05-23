# Macro

나 쓸려고 간단하게 만든 매크로 자동화 도구 모음

---

1. **click.py** : 특정 위치를 빠르게 반복 클릭하는 매크로 도구

   ### 기능 설명
   - 초당 최대 50번 클릭
   - 랜덤 오프셋과 딜레이로 탐지 방지
   - GUI를 통해 클릭 위치 선택 및 재설정 가능
   - 마우스를 화면 모서리로 이동하면 자동 종료

   ### 사용 방법
   1. **라이브러리 설치**:
      ```bash
      pip install pyautogui tkinter
      ```

   2. **매크로 실행**:
      ```bash
      python click.py
      ```
      - 실행 후 클릭 위치를 선택 후 "시작" 버튼 클릭
      - 중단하려면 마우스를 화면 모서리로 이동

   ### 구성 요소
   - `pyautogui`: 클릭 실행 및 위치 감지.
   - `tkinter`: GUI 제공 (시작/재설정 버튼 및 팝업).
