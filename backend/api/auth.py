from datetime import date
from flask import Blueprint, jsonify, request
from flask_restful import Resource, Api, abort, reqparse
from functools import wraps
import jwt
from flask_bcrypt import Bcrypt
import datetime
from flask_cors import CORS
from random import randint

from flask_mail import Mail, Message

# from iroha_sdk import Iroha


bp_auth = Blueprint('auth', __name__)
auth = Api(bp_auth)

bcrypt = Bcrypt()

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get("token") # http://127.0.0.1:5000/route?token=sdasdasdaqwesadaw
        if not token:
            return jsonify({"msg" : "Token is missing!", "status": 402})

        try:
            data = jwt.decode(token, app.config["SECRET_KEY"])

        except:
            return jsonify({"msg" : "Token is invalid!", "status": 403})

        return f(*args, **kwargs)

    return decorated

def UserExist(username):
    if users.find({"username": username}).count() == 0:
        return False
    else: 
        return True

def EmailExist(email):
    if users.find({"email": email}).count() == 0:
        return False
    else: 
        return True

def verifyPw(username, password):
    if not UserExist(username):
        return False

    hashed_pw = users.find({
        "username": username
    })[0]["password"]

    if bcrypt.hashpw(password.encode("utf8"), hashed_pw) == hashed_pw:
        return True
    else:
        return False

def verifyPwWithEmail(email, password):
    if not EmailExist(email):
        return False

    hashed_pw = users.find({
        "email": email
    })[0]["password"]

    if bcrypt.hashpw(password.encode("utf8"), hashed_pw) == hashed_pw:
        return True
    else:
        return False

def updateVerificationCode(email):
    code = users.find({
            "email": email
        })[0]["verification_code"]

    generated_code = randint(10000, 99999)
    
    users.update({"verification_code" : code}, {"$set" : {"verification_code": generated_code}})

    return generated_code


def GetCodeFromDb(email):
    code = users.find({
            "email": email
        })[0]["verification_code"]
    print("Code Here : ", code)
    return code

def setNewPassword(email, updated_password):
    password = users.find({
            "email": email
        })[0]["password"]
    
    users.update({"password" : password}, {"$set" : {"password": updated_password}})    

class Register(Resource):
    """This is a register function."""
    def post(self):

        postedData = request.get_json()
        name = postedData["name"]
        email = postedData["email"]
        password = postedData["password"]
        if name and email and password:
            hashed_pw = bcrypt.generate_password_hash(email+password).decode('utf-8')
            retJson = {
                "name": name,
                "password": hashed_pw
            }

            return jsonify(retJson)
        
        retJson = {
            "status" : 303,
            "msg" : "Please fill all the fields."
        }
        return jsonify(retJson)

class Login(Resource):
    """This is a login function."""
    def post(self):
        postedData = request.get_json()
        email = postedData["email"] 
        password = postedData["password"]
        chk_password = postedData["chk_password"]
        if email and password and chk_password:
            result = bcrypt.check_password_hash(chk_password, email+password)
            return result

        retJson = {
            "msg" : "Fields can not be empty. Login required!",
            "status" : 401
        }
        return jsonify(retJson)

class ForgetPass(Resource):
    def post(self):
        postedData = request.get_json()
        email = postedData["email"]
        new_password = postedData["newPassword"]
        confirm_password = postedData["confirmPassword"]
        code = postedData["code"]

        if email and new_password and confirm_password and code:

            if new_password != confirm_password:
                retJson = {
                    "msg": "Password doesn't match!",
                    "status" : 301 
                }
                return jsonify(retJson)

            db_code = GetCodeFromDb(email)

            if db_code != code:
                retJson = {
                    "msg": "The code didn't match!",
                    "status" : 302 
                }
                return jsonify(retJson)
            
            hashed_password = bcrypt.hashpw(new_password.encode('utf8'), bcrypt.gensalt())
            setNewPassword(email, hashed_password)

            retJson = {
                "msg" : "Password updated successfully.",
                "status" : 200
            }
            return jsonify(retJson)

        retJson = {
            "message" : "Please fill all the fields",
            "status" : 303
        }
            
        return retJson


class SendVerificationCode(Resource):
    def post(self):
        postedData = request.get_json()
        email = postedData["email"]
        
        if email:
            if not EmailExist(email):
                retJson = {
                    "msg" : "No such registered email",
                    "status" : 303
                }
                return jsonify(retJson)

            code = updateVerificationCode(email)
            msg = Message('Covid Tracker: {}'.format(code), sender = 'furqan4545@yandex.ru', recipients = [email])
            msg.body = "Here is your verification code: {}".format(code)
            mail.send(msg)

            retJson = {
                "msg": "Email has been sent to the registered email",
                "status" : 200
            }            
            return jsonify(retJson)

        retJson = {
            "msg": "Email field can't be empty!",
            "status": 302
        }
        return jsonify(retJson)


# @app.route("/protected") 
# @token_required
# def protected():
#     return jsonify({"msg": "This is only available to people with valid token!"})

auth.add_resource(Register, '/register')

auth.add_resource(Login, '/login')

auth.add_resource(SendVerificationCode, '/sendcode')

auth.add_resource(ForgetPass, '/resetpass')
