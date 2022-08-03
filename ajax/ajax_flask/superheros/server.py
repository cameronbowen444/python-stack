from flask import Flask, render_template, redirect, request, session, flash
import os
print( os.environ.get("FLASK_APP_API_KEY") )

app = Flask(__name__)
app.secret_key = "vlaksdhgoairhgweojnv234325"




if __name__=="__main__":
    app.run(debug=True)
