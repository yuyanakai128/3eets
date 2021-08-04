from datetime import date
from flask import Blueprint, jsonify, request
from flask_restful import Resource, Api, abort, reqparse

from api import iroha_sdk


bp_goods = Blueprint('goods', __name__)

@bp_goods.route('/create_domain', methods=['POST'])

def create_domain():
    """
    Create domain 'domain' 
    """
    # postedData = request.form.to_dict()
    postedData = request.get_json()
    domain_id = postedData["domain_id"]
    res = iroha_sdk.create_domain(domain_id)
    return res


@bp_goods.route('/create_asset', methods=['POST'])
def create_asset():
    """
    Create asset 'coin#domain' with precision 2
    """
    postedData = request.get_json()
    asset_name = postedData["asset_name"]
    domain_id = postedData["domain_id"]
    precision = postedData["precision"]
    res=iroha_sdk.create_asset(asset_name, domain_id,precision)
    return res

@bp_goods.route('/add_coin_to_admin', methods=['POST'])
def add_coin_to_admin():
    """
    Add some units of specified asset to 'admin@test'
    """
    postedData = request.get_json()
    asset_id = postedData["asset_id"]
    amount = postedData["amount"]
    res = iroha_sdk.add_coin_to_admin(asset_id, amount)
    return res

@bp_goods.route('/create_account', methods=['POST'])
def create_account_userone():
    """
    Create account 'userone@domain'
    """
    postedData = request.get_json()
    account_name = postedData["account_name"]
    domain_id = postedData["domain_id"]
    res = iroha_sdk.create_account(account_name, domain_id)
    return res


@bp_goods.route('/transfer_coin_from_src_to_dest', methods=['POST'])
def transfer_coin_from_src_to_dest():
    """
    Transfer 2.00 'coin#domain' from 'admin@test' to 'userone@domain'
    """
    postedData = request.get_json()
    src_account_id = postedData["src_account_id"]
    dest_account_id = postedData["dest_account_id"]
    asset_id = postedData["asset_id"]
    amount = postedData["amount"]
    res = iroha_sdk.transfer_coin_from_src_to_dest(src_account_id, dest_account_id, asset_id, amount)
    return res


@bp_goods.route('/userone_grants_to_admin_set_account_detail_permission', methods=['POST'])
def userone_grants_to_admin_set_account_detail_permission():
    """
    Make admin@test able to set detail to userone@domain
    """
    postedData = request.get_json()
    account_id = postedData["account_id"]
    creator_account = postedData["creator_account"]
    res = iroha_sdk.userone_grants_to_admin_set_account_detail_permission(account_id, creator_account)
    return res


@bp_goods.route('/set_age_to_userone', methods=['POST'])
def set_age_to_userone():
    """
    Set age to userone@domain by admin@test
    """
    postedData = request.get_json()
    account_id = postedData["account_id"]
    detailed_data = postedData["detailed_data"]
    res = iroha_sdk.set_account_detail(account_id, detailed_data)
    return res


@bp_goods.route('/get_coin_info', methods=['POST'])
def get_coin_info():
    """
    Get asset info for coin#domain
    :return:
    """
    postedData = request.get_json()
    asset_id = postedData["asset_id"]
    res = iroha_sdk.get_coin_info(asset_id)
    return res


@bp_goods.route('/get_account_assets', methods=['POST'])
def get_account_assets():
    """
    List all the assets of userone@domain
    """
    postedData = request.get_json()
    account_id = postedData["account_id"]
    res = iroha_sdk.get_account_assets(account_id)
    return res


@bp_goods.route('/get_userone_details', methods=['POST'])
def get_userone_details():
    """
    Get all the kv-storage entries for userone@domain
    """
    postedData = request.get_json()
    account_id = postedData["account_id"]
    res = iroha_sdk.get_userone_details(account_id)
    return res
