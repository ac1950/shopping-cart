# shopping_cart.py

import datetime
import pandas as pd
import os
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


def read_csv(): 
    """ 
    Does not take any params 
    Reads the product list from the CSV in the data file 
    Creates a list 
    """ 

    products = []
    stats = pd.read_csv("Data/products.csv")
    for index, row in stats.iterrows():
        p={}
        p["id"] = row["id"]
        p["name"] = row["name"]
        p["department"] = row["department"]
        p["aisle"] = row["aisle"]
        p["price"] = float(row["price"])
        products.append(p)
    return products
        
def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.
    Source: https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/datatypes/numbers.md#formatting-as-currency
    Param: my_price (int or float) like 4000.444444
    Example: to_usd(4000.444444)
    Returns: $4,000.44
    """
    my_priceType = float(my_price)
    return f"${my_priceType:,.2f}" #> $12,000.71

def get_time_day(): 
    #print checkout time and date
    now = datetime.datetime.now()
    time = now.strftime("%H:%M:%p")
    day = datetime.date.today()
    return [time, day]

def final_output_welcome(day, time):
    print("                                 ")
    print("CLEAN EATS GROCERY")
    print("WWW.CLEAN-EATS-GROCERY.COM")

    print("----------------------------------------------------------------------")
    print("CHECK OUT AT: " + str(day) + " " + time)
    print("----------------------------------------------------------------------")

def print_selected_products(inputed_ids):
    #printing the selected products
    #for loop saying: for my inputed id in the list of the inputed_ids (see else statement above),
    # list comprehension -> #Return an item for each item in our list of products if condition
    # 3rd line in embedded for loops sets the product as first in the loops
    running_total_price = 0
    print("SELECTED PRODUCTS: ")
    for inputed_id in inputed_ids: 
        matching_products = [p for p in products if str(p["id"]) == str(inputed_id)] #had to convert to str in order for the loop to match
        matching_product = matching_products[0]
        running_total_price = running_total_price + matching_product["price"]
        print ("..." + matching_product["name"] + " " + "(" + to_usd(matching_product["price"]) + ")" )

    print("----------------------------------------------------------------------")
    return running_total_price

def get_tax(running_total_price):
    #NYC sales tax rate: 8.75%
    sales_tax = .0875
    tax = running_total_price * sales_tax
    #print("TAX: "+ to_usd(tax))
    return tax

def get_total_due(running_total_price):
    totaldue = to_usd(get_tax(running_total_price) + running_total_price)
    return totaldue

def print_final_totals(running_total_price):
    print("SUBTOTAL: " + to_usd(running_total_price)) 
    print("TOTAL: " + get_total_due(running_total_price))
    print("----------------------------------------------------------------------")
    print("                     ")
    print("Thank you for shopping at Clean Eats Grocery!")
    print("See you again soon!")
    print("----------------------------------------------------------------------")

def send_email(running_total_price): 
    load_dotenv()

    SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY", "OOPS, please set env var called 'SENDGRID_API_KEY'")
    MY_ADDRESS = os.environ.get("MY_EMAIL_ADDRESS", "OOPS, please set env var called 'MY_EMAIL_ADDRESS'")


    email_decision = False
    while email_decision == False:

        print("Would You Like An Email Receipt?")
        email_decision = input("Please Enter 'yes' or 'no': ")
        if email_decision == 'no' or email_decision == 'NO' or email_decision == 'No' or email_decision == 'n' or email_decision == 'N':
            print("Okay! No Email Receipt Will Be Sent")
            email_decision = True
        elif email_decision == 'yes' or email_decision == 'YES' or email_decision == 'Yes' or email_decision == 'y' or email_decision == 'Y':
            email_decision = True
            print("----------------------------------------------------------------------")
            emailed = input("Please enter your email address receipt: ")
            print("                 ")
            while '@' not in emailed:
                print("Invalid Email Detected")
                emailed = input("Please enter your email address: ")
            client = SendGridAPIClient(SENDGRID_API_KEY) #> <class 'sendgrid.sendgrid.SendGridAPIClient>
            print("CLIENT:", type(client))

            subject = "Your Receipt from Clean Eats Grocery Store"





            html_content = "Thank You For Shopping at Clean Eats Grocery Store! Your Total is: " + get_total_due(running_total_price) + "       " + " Thank you. Come again!"
            message = Mail(from_email=MY_ADDRESS, to_emails=emailed, subject=subject, html_content=html_content)



            try:
                response = client.send(message)

                print("RESPONSE:", type(response)) #> <class 'python_http_client.client.Response'>
                print(response.status_code) #> 202 indicates SUCCESS
                print(response.body)
                print(response.headers)

            except Exception as e:
              print("OOPS", e.message)


            if str(response.status_code) == "202":
                    print("Email sent successfully!")
            else:
                    print("Oh, something went wrong with sending the email.")
                    print(response.status_code)
                    print(response.body)
        else:
            email_decision = False


if __name__ == "__main__":
    products = read_csv()

    ### ID Input
    running_total_price = 0
    inputed_ids = []
    while True: 
        check_range = False
        inputed_id = input("Please input a product indentifier or enter 'done': ")
        # Stops loop if the user enters done
        if inputed_id == "DONE" or inputed_id == "Done" or inputed_id == "done":
            break 
        else:
            for p in products:
                if str(p["id"]) == inputed_id:
                    check_range = True
        if check_range == False:
            print("----------------------------------------------------------------------")
            print("Product Indentifier Entered Not In Range")
            print("Please Make Sure You Entered The Correct Product ID")
            print("Please Make Sure You imported The Correct CSV File")
            print("----------------------------------------------------------------------")
        else:
            inputed_ids.append(inputed_id)
    
    time = get_time_day()[0]
    day = get_time_day()[1]

    final_output_welcome(day, time)

    running_total_price =  print_selected_products(inputed_ids)
    print_final_totals(running_total_price)

    send_email(running_total_price)







