from pywebio import STATIC_PATH
from flask import Flask, send_from_directory
from pywebio.input import *
from pywebio.output import *
from pywebio.output import put_html, put_loading
from pywebio import start_server
import pandas as pd
import dtale
import argparse

def dapp():
    userfile = file_upload('Upload CSV data file')
    open(userfile['filename'],'wb').write(userfile['content'])
    df=pd.read_csv(userfile['filename'])
    d = dtale.show(df)
    d.open_browser()
    col=list(df.columns)
    Target_column = checkbox("Column to be encoded with Dummies", options=col)
    datatf=pd.get_dummies(df,columns=Target_column)
    d = dtale.show(datatf)
    d.open_browser()

    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", type=int, default=8080)
    args = parser.parse_args()

    start_server(dapp, port=args.port)