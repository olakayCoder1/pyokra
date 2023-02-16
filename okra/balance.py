from .main import BaseConfig
from .exceptions import MissingRequiredDataError


class Balance(BaseConfig):

    def getById(self, id, includePeriodic=True ):
        """
        Retrieve a bank account balance associated with a record's 
        current, savings , and domiciliary accounts using the id
        id : The unique identifier created by Okra used to reference the balance
        includePeriodic : Flag to determine if the periodic field should be included
        """
        data = {
            'id':id, 
            'includePeriodic': includePeriodic
        }
        
        url = self._BASE_END_POINT + 'balance/getById'
        return self._handle_request('POST', url , data) 


    def getByCustomer(self, id, includePeriodic=True, page=1 , limit=5 ):
        """
        Retrieve a bank account balance associated with a record's 
        current, savings , and domiciliary accounts using the customer id
        id : The unique identifier created by Okra used to reference the balance
        includePeriodic : Flag to determine if the periodic field should be included
        page : A page number within the paginated result set. default to 1
        limit : This limits the number of records returned based on a limit value default 1 
        """
        data = {
            'id':id, 
            'includePeriodic': includePeriodic , 
            'page':page, 
            'limit': limit
        }
        
        url = self._BASE_END_POINT + 'balance/getByCustomer'
        return self._handle_request('POST', url , data)


    def refresh(self, account_id):
        """
        Retrieve a bank account balance associated with a record's 
        current, savings , and domiciliary accounts when slight change occurs in the account using the account id
        account_id : account unique identifier created by Okra used to reference the account
        """
        data = { 'account_id':account_id }
        url = self._BASE_END_POINT + 'balance/refresh'
        return self._handle_request('POST', url , data) 


    
    def checkBalance(self, account_id , record_id):
        """
        Retrieve a bank account balance associated with a record's 
        current, savings , and domiciliary accounts
        account_id : account unique identifier created by Okra used to reference the account
        record_id : record unique identifier created by Okra used to reference the record
        """
        data = {}

        if account_id is None:
            raise MissingRequiredDataError('Missing a required data "account_id"')
        data.update(
            {'account_id':account_id ,}
        )
        if record_id is None:
            raise MissingRequiredDataError('Missing a required data "record_id"')

        data.update(
            {'record_id': record_id}
        )
        url = self._BASE_END_POINT + 'balance/check' 
        return self._handle_request('POST', url , data) 


    
    def checkAccountBalance(self, account_id:str = None ,includePeriodic=True,  page=1 , limit=1):
        """
        Retrieve a bank account balance associated with a record's 
        current, savings , and domiciliary accounts
        account_id : account unique identifier to get information about
        record_id : record unique identifier created by Okra used to reference the record
        page : A page number within the paginated result set. default to 1
        limit : This limits the number of records returned based on a limit value default 1 
        """
        data = {
            'page':page, 
            'limit': limit,
            'includePeriodic': includePeriodic 
        }

        if account_id is None:
            raise MissingRequiredDataError('Missing a required data "account_id"')
        data.update(
            {'account_id':account_id ,}
        )
        url = self._BASE_END_POINT + 'balance/getByAccount' 
        return self._handle_request('POST', url , data) 







        