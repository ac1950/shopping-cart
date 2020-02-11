# shopping-cart

1. Clone this repository onto your local harddrive 
2. Navigate to the pathname in terminal 

## environments

1. 
Create an environment by:
conda create -n shopping-env python=3.7 # (first time only)
conda activate shopping-env

## email receipt 

1. From within a virtual environment install sendgrid
'pip install sendgrid == 6.0.5'

2. sign up for a sendgrid account and set up an API key with full access permissions

3. Create a .env file with the following:
SENDGRID_API_KEY=" YOUR API KEY"
SENDGRID_TEMPLATE_ID="YOUR TEMPLATE ID "
MY_EMAIL_ADDRESS="YOUR EMAIL ADDRESS"



## from within the virtual environment run using 'python shopping_cart.py'