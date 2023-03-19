from flask import Blueprint, Response
from flask_sqlalchemy.session import Session

from bookstore_billing.domain.user.user import User
from bookstore_billing.settings import db

admin_blueprint = Blueprint(name="admin", import_name=__name__, url_prefix="/admin")


def __generate_users_data(session: Session = None) -> None:
    users = [
        User(id="e5e61e0d-9bf9-4e54-9d1e-7d4b4af1e7a3", username="johndoe123", first_name="Emily",
             last_name="Rodriguez", email="johnsmith@example.com", user_status=True),
        User(id="c3f4d9b9-037b-4b04-9e11-f2b37dc371a6", username="sarahsmith", first_name="Jacob", last_name="Kim",
             email="jane.doe@gmail.com", user_status=True),
        User(id="a593c421-7147-4b88-a32f-af200109a1bc", username="brian.williams", first_name="Sophia",
             last_name="Patel", email="mario.rossi@hotmail.com", user_status=True),
        User(id="4f80b2cf-cb4c-4a4a-b9c9-7e24b918c224", username="katie88", first_name="William", last_name="Chen",
             email="amy.nguyen@yahoo.com", user_status=True),
        User(id="28d082e1-7ca7-4d72-b7e7-9c9b7f8256b9", username="markjones27", first_name="Natalie", last_name="Wong",
             email="tom.baker@outlook.com", user_status=True),
    ]

    if session is None:
        session = Session(db)

    for user in users:
        try:
            session.add(user)
            session.commit()
        except Exception as e:
            session.rollback()
            print(e)


@admin_blueprint.route("/gen_users_data", methods=["POST"])
def gen_users_data():
    __generate_users_data()
    return Response(response={"Users inserted in DB"}, status=200)
