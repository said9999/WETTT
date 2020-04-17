from flask import Flask, escape, request, redirect, jsonify
from db.db import get_dao, format_restaurant, format_mall


app = Flask(__name__, static_folder='../web', static_url_path='')

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return redirect('/index.html', code=302) 

@app.route('/restaurants/random', methods=['POST'])
def random():
    # process input
    req_data = request.get_json()

    mall_name = req_data("mall")
    cuisines = req_data("cuisines")
    promo_bank = req_data("promo_bank")
    is_hala = req_data("is_hala")
    is_veg = req_data("is_veg")

    if cuisines == '':
        cuisines = None
    if promo_bank == '':
        promo_bank = None
    if is_hala == '':
        is_hala = None
    if is_veg == '':
        is_veg = None

    # access database
    dao = get_dao()

    mall_id = dao.get_mall_id(mall_name)
    if not mall_id:
        return jsonify({'status': 405})

    # get 1 recommendation and 5 ads
    ret = dao.get_random_choice(mall_id, cuisines, promo_bank, is_hala, is_veg)
    if ret:
        mall, rest, promo = ret
        ads = dao.get_ads(rest.rid, mall_id)
        recommend = format_restaurant(rest, [promo])  # to change!
        mall = format_mall(mall)

    # no recommendation found
    else:
        mall = ''
        recommend = ''
        ads = dao.get_ads(-1, mall_id)

    ad_rest = [format_restaurant(r, None) for r in ads]

    # return format
    message = {
        'status': 200,
        'restaurant': recommend,
        'ads': ad_rest,
        'mall': mall
    }

    return jsonify(message)
