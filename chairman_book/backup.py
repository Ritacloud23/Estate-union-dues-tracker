import os
import shutil
from datetime import datetime


def create_backup():
    data_file = "data.json"

    if not os.path.exists(data_file):
        return None

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_file = f"data_backup_{timestamp}.json"

    shutil.copy(data_file, backup_file)

    return backup_file