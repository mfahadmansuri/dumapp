from pywebio import STATIC_PATH
from flask import Flask, send_from_directory
from pywebio.input import *
from pywebio.output import *
from pywebio import start_server
import pandas as pd
import dtale

def dapp():
    userfile = file_upload('upload data file')
    open(userfile['filename'],'wb').write(userfile['content'])
    df=pd.read_csv(userfile['filename'])
    put_text(df.head())
    col=list(df.columns)
    Target_column = checkbox("Column to encoded with Dummies", options=col)
    datatf=pd.get_dummies(df,columns=Target_column)
    d = dtale.show(datatf)
    d.open_browser()

if __name__ == '__main__':
    dapp()