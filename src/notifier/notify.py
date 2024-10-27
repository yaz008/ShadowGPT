from plyer import notification

def notify(title: str, message: str, duration: int = 5) -> None:
    notification.notify(app_name='ShadowGPT',
                        title=title,
                        message=message,
                        timeout=duration)
