from packages.api import summoner, match
from flask import Flask, render_template, request
app = Flask(__name__)
 
@app.route('/')
def index():
    return render_template('index.html', tabName="firstApi")

@app.route('/summoner_info', methods=['post'])
def summoner_info():
    messages = {}
    acc = apiacc(request.form["api_key"] , request.form["summoner_name"])

    # try RiotAPI connection with input apikey.
    exceptions = {}
    if(acc.try_connect(exceptions) == False):
        # fail api key. or...
        messages["exception"] = str(exceptions)
        return render_template("fail.html", messages=messages)

    # TODO : want to move this push messages. may not need to do it here.
    messages["tab_name"] = "firstAPI"
    messages["api_key"] = request.form["api_key"]
    messages["summoner_name"] = request.form["summoner_name"]
    messages["account_id"] = acc.get_summoner_account_id()

    return render_template("summoner_info.html", messages=messages)

class apiacc():
    def __init__(self, api_key, summoner_name):
        self._api_key = api_key
        self._summoner_name = summoner_name

    def try_connect(self, exceptions):
        """
        try connect 

        return
        -------------
        true :PASS
        false:FAIL(dis connect) and exception string to exception

        remarks
        -------------
        must move to api reader_base class. 
        """
        try:
            summoner_reader = summoner.summoner_reader.Reader(self._api_key)
            summoner_reader.get_by_summoner(self._summoner_name)
            return True
        except Exception as ex:
            # api fail or... 
            print(str(ex))
            exceptions["exception"] = str(ex)
            return False

    def get_summoner_account_id(self):
        summoner_reader =  summoner.summoner_reader.Reader(self._api_key)
        suminfo = summoner_reader.get_by_summoner(self._summoner_name)
                
        return suminfo.account_id
        
if __name__ == '__main__':
    app.run()