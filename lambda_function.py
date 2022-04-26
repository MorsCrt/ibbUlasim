import pandas
import requests
import src.main as main

def lambda_handler(event,context):
    main.main()
