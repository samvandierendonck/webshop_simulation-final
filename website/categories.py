from decimal import Decimal
from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for, app
from flask_login import login_user, login_required, logout_user, current_user
from .models import Note, Selected_item, User, Purchases, Ordered_item
from . import db
import json
from werkzeug.security import generate_password_hash, check_password_hash
import pandas as pd
import os 
from flask import send_from_directory

categories = Blueprint('categories', __name__)

def clean_name(name):
    name_header = name.replace('__',' & ')
    name_header = name_header.replace('_',' ')
    name_header = name_header.replace(',',', ')
    name_header = name_header[0].upper() + name_header[1:]
    return name_header

@categories.route('/fresh-products', methods=['GET', 'POST'])
@login_required
def fresh_products():
    #if request.method == 'POST':
        
    return render_template("fresh_products.html", user=current_user)

#all categories of fresh products

@categories.route('/dairy',methods=['GET','POST'])
@login_required
def dairy():
    name = 'zuivel'
    name_header = clean_name(name)

    static_directory = os.path.join(os.getcwd(),r'website/static')
    df_products_info = pd.read_csv(f'{static_directory}/webscrape_info_{name}.csv')
    products_info = df_products_info.to_dict('records')

    if request.method == 'POST':
        product_name = request.form.get('product_name')
        product_img = request.form.get('product_img')
        product_base_price = request.form.get('product_base_price')
        product_base_price_type = request.form.get('product_base_price_type')
        product_big_price = request.form.get('product_big_price')
        new_product = Selected_item(name=product_name,img=product_img,base_price=product_base_price,base_price_type=product_base_price_type,big_price=product_big_price, user_id=current_user.id)
        db.session.add(new_product)
        db.session.commit()
        if product_name != '':
            flash(f'Artiekel {product_name} toegevoegd aan mandje', category='success')

    

    return render_template("category.html",name_header=name_header,products_info=products_info, user=current_user)

@categories.route('/apero',methods=['GET','POST'])
@login_required
def apero_products():
    name = 'aperitief'
    name_header = clean_name(name)
    if request.method == 'POST':
        product_name = request.form.get('product_name')
        product_img = request.form.get('product_img')
        product_base_price = request.form.get('product_base_price')
        product_base_price_type = request.form.get('product_base_price_type')
        product_big_price = request.form.get('product_big_price')
        new_product = Selected_item(name=product_name,img=product_img,base_price=product_base_price,base_price_type=product_base_price_type,big_price=product_big_price, user_id=current_user.id)
        db.session.add(new_product)
        db.session.commit()
        if product_name != '':
            flash(f'Item {product_name} added to cart', category='success')

    static_directory = os.path.join(os.getcwd(),r'website/static')
    df_products_info = pd.read_csv(f'{static_directory}/webscrape_info_{name}.csv')
    products_info = df_products_info.to_dict('records')

    return render_template("category.html",name_header=name_header,products_info=products_info, user=current_user)

@categories.route('/bread-pastry',methods=['GET','POST'])
@login_required
def bread_pastry_products():
    name = 'brood__patisserie'
    name_header = clean_name(name)
    if request.method == 'POST':
        product_name = request.form.get('product_name')
        product_img = request.form.get('product_img')
        product_base_price = request.form.get('product_base_price')
        product_base_price_type = request.form.get('product_base_price_type')
        product_big_price = request.form.get('product_big_price')
        new_product = Selected_item(name=product_name,img=product_img,base_price=product_base_price,base_price_type=product_base_price_type,big_price=product_big_price, user_id=current_user.id)
        db.session.add(new_product)
        db.session.commit()
        if product_name != '':
            flash(f'Item {product_name} added to cart', category='success')

    static_directory = os.path.join(os.getcwd(),r'website/static')
    df_products_info = pd.read_csv(f'{static_directory}/webscrape_info_{name}.csv')
    products_info = df_products_info.to_dict('records')

    return render_template("category.html",name_header=name_header,products_info=products_info, user=current_user)

@categories.route('/meat',methods=['GET','POST'])
@login_required
def meat_products():
    name = 'charcuterie'
    name_header = clean_name(name)
    if request.method == 'POST':
        product_name = request.form.get('product_name')
        product_img = request.form.get('product_img')
        product_base_price = request.form.get('product_base_price')
        product_base_price_type = request.form.get('product_base_price_type')
        product_big_price = request.form.get('product_big_price')
        new_product = Selected_item(name=product_name,img=product_img,base_price=product_base_price,base_price_type=product_base_price_type,big_price=product_big_price, user_id=current_user.id)
        db.session.add(new_product)
        db.session.commit()
        if product_name != '':
            flash(f'Item {product_name} added to cart', category='success')

    static_directory = os.path.join(os.getcwd(),r'website/static')
    df_products_info = pd.read_csv(f'{static_directory}/webscrape_info_{name}.csv')
    products_info = df_products_info.to_dict('records')

    return render_template("category.html",name_header=name_header,products_info=products_info, user=current_user)

@categories.route('/fruit-vegetables',methods=['GET','POST'])
@login_required
def fruit_vegetables_products():
    name = 'groenten__fruit'
    name_header = clean_name(name)
    if request.method == 'POST':
        product_name = request.form.get('product_name')
        product_img = request.form.get('product_img')
        product_base_price = request.form.get('product_base_price')
        product_base_price_type = request.form.get('product_base_price_type')
        product_big_price = request.form.get('product_big_price')
        new_product = Selected_item(name=product_name,img=product_img,base_price=product_base_price,base_price_type=product_base_price_type,big_price=product_big_price, user_id=current_user.id)
        db.session.add(new_product)
        db.session.commit()
        if product_name != '':
            flash(f'Item {product_name} added to cart', category='success')

    static_directory = os.path.join(os.getcwd(),r'website/static')
    df_products_info = pd.read_csv(f'{static_directory}/webscrape_info_{name}.csv')
    products_info = df_products_info.to_dict('records')

    return render_template("category.html",name_header=name_header,products_info=products_info, user=current_user)

@categories.route('/butcher',methods=['GET','POST'])
@login_required
def butcher():
    name = 'beenhouwerij'
    name_header = clean_name(name)
    if request.method == 'POST':
        product_name = request.form.get('product_name')
        product_img = request.form.get('product_img')
        product_base_price = request.form.get('product_base_price')
        product_base_price_type = request.form.get('product_base_price_type')
        product_big_price = request.form.get('product_big_price')
        new_product = Selected_item(name=product_name,img=product_img,base_price=product_base_price,base_price_type=product_base_price_type,big_price=product_big_price, user_id=current_user.id)
        db.session.add(new_product)
        db.session.commit()
        if product_name != '':
            flash(f'Item {product_name} added to cart', category='success')

    static_directory = os.path.join(os.getcwd(),r'website/static')
    df_products_info = pd.read_csv(f'{static_directory}/webscrape_info_{name}.csv')
    products_info = df_products_info.to_dict('records')

    return render_template("category.html",name_header=name_header,products_info=products_info, user=current_user)


@categories.route('/catering-prepared-meals',methods=['GET','POST'])
@login_required
def catering_prepared_meals_products():
    name = 'traiteur__bereide_maaltijden'
    name_header = clean_name(name)
    if request.method == 'POST':
        product_name = request.form.get('product_name')
        product_img = request.form.get('product_img')
        product_base_price = request.form.get('product_base_price')
        product_base_price_type = request.form.get('product_base_price_type')
        product_big_price = request.form.get('product_big_price')
        new_product = Selected_item(name=product_name,img=product_img,base_price=product_base_price,base_price_type=product_base_price_type,big_price=product_big_price, user_id=current_user.id)
        db.session.add(new_product)
        db.session.commit()
        if product_name != '':
            flash(f'Item {product_name} added to cart', category='success')

    static_directory = os.path.join(os.getcwd(),r'website/static')
    df_products_info = pd.read_csv(f'{static_directory}/webscrape_info_{name}.csv')
    products_info = df_products_info.to_dict('records')

    return render_template("category.html",name_header=name_header,products_info=products_info, user=current_user)

