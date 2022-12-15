from flask import Flask;

app = Flask(__name__)

stores = [
    {
        "name": "Computer Shop",
        "items":[
            {
                "name": "Macbook Pro",
                "price": "19USD"
            }
        ]
    }
]

@app.get("/store")
def get_stores():
    return {"stores":stores}
