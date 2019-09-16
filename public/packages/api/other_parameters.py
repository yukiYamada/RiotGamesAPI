
class Other_Parameters():
    """
    api other parameters. 
    """
    def __init__(self, keypairs):
        """
        Parameters
        ------------
        keypairs: [str:str]
            other parameter keys and values
        """       
        self._keyPairs = keypairs

    def get_url(self):
        """
        return parameter url
        """
        retvalue = ""
        for key in self._keyPairs:
            retvalue += "?"
            retvalue += str(key)
            retvalue += "="
            retvalue += str(self._keyPairs[key])

        return retvalue

class None_OtherParameters(Other_Parameters):
    def __init__(self):
        None
    def get_url(self):
        return ""    
