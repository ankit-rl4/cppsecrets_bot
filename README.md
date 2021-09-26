# cppsecrets_bot
A chatbot for cppsecrets.com . It uses the chatterbot Python library to create a bot which uses machine learning to reply to your messages . we train it with the training data which is available in the traning_data folder.

# How to run it ?

clone the repository and run the app.py
Then visit the url provided by the terminal

# Note :
 If you are updating the training data and rerunning the program , make sure you delete the database.sqlite3 file or it will keep using the old training data.
 
 If you ae using python 3.3+ you may get a error like this
 ```
 File "C:\Python38-64\lib\site-packages\sqlalchemy\util\compat.py", line 264, in
time_func = time.clock
AttributeError: module 'time' has no attribute 'clock'
```
in that case just go to  compat.py and replace the error line with ```time_func = time.perf_counter()``` from ```time_func = time.clock```
