from datetime import datetime

def build_message(url):
    current_hour = datetime.now().hour
    return "\n".join([
        f"NOAA hurricane center {current_hour}:00 update",
        "click here to see the full report:",
        url
    ])
    