@categories.route('/vegi-vegan-fresh',methods=['GET','POST'])
@login_required
def vegi_vegan_fresh():
    name = 'vegetarisch_vegan'
    name_header = clean_name(name)
    if request.method == 'POST':
        product_name = request.form.get('product_name')
        product_img = request.form.get('product_img')
        product_base_price = request.form.get('product_base_price')
        product_base_price_type = request.form.get('product_base_price_type')
        product_big_price = request.form.get('product_big_price')
        new_product = Selected_item(name=product_name,img=product_img,base_price=product_base_price,base_price_type=product_base_price_type,big_price=product_big_price, user_id=current_user.id)
        db.session.add(new_product)
        db.session.commit()
        if product_name != '':
            flash(f'Item {product_name} added to cart', category='success')

    static_directory = os.path.join(os.getcwd(),r'website/static')
    df_products_info = pd.read_csv(f'{static_directory}/webscrape_info_{name}.csv')
    products_info = df_products_info.to_dict('records')

    return render_template("category.html",name_header=name_header,products_info=products_info, user=current_user)

@categories.route('/fish-sushi',methods=['GET','POST'])
@login_required
def fish_sushi_products():
    name = 'vis__sushi'
    name_header = clean_name(name)
    if request.method == 'POST':
        product_name = request.form.get('product_name')
        product_img = request.form.get('product_img')
        product_base_price = request.form.get('product_base_price')
        product_base_price_type = request.form.get('product_base_price_type')
        product_big_price = request.form.get('product_big_price')
        new_product = Selected_item(name=product_name,img=product_img,base_price=product_base_price,base_price_type=product_base_price_type,big_price=product_big_price, user_id=current_user.id)
        db.session.add(new_product)
        db.session.commit()
        if product_name != '':
            flash(f'Item {product_name} added to cart', category='success')

    static_directory = os.path.join(os.getcwd(),r'website/static')
    df_products_info = pd.read_csv(f'{static_directory}/webscrape_info_{name}.csv')
    products_info = df_products_info.to_dict('records')

    return render_template("category.html",name_header=name_header,products_info=products_info, user=current_user)

#all categories of groceries

@categories.route('/breakfast',methods=['GET','POST'])
@login_required
def breakfast():
    name = 'ontbijt'
    name_header = clean_name(name)

    static_directory = os.path.join(os.getcwd(),r'website/static')
    df_products_info = pd.read_csv(f'{static_directory}/webscrape_info_{name}.csv')
    products_info = df_products_info.to_dict('records')

    if request.method == 'POST':
        product_name = request.form.get('product_name')
        product_img = request.form.get('product_img')
        product_base_price = request.form.get('product_base_price')
        product_base_price_type = request.form.get('product_base_price_type')
        product_big_price = request.form.get('product_big_price')
        new_product = Selected_item(name=product_name,img=product_img,base_price=product_base_price,base_price_type=product_base_price_type,big_price=product_big_price, user_id=current_user.id)
        db.session.add(new_product)
        db.session.commit()
        if product_name != '':
            flash(f'Artiekel {product_name} toegevoegd aan mandje', category='success')

    

    return render_template("category.html",name_header=name_header,products_info=products_info, user=current_user)

@categories.route('/world-kitchen',methods=['GET','POST'])
@login_required
def world_kitchen():
    name = 'wereldkeuken'
    name_header = clean_name(name)

    static_directory = os.path.join(os.getcwd(),r'website/static')
    df_products_info = pd.read_csv(f'{static_directory}/webscrape_info_{name}.csv')
    products_info = df_products_info.to_dict('records')

    if request.method == 'POST':
        product_name = request.form.get('product_name')
        product_img = request.form.get('product_img')
        product_base_price = request.form.get('product_base_price')
        product_base_price_type = request.form.get('product_base_price_type')
        product_big_price = request.form.get('product_big_price')
        new_product = Selected_item(name=product_name,img=product_img,base_price=product_base_price,base_price_type=product_base_price_type,big_price=product_big_price, user_id=current_user.id)
        db.session.add(new_product)
        db.session.commit()
        if product_name != '':
            flash(f'Artiekel {product_name} toegevoegd aan mandje', category='success')

    

    return render_template("category.html",name_header=name_header,products_info=products_info, user=current_user)

@categories.route('/desserts-sugar-flour',methods=['GET','POST'])
@login_required
def desserts_sugar_flour():
    name = 'desserts,suiker__bloem'
    name_header = clean_name(name)

    static_directory = os.path.join(os.getcwd(),r'website/static')
    df_products_info = pd.read_csv(f'{static_directory}/webscrape_info_{name}.csv')
    products_info = df_products_info.to_dict('records')

    if request.method == 'POST':
        product_name = request.form.get('product_name')
        product_img = request.form.get('product_img')
        product_base_price = request.form.get('product_base_price')
        product_base_price_type = request.form.get('product_base_price_type')
        product_big_price = request.form.get('product_big_price')
        new_product = Selected_item(name=product_name,img=product_img,base_price=product_base_price,base_price_type=product_base_price_type,big_price=product_big_price, user_id=current_user.id)
        db.session.add(new_product)
        db.session.commit()
        if product_name != '':
            flash(f'Artiekel {product_name} toegevoegd aan mandje', category='success')

    

    return render_template("category.html",name_header=name_header,products_info=products_info, user=current_user)

@categories.route('/candy',methods=['GET','POST'])
@login_required
def candy():
    name = 'snoepgoed'
    name_header = clean_name(name)

    static_directory = os.path.join(os.getcwd(),r'website/static')
    df_products_info = pd.read_csv(f'{static_directory}/webscrape_info_{name}.csv')
    products_info = df_products_info.to_dict('records')

    if request.method == 'POST':
        product_name = request.form.get('product_name')
        product_img = request.form.get('product_img')
        product_base_price = request.form.get('product_base_price')
        product_base_price_type = request.form.get('product_base_price_type')
        product_big_price = request.form.get('product_big_price')
        new_product = Selected_item(name=product_name,img=product_img,base_price=product_base_price,base_price_type=product_base_price_type,big_price=product_big_price, user_id=current_user.id)
        db.session.add(new_product)
        db.session.commit()
        if product_name != '':
            flash(f'Artiekel {product_name} toegevoegd aan mandje', category='success')

    

    return render_template("category.html",name_header=name_header,products_info=products_info, user=current_user)

@categories.route('/chocolate',methods=['GET','POST'])
@login_required
def chocolate():
    name = 'chocolade'
    name_header = clean_name(name)

    static_directory = os.path.join(os.getcwd(),r'website/static')
    df_products_info = pd.read_csv(f'{static_directory}/webscrape_info_{name}.csv')
    products_info = df_products_info.to_dict('records')

    if request.method == 'POST':
        product_name = request.form.get('product_name')
        product_img = request.form.get('product_img')
        product_base_price = request.form.get('product_base_price')
        product_base_price_type = request.form.get('product_base_price_type')
        product_big_price = request.form.get('product_big_price')
        new_product = Selected_item(name=product_name,img=product_img,base_price=product_base_price,base_price_type=product_base_price_type,big_price=product_big_price, user_id=current_user.id)
        db.session.add(new_product)
        db.session.commit()
        if product_name != '':
            flash(f'Artiekel {product_name} toegevoegd aan mandje', category='success')

    

    return render_template("category.html",name_header=name_header,products_info=products_info, user=current_user)

