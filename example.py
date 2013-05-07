import shirtsio

shirtsio.resources.api_key='a086134c5625ebfd4e080d19749bc0cb736ad1d5'

# get api key
auth_resp = shirtsio.Account.integration_auth({'username': 'deantest', 'password': 'Pa$$w0rd'})
print auth_resp['api_key']

# get quote
quote_resp = shirtsio.Quote.get_quote({'garment[0][product_id]': 3, 'garment[0][color]': 'White', 'garment[0][sizes][med]': 100,
                          'print[front][color_count]': 5})
print quote_resp['subtotal']