import os
import binascii
from iroha import IrohaCrypto
from iroha import Iroha, IrohaGrpc

from iroha.primitive_pb2 import can_set_my_account_detail
import sys

if sys.version_info[0] < 3:
    raise Exception('Python 3 or a more recent version is required.')

# Here is the information about the environment and admin account information:
IROHA_HOST_ADDR = os.getenv('IROHA_HOST_ADDR', 'irohaNode')
# IROHA_HOST_ADDR = os.getenv('IROHA_HOST_ADDR', '127.0.0.1')
IROHA_PORT = os.getenv('IROHPORT', '50051')
ADMIN_ACCOUNT_ID = os.getenv('ADMIN_ACCOUNT_ID', 'admin@test')
ADMIN_PRIVATE_KEY = os.getenv(
    'ADMIN_PRIVATE_KEY', 'f101537e319568c765b2cc89698325604991dca57b9716b58016b253506cab70')

# Here we will create user keys
user_private_key = IrohaCrypto.private_key()
user_public_key = IrohaCrypto.derive_public_key(user_private_key)
iroha = Iroha(ADMIN_ACCOUNT_ID)
net = IrohaGrpc('{}:{}'.format(IROHA_HOST_ADDR, IROHA_PORT))
# net = IrohaGrpc('irohaNode:50051')


def trace(func):
    """
    A decorator for tracing methods' begin/end execution points
    """

    def tracer(*args, **kwargs):
        name = func.__name__
        print('\tEntering "{}"'.format(name))
        result = func(*args, **kwargs)
        print('\tLeaving "{}"'.format(name))
        return result

    return tracer

# Let's start defining the commands:
@trace
def send_transaction_and_print_status(transaction):
    hex_hash = binascii.hexlify(IrohaCrypto.hash(transaction))
    print('Transaction hash = {}, creator = {}'.format(
        hex_hash, transaction.payload.reduced_payload.creator_account_id))
    net.send_tx(transaction)
    to_send_back = []
    to_send_back.append(hex_hash)
    for status in net.tx_status_stream(transaction):
        to_send_back.append(status)
    return to_send_back
    # return (net.tx_status_stream(transaction))
    # for status in net.tx_status_stream(transaction):
    #     print(status)

# For example, below we define a transaction made of 2 commands:
# CreateDomain and CreateAsset.
# Each of Iroha commands has its own set of parameters and there are many commands.
# You can check out all of them here:
# https://iroha.readthedocs.io/en/main/develop/api/commands.html
@trace
def create_domain(domain_id):
    """
    Create domain 'domain'
    """
    commands = [
        iroha.command('CreateDomain', domain_id=domain_id, default_role='user'),
    ]
# And sign the transaction using the keys from earlier:
    tx = IrohaCrypto.sign_transaction(
        iroha.transaction(commands), ADMIN_PRIVATE_KEY)
    res=send_transaction_and_print_status(tx)
    return res
# You can define queries 
# (https://iroha.readthedocs.io/en/main/develop/api/queries.html) 
# the same way.

@trace
def create_asset(asset_name,domain_id,precision):
    """
    Create asset 'coin#domain' with precision 2
    """
    commands = [
        iroha.command('CreateAsset', asset_name=asset_name,domain_id=domain_id, precision=precision)
        # iroha.command('CreateAsset', asset_name='coin',domain_id='domain', precision=2)
    ]
# And sign the transaction using the keys from earlier:
    tx = IrohaCrypto.sign_transaction(
        iroha.transaction(commands), ADMIN_PRIVATE_KEY)
    res=send_transaction_and_print_status(tx)
    return res
# You can define queries 
# (https://iroha.readthedocs.io/en/main/develop/api/queries.html) 
# the same way.

@trace
def add_coin_to_admin(asset_id,amount):
    """
    Add 1000.00 units of 'coin#domain' to 'admin@test'
    """
    tx = iroha.transaction([
        iroha.command('AddAssetQuantity',
                      asset_id=asset_id, amount=amount)
    ])
    IrohaCrypto.sign_transaction(tx, ADMIN_PRIVATE_KEY)
    res=send_transaction_and_print_status(tx)
    return res


