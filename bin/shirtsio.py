# coding=utf-8
import ast
import requests


# This is the Base class for Shirt.io requests library
class Base():
    def __init__(self):
        self.url_shirtsio = "https://www.shirts.io/api/v1/"

    def do_request(self, url, params, method='get', files=None):
        response = None
        try:
            if method == 'get':
                response = requests.get(url, params=params)
            elif method == 'post':
                response = requests.post(url, data=params, files=files)

            if response.status_code == 200:
                results = response.json()["result"]
                if type(results) == unicode:
                    return ast.literal_eval(results)
            else:
                results = response.json()["error"]

            return results
        except requests.exceptions.RequestException:
            print "Send request to Shirt.io failed."
            # raise Exception(err)
        except ValueError:
            print "request error:", response.text
            # raise Exception(err)


# This is the encapsulation class for accounts requests to Shirt.io
class Accounts(Base):
    def __init__(self, api_key):
        Base.__init__(self)
        self.params = {'api_key': api_key}

        self.url_balance = self.url_shirtsio + "internal/integration/balance/"

    @staticmethod
    def get_balance(self):
        print self.url_balance
        return self.do_request(self.url_balance, self.params)


# This is the encapsulation class for authentication requests to Shirt.io
class Authentication(Base):
    def __init__(self):
        Base.__init__(self)

        self.url_order = self.url_shirtsio + "internal/integration/auth/"

    def auth(self, params):
        # https://shirts.io/api/v1/internal/integration/auth/
        return self.do_request(self.url_order, params)


# This is the encapsulation class for billing requests to Shirt.io
class Billing(Base):
    def __init__(self, api_key):
        Base.__init__(self)
        self.params = {'api_key': api_key}

        self.url_payment = self.url_shirtsio + "payment/"
        self.url_payment_status = self.url_shirtsio + "payment_status/"

    def payment(self, params):
        params = dict(self.params, **params)
        return self.do_request(self.url_payment, params, 'post')

    def update_payment_status(self, params):
        params = dict(self.params, **params)
        return self.do_request(self.url_payment_status, params, 'post')


# This is the encapsulation class for order requests to Shirt.io
class Order(Base):
    def __init__(self, api_key):
        Base.__init__(self)
        self.params = {'api_key': api_key}

        self.url_order = self.url_shirtsio + "order/"

    def place_order(self, params, files):
        # https://shirts.io/api/v1/order/
        params = dict(self.params, **params)
        return self.do_request(self.url_order, params, 'post', files)


# This is the encapsulation class for products requests to Shirt.io
class Products(Base):
    def __init__(self, api_key):
        Base.__init__(self)
        self.params = {'api_key': api_key}

        self.url_products = self.url_shirtsio + "products/"
        self.url_category = self.url_shirtsio + "products/category/"

    def list_categories(self):
        # https://shirts.io/api/v1/products/category/
        return self.do_request(self.url_category, self.params)

    def list_products(self, category_id):
        # https://shirts.io/api/v1/products/category/{Category_ID}/
        url = self.url_category + category_id + "/"
        return self.do_request(url, self.params)

    def get_product(self, product_id):
        # https://shirts.io/api/v1/products/{Product_ID}/
        url = self.url_products + product_id + "/"
        return self.do_request(url, self.params)

    def inventory_count(self, product_id, color, state=None):
        self.params['color'] = color
        self.params['state'] = state
        inventory = None
        # https://shirts.io/api/v1/products/{Product_ID}/
        url = self.url_products + product_id + "/"
        result_inventory = self.do_request(url, self.params)
        if result_inventory and ('inventory' in result_inventory):
            inventory = ast.literal_eval(result_inventory['inventory'])
        return inventory


# This is the encapsulation class for quote requests to Shirt.io
class Quote(Base):
    def __init__(self, api_key):
        Base.__init__(self)
        self.params = {'api_key': api_key}

        self.url_quote = self.url_shirtsio + "quote"

    def get_quote(self, params):
        # https://shirts.io/api/v1/quote
        params = dict(self.params, **params)
        return self.do_request(self.url_quote, params)


# This is the encapsulation class for order status requests to Shirt.io
class Status(Base):
    def __init__(self, api_key):
        Base.__init__(self)
        self.params = {'api_key': api_key}

        self.url_status = self.url_shirtsio + "status/"

    def check_order_status(self, order_id):
        # https://shirts.io/api/v1/status/{Order_ID}
        url = self.url_status + order_id + "/"
        return self.do_request(url, self.params)


# This is the encapsulation class for webhook registration，list，delete requests to Shirt.io
class Webhook(Base):
    def __init__(self, api_key):
        Base.__init__(self)
        self.params = {'api_key': api_key}

        self.url_webhook = self.url_shirtsio + "webhook/"

    def add_webhook(self, listener_url):
        url = self.url_webhook + "register" + "/"
        self.params['url'] = "'%s'" % listener_url
        return self.do_request(url, self.params, method='post')

    def delete_webhook(self, listener_url):
        url = self.url_webhook + "delete" + "/"
        self.params['url'] = "'%s'" % listener_url
        return self.do_request(url, self.params)

    def list_webhook(self):
        url = self.url_webhook + "list" + "/"
        return self.do_request(url, self.params, method='get')

    def add_payment_webhook(self):
        url = self.url_shirtsio + "shirtsio_webhook/payments/"
        self.params['url'] = "%s" % url
        return self.do_request(url, self.params, method='post')
