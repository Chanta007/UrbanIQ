class NotificationSystem:
    def __init__(self):
        self.notifications = []

    def send_notification(self, message, notification_type="info"):
        # Send a notification and add it to the notification list
        notification = {
            "message": message,
            "type": notification_type,
            "timestamp": self.get_current_time()
        }
        self.notifications.append(notification)
        # In a real implementation, this could push notifications to the UI
        return notification

    def get_notifications(self):
        # Return a list of all notifications
        return self.notifications

    def clear_notifications(self):
        # Clear all notifications
        self.notifications.clear()
        return {"message": "All notifications cleared."}

    def get_current_time(self):
        # Get the current timestamp for logging notifications
        import time
        return time.strftime("%Y-%m-%d %H:%M:%S")

# Example Usage:
notification_system = NotificationSystem()

# Send notifications
print(notification_system.send_notification("Traffic density increased by 20%.", "info"))
print(notification_system.send_notification("A medical emergency has been declared.", "emergency"))
print(notification_system.send_notification("Heavy rain detected, reducing vehicle speed.", "weather"))

# Get all notifications
print(notification_system.get_notifications())

# Clear all notifications
print(notification_system.clear_notifications())

# Get all notifications after clearing
print(notification_system.get_notifications())