@trace
def create_account(account_name,domain_id):
    """
    Create account 'userone@domain'
    """
    tx = iroha.transaction([
        iroha.command('CreateAccount', account_name=account_name, domain_id=domain_id,
                      public_key=user_public_key)
    ])
    IrohaCrypto.sign_transaction(tx, ADMIN_PRIVATE_KEY)
    res=send_transaction_and_print_status(tx)
    return res


@trace
def transfer_coin_from_src_to_dest(src_account_id,dest_account_id,asset_id,amount):
    """
    Transfer 2.00 'coin#domain' from 'admin@test' to 'userone@domain'
    """
    tx = iroha.transaction([
        iroha.command('TransferAsset', src_account_id=src_account_id, dest_account_id=dest_account_id,
                      asset_id=asset_id, description='init top up', amount=amount)
    ])
    IrohaCrypto.sign_transaction(tx, ADMIN_PRIVATE_KEY)
    res=send_transaction_and_print_status(tx)
    return res


@trace
def userone_grants_to_admin_set_account_detail_permission(account_id,creator_account):
    """
    Make admin@test able to set detail to userone@domain
    """
    tx = iroha.transaction([
        iroha.command('GrantPermission', account_id=account_id,permission=can_set_my_account_detail)
        # iroha.command('GrantPermission', account_id='admin@test',permission=can_set_my_account_detail)
    ], creator_account=creator_account)
    # ], creator_account='userone@domain')
    IrohaCrypto.sign_transaction(tx, user_private_key)
    res=send_transaction_and_print_status(tx)
    return res


@trace
def set_account_detail(account_id,detailed_data):
    """
    Set age to userone@domain by admin@test
    """
    
    tx = iroha.transaction([
        iroha.command('SetAccountDetail',account_id=account_id, key=detailed_data['key'], value=detailed_data['value'])
        # iroha.command('SetAccountDetail',account_id='userone@domain', key='age', value='18')
    ])
    IrohaCrypto.sign_transaction(tx, ADMIN_PRIVATE_KEY)
    res=send_transaction_and_print_status(tx)
    return res


@trace
def get_coin_info(asset_id):
    """
    Get asset info for coin#domain
    :return:
    """
    query = iroha.query('GetAssetInfo', asset_id=asset_id)
    # query = iroha.query('GetAssetInfo', asset_id='coin#domain')
    IrohaCrypto.sign_query(query, ADMIN_PRIVATE_KEY)

    response = net.send_query(query)
    data = response.asset_response.asset
    jsonstr={
        'asset_id':data.asset_id,
        'domain_id':data.domain_id,
        'precision':data.precision
    }
    return (jsonstr)
    # print('Asset id = {}, precision = {}'.format(data.asset_id, data.precision))


# @trace
def get_account_assets(account_id):
    """
    List all the assets of userone@domain
    """
    query = iroha.query('GetAccountAssets', account_id=account_id)
    # query = iroha.query('GetAccountAssets', account_id='userone@domain')
    IrohaCrypto.sign_query(query, ADMIN_PRIVATE_KEY)
    response = net.send_query(query)
    data = response.account_assets_response.account_assets
    jsonstr={
        'asset_id':data[0].asset_id,
        'account_id':data[0].account_id,
        'balance':data[0].balance,
    }
    return (jsonstr)
    # return data
    # for asset in data:
    #     print('Asset id = {}, balance = {}'.format(
    #         asset.asset_id, asset.balance))


@trace
def get_userone_details(account_id):
    """
    Get all the kv-storage entries for userone@domain
    """
    query = iroha.query('GetAccountDetail', account_id=account_id)
    # query = iroha.query('GetAccountDetail', account_id='userone@domain')
    IrohaCrypto.sign_query(query, ADMIN_PRIVATE_KEY)

    response = net.send_query(query)
    data = response.account_detail_response
    jsonstr={
        
    }
    return (jsonstr)
    # print('Account id = {}, details = {}'.format('userone@domain', data.detail))
