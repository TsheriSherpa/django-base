from base64 import encode
from utils.api_service import ApiService
from imepay.models import ImePayCredential
import base64
import requests
import json
class ImePayService(ApiService):
    """
    Esewa utility class

    Extends (ApiService)
    """

    def fetch_payment_token(request,credential:ImePayCredential):

        """

        """
        try:
            url=credential.base_url+"api/Web/GetToken"
            module=(credential.module).encode("ascii")
            token=(credential.api_username+ ":" +credential.password).encode('ascii')
            data = {
                    'MerchantCode': credential.merchant_code, 
                    'RefId': "250",
                    'Amount': 120
            }
            headers = {
                    'Authorization': 'Basic '+ base64.b64encode(token).decode(),
                    'Module': base64.b64encode(module).decode(),
                    'Content-Type': 'application/json'
                }
            res = requests.post(url, data=json.dumps(data), headers=headers)
            return json.loads(res.text)
        except:
            pass



       
