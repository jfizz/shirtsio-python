# coding=utf-8
import ast
import logging
from shirtsio.requestor import APIRequestor

logger = logging.getLogger('shirtsio')

api_key = None


class APIResource(object):
    @classmethod
    def dict_params(cls, no_api_key, params):
        api_key_param = {'api_key': api_key}

        if no_api_key:
            return params

        if params:
            return dict(api_key_param, **params)

        return api_key_param

    @classmethod
    def do_request(cls, url=None, params=None, method="get", files=None, no_api_key=False):
        requestor = APIRequestor()
        params = cls.dict_params(no_api_key, params)
        url = requestor.api_url(url)
        return requestor.request(url, params, method, files)


# This is the encapsulation class for accounts requests to Shirt.io
class Account(APIResource):
    url_register_user = "internal/user/register/"
    url_update_user = "internal/user/update/"
    url_integration_auth = "internal/integration/auth/"

    @classmethod
    def register(cls, params):
        return cls.do_request(cls.url_register_user, params, method='post', no_api_key=True)

    @classmethod
    def update_user(cls, params):
        return cls.do_request(cls.url_update_user, params, method='post')

    @classmethod
    def integration_auth(cls, params):
        # https://shirts.io/api/v1/internal/integration/auth/
        return cls.do_request(cls.url_integration_auth, params, no_api_key=True)


# This is the encapsulation class for balance requests to Shirt.io
class Balance(APIResource):
    url_balance = "internal/integration/balance/"
    url_credit_limit = "internal/integration/credit_limit/"

    @classmethod
    def get_balance(cls):
        return cls.do_request(cls.url_balance)

    @classmethod
    def credit_limit(cls, params):
        pass
        # TODO
        #return cls.do_request(cls.url_credit_limit, params)


# This is the encapsulation class for billing requests to Shirt.io
class Payment(APIResource):
    url_payment = "payment/"
    url_payment_status = "payment_status/"

    @classmethod
    def payment(cls, params):
        # https://shirts.io/api/v1/internal/integration/payment/
        return cls.do_request(cls.url_payment, params, method='post')

    @classmethod
    def update_payment_status(cls, params):
        # https://shirts.io/api/v1/internal/integration/payment_status/
        return cls.do_request(cls.url_payment_status, params, method='post')


# This is the encapsulation class for order requests to Shirt.io
class Order(APIResource):
    url_order = "order/"
    url_status = "status/"

    @classmethod
    def place_order(cls, params, files):
        return cls.do_request(cls.url_order, params, method='post', files=files)

    @classmethod
    def get_order_status(cls, order_id):
        # https://shirts.io/api/v1/status/{Order_ID}
        url = cls.url_status + order_id + "/"
        return cls.do_request(url)


# This is the encapsulation class for products requests to Shirt.io
class Products(APIResource):
    url_products = "products/"
    url_category = "products/category/"

    @classmethod
    def list_categories(cls):
        # https://shirts.io/api/v1/products/category/
        return cls.do_request(cls.url_category)

    @classmethod
    def list_products(cls, category_id):
        # https://shirts.io/api/v1/products/category/{Category_ID}/
        url = cls.url_category + category_id + "/"
        return cls.do_request(url)

    @classmethod
    def get_product(cls, product_id):
        # https://shirts.io/api/v1/products/{Product_ID}/
        url = cls.url_products + product_id + "/"
        return cls.do_request(url)

    @classmethod
    def inventory_count(cls, product_id, color, state=None):
        params = {'color': color, 'state': state}
        inventory = None
        # https://shirts.io/api/v1/products/{Product_ID}/
        url = cls.url_products + product_id + "/"
        result_inventory = cls.do_request(url, params)
        if result_inventory and ('inventory' in result_inventory):
            inventory = ast.literal_eval(result_inventory['inventory'])
        return inventory


# This is the encapsulation class for quote requests to Shirt.io
class Quote(APIResource):
    url_quote = "quote/"

    @classmethod
    def get_quote(cls, params):
        # https://shirts.io/api/v1/quote
        return cls.do_request(cls.url_quote, params)


# This is the encapsulation class for webhook registration，list，delete requests to Shirt.io
class Webhook(APIResource):
    url_webhook = "webhook/"

    @classmethod
    def add_webhook(cls, listener_url):
        url = cls.url_webhook + "register" + "/"
        params = {'url': "'%s'" % listener_url}
        return cls.do_request(url, params, method='post')

    @classmethod
    def delete_webhook(cls, listener_url):
        url = cls.url_webhook + "delete" + "/"
        params = {'url': "'%s'" % listener_url}
        return cls.do_request(url, params)

    @classmethod
    def list_webhook(cls):
        url = cls.url_webhook + "list" + "/"
        return cls.do_request(url)

    @classmethod
    def add_payment_webhook(cls):
        url = "shirtsio_webhook/payments/"
        params = {'url': "%s" % url}
        return cls.do_request(url, params, method='post')