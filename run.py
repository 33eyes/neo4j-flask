from blog import app
import os

app.secret_key = os.urandom(24)
app.run(host="0.0.0.0", port=80, debug=True)