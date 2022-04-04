from flask import Flask, jsonify, request
from flask.views import MethodView
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import func

engine = create_engine('postgresql://admin:1234@127.0.0.1:5433/flask_netology')
Base = declarative_base()
Session = sessionmaker(bind=engine)


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    user_name = Column(String, unique=True)
    email = Column(String)
    registration_time = Column(DateTime, server_default=func.now())
    password = Column(String, nullable=False)

    def to_dict(self):
        return {
            'user_name': self.user_name,
            'registration_time': int(self.registration_time.timestamp()),
            'id': self.id,
        }


class Ad(Base):
    __tablename__ = 'ad'

    id = Column(Integer, primary_key=True)
    body = Column(String)
    stamp_time = Column(DateTime, server_default=func.now())
    user_id = Column(Integer, ForeignKey('users.id'))


Base.metadata.create_all(engine)

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
