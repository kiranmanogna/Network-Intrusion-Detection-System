

from tkinter import filedialog
from imutils import paths
import matplotlib.pyplot as plt
import numpy as np
from tkinter.filedialog import askopenfilename
import numpy as np 
import pandas as pd 
from sklearn import *
from sklearn.model_selection import train_test_split 
from sklearn import svm
from sklearn.metrics import accuracy_score 
from sklearn.feature_selection import SelectFromModel
from sklearn.linear_model import Lasso
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False


filename = askopenfilename(initialdir = "NSL-KDD-Dataset")
columns = ["duration","protocol_type","service","flag","src_bytes","dst_bytes","land","wrong_fragment","urgent","hot","num_failed_logins","logged_in","num_compromised","root_shell","su_attempted","num_root","num_file_creations","num_shells","num_access_files","num_outbound_cmds","is_host_login","is_guest_login","count","srv_count","serror_rate","srv_serror_rate","rerror_rate","srv_rerror_rate","same_srv_rate","diff_srv_rate","srv_diff_host_rate","dst_host_count","dst_host_srv_count","dst_host_same_srv_rate","dst_host_diff_srv_rate","dst_host_same_src_port_rate","dst_host_srv_diff_host_rate","dst_host_serror_rate","dst_host_srv_serror_rate","dst_host_rerror_rate","dst_host_srv_rerror_rate","label"]

labels = {"normal":0,"neptune":1,"warezclient":2,"ipsweep":3,"portsweep":4,"teardrop":5,"nmap":6,"satan":7,"smurf":8,"pod":9,"back":10,"guess_passwd":11,"ftp_write":12,"multihop":13,"rootkit":14,"buffer_overflow":15,"imap":16,"warezmaster":17,"phf":18,"land":19,"loadmodule":20,"spy":21,"perl":22,"saint":23,"mscan":24,"apache2":25,"snmpgetattack":26,"processtable":27,"httptunnel":28,"ps":29,"snmpguess":30,"mailbomb":31,"named":32,"sendmail":33,"xterm":34,"worm":35,"xlock":36,"xsnoop":37,"sqlattack":38,"udpstorm":39}
balance_data = pd.read_csv(filename,sep='\t')
dataset = ''
index = 0
cols = ''
print(balance_data.info())
print(balance_data.head())


for index, row in balance_data.iterrows():
        


        if(index == 0 ):
            for i in range(0,41):
                cols+=columns[i]+','
            cols+='Label'
        else:
            for i in range(0,42):
                if(isfloat(row[i])):
                    dataset+=str(row[i])+','
                if row[41] == 'normal':
                    dataset+='0'
                if row[41] == 'anomaly':
                    dataset+='1'
        dataset+='\n'
f = open("clean.txt", "w")
f.write(cols+"\n"+dataset)
f.close()    
print(cols);
            
      
