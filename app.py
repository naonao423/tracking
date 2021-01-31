from chalice import Chalice,NotFoundError,BadRequestError
from chalicelib import database

app = Chalice(app_name='tracking')

@app.route('/track/{name}',methods=["GET"],cors=True)
def tracks(name):
    return database.track(name)
