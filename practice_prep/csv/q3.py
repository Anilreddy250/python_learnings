import json
def save_config():
    user_settings = {
        "theme": "dark",
        "notifications_enabled": True,
        "font_size": 14,
        "language": "en-US",
        "auto_save": {
            "enabled": True,
            "interval_minutes": 5
    }
    }
    filename = "config.json" 
    try:
        with open(filename, "w") as json_file:
            json.dump(user_settings, json_file, indent =4, sort_keys=True)
        print(f"Configuration successfullu saved{filename}")

    except Exception as e:
        print(f" an error occurred while sacing{e}")
if __name__ =="__main__":
    save_config()