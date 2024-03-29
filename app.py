from flask import Flask
app = Flask(__name__)

@app.route("/")
def Hello_World():
    return ''' ' Learned basics to devlope a website '\n\n


                   \n\nWhatever you do, do it well. 
                 
                                               – Walt Disney   ''' 



if __name__ == "__main__":
    app.run(debug-True,host="0.0.0.0", port=5000)

