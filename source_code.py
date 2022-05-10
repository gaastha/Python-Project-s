import time
from plyer import notification

if __name__=="__main__":
    while True:
        notification.notify(
            title="**Please drink water!!",
            message="Drink plenty of water throughout the day to avoid dehydration",
            app_icon=r"F:\Python Projects\Notification app\icon.ico",
            timeout=10
    )
        time.sleep(60*60)
