import time
from compress_dir import compress_dir


def auto_backup(src_path, des_path, backup_time=300):
    start_time = time.time()
    while True:
        if time.time() - start_time >= backup_time:
            start_time = time.time()
            current_time = time.strftime("%Y%m%d_%H%M%S", time.localtime())
            compress_dir(src_path, des_path + current_time + ".zip")
        time.sleep(5)
        print("running")