@categories.route('/chips-apero',methods=['GET','POST'])
@login_required
def chips_apero():
    name = 'chips__aperitief'
    name_header = clean_name(name)

    static_directory = os.path.join(os.getcwd(),r'website/static')
    df_products_info = pd.read_csv(f'{static_directory}/webscrape_info_{name}.csv')
    products_info = df_products_info.to_dict('records')

    if request.method == 'POST':
        product_name = request.form.get('product_name')
        product_img = request.form.get('product_img')
        product_base_price = request.form.get('product_base_price')
        product_base_price_type = request.form.get('product_base_price_type')
        product_big_price = request.form.get('product_big_price')
        new_product = Selected_item(name=product_name,img=product_img,base_price=product_base_price,base_price_type=product_base_price_type,big_price=product_big_price, user_id=current_user.id)
        db.session.add(new_product)
        db.session.commit()
        if product_name != '':
            flash(f'Artiekel {product_name} toegevoegd aan mandje', category='success')

    

    return render_template("category.html",name_header=name_header,products_info=products_info, user=current_user)

@categories.route('/cookies-pies',methods=['GET','POST'])
@login_required
def cookies_pies():
    name = 'koeken__taarten'
    name_header = clean_name(name)

    static_directory = os.path.join(os.getcwd(),r'website/static')
    df_products_info = pd.read_csv(f'{static_directory}/webscrape_info_{name}.csv')
    products_info = df_products_info.to_dict('records')

    if request.method == 'POST':
        product_name = request.form.get('product_name')
        product_img = request.form.get('product_img')
        product_base_price = request.form.get('product_base_price')
        product_base_price_type = request.form.get('product_base_price_type')
        product_big_price = request.form.get('product_big_price')
        new_product = Selected_item(name=product_name,img=product_img,base_price=product_base_price,base_price_type=product_base_price_type,big_price=product_big_price, user_id=current_user.id)
        db.session.add(new_product)
        db.session.commit()
        if product_name != '':
            flash(f'Artiekel {product_name} toegevoegd aan mandje', category='success')

    

    return render_template("category.html",name_header=name_header,products_info=products_info, user=current_user)

@categories.route('/rusk-crackers',methods=['GET','POST'])
@login_required
def rusk_crackers():
    name = 'beschuit__crackers'
    name_header = clean_name(name)

    static_directory = os.path.join(os.getcwd(),r'website/static')
    df_products_info = pd.read_csv(f'{static_directory}/webscrape_info_{name}.csv')
    products_info = df_products_info.to_dict('records')

    if request.method == 'POST':
        product_name = request.form.get('product_name')
        product_img = request.form.get('product_img')
        product_base_price = request.form.get('product_base_price')
        product_base_price_type = request.form.get('product_base_price_type')
        product_big_price = request.form.get('product_big_price')
        new_product = Selected_item(name=product_name,img=product_img,base_price=product_base_price,base_price_type=product_base_price_type,big_price=product_big_price, user_id=current_user.id)
        db.session.add(new_product)
        db.session.commit()
        if product_name != '':
            flash(f'Artiekel {product_name} toegevoegd aan mandje', category='success')

    

    return render_template("category.html",name_header=name_header,products_info=products_info, user=current_user)

@categories.route('/canned',methods=['GET','POST'])
@login_required
def canned():
    name = 'conserven'
    name_header = clean_name(name)

    static_directory = os.path.join(os.getcwd(),r'website/static')
    df_products_info = pd.read_csv(f'{static_directory}/webscrape_info_{name}.csv')
    products_info = df_products_info.to_dict('records')

    if request.method == 'POST':
        product_name = request.form.get('product_name')
        product_img = request.form.get('product_img')
        product_base_price = request.form.get('product_base_price')
        product_base_price_type = request.form.get('product_base_price_type')
        product_big_price = request.form.get('product_big_price')
        new_product = Selected_item(name=product_name,img=product_img,base_price=product_base_price,base_price_type=product_base_price_type,big_price=product_big_price, user_id=current_user.id)
        db.session.add(new_product)
        db.session.commit()
        if product_name != '':
            flash(f'Artiekel {product_name} toegevoegd aan mandje', category='success')

    

    return render_template("category.html",name_header=name_header,products_info=products_info, user=current_user)

####categories within drinks###

@categories.route('/water',methods=['GET','POST'])
@login_required
def water():
    name = 'water'
    name_header = clean_name(name)

    static_directory = os.path.join(os.getcwd(),r'website/static')
    df_products_info = pd.read_csv(f'{static_directory}/webscrape_info_{name}.csv')
    products_info = df_products_info.to_dict('records')

    if request.method == 'POST':
        product_name = request.form.get('product_name')
        product_img = request.form.get('product_img')
        product_base_price = request.form.get('product_base_price')
        product_base_price_type = request.form.get('product_base_price_type')
        product_big_price = request.form.get('product_big_price')
        new_product = Selected_item(name=product_name,img=product_img,base_price=product_base_price,base_price_type=product_base_price_type,big_price=product_big_price, user_id=current_user.id)
        db.session.add(new_product)
        db.session.commit()
        if product_name != '':
            flash(f'Artiekel {product_name} toegevoegd aan mandje', category='success')

    

    return render_template("category.html",name_header=name_header,products_info=products_info, user=current_user)

@categories.route('/fruit-vegetables-drinks',methods=['GET','POST'])
@login_required
def fruit_vegetables_drinks():
    name = 'vruchten__groentensap'
    name_header = clean_name(name)

    static_directory = os.path.join(os.getcwd(),r'website/static')
    df_products_info = pd.read_csv(f'{static_directory}/webscrape_info_{name}.csv')
    products_info = df_products_info.to_dict('records')

    if request.method == 'POST':
        product_name = request.form.get('product_name')
        product_img = request.form.get('product_img')
        product_base_price = request.form.get('product_base_price')
        product_base_price_type = request.form.get('product_base_price_type')
        product_big_price = request.form.get('product_big_price')
        new_product = Selected_item(name=product_name,img=product_img,base_price=product_base_price,base_price_type=product_base_price_type,big_price=product_big_price, user_id=current_user.id)
        db.session.add(new_product)
        db.session.commit()
        if product_name != '':
            flash(f'Artiekel {product_name} toegevoegd aan mandje', category='success')

    

    return render_template("category.html",name_header=name_header,products_info=products_info, user=current_user)

@categories.route('/syrups',methods=['GET','POST'])
@login_required
def syrups():
    name = 'siropen'
    name_header = clean_name(name)

    static_directory = os.path.join(os.getcwd(),r'website/static')
    df_products_info = pd.read_csv(f'{static_directory}/webscrape_info_{name}.csv')
    products_info = df_products_info.to_dict('records')

    if request.method == 'POST':
        product_name = request.form.get('product_name')
        product_img = request.form.get('product_img')
        product_base_price = request.form.get('product_base_price')
        product_base_price_type = request.form.get('product_base_price_type')
        product_big_price = request.form.get('product_big_price')
        new_product = Selected_item(name=product_name,img=product_img,base_price=product_base_price,base_price_type=product_base_price_type,big_price=product_big_price, user_id=current_user.id)
        db.session.add(new_product)
        db.session.commit()
        if product_name != '':
            flash(f'Artiekel {product_name} toegevoegd aan mandje', category='success')

    

    return render_template("category.html",name_header=name_header,products_info=products_info, user=current_user)

@categories.route('/milk-plant-based-drinks',methods=['GET','POST'])
@login_required
def milk_plant_based_drinks():
    name = 'melk__plantaardige_dranken'
    name_header = clean_name(name)

    static_directory = os.path.join(os.getcwd(),r'website/static')
    df_products_info = pd.read_csv(f'{static_directory}/webscrape_info_{name}.csv')
    products_info = df_products_info.to_dict('records')

    if request.method == 'POST':
        product_name = request.form.get('product_name')
        product_img = request.form.get('product_img')
        product_base_price = request.form.get('product_base_price')
        product_base_price_type = request.form.get('product_base_price_type')
        product_big_price = request.form.get('product_big_price')
        new_product = Selected_item(name=product_name,img=product_img,base_price=product_base_price,base_price_type=product_base_price_type,big_price=product_big_price, user_id=current_user.id)
        db.session.add(new_product)
        db.session.commit()
        if product_name != '':
            flash(f'Artiekel {product_name} toegevoegd aan mandje', category='success')

    return render_template("category.html",name_header=name_header,products_info=products_info, user=current_user)

