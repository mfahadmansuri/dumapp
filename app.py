from pywebio import STATIC_PATH
from flask import Flask, send_from_directory
from pywebio.input import *
from pywebio.output import *
from pywebio import start_server
import pandas as pd
import argparse

def dapp():

    userfile = file_upload('Upload csv data file')

    open(userfile['filename'],'wb').write(userfile['content'])

    df=pd.read_csv(userfile['filename'])

    put_html(df.head())

    col=list(df.columns)

    Target_column = checkbox("Column to be encoded with Dummies", options=col)

    catencodd=pd.get_dummies(df,columns=Target_column)
    catencodd.to_csv('catencodd.csv')
    content = open('catencodd.csv', 'rb').read()

    put_html(catencodd.head())
    put_file('catencodd.csv', content, 'Encoded Processed file')
    




if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", type=int, default=8080)
    args = parser.parse_args()
    
    start_server(dapp, port=args.port)