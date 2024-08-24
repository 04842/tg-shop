文件
警告

首先，請注意，這個機器人是一個概念驗證！
如果您使用它，我們不提供任何保證，包括支援保證，因此在現實世界中使用它需要您自擔風險！

歷史
《Greed》是作為一個高中期末專案開發的，然後獨立於學校繼續進行，這要歸功於各個開發人員的貢獻者，您可以看到他們的每個單獨提交都得到了認可。

從那時起，機器人就停止了開發，但問題和拉取請求有時仍然在創建者的空閒時間處理。

特徵
貪婪支持：

對於用戶：

建立訂單
列出所有訂單的狀態
為機器人的錢包添加更多資金
透過現金
透過電報付款
改變語言
顯示有​​關機器人的資訊和幫助
對於商店經理：

建立/編輯/刪除產品
以訊息形式接收要履行或退款的即時訂單流
手動為用戶添加資金
顯示已執行交易的列表
將已執行交易的清單匯出為 CSV 文件
新增其他使用者作為管理員並指定他們的權限
透過 Docker 引擎安裝
此安裝過程假設您所在的系統已docker安裝並具有支援的 CPU 架構。

要求
Docker引擎
網路連線
Telegram 機器人代幣（可在@Botfather取得）
支付提供者令牌（可透過將提供者與您的機器人連接來取得）
步驟
使用專案的 Docker 映像運行容器：

# docker run --volume "$(pwd)/config:/etc/greed" --volume "$(pwd)/strings:/usr/src/greed/strings" --volume "$(pwd)/data:/var/lib/greed" ghcr.io/steffo99/greed
config.toml編輯在目錄中建立的配置文件strings，向其中添加您的機器人和支付令牌：

# nano config/config.toml
（按Ctrl+X，然後按兩次Enter儲存並退出nano。）

可選：自訂資料夾中的檔案strings以存放自訂訊息。

啟動機器人：

python -OO core.py
打開 Telegram，並向/start您的機器人發送命令以自動晉升為 💼 經理。

按Ctrl+C停止機器人。

運行機器人
安裝後，要運行機器人，您需要：

從安裝它的相同目錄運行它的 Docker 容器：
# docker run --volume "$(pwd)/config:/etc/greed" --volume "$(pwd)/strings:/usr/src/greed/strings" --volume "$(pwd)/data:/var/lib/greed" ghcr.io/steffo99/greed
保持機器人運行
如果您希望在關閉終端機視窗後仍保持機器人打開，則需要將適當的參數傳遞給 docker 命令：

將 Docker 容器設定為始終重新啟動並在成功啟動時分開：
# docker run --detach --restart always --volume "$(pwd)/config:/etc/greed" --volume "$(pwd)/strings:/usr/src/greed/strings" --volume "$(pwd)/data:/var/lib/greed" ghcr.io/steffo99/greed
更新中
若要更新機器人，請執行以下命令：

尋找機器人的 Docker 容器的 ID：

# docker container ls
CONTAINER ID   IMAGE                    COMMAND                CREATED         STATUS                  PORTS     NAMES
abcdefabcdef   ghcr.io/steffo99/greed   "python -OO core.py"   6 seconds ago   Up Less than a second             relaxed_hypatia
停止機器人的 Docker 容器：

# docker container stop abcdefabcdef
刪除機器人的 Docker 容器：

# docker container rm abcdefabcdef
拉取機器人的最新 Docker 映像：

# docker pull ghcr.io/steffo99/greed:latest
使用新下載的影像重新啟動機器人：

# docker run --detach --restart always --volume "$(pwd)/config:/etc/greed" --volume "$(pwd)/strings:/usr/src/greed/strings" --volume "$(pwd)/data:/var/lib/greed" ghcr.io/steffo99/greed
透過 pip 安裝
此安裝過程假設您在 Linux 系統上，bash並且使用 和python安裝。

要求
git
Python 3.8（或更高版本）
網路連線
Telegram 機器人代幣（可在@Botfather取得）
支付提供者令牌（可透過將提供者與您的機器人連接來取得）
考慮租用虛擬專用伺服器（VPS）來託管機器人；便宜的應該可以，因為貪婪是相當輕的！ :)

步驟
透過執行以下命令下載專案檔：

$ git clone https://github.com/Steffo99/greed.git
進入新建的資料夾：

$ cd greed
建立一個新的 venv：

$ python3 -m venv venv
啟動 venv：

$ source venv/bin/activate
安裝專案要求：

$ pip install -r requirements.txt
可選：對於彩色控制台輸出，安裝coloredlogs：

$ pip install coloredlogs
產生設定檔：

$ python -OO core.py
編輯配置文件config.toml，向其中添加您的機器人和支付令牌：

$ nano config/config.toml
（按Ctrl+X，然後按兩次Enter儲存並退出nano。）

請注意不要在template_config.toml文件中輸入您的配置，因為它會被忽略並可能在更新時造成麻煩。

可選：自訂資料夾中的檔案strings以存放自訂訊息。

啟動機器人：

$ python -OO core.py
打開 Telegram，並向/start您的機器人發送命令以自動晉升為 💼 經理。

按Ctrl+C停止機器人。

運行機器人
安裝後，要運行機器人，您需要：

啟動 venv（如果尚未在目前控制台會話中啟動）：

$ source venv/bin/activate
啟動機器人：

$ python -OO core.py
保持機器人運行
如果您希望在關閉終端機視窗後仍保持機器人打開，則需要使用外部程序，例如：

screen（更簡單，但不會自動重新啟動）
systemd（推薦，但比較複雜）
screen
screen使用以下命令 打開將運行機器人的機器人：
$ screen venv/bin/python -OO core.py
若要安全地分離螢幕，請按 Ctrl+A，然後按 Ctrl+D。
systemd
假設您下載greed於/srv/greed：

建立一個名為 的新使用者greed：

$ useradd greed --system
將您先前下載的貪婪資料夾的所有權授予使用者greed：

$ chown -R greed: /srv/greed
/etc/systemd/system在命名中建立一個新文件，bot-greed.service包含以下內容：

[Unit]
Name=bot-greed
Description=Greed Bot
Wants=network-online.target
After=network-online.target nss-lookup.target

[Service]
Type=exec
User=greed
WorkingDirectory=/srv/greed
ExecStart=/srv/greed/venv/bin/python -OO /srv/greed/core.py
Environment=PYTHONUNBUFFERED=1

[Install]
WantedBy=multi-user.target
啟動bot-greed服務：

$ systemctl start bot-greed
如果一切順利，請啟用 bot-greed 服務，以便它將在重新啟動時自動啟動：

$ systemctl enable bot-greed   
更新中
若要更新機器人，請執行以下命令：

$ git stash
$ git pull
$ git stash pop
如果您使用舊版的greece，則可能需要重新建立配置，因為greece不再使用config.ini而是使用config.toml。

技術結構
該機器人由兩個部分組成：

core.py，它處理與 Telegram 的通信並向工作人員發送更新
worker.py，它處理單一使用者的對話流，並在每個對話的單獨執行緒上運行
機器人使用的其他資源有：

utils.py，包含實用方法
nuconfig.py，包含配置載入器
database.py，處理與 SQLite 或 PostgreSQL 資料庫的交互
localization.py並且strings/*，管理機器人的語言
config/*，最初包含生成配置文件的模板，然後是機器人運行一次後的配置文件本身
大師的貪婪/
