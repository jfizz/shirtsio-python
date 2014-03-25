# Shirts.io Python Wrapper


## Introduction

Shirts.io is a t-shirt printing and fulfillment platform that lets you print and ship shirts anywhere in the world on demand.

### Create an Account

Creating an account is simple and quick! <a href="https://shirts.io/accounts/register">Create an account here.</a>

After creating an account, you will be given a unique API key to grant you access to the Shirts.io API.

### How it works

The Shirts.io API is broken up into four main components:

<ul>
<li><a href="https://shirts.io/docs/products_reference">Products API</a>
<ul>
<li>View our entire product selection</li>
<li>Access thousands of high-quality product images</li>
<li>View product specifications, available colors, available sizes</li>
<li>Check stock levels before placing an order</li>
</ul></li>
<li><a href="https://shirts.io/docs/quote_reference">Quote API</a>
<ul>
<li>Get an exact quote before placing an order</li>
</ul></li>
<li><a href="https://shirts.io/docs/order_reference">Order API</a>
<ul>
<li>Place an order</li>
<li>Upload artwork and all order details</li>
</ul></li>
<li><a href="https://shirts.io/docs/status_reference">Status API</a>
<ul>
<li>Check the current status of your order</li>
<li>Receive tracking numbers when available</li>
</ul></li>
</ul>

You can learn more by reading the <a href="https://www.shirts.io/docs/api_basics">API Manual</a>


## Installation

To install from source, run:

`python setup.py install`
    

## Usage

See <a href="https://github.com/ooshirts/shirtsio-python/blob/master/example.py">example.py</a>


## API Basics

### Authentication

Our API uses an API key authentication system. When you create an account, you will be given a unique API key. Every call you make through the shirts.io API must include this key.

### Errors

    HTTP Status Code Summary
    200 OK - Request successfully delivered.
    400 Bad Request - Parameters invalid.
    401 Unauthorized - API key was invalid or deactivated.
    402 Request Failed - Request failed on server end.
    
### Product Sizes

    xxsml - 2XSmall
    xsml - XSmall
    sml - Small
    med - Medium
    lrg - Large
    xlg - XLarge
    xxl - 2XLarge
    xxxl - 3XLarge
    xxxxl - 4XLarge
    xxxxxl - 5XLarge
    xxxxxxl - 6XLarge

Please see https://www.shirts.io/docs/getting_started/ for the most up-to-date documentation.


## Contributing

1. Fork it
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create new Pull Request