@categories.route('/hot-drinks',methods=['GET','POST'])
@login_required
def hot_drinks():
    name = 'warme_dranken'
    name_header = clean_name(name)

    static_directory = os.path.join(os.getcwd(),r'website/static')
    df_products_info = pd.read_csv(f'{static_directory}/webscrape_info_{name}.csv')
    products_info = df_products_info.to_dict('records')

    if request.method == 'POST':
        product_name = request.form.get('product_name')
        product_img = request.form.get('product_img')
        product_base_price = request.form.get('product_base_price')
        product_base_price_type = request.form.get('product_base_price_type')
        product_big_price = request.form.get('product_big_price')
        new_product = Selected_item(name=product_name,img=product_img,base_price=product_base_price,base_price_type=product_base_price_type,big_price=product_big_price, user_id=current_user.id)
        db.session.add(new_product)
        db.session.commit()
        if product_name != '':
            flash(f'Artiekel {product_name} toegevoegd aan mandje', category='success')

    return render_template("category.html",name_header=name_header,products_info=products_info, user=current_user)

@categories.route('/soft-drinks',methods=['GET','POST'])
@login_required
def soft_drinks():
    name = 'softdrinks'
    name_header = clean_name(name)

    static_directory = os.path.join(os.getcwd(),r'website/static')
    df_products_info = pd.read_csv(f'{static_directory}/webscrape_info_{name}.csv')
    products_info = df_products_info.to_dict('records')

    if request.method == 'POST':
        product_name = request.form.get('product_name')
        product_img = request.form.get('product_img')
        product_base_price = request.form.get('product_base_price')
        product_base_price_type = request.form.get('product_base_price_type')
        product_big_price = request.form.get('product_big_price')
        new_product = Selected_item(name=product_name,img=product_img,base_price=product_base_price,base_price_type=product_base_price_type,big_price=product_big_price, user_id=current_user.id)
        db.session.add(new_product)
        db.session.commit()
        if product_name != '':
            flash(f'Artiekel {product_name} toegevoegd aan mandje', category='success')

    return render_template("category.html",name_header=name_header,products_info=products_info, user=current_user)

@categories.route('/beer',methods=['GET','POST'])
@login_required
def beer():
    name = 'bier'
    name_header = clean_name(name)

    static_directory = os.path.join(os.getcwd(),r'website/static')
    df_products_info = pd.read_csv(f'{static_directory}/webscrape_info_{name}.csv')
    products_info = df_products_info.to_dict('records')

    if request.method == 'POST':
        product_name = request.form.get('product_name')
        product_img = request.form.get('product_img')
        product_base_price = request.form.get('product_base_price')
        product_base_price_type = request.form.get('product_base_price_type')
        product_big_price = request.form.get('product_big_price')
        new_product = Selected_item(name=product_name,img=product_img,base_price=product_base_price,base_price_type=product_base_price_type,big_price=product_big_price, user_id=current_user.id)
        db.session.add(new_product)
        db.session.commit()
        if product_name != '':
            flash(f'Artiekel {product_name} toegevoegd aan mandje', category='success')

    return render_template("category.html",name_header=name_header,products_info=products_info, user=current_user)

@categories.route('/apero-strong-drink',methods=['GET','POST'])
@login_required
def apero_strong_drink():
    name = 'aperitieven__sterke_drank'
    name_header = clean_name(name)

    static_directory = os.path.join(os.getcwd(),r'website/static')
    df_products_info = pd.read_csv(f'{static_directory}/webscrape_info_{name}.csv')
    products_info = df_products_info.to_dict('records')

    if request.method == 'POST':
        product_name = request.form.get('product_name')
        product_img = request.form.get('product_img')
        product_base_price = request.form.get('product_base_price')
        product_base_price_type = request.form.get('product_base_price_type')
        product_big_price = request.form.get('product_big_price')
        new_product = Selected_item(name=product_name,img=product_img,base_price=product_base_price,base_price_type=product_base_price_type,big_price=product_big_price, user_id=current_user.id)
        db.session.add(new_product)
        db.session.commit()
        if product_name != '':
            flash(f'Artiekel {product_name} toegevoegd aan mandje', category='success')

    return render_template("category.html",name_header=name_header,products_info=products_info, user=current_user)

@categories.route('/wines',methods=['GET','POST'])
@login_required
def wines():
    name = 'wijnen'
    name_header = clean_name(name)

    static_directory = os.path.join(os.getcwd(),r'website/static')
    df_products_info = pd.read_csv(f'{static_directory}/webscrape_info_{name}.csv')
    products_info = df_products_info.to_dict('records')

    if request.method == 'POST':
        product_name = request.form.get('product_name')
        product_img = request.form.get('product_img')
        product_base_price = request.form.get('product_base_price')
        product_base_price_type = request.form.get('product_base_price_type')
        product_big_price = request.form.get('product_big_price')
        new_product = Selected_item(name=product_name,img=product_img,base_price=product_base_price,base_price_type=product_base_price_type,big_price=product_big_price, user_id=current_user.id)
        db.session.add(new_product)
        db.session.commit()
        if product_name != '':
            flash(f'Artiekel {product_name} toegevoegd aan mandje', category='success')

    return render_template("category.html",name_header=name_header,products_info=products_info, user=current_user)

###categories within frozen###

@categories.route('/vegi-vegan-frozen',methods=['GET','POST'])
@login_required
def vegi_vegan_frozen():
    name = 'vegetarisch__vegan'
    name_header = clean_name(name)

    static_directory = os.path.join(os.getcwd(),r'website/static')
    df_products_info = pd.read_csv(f'{static_directory}/webscrape_info_{name}.csv')
    products_info = df_products_info.to_dict('records')

    if request.method == 'POST':
        product_name = request.form.get('product_name')
        product_img = request.form.get('product_img')
        product_base_price = request.form.get('product_base_price')
        product_base_price_type = request.form.get('product_base_price_type')
        product_big_price = request.form.get('product_big_price')
        new_product = Selected_item(name=product_name,img=product_img,base_price=product_base_price,base_price_type=product_base_price_type,big_price=product_big_price, user_id=current_user.id)
        db.session.add(new_product)
        db.session.commit()
        if product_name != '':
            flash(f'Artiekel {product_name} toegevoegd aan mandje', category='success')

    

    return render_template("category.html",name_header=name_header,products_info=products_info, user=current_user)

@categories.route('/ice-desserts',methods=['GET','POST'])
@login_required
def ice_desserts():
    name = 'ijs__desserten'
    name_header = clean_name(name)

    static_directory = os.path.join(os.getcwd(),r'website/static')
    df_products_info = pd.read_csv(f'{static_directory}/webscrape_info_{name}.csv')
    products_info = df_products_info.to_dict('records')

    if request.method == 'POST':
        product_name = request.form.get('product_name')
        product_img = request.form.get('product_img')
        product_base_price = request.form.get('product_base_price')
        product_base_price_type = request.form.get('product_base_price_type')
        product_big_price = request.form.get('product_big_price')
        new_product = Selected_item(name=product_name,img=product_img,base_price=product_base_price,base_price_type=product_base_price_type,big_price=product_big_price, user_id=current_user.id)
        db.session.add(new_product)
        db.session.commit()
        if product_name != '':
            flash(f'Artiekel {product_name} toegevoegd aan mandje', category='success')

    

    return render_template("category.html",name_header=name_header,products_info=products_info, user=current_user)

