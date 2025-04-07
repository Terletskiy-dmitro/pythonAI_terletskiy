import logging
from datetime import datetime

logging.basicConfig(
    filename='logfile.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d',encoding = "utf-8")


current_date = datetime.now().strftime('%Y-%m-%d')

# Запис повідомлення у лог
logging.info(f"Поточна дата: {current_date}")