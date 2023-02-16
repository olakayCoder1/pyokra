from .main import BaseConfig
from .exceptions import MissingRequiredDataError


class Auth(BaseConfig):

    # auth_base_url = self.

    def auth_id(self, id ):
        """
        Retrieve the bank account associated with a record's 
        current, savings, and domiciliary accounts, along with high-level account data and balances when available using the id
        id : account id 
        """
        url = self._BASE_END_POINT + 'auth/getById'
        return self._handle_request('POST', url , id )


    def auth_customer(self, customer=None , page=1 , limit=1):
        """
        Retrieve the bank account associated with a record's 
        current, savings, and domiciliary accounts, along with high-level account data and balances using the customer ID.

        customer : The customer.id you want to get detailed information about.
        page : A page number within the paginated result set. default to 1
        limit : This limits the number of records returned based on a limit value default 1 
        """
        data = {}
        data.update(
            {'page':page, 'limit': limit}
        )
        url = self._BASE_END_POINT + 'auth/getByCustomer' 

        if customer is None:
            raise MissingRequiredDataError('Missing a required data "customer"')

        data.update({
            'customer':customer
        })
        
        return self._handle_request('POST', url , data)



    def auth_date(self, start=None , end=None , page=1 , limit=1 ):
        """
        retrieve the bank account associated with a record's
        current, savings, and domiciliary accounts, along with high-level account data and balances within a specified date range.
        start : Start date
        end : End date
        page : A page number within the paginated result set. default to 1
        limit : This limits the number of records returned based on a limit value default 1 
        """

        data = {}
        data.update(
            {'page':page, 'limit': limit}
        )
        url = self._BASE_END_POINT + 'auth/getByDate' 
        if start is None:
            raise MissingRequiredDataError('Missing a required data "start" ')
        if end is None:
            raise MissingRequiredDataError('Missing a required data "end" ') 

        if not isinstance(start, str ) :
            raise TypeError('{} is not a string'.format(start))
        if not isinstance(end , str):
            raise TypeError('{} is not a string'.format(end))

        data.update(
            {'start':start, 'end': end }
        )
        return self._handle_request('POST', url , data)


    def auth_bank(self , bank=None , page=1 , limit=1  ):
        """
        Retrieve the bank account associated with a record's 
        current, savings, and domiciliary accounts, along with high-level account data and balances using the bank Id
        bank : Bank id 
        page : A page number within the paginated result set. default to 1
        limit : This limits the number of records returned based on a limit value default 1 
        """

        data = {}
        data.update(
            {'page':page, 'limit': limit}
        )
        url = self._BASE_END_POINT + 'auth/getByBank' 
        if not bank : raise  MissingRequiredDataError('Missing a required data "bank" ')
        data.update({
            'bank': bank
        })
        return self._handle_request('POST',url , data )