@categories.route('/pizza-quiches',methods=['GET','POST'])
@login_required
def pizza_quiches():
    name = 'pizza__quiches'
    name_header = clean_name(name)

    static_directory = os.path.join(os.getcwd(),r'website/static')
    df_products_info = pd.read_csv(f'{static_directory}/webscrape_info_{name}.csv')
    products_info = df_products_info.to_dict('records')

    if request.method == 'POST':
        product_name = request.form.get('product_name')
        product_img = request.form.get('product_img')
        product_base_price = request.form.get('product_base_price')
        product_base_price_type = request.form.get('product_base_price_type')
        product_big_price = request.form.get('product_big_price')
        new_product = Selected_item(name=product_name,img=product_img,base_price=product_base_price,base_price_type=product_base_price_type,big_price=product_big_price, user_id=current_user.id)
        db.session.add(new_product)
        db.session.commit()
        if product_name != '':
            flash(f'Artiekel {product_name} toegevoegd aan mandje', category='success')

    return render_template("category.html",name_header=name_header,products_info=products_info, user=current_user)

@categories.route('/bread-cake',methods=['GET','POST'])
@login_required
def bread_cake():
    name = 'brood__gebak'
    name_header = clean_name(name)

    static_directory = os.path.join(os.getcwd(),r'website/static')
    df_products_info = pd.read_csv(f'{static_directory}/webscrape_info_{name}.csv')
    products_info = df_products_info.to_dict('records')

    if request.method == 'POST':
        product_name = request.form.get('product_name')
        product_img = request.form.get('product_img')
        product_base_price = request.form.get('product_base_price')
        product_base_price_type = request.form.get('product_base_price_type')
        product_big_price = request.form.get('product_big_price')
        new_product = Selected_item(name=product_name,img=product_img,base_price=product_base_price,base_price_type=product_base_price_type,big_price=product_big_price, user_id=current_user.id)
        db.session.add(new_product)
        db.session.commit()
        if product_name != '':
            flash(f'Artiekel {product_name} toegevoegd aan mandje', category='success')

    return render_template("category.html",name_header=name_header,products_info=products_info, user=current_user)

@categories.route('/snacks-apero',methods=['GET','POST'])
@login_required
def snacks_apero():
    name = 'snacks__aperitiefhapjes'
    name_header = clean_name(name)

    static_directory = os.path.join(os.getcwd(),r'website/static')
    df_products_info = pd.read_csv(f'{static_directory}/webscrape_info_{name}.csv')
    products_info = df_products_info.to_dict('records')

    if request.method == 'POST':
        product_name = request.form.get('product_name')
        product_img = request.form.get('product_img')
        product_base_price = request.form.get('product_base_price')
        product_base_price_type = request.form.get('product_base_price_type')
        product_big_price = request.form.get('product_big_price')
        new_product = Selected_item(name=product_name,img=product_img,base_price=product_base_price,base_price_type=product_base_price_type,big_price=product_big_price, user_id=current_user.id)
        db.session.add(new_product)
        db.session.commit()
        if product_name != '':
            flash(f'Artiekel {product_name} toegevoegd aan mandje', category='success')

    return render_template("category.html",name_header=name_header,products_info=products_info, user=current_user)

@categories.route('/starters',methods=['GET','POST'])
@login_required
def starters():
    name = 'voorgerechten'
    name_header = clean_name(name)

    static_directory = os.path.join(os.getcwd(),r'website/static')
    df_products_info = pd.read_csv(f'{static_directory}/webscrape_info_{name}.csv')
    products_info = df_products_info.to_dict('records')

    if request.method == 'POST':
        product_name = request.form.get('product_name')
        product_img = request.form.get('product_img')
        product_base_price = request.form.get('product_base_price')
        product_base_price_type = request.form.get('product_base_price_type')
        product_big_price = request.form.get('product_big_price')
        new_product = Selected_item(name=product_name,img=product_img,base_price=product_base_price,base_price_type=product_base_price_type,big_price=product_big_price, user_id=current_user.id)
        db.session.add(new_product)
        db.session.commit()
        if product_name != '':
            flash(f'Artiekel {product_name} toegevoegd aan mandje', category='success')

    return render_template("category.html",name_header=name_header,products_info=products_info, user=current_user)

@categories.route('/prepared-meals',methods=['GET','POST'])
@login_required
def prepared_meals():
    name = 'bereide_maaltijden'
    name_header = clean_name(name)

    static_directory = os.path.join(os.getcwd(),r'website/static')
    df_products_info = pd.read_csv(f'{static_directory}/webscrape_info_{name}.csv')
    products_info = df_products_info.to_dict('records')

    if request.method == 'POST':
        product_name = request.form.get('product_name')
        product_img = request.form.get('product_img')
        product_base_price = request.form.get('product_base_price')
        product_base_price_type = request.form.get('product_base_price_type')
        product_big_price = request.form.get('product_big_price')
        new_product = Selected_item(name=product_name,img=product_img,base_price=product_base_price,base_price_type=product_base_price_type,big_price=product_big_price, user_id=current_user.id)
        db.session.add(new_product)
        db.session.commit()
        if product_name != '':
            flash(f'Artiekel {product_name} toegevoegd aan mandje', category='success')

    return render_template("category.html",name_header=name_header,products_info=products_info, user=current_user)

@categories.route('/fish',methods=['GET','POST'])
@login_required
def fish():
    name = 'vis'
    name_header = clean_name(name)

    static_directory = os.path.join(os.getcwd(),r'website/static')
    df_products_info = pd.read_csv(f'{static_directory}/webscrape_info_{name}.csv')
    products_info = df_products_info.to_dict('records')

    if request.method == 'POST':
        product_name = request.form.get('product_name')
        product_img = request.form.get('product_img')
        product_base_price = request.form.get('product_base_price')
        product_base_price_type = request.form.get('product_base_price_type')
        product_big_price = request.form.get('product_big_price')
        new_product = Selected_item(name=product_name,img=product_img,base_price=product_base_price,base_price_type=product_base_price_type,big_price=product_big_price, user_id=current_user.id)
        db.session.add(new_product)
        db.session.commit()
        if product_name != '':
            flash(f'Artiekel {product_name} toegevoegd aan mandje', category='success')

    return render_template("category.html",name_header=name_header,products_info=products_info, user=current_user)

@categories.route('/vegetables',methods=['GET','POST'])
@login_required
def vegetables():
    name = 'groenten'
    name_header = clean_name(name)

    static_directory = os.path.join(os.getcwd(),r'website/static')
    df_products_info = pd.read_csv(f'{static_directory}/webscrape_info_{name}.csv')
    products_info = df_products_info.to_dict('records')

    if request.method == 'POST':
        product_name = request.form.get('product_name')
        product_img = request.form.get('product_img')
        product_base_price = request.form.get('product_base_price')
        product_base_price_type = request.form.get('product_base_price_type')
        product_big_price = request.form.get('product_big_price')
        new_product = Selected_item(name=product_name,img=product_img,base_price=product_base_price,base_price_type=product_base_price_type,big_price=product_big_price, user_id=current_user.id)
        db.session.add(new_product)
        db.session.commit()
        if product_name != '':
            flash(f'Artiekel {product_name} toegevoegd aan mandje', category='success')

    return render_template("category.html",name_header=name_header,products_info=products_info, user=current_user)

###Categories of baby related products###

@categories.route('/milk-drinks',methods=['GET','POST'])
@login_required
def milk_drinks():
    name = 'melk__dranken'
    name_header = clean_name(name)

    static_directory = os.path.join(os.getcwd(),r'website/static')
    df_products_info = pd.read_csv(f'{static_directory}/webscrape_info_{name}.csv')
    products_info = df_products_info.to_dict('records')

    if request.method == 'POST':
        product_name = request.form.get('product_name')
        product_img = request.form.get('product_img')
        product_base_price = request.form.get('product_base_price')
        product_base_price_type = request.form.get('product_base_price_type')
        product_big_price = request.form.get('product_big_price')
        new_product = Selected_item(name=product_name,img=product_img,base_price=product_base_price,base_price_type=product_base_price_type,big_price=product_big_price, user_id=current_user.id)
        db.session.add(new_product)
        db.session.commit()
        if product_name != '':
            flash(f'Artiekel {product_name} toegevoegd aan mandje', category='success')

    

    return render_template("category.html",name_header=name_header,products_info=products_info, user=current_user)

