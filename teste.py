{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "ename": "RuntimeError",
     "evalue": "Working outside of application context.\n\nThis typically means that you attempted to use functionality that needed\nthe current application. To solve this, set up an application context\nwith app.app_context(). See the documentation for more information.",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mRuntimeError\u001b[0m                              Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[2], line 60\u001b[0m\n\u001b[0;32m     57\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m redirect(url_for(\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mindex\u001b[39m\u001b[38;5;124m'\u001b[39m))\n\u001b[0;32m     59\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;18m__name__\u001b[39m \u001b[38;5;241m==\u001b[39m \u001b[38;5;124m'\u001b[39m\u001b[38;5;124m__main__\u001b[39m\u001b[38;5;124m'\u001b[39m:\n\u001b[1;32m---> 60\u001b[0m     \u001b[43mdb\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mcreate_all\u001b[49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\n\u001b[0;32m     61\u001b[0m     app\u001b[38;5;241m.\u001b[39mrun(debug\u001b[38;5;241m=\u001b[39m\u001b[38;5;28;01mTrue\u001b[39;00m)\n",
      "File \u001b[1;32mc:\\Users\\Ralvino\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\site-packages\\flask_sqlalchemy\\extension.py:900\u001b[0m, in \u001b[0;36mSQLAlchemy.create_all\u001b[1;34m(self, bind_key)\u001b[0m\n\u001b[0;32m    883\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21mcreate_all\u001b[39m(\u001b[38;5;28mself\u001b[39m, bind_key: \u001b[38;5;28mstr\u001b[39m \u001b[38;5;241m|\u001b[39m \u001b[38;5;28;01mNone\u001b[39;00m \u001b[38;5;241m|\u001b[39m \u001b[38;5;28mlist\u001b[39m[\u001b[38;5;28mstr\u001b[39m \u001b[38;5;241m|\u001b[39m \u001b[38;5;28;01mNone\u001b[39;00m] \u001b[38;5;241m=\u001b[39m \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m__all__\u001b[39m\u001b[38;5;124m\"\u001b[39m) \u001b[38;5;241m-\u001b[39m\u001b[38;5;241m>\u001b[39m \u001b[38;5;28;01mNone\u001b[39;00m:\n\u001b[0;32m    884\u001b[0m \u001b[38;5;250m    \u001b[39m\u001b[38;5;124;03m\"\"\"Create tables that do not exist in the database by calling\u001b[39;00m\n\u001b[0;32m    885\u001b[0m \u001b[38;5;124;03m    ``metadata.create_all()`` for all or some bind keys. This does not\u001b[39;00m\n\u001b[0;32m    886\u001b[0m \u001b[38;5;124;03m    update existing tables, use a migration library for that.\u001b[39;00m\n\u001b[1;32m   (...)\u001b[0m\n\u001b[0;32m    898\u001b[0m \u001b[38;5;124;03m        Added the ``bind`` and ``app`` parameters.\u001b[39;00m\n\u001b[0;32m    899\u001b[0m \u001b[38;5;124;03m    \"\"\"\u001b[39;00m\n\u001b[1;32m--> 900\u001b[0m     \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_call_for_binds\u001b[49m\u001b[43m(\u001b[49m\u001b[43mbind_key\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[38;5;124;43mcreate_all\u001b[39;49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[43m)\u001b[49m\n",
      "File \u001b[1;32mc:\\Users\\Ralvino\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\site-packages\\flask_sqlalchemy\\extension.py:871\u001b[0m, in \u001b[0;36mSQLAlchemy._call_for_binds\u001b[1;34m(self, bind_key, op_name)\u001b[0m\n\u001b[0;32m    869\u001b[0m \u001b[38;5;28;01mfor\u001b[39;00m key \u001b[38;5;129;01min\u001b[39;00m keys:\n\u001b[0;32m    870\u001b[0m     \u001b[38;5;28;01mtry\u001b[39;00m:\n\u001b[1;32m--> 871\u001b[0m         engine \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mengines\u001b[49m[key]\n\u001b[0;32m    872\u001b[0m     \u001b[38;5;28;01mexcept\u001b[39;00m \u001b[38;5;167;01mKeyError\u001b[39;00m:\n\u001b[0;32m    873\u001b[0m         message \u001b[38;5;241m=\u001b[39m \u001b[38;5;124mf\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mBind key \u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;132;01m{\u001b[39;00mkey\u001b[38;5;132;01m}\u001b[39;00m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124m is not in \u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mSQLALCHEMY_BINDS\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124m config.\u001b[39m\u001b[38;5;124m\"\u001b[39m\n",
      "File \u001b[1;32mc:\\Users\\Ralvino\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\site-packages\\flask_sqlalchemy\\extension.py:687\u001b[0m, in \u001b[0;36mSQLAlchemy.engines\u001b[1;34m(self)\u001b[0m\n\u001b[0;32m    674\u001b[0m \u001b[38;5;129m@property\u001b[39m\n\u001b[0;32m    675\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21mengines\u001b[39m(\u001b[38;5;28mself\u001b[39m) \u001b[38;5;241m-\u001b[39m\u001b[38;5;241m>\u001b[39m t\u001b[38;5;241m.\u001b[39mMapping[\u001b[38;5;28mstr\u001b[39m \u001b[38;5;241m|\u001b[39m \u001b[38;5;28;01mNone\u001b[39;00m, sa\u001b[38;5;241m.\u001b[39mengine\u001b[38;5;241m.\u001b[39mEngine]:\n\u001b[0;32m    676\u001b[0m \u001b[38;5;250m    \u001b[39m\u001b[38;5;124;03m\"\"\"Map of bind keys to :class:`sqlalchemy.engine.Engine` instances for current\u001b[39;00m\n\u001b[0;32m    677\u001b[0m \u001b[38;5;124;03m    application. The ``None`` key refers to the default engine, and is available as\u001b[39;00m\n\u001b[0;32m    678\u001b[0m \u001b[38;5;124;03m    :attr:`engine`.\u001b[39;00m\n\u001b[1;32m   (...)\u001b[0m\n\u001b[0;32m    685\u001b[0m \u001b[38;5;124;03m    .. versionadded:: 3.0\u001b[39;00m\n\u001b[0;32m    686\u001b[0m \u001b[38;5;124;03m    \"\"\"\u001b[39;00m\n\u001b[1;32m--> 687\u001b[0m     app \u001b[38;5;241m=\u001b[39m \u001b[43mcurrent_app\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_get_current_object\u001b[49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m  \u001b[38;5;66;03m# type: ignore[attr-defined]\u001b[39;00m\n\u001b[0;32m    689\u001b[0m     \u001b[38;5;28;01mif\u001b[39;00m app \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;129;01min\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_app_engines:\n\u001b[0;32m    690\u001b[0m         \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mRuntimeError\u001b[39;00m(\n\u001b[0;32m    691\u001b[0m             \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mThe current Flask app is not registered with this \u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mSQLAlchemy\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    692\u001b[0m             \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m instance. Did you forget to call \u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124minit_app\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124m, or did you create\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    693\u001b[0m             \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m multiple \u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mSQLAlchemy\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124m instances?\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    694\u001b[0m         )\n",
      "File \u001b[1;32mc:\\Users\\Ralvino\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\site-packages\\werkzeug\\local.py:508\u001b[0m, in \u001b[0;36mLocalProxy.__init__.<locals>._get_current_object\u001b[1;34m()\u001b[0m\n\u001b[0;32m    506\u001b[0m     obj \u001b[38;5;241m=\u001b[39m local\u001b[38;5;241m.\u001b[39mget()\n\u001b[0;32m    507\u001b[0m \u001b[38;5;28;01mexcept\u001b[39;00m \u001b[38;5;167;01mLookupError\u001b[39;00m:\n\u001b[1;32m--> 508\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mRuntimeError\u001b[39;00m(unbound_message) \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m\n\u001b[0;32m    510\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m get_name(obj)\n",
      "\u001b[1;31mRuntimeError\u001b[0m: Working outside of application context.\n\nThis typically means that you attempted to use functionality that needed\nthe current application. To solve this, set up an application context\nwith app.app_context(). See the documentation for more information."
     ]
    }
   ],
   "source": [
    "from flask import Flask, render_template, request, redirect, url_for\n",
    "from flask_sqlalchemy import SQLAlchemy\n",
    "\n",
    "app = Flask(__name__)\n",
    "app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'\n",
    "db = SQLAlchemy(app)\n",
    "\n",
    "class Product(db.Model):\n",
    "    id = db.Column(db.Integer, primary_key=True)\n",
    "    name = db.Column(db.String(255), nullable=False)\n",
    "    code = db.Column(db.String(50), nullable=False, unique=True)\n",
    "    description = db.Column(db.Text, nullable=True)\n",
    "    price = db.Column(db.Float, nullable=False)\n",
    "\n",
    "@app.route('/')\n",
    "def index():\n",
    "    products = Product.query.all()\n",
    "    return render_template('index.html', products=products)\n",
    "\n",
    "@app.route('/create', methods=['GET', 'POST'])\n",
    "def create():\n",
    "    if request.method == 'POST':\n",
    "        name = request.form['name']\n",
    "        code = request.form['code']\n",
    "        description = request.form['description']\n",
    "        price = float(request.form['price'])\n",
    "\n",
    "        new_product = Product(name=name, code=code, description=description, price=price)\n",
    "        db.session.add(new_product)\n",
    "        db.session.commit()\n",
    "\n",
    "        return redirect(url_for('index'))\n",
    "\n",
    "    return render_template('create.html')\n",
    "\n",
    "@app.route('/edit/<int:id>', methods=['GET', 'POST'])\n",
    "def edit(id):\n",
    "    product = Product.query.get(id)\n",
    "\n",
    "    if request.method == 'POST':\n",
    "        product.name = request.form['name']\n",
    "        product.code = request.form['code']\n",
    "        product.description = request.form['description']\n",
    "        product.price = float(request.form['price'])\n",
    "\n",
    "        db.session.commit()\n",
    "\n",
    "        return redirect(url_for('index'))\n",
    "\n",
    "    return render_template('edit.html', product=product)\n",
    "\n",
    "@app.route('/delete/<int:id>')\n",
    "def delete(id):\n",
    "    product = Product.query.get(id)\n",
    "    db.session.delete(product)\n",
    "    db.session.commit()\n",
    "    return redirect(url_for('index'))\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    db.create_all()\n",
    "    app.run(debug=True)\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.0b4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
