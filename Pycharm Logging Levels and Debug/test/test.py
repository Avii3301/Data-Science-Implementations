import logging
logging.basicConfig(filename="test.log", level=logging.INFO)
logging.info("this is my first code for logging")
logging.warning("this will try to log a warning")
logging.error("error message from system")
l = [1,2,3,4,45,6]
for i in l:
    if i == 2 :
        logging.info(i)
        logging.warning("2 FOUND!!!")

logging.shutdown()