@categories.route('/baby-food',methods=['GET','POST'])
@login_required
def baby_food():
    name = 'babyvoeding'
    name_header = clean_name(name)

    static_directory = os.path.join(os.getcwd(),r'website/static')
    df_products_info = pd.read_csv(f'{static_directory}/webscrape_info_{name}.csv')
    products_info = df_products_info.to_dict('records')

    if request.method == 'POST':
        product_name = request.form.get('product_name')
        product_img = request.form.get('product_img')
        product_base_price = request.form.get('product_base_price')
        product_base_price_type = request.form.get('product_base_price_type')
        product_big_price = request.form.get('product_big_price')
        new_product = Selected_item(name=product_name,img=product_img,base_price=product_base_price,base_price_type=product_base_price_type,big_price=product_big_price, user_id=current_user.id)
        db.session.add(new_product)
        db.session.commit()
        if product_name != '':
            flash(f'Artiekel {product_name} toegevoegd aan mandje', category='success')

    

    return render_template("category.html",name_header=name_header,products_info=products_info, user=current_user)

@categories.route('/baby-care',methods=['GET','POST'])
@login_required
def baby_care():
    name = 'verzorging_baby'
    name_header = clean_name(name)

    static_directory = os.path.join(os.getcwd(),r'website/static')
    df_products_info = pd.read_csv(f'{static_directory}/webscrape_info_{name}.csv')
    products_info = df_products_info.to_dict('records')

    if request.method == 'POST':
        product_name = request.form.get('product_name')
        product_img = request.form.get('product_img')
        product_base_price = request.form.get('product_base_price')
        product_base_price_type = request.form.get('product_base_price_type')
        product_big_price = request.form.get('product_big_price')
        new_product = Selected_item(name=product_name,img=product_img,base_price=product_base_price,base_price_type=product_base_price_type,big_price=product_big_price, user_id=current_user.id)
        db.session.add(new_product)
        db.session.commit()
        if product_name != '':
            flash(f'Artiekel {product_name} toegevoegd aan mandje', category='success')

    

    return render_template("category.html",name_header=name_header,products_info=products_info, user=current_user)

@categories.route('/diapers',methods=['GET','POST'])
@login_required
def diapers():
    name = 'luiers__luierbroekjes'
    name_header = clean_name(name)

    static_directory = os.path.join(os.getcwd(),r'website/static')
    df_products_info = pd.read_csv(f'{static_directory}/webscrape_info_{name}.csv')
    products_info = df_products_info.to_dict('records')

    if request.method == 'POST':
        product_name = request.form.get('product_name')
        product_img = request.form.get('product_img')
        product_base_price = request.form.get('product_base_price')
        product_base_price_type = request.form.get('product_base_price_type')
        product_big_price = request.form.get('product_big_price')
        new_product = Selected_item(name=product_name,img=product_img,base_price=product_base_price,base_price_type=product_base_price_type,big_price=product_big_price, user_id=current_user.id)
        db.session.add(new_product)
        db.session.commit()
        if product_name != '':
            flash(f'Artiekel {product_name} toegevoegd aan mandje', category='success')

    

    return render_template("category.html",name_header=name_header,products_info=products_info, user=current_user)

@categories.route('/detergent-baby',methods=['GET','POST'])
@login_required
def detergent_baby():
    name = 'wasmiddelen_baby'
    name_header = clean_name(name)

    static_directory = os.path.join(os.getcwd(),r'website/static')
    df_products_info = pd.read_csv(f'{static_directory}/webscrape_info_{name}.csv')
    products_info = df_products_info.to_dict('records')

    if request.method == 'POST':
        product_name = request.form.get('product_name')
        product_img = request.form.get('product_img')
        product_base_price = request.form.get('product_base_price')
        product_base_price_type = request.form.get('product_base_price_type')
        product_big_price = request.form.get('product_big_price')
        new_product = Selected_item(name=product_name,img=product_img,base_price=product_base_price,base_price_type=product_base_price_type,big_price=product_big_price, user_id=current_user.id)
        db.session.add(new_product)
        db.session.commit()
        if product_name != '':
            flash(f'Artiekel {product_name} toegevoegd aan mandje', category='success')

    

    return render_template("category.html",name_header=name_header,products_info=products_info, user=current_user)

###Categories of care and hiegene###

@categories.route('/mouth-hiegene',methods=['GET','POST'])
@login_required
def mouth_hiegene():
    name = 'mondhygiëne'
    name_header = clean_name(name)

    static_directory = os.path.join(os.getcwd(),r'website/static')
    df_products_info = pd.read_csv(f'{static_directory}/webscrape_info_{name}.csv')
    products_info = df_products_info.to_dict('records')

    if request.method == 'POST':
        product_name = request.form.get('product_name')
        product_img = request.form.get('product_img')
        product_base_price = request.form.get('product_base_price')
        product_base_price_type = request.form.get('product_base_price_type')
        product_big_price = request.form.get('product_big_price')
        new_product = Selected_item(name=product_name,img=product_img,base_price=product_base_price,base_price_type=product_base_price_type,big_price=product_big_price, user_id=current_user.id)
        db.session.add(new_product)
        db.session.commit()
        if product_name != '':
            flash(f'Artiekel {product_name} toegevoegd aan mandje', category='success')

    return render_template("category.html",name_header=name_header,products_info=products_info, user=current_user)

@categories.route('/body',methods=['GET','POST'])
@login_required
def body():
    name = 'lichaam'
    name_header = clean_name(name)

    static_directory = os.path.join(os.getcwd(),r'website/static')
    df_products_info = pd.read_csv(f'{static_directory}/webscrape_info_{name}.csv')
    products_info = df_products_info.to_dict('records')

    if request.method == 'POST':
        product_name = request.form.get('product_name')
        product_img = request.form.get('product_img')
        product_base_price = request.form.get('product_base_price')
        product_base_price_type = request.form.get('product_base_price_type')
        product_big_price = request.form.get('product_big_price')
        new_product = Selected_item(name=product_name,img=product_img,base_price=product_base_price,base_price_type=product_base_price_type,big_price=product_big_price, user_id=current_user.id)
        db.session.add(new_product)
        db.session.commit()
        if product_name != '':
            flash(f'Artiekel {product_name} toegevoegd aan mandje', category='success')

    return render_template("category.html",name_header=name_header,products_info=products_info, user=current_user)

@categories.route('/hair',methods=['GET','POST'])
@login_required
def hair():
    name = 'haar'
    name_header = clean_name(name)

    static_directory = os.path.join(os.getcwd(),r'website/static')
    df_products_info = pd.read_csv(f'{static_directory}/webscrape_info_{name}.csv')
    products_info = df_products_info.to_dict('records')

    if request.method == 'POST':
        product_name = request.form.get('product_name')
        product_img = request.form.get('product_img')
        product_base_price = request.form.get('product_base_price')
        product_base_price_type = request.form.get('product_base_price_type')
        product_big_price = request.form.get('product_big_price')
        new_product = Selected_item(name=product_name,img=product_img,base_price=product_base_price,base_price_type=product_base_price_type,big_price=product_big_price, user_id=current_user.id)
        db.session.add(new_product)
        db.session.commit()
        if product_name != '':
            flash(f'Artiekel {product_name} toegevoegd aan mandje', category='success')

    return render_template("category.html",name_header=name_header,products_info=products_info, user=current_user)

@categories.route('/face',methods=['GET','POST'])
@login_required
def face():
    name = 'gezicht'
    name_header = clean_name(name)

    static_directory = os.path.join(os.getcwd(),r'website/static')
    df_products_info = pd.read_csv(f'{static_directory}/webscrape_info_{name}.csv')
    products_info = df_products_info.to_dict('records')

    if request.method == 'POST':
        product_name = request.form.get('product_name')
        product_img = request.form.get('product_img')
        product_base_price = request.form.get('product_base_price')
        product_base_price_type = request.form.get('product_base_price_type')
        product_big_price = request.form.get('product_big_price')
        new_product = Selected_item(name=product_name,img=product_img,base_price=product_base_price,base_price_type=product_base_price_type,big_price=product_big_price, user_id=current_user.id)
        db.session.add(new_product)
        db.session.commit()
        if product_name != '':
            flash(f'Artiekel {product_name} toegevoegd aan mandje', category='success')

    return render_template("category.html",name_header=name_header,products_info=products_info, user=current_user)

