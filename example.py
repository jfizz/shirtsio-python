import shirtsio

################# Account #################
# set api key
shirtsio.resources.api_key='3ef58f89c6c8d0ce3f71e4ab3537db4e24d6ac40'
################# End Account #################

################# Quote #################
# get quote
quote_resp = shirtsio.Quote.get_quote({'garment[0][product_id]': 3, 'garment[0][color]': 'White',
                                       'garment[0][sizes][med]': 100, 'print[front][color_count]': 5,
                                       'third_party_shipping': 0})
print quote_resp['subtotal']
################# End Quote #################


################# Payment #################
# check payment
TEST_CHECK_PAYMENT = {
    'name': 'John Doe',
    'company': 'Acme Corp',
    'address1': '1 Test Drive',
    'city': 'Test Town',
    'state': 'New York',
    'zip': '99999',
    'amount': '500.23',
    'payment_type': 'check',
    'account_number': '39494949',
    'routing_number': '5903495',
    'account_type': 'C',
}

TEST_CREDIT_PAYMENT = {
    'name': 'Johnny Appleseed',
    'company': 'Bigcorp',
    'address1': '1 Hope Lane',
    'city': 'Big city',
    'state': 'Iowa',
    'zip': '99999',
    'amount': '1000',
    'payment_type': 'credit_card',
    'card_number': '4242424242424242',
    'expiration': '0215',
    'cvc': '123',
}

check_payment_resp = shirtsio.Payment.payment(TEST_CHECK_PAYMENT)
credit_payment_resp = shirtsio.Payment.payment(TEST_CREDIT_PAYMENT)
print credit_payment_resp

# get payment status
payment_status_resp = shirtsio.Payment.get_payment_status({'transaction_id': '329402'})
print payment_status_resp

# add payment webhook url
payment_status_resp2 = shirtsio.Payment.update_payment_url({'url': "http://yourappurl"})
print payment_status_resp2
################# End Payment #################



################# Order #################
#place order
art_work_file_front = open("front.png", "rb")
proof_file_front = open("front.jpg", "rb")
art_work_file_back = open("back.png", "rb")
proof_front_file_back = open("back.jpg", "rb")
data = {'test': True, 'price': 79.28,
        'print[back][color_count]': 4, 'print[back][colors][0]': "101C", 'print[back][colors][1]': '107U',
        'addresses[0][name]': 'John Doe', 'addresses[0][address]': '123 Hope Ln.',
        'addresses[0][city]': 'Las Vegas', 'addresses[0][state]': 'Nevada', 'addresses[0][country]': 'US',
        'addresses[0][zipcode]': '12345', 'addresses[0][batch]': 1, 'addresses[0][sizes][med]': 2,
        'addresses[0][sizes][lrg]': 2,
        'print_type': 'DTG Print', 'third_party_shipping': 0,
        'garment[0][product_id]': 2, 'garment[0][color]': "White",
        'garment[0][sizes][med]': 2, 'garment[0][sizes][lrg]': 2, 'print[front][color_count]': 5}
data_ups = {'test': True, 'price': 79.28,
        'print[back][color_count]': 4, 'print[back][colors][0]': "101C", 'print[back][colors][1]': '107U',
        'addresses[0][name]': 'John Doe', 'addresses[0][address]': '123 Hope Ln.',
        'addresses[0][city]': 'Las Vegas', 'addresses[0][state]': 'Nevada', 'addresses[0][country]': 'US',
        'addresses[0][zipcode]': '12345', 'addresses[0][batch]': 1, 'addresses[0][sizes][med]': 2,
        'addresses[0][sizes][lrg]': 2,
        'print_type': 'DTG Print', 'third_party_shipping': 1,
        'garment[0][product_id]': 2, 'garment[0][color]': "White",
        'garment[0][sizes][med]': 2, 'garment[0][sizes][lrg]': 2, 'print[front][color_count]': 5,
        'addresses[0][third_party_ship_type]': 'ups',
        'third_party_shipping[0][account_type]': 'ups', 'third_party_shipping[0][account_number]': 'ups1234567890'}
data_usps = {'test': True, 'price': 79.28,
            'print[back][color_count]': 4, 'print[back][colors][0]': "101C", 'print[back][colors][1]': '107U',
            'addresses[0][name]': 'John Doe', 'addresses[0][address]': '123 Hope Ln.',
            'addresses[0][city]': 'Las Vegas', 'addresses[0][state]': 'Nevada', 'addresses[0][country]': 'US',
            'addresses[0][zipcode]': '12345', 'addresses[0][batch]': 1, 'addresses[0][sizes][med]': 2,
            'addresses[0][sizes][lrg]': 2,
            'print_type': 'DTG Print', 'third_party_shipping': 1,
            'garment[0][product_id]': 2, 'garment[0][color]': "White",
            'garment[0][sizes][med]': 2, 'garment[0][sizes][lrg]': 2, 'print[front][color_count]': 5,
            'addresses[0][third_party_ship_type]': 'usps',
            'third_party_shipping[0][account_type]': 'usps',
            'third_party_shipping[0][username]': 'Test Account', 'third_party_shipping[0][password]': 'test'}
data_dhl = {'test': True, 'price': 79.28,
            'print[back][color_count]': 4, 'print[back][colors][0]': "101C", 'print[back][colors][1]': '107U',
            'addresses[0][name]': 'John Doe', 'addresses[0][address]': '123 Hope Ln.',
            'addresses[0][city]': 'Las Vegas', 'addresses[0][state]': 'Nevada', 'addresses[0][country]': 'US',
            'addresses[0][zipcode]': '12345', 'addresses[0][batch]': 1, 'addresses[0][sizes][med]': 2,
            'addresses[0][sizes][lrg]': 2,
            'print_type': 'DTG Print', 'third_party_shipping': 1,
            'garment[0][product_id]': 2, 'garment[0][color]': "White",
            'garment[0][sizes][med]': 2, 'garment[0][sizes][lrg]': 2, 'print[front][color_count]': 5,
            'addresses[0][third_party_ship_type]': 'dhl',
            'third_party_shipping[0][account_type]': 'dhl', 'third_party_shipping[0][account_number]': 'dhl1234567890'}
files = {'print[front][artwork]': art_work_file_front, 'print[front][proof]': proof_file_front,
         'print[back][artwork]': art_work_file_back, 'print[back][proof]': proof_front_file_back}

try:
    order_resp = shirtsio.Order.place_order(data, files)
    print order_resp
    print order_resp['order_id']
finally:
    art_work_file_front.close()
    proof_file_front.close()
    art_work_file_back.close()
    proof_front_file_back.close()

# get order status
order_status_resp = shirtsio.Order.get_order_status({"order_id": '9999999'})
print order_status_resp
################# End Order #################



################# Products #################
#list categories
categories_resp = shirtsio.Products.list_categories()
print categories_resp
print "category ID: %s" % categories_resp[0]['category_id']

# list products
products_resp = shirtsio.Products.list_products(categories_resp[0]['category_id'])
print products_resp
print "product ID: %s" % products_resp[0]['product_id']

product_resp = shirtsio.Products.get_product(products_resp[0]['product_id'])
print product_resp

# inventory count
inventory_resp = shirtsio.Products.inventory_count(products_resp[0]['product_id'], 'White', 'CA')
print inventory_resp
################# End Products #################



################# Webhook ##################
# register webhook
register_webhook_resp = shirtsio.Webhook.add_webhook("http://test_webhook")
print register_webhook_resp

# list webhook
list_webhook_resp = shirtsio.Webhook.list_webhook()
print list_webhook_resp

# delete webhook
delete_webhook_resp = shirtsio.Webhook.delete_webhook("http://test_webhook")
print delete_webhook_resp
################# End Webhook ##################
