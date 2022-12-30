import logging
logging.basicConfig(filename='dividetest.log',level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

def divide(a,b):
    logging.info("the numbers entered by user are %s and %s" ,a,b)
    try:
        logging.info("we are into function")
        div = a/b
        logging.info("we have completed division operation")
        return div
    except  Exception as e:
        logging.exception(e)
    return a/b
print(divide(3,0))