@categories.route('/men',methods=['GET','POST'])
@login_required
def men():
    name = 'mannen'
    name_header = clean_name(name)

    static_directory = os.path.join(os.getcwd(),r'website/static')
    df_products_info = pd.read_csv(f'{static_directory}/webscrape_info_{name}.csv')
    products_info = df_products_info.to_dict('records')

    if request.method == 'POST':
        product_name = request.form.get('product_name')
        product_img = request.form.get('product_img')
        product_base_price = request.form.get('product_base_price')
        product_base_price_type = request.form.get('product_base_price_type')
        product_big_price = request.form.get('product_big_price')
        new_product = Selected_item(name=product_name,img=product_img,base_price=product_base_price,base_price_type=product_base_price_type,big_price=product_big_price, user_id=current_user.id)
        db.session.add(new_product)
        db.session.commit()
        if product_name != '':
            flash(f'Artiekel {product_name} toegevoegd aan mandje', category='success')

    return render_template("category.html",name_header=name_header,products_info=products_info, user=current_user)

@categories.route('/hiegene',methods=['GET','POST'])
@login_required
def hiegene():
    name = 'hygiëne'
    name_header = clean_name(name)

    static_directory = os.path.join(os.getcwd(),r'website/static')
    df_products_info = pd.read_csv(f'{static_directory}/webscrape_info_{name}.csv')
    products_info = df_products_info.to_dict('records')

    if request.method == 'POST':
        product_name = request.form.get('product_name')
        product_img = request.form.get('product_img')
        product_base_price = request.form.get('product_base_price')
        product_base_price_type = request.form.get('product_base_price_type')
        product_big_price = request.form.get('product_big_price')
        new_product = Selected_item(name=product_name,img=product_img,base_price=product_base_price,base_price_type=product_base_price_type,big_price=product_big_price, user_id=current_user.id)
        db.session.add(new_product)
        db.session.commit()
        if product_name != '':
            flash(f'Artiekel {product_name} toegevoegd aan mandje', category='success')

    return render_template("category.html",name_header=name_header,products_info=products_info, user=current_user)

@categories.route('/pharmacy',methods=['GET','POST'])
@login_required
def pharmacy():
    name = 'apotheek'
    name_header = clean_name(name)

    static_directory = os.path.join(os.getcwd(),r'website/static')
    df_products_info = pd.read_csv(f'{static_directory}/webscrape_info_{name}.csv')
    products_info = df_products_info.to_dict('records')

    if request.method == 'POST':
        product_name = request.form.get('product_name')
        product_img = request.form.get('product_img')
        product_base_price = request.form.get('product_base_price')
        product_base_price_type = request.form.get('product_base_price_type')
        product_big_price = request.form.get('product_big_price')
        new_product = Selected_item(name=product_name,img=product_img,base_price=product_base_price,base_price_type=product_base_price_type,big_price=product_big_price, user_id=current_user.id)
        db.session.add(new_product)
        db.session.commit()
        if product_name != '':
            flash(f'Artiekel {product_name} toegevoegd aan mandje', category='success')

    return render_template("category.html",name_header=name_header,products_info=products_info, user=current_user)

@categories.route('/travel-size',methods=['GET','POST'])
@login_required
def travel_size():
    name = 'reisformaat'
    name_header = clean_name(name)

    static_directory = os.path.join(os.getcwd(),r'website/static')
    df_products_info = pd.read_csv(f'{static_directory}/webscrape_info_{name}.csv')
    products_info = df_products_info.to_dict('records')

    if request.method == 'POST':
        product_name = request.form.get('product_name')
        product_img = request.form.get('product_img')
        product_base_price = request.form.get('product_base_price')
        product_base_price_type = request.form.get('product_base_price_type')
        product_big_price = request.form.get('product_big_price')
        new_product = Selected_item(name=product_name,img=product_img,base_price=product_base_price,base_price_type=product_base_price_type,big_price=product_big_price, user_id=current_user.id)
        db.session.add(new_product)
        db.session.commit()
        if product_name != '':
            flash(f'Artiekel {product_name} toegevoegd aan mandje', category='success')

    return render_template("category.html",name_header=name_header,products_info=products_info, user=current_user)

###Categories of maintenance###

@categories.route('/toiletpaper-papertowels-tissues',methods=['GET','POST'])
@login_required
def toiletpaper_papertowels_tissues():
    name = 'toiletpapier,keukenpapier__zakdoeken'
    name_header = clean_name(name)

    static_directory = os.path.join(os.getcwd(),r'website/static')
    df_products_info = pd.read_csv(f'{static_directory}/webscrape_info_{name}.csv')
    products_info = df_products_info.to_dict('records')

    if request.method == 'POST':
        product_name = request.form.get('product_name')
        product_img = request.form.get('product_img')
        product_base_price = request.form.get('product_base_price')
        product_base_price_type = request.form.get('product_base_price_type')
        product_big_price = request.form.get('product_big_price')
        new_product = Selected_item(name=product_name,img=product_img,base_price=product_base_price,base_price_type=product_base_price_type,big_price=product_big_price, user_id=current_user.id)
        db.session.add(new_product)
        db.session.commit()
        if product_name != '':
            flash(f'Artiekel {product_name} toegevoegd aan mandje', category='success')

    return render_template("category.html",name_header=name_header,products_info=products_info, user=current_user)

@categories.route('/detergents',methods=['GET','POST'])
@login_required
def detergents():
    name = 'wasmiddelen'
    name_header = clean_name(name)

    static_directory = os.path.join(os.getcwd(),r'website/static')
    df_products_info = pd.read_csv(f'{static_directory}/webscrape_info_{name}.csv')
    products_info = df_products_info.to_dict('records')

    if request.method == 'POST':
        product_name = request.form.get('product_name')
        product_img = request.form.get('product_img')
        product_base_price = request.form.get('product_base_price')
        product_base_price_type = request.form.get('product_base_price_type')
        product_big_price = request.form.get('product_big_price')
        new_product = Selected_item(name=product_name,img=product_img,base_price=product_base_price,base_price_type=product_base_price_type,big_price=product_big_price, user_id=current_user.id)
        db.session.add(new_product)
        db.session.commit()
        if product_name != '':
            flash(f'Artiekel {product_name} toegevoegd aan mandje', category='success')

    return render_template("category.html",name_header=name_header,products_info=products_info, user=current_user)

@categories.route('/laundry-care',methods=['GET','POST'])
@login_required
def laundry_care():
    name = 'verzorging_van_de_was'
    name_header = clean_name(name)

    static_directory = os.path.join(os.getcwd(),r'website/static')
    df_products_info = pd.read_csv(f'{static_directory}/webscrape_info_{name}.csv')
    products_info = df_products_info.to_dict('records')

    if request.method == 'POST':
        product_name = request.form.get('product_name')
        product_img = request.form.get('product_img')
        product_base_price = request.form.get('product_base_price')
        product_base_price_type = request.form.get('product_base_price_type')
        product_big_price = request.form.get('product_big_price')
        new_product = Selected_item(name=product_name,img=product_img,base_price=product_base_price,base_price_type=product_base_price_type,big_price=product_big_price, user_id=current_user.id)
        db.session.add(new_product)
        db.session.commit()
        if product_name != '':
            flash(f'Artiekel {product_name} toegevoegd aan mandje', category='success')

    return render_template("category.html",name_header=name_header,products_info=products_info, user=current_user)

