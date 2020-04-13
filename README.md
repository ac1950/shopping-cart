### shopping-cart

1. Clone this repository onto your local hardrive 
2. Navigate to the pathname in terminal 

### Environments

1. Create an environment by:
conda create -n shopping-env python=3.7 # (first time only)
conda activate shopping-env

### Email Receipt 

1. From within a virtual environment install sendgrid
'pip install sendgrid == 6.0.5'

2. sign up for a sendgrid account and set up an API key with full access permissions

3. Create a .env file with the following:
SENDGRID_API_KEY=" YOUR API KEY"
SENDGRID_TEMPLATE_ID="YOUR TEMPLATE ID "
MY_EMAIL_ADDRESS="YOUR EMAIL ADDRESS"

### Importing CSV
1. Create a folder called Data if not already made
2. place your products.csv file inside of said folder
3. from within a virtual environment install pandas 
'pip install pandas' 

### Install Packages 
From within the virtual environment install the required packages 
` pip install -r requirements.txt` 


### from within the virtual environment run using 
`python shopping_cart.py`

