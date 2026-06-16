
import logging

# logging.basicConfig(level=logging.DEBUG)

logging.basicConfig(
    format = "%(asctime)s - %(user)s -  %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    filename="app.log",
    filemode="a",
    level=logging.INFO
)

num = 10
div = 0

try:
    res = num / div

except ZeroDivisionError as z:
    logging.error(z)
else:
    logging.info(f"The result is :{res}")