@categories.route('/dishwashing-products',methods=['GET','POST'])
@login_required
def dishwashing_products():
    name = 'Vaatwasproducten'
    name_header = clean_name(name)

    static_directory = os.path.join(os.getcwd(),r'website/static')
    df_products_info = pd.read_csv(f'{static_directory}/webscrape_info_{name}.csv')
    products_info = df_products_info.to_dict('records')

    if request.method == 'POST':
        product_name = request.form.get('product_name')
        product_img = request.form.get('product_img')
        product_base_price = request.form.get('product_base_price')
        product_base_price_type = request.form.get('product_base_price_type')
        product_big_price = request.form.get('product_big_price')
        new_product = Selected_item(name=product_name,img=product_img,base_price=product_base_price,base_price_type=product_base_price_type,big_price=product_big_price, user_id=current_user.id)
        db.session.add(new_product)
        db.session.commit()
        if product_name != '':
            flash(f'Artiekel {product_name} toegevoegd aan mandje', category='success')

    return render_template("category.html",name_header=name_header,products_info=products_info, user=current_user)

@categories.route('/cleaning-products',methods=['GET','POST'])
@login_required
def cleaning_products():
    name = 'schoonmaakproducten'
    name_header = clean_name(name)

    static_directory = os.path.join(os.getcwd(),r'website/static')
    df_products_info = pd.read_csv(f'{static_directory}/webscrape_info_{name}.csv')
    products_info = df_products_info.to_dict('records')

    if request.method == 'POST':
        product_name = request.form.get('product_name')
        product_img = request.form.get('product_img')
        product_base_price = request.form.get('product_base_price')
        product_base_price_type = request.form.get('product_base_price_type')
        product_big_price = request.form.get('product_big_price')
        new_product = Selected_item(name=product_name,img=product_img,base_price=product_base_price,base_price_type=product_base_price_type,big_price=product_big_price, user_id=current_user.id)
        db.session.add(new_product)
        db.session.commit()
        if product_name != '':
            flash(f'Artiekel {product_name} toegevoegd aan mandje', category='success')

    return render_template("category.html",name_header=name_header,products_info=products_info, user=current_user)

@categories.route('/airfreshener-refill',methods=['GET','POST'])
@login_required
def air_freshener_refill():
    name = 'luchtverfrissers__navullingen'
    name_header = clean_name(name)

    static_directory = os.path.join(os.getcwd(),r'website/static')
    df_products_info = pd.read_csv(f'{static_directory}/webscrape_info_{name}.csv')
    products_info = df_products_info.to_dict('records')

    if request.method == 'POST':
        product_name = request.form.get('product_name')
        product_img = request.form.get('product_img')
        product_base_price = request.form.get('product_base_price')
        product_base_price_type = request.form.get('product_base_price_type')
        product_big_price = request.form.get('product_big_price')
        new_product = Selected_item(name=product_name,img=product_img,base_price=product_base_price,base_price_type=product_base_price_type,big_price=product_big_price, user_id=current_user.id)
        db.session.add(new_product)
        db.session.commit()
        if product_name != '':
            flash(f'Artiekel {product_name} toegevoegd aan mandje', category='success')

    return render_template("category.html",name_header=name_header,products_info=products_info, user=current_user)

@categories.route('/maintenance-accessoires',methods=['GET','POST'])
@login_required
def maintenance_accessoires():
    name = 'onderhoudsaccessoires'
    name_header = clean_name(name)

    static_directory = os.path.join(os.getcwd(),r'website/static')
    df_products_info = pd.read_csv(f'{static_directory}/webscrape_info_{name}.csv')
    products_info = df_products_info.to_dict('records')

    if request.method == 'POST':
        product_name = request.form.get('product_name')
        product_img = request.form.get('product_img')
        product_base_price = request.form.get('product_base_price')
        product_base_price_type = request.form.get('product_base_price_type')
        product_big_price = request.form.get('product_big_price')
        new_product = Selected_item(name=product_name,img=product_img,base_price=product_base_price,base_price_type=product_base_price_type,big_price=product_big_price, user_id=current_user.id)
        db.session.add(new_product)
        db.session.commit()
        if product_name != '':
            flash(f'Artiekel {product_name} toegevoegd aan mandje', category='success')

    return render_template("category.html",name_header=name_header,products_info=products_info, user=current_user)

@categories.route('/cleaning-accessoires',methods=['GET','POST'])
@login_required
def cleaning_accessoires():
    name = 'huishoudaccessoires'
    name_header = clean_name(name)

    static_directory = os.path.join(os.getcwd(),r'website/static')
    df_products_info = pd.read_csv(f'{static_directory}/webscrape_info_{name}.csv')
    products_info = df_products_info.to_dict('records')

    if request.method == 'POST':
        product_name = request.form.get('product_name')
        product_img = request.form.get('product_img')
        product_base_price = request.form.get('product_base_price')
        product_base_price_type = request.form.get('product_base_price_type')
        product_big_price = request.form.get('product_big_price')
        new_product = Selected_item(name=product_name,img=product_img,base_price=product_base_price,base_price_type=product_base_price_type,big_price=product_big_price, user_id=current_user.id)
        db.session.add(new_product)
        db.session.commit()
        if product_name != '':
            flash(f'Artiekel {product_name} toegevoegd aan mandje', category='success')

    return render_template("category.html",name_header=name_header,products_info=products_info, user=current_user)

@categories.route('/pesticides',methods=['GET','POST'])
@login_required
def pesticides():
    name = 'insecticides'
    name_header = clean_name(name)

    static_directory = os.path.join(os.getcwd(),r'website/static')
    df_products_info = pd.read_csv(f'{static_directory}/webscrape_info_{name}.csv')
    products_info = df_products_info.to_dict('records')

    if request.method == 'POST':
        product_name = request.form.get('product_name')
        product_img = request.form.get('product_img')
        product_base_price = request.form.get('product_base_price')
        product_base_price_type = request.form.get('product_base_price_type')
        product_big_price = request.form.get('product_big_price')
        new_product = Selected_item(name=product_name,img=product_img,base_price=product_base_price,base_price_type=product_base_price_type,big_price=product_big_price, user_id=current_user.id)
        db.session.add(new_product)
        db.session.commit()
        if product_name != '':
            flash(f'Artiekel {product_name} toegevoegd aan mandje', category='success')

    return render_template("category.html",name_header=name_header,products_info=products_info, user=current_user)

### Cart-items page###

@categories.route('/cart-items', methods=['GET', 'POST'])
@login_required
def cart_items():
    if request.method == 'POST':
        itemId = request.form.get('id')
        userId = request.form.get('save_shoppinglist')
        if itemId:
            item = Selected_item.query.get(itemId)
            if item:
                if item.user_id == current_user.id:
                    db.session.delete(item)
                    db.session.commit()
                    flash(f'{item.name} verwijderd uit mandje')
        elif userId:
            user = User.query.get(userId)
            if user:
                if user.id == current_user.id:
                    if current_user.shoppinglist:
                        new_purchase = Purchases(user_id=current_user.id)
                        db.session.add(new_purchase)
                        db.session.commit()
                        for item in current_user.shoppinglist:
                            new_ordered_item = Ordered_item(name = item.name,img = item.img, base_price = item.base_price, base_price_type = item.base_price_type, big_price = item.big_price, purchase_id = new_purchase.id)
                            db.session.add(new_ordered_item)
                            db.session.delete(item)
                            db.session.commit()
                        flash(f"Winkelmandje succesvol doorgestuurd", category='success')
                        return redirect(url_for('views.home'))
                    else:
                        flash(f"Winkelmandje kan niet leeg worden opgeslaan", category='error')
    
    sum_prices = 0
    for item in current_user.shoppinglist:
        sum_prices += Decimal(item.base_price[:-1].replace(',','.'))
    #current_user.total_price = sum_prices  enkel nodig als ik echt in database wil opslaan

    return render_template("shopping_list_display.html",sum_prices=str(sum_prices), user=current_user)

