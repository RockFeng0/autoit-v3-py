from win32com.client import Dispatch
from win32com.client.gencache import EnsureDispatch

__all__ = [
    'WinMFCDriver',
    ]

class WinMFCDriver():    
    ''' automation Win WFC GUI'''
    def __init__(self):
        EnsureDispatch("AutoItX3.Control")
        self.autoHd = Dispatch("AutoItX3.Control")
        self.autoHd.Opt("WinTitleMatchMode",2)
    
    def invoke(self,method,*args):
        if not method in dir(self.autoHd):
            raise Exception("Invalide method: '%s'" %(method))        
        return getattr(self.autoHd,method)(*args)
