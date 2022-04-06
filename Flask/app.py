from flask import Flask, jsonify, request
from flask.views import MethodView

from models import Session, User

app = Flask('app')


class UserView(MethodView):

    def get(self):
        pass

    def post(self):
        user_data = request.json
        with Session() as session:
            new_user = User(user_name=user_data['user_name'], password=user_data['password'])
            session.add(new_user)
            session.commit()
            return jsonify(new_user.to_dict())


# app.add_url_rule('/user/', methods=['POST'], view_func=UserView.as_view('user_create'))
app.add_url_rule("/user/", view_func=UserView.as_view("register_user"), methods=["POST"])

if __name__ == '__main__':
    app.debug = True
    app.run()
