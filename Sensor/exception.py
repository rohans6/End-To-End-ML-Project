import os,sys
import traceback
import sys
import traceback
class SensorException(Exception):
    def __init__(self,message):
        super().__init__(self,message)
        _,_,tb=sys.exc_info()
        filename=tb.tb_frame.f_code.co_filename
        lineno=tb.tb_lineno
        self.error_message=f"Error occured from file: {tb.tb_frame.f_code.co_filename} Line number: {lineno} Error message: {message}"
    def __str__(self):
        return self.error_message


    

        