import requests
import plyer
from plyer import notification

notification_title = "Mesaj Deneme 1"
notification_message = "Basarili Tesekkurler"

notification.notify(
    title = notification_title,
    message = notification_message,
    app_icon = None,
    timeout = 10,
    toast = False,
)
