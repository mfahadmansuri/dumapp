from pywebio import STATIC_PATH

from flask import Flask, send_from_directory

from pywebio.input import *

from pywebio.output import *

from pywebio import start_server

import pandas as pd

import dtale

import argparse



def dapp():

    userfile = file_upload('upload data file')

    open(userfile['filename'],'wb').write(userfile['content'])

    df=pd.read_csv(userfile['filename'])

    put_table(df.head())

    col=list(df.columns)

    Target_column = checkbox("Column to encoded with Dummies", options=col)

    datatf=pd.get_dummies(df,columns=Target_column)

    put_table(datatf.head())
    put_file('datatf.csv', b'hello world!', 'encoded file')



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", type=int, default=8080)
    args = parser.parse_args()
    start_server(dapp, port=args.port)