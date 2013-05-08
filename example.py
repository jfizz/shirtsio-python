import shirtsio

# get api key
auth_resp = shirtsio.Account.integration_auth({'username': 'yourtestuser', 'password': 'Pa$$w0rd'})
print auth_resp['api_key']


shirtsio.resources.api_key=auth_resp['api_key']

# get quote
quote_resp = shirtsio.Quote.get_quote({'garment[0][product_id]': 3, 'garment[0][color]': 'White', 'garment[0][sizes][med]': 100,
                          'print[front][color_count]': 5})
print quote_resp['subtotal']
