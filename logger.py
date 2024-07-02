import logging
import os,shutil,sys
import shutil
class Logger:
    def __init__(self,log_dir,filename):
        self.log_dir=log_dir
        self.logger=logging.getLogger()
        self.logger.setLevel(logging.INFO)
        self.file_handler=logging.FileHandler(os.path.join(self.log_dir,filename))
        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.file_handler.setFormatter(self.formatter)
        self.logger.addHandler(self.file_handler)

    def log_message(self,message):
        self.logger.info(message)
    
