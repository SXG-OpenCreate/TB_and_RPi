
# VSCODE執行Python, 環境設定
1. 安裝VSCODE
2. 開啟VSODE內安裝插件 pyhton
   1. 開啟vscode軟體
   2. 畫面左側 點擊Extensions, 搜尋Python插件&安裝
3. pc主機安裝 python
4. vscode 內選擇python版本(選第3項安裝的版本&路徑)
    1. 開啟vscode
    2. 快捷鍵 ctrl+shift+p (Command Palette..)
    3. python: Select Interpreter
    4. 選第3項安裝的python版本&路徑
5. 安裝python虛擬環境
    1. 快捷鍵 ctrl+shift+p (Command Palette..)
    2. python: Creat Termina (開啟終端機視窗)
    3. 在終端機內 輸入pip install virtualenv (安裝virtualenv插件)
    4. 在vscode 上面菜單打開或新增資料夾(專案資夾)
    5. python: Creat Termina (開啟終端機視窗)
    6. 此時終端機路徑應該在專案資料夾底下
    7. 在終端機輸入virtualenv .venv
    8. 此時vscode 左側 專案資料夾底 應該會出現.venv的資料夾
    9. 在終端機視窗右上 點擊關閉終端機
    10. 切換到虛擬環境 
        1. 快捷鍵 ctrl+shift+p (Command Palette..)
        2. 選有python...('.venv':venv)... 這個版本
6. 測試虛擬環境
    1. 快捷鍵 ctrl+shift+p (Command Palette..)
    2. python: Creat Termina (開啟終端機視窗)
    3 .在終端機輸入 pip install paho-mqtt (安裝mqtt插件)
    4. 在vscode 左側專案資料夾內的.venv/lib 會看到剛安裝的paho, 點開paho 會看到mqtt
7. 重置虛擬環境
    1. 刪除.venv資料夾 
    2. 手動右鍵刪除 或 終端機輸入 rm -rf .venv
    3. 5.7項 再重做一次 建立新的 .venv
