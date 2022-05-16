from brownie import SimpleStorage,accounts,config

def read_contract():
   xrecent_contact_=  SimpleStorage[-1]
   print(xrecent_contact_.retrieve())

def main():
    read_contract()