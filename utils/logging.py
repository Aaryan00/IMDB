import logging
import os

class Logger:
    logger = None

    @classmethod
    def set_logger(cls):
        log_folder = 'logs'
        if not os.path.exists(log_folder):
            os.makedirs(log_folder)
              
        log_format = "[%(asctime)s] [%(levelname)s]" \
                     "[%(filename)s:%(funcName)s:%(lineno)d] %(message)s"
        
        formatter = logging.Formatter(log_format)
        
        fileHandler = logging.FileHandler(os.path.join(log_folder, 'app.log'))
        fileHandler.setLevel(logging.DEBUG) 
        fileHandler.setFormatter(formatter)
        
        cls.logger = logging.getLogger(__file__)
        cls.logger.propagate = False       
        cls.logger.setLevel(logging.INFO)
        if not cls.logger.handlers:
            cls.logger.addHandler(fileHandler)

    @classmethod
    def get_logger(cls):
        """Return the logger instance"""
        if cls.logger is None:
            cls.set_logger() 
        return cls.logger