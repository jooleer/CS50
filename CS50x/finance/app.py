import os
import time

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd, return_symbol

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    userid = session["user_id"]
    row_users = db.execute("SELECT * FROM users WHERE id = ?", userid)
    cash_balance = row_users[0]["cash"]
    username = row_users[0]["username"]

    row_buy = db.execute("SELECT * FROM buy WHERE userid = ?", userid)
    row_portfolio = db.execute(
        "SELECT * FROM portfolio WHERE userid = ? AND shares > 0", userid)

    total_balance = 0
    list_prices = {}
    list_prices_usd = {}
    list_companies = {}
    list_total_value = {}

    for row in row_portfolio:
        iex_data = lookup(row["symbol"])
        list_prices_usd[row["symbol"]] = usd(iex_data["price"])
        list_prices[row["symbol"]] = iex_data["price"]
        list_companies[row["symbol"]] = iex_data["name"]
        total_balance += (iex_data["price"] * row["shares"])
        list_total_value[row["symbol"]] = usd(
            row["shares"] * iex_data["price"])

    total_balance += cash_balance
    cash_balance_usd = usd(cash_balance)
    total_balance_usd = usd(total_balance)
    return render_template("index.html", username=username, cash_balance_usd=cash_balance_usd, total_balance_usd=total_balance_usd, list_companies=list_companies, list_prices=list_prices, row_portfolio=row_portfolio, list_prices_usd=list_prices_usd, list_total_value=list_total_value)


@app.route("/topup", methods=["GET", "POST"])
@login_required
def topup():
    userid = session["user_id"]
    row_users = db.execute("SELECT * FROM users WHERE id = ?", userid)
    old_cash = row_users[0]["cash"]

    if request.method == "POST":
        deposit = request.form.get("deposit")

        if not deposit.isnumeric():
            return apology("Invalid amount")
        try:
            int(deposit)
        except (ValueError, TypeError):
            return apology("Invalid amount")

        # row_users = db.execute("SELECT cash FROM users WHERE id = ?", userid)
        # old_cash = row_users["cash"]
        new_cash = int(old_cash) + int(deposit)

        db.execute("UPDATE users SET cash = ? WHERE id = ?", new_cash, userid)
    else:
        return render_template("topup.html", name=row_users[0]["username"], balance=old_cash)

    return redirect("/")


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    userid = session["user_id"]
    row = db.execute("SELECT * FROM users WHERE id = ?", userid)
    balance = row[0]["cash"]
    name = row[0]["username"]
    balance_usd = usd(balance)

    if request.method == "POST":
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")

        if not shares.isnumeric():
            return apology("enter a valid amount of shares")
        if not symbol:
            return apology("you must enter a valid stock symbol")
        elif not shares or int(shares) < 0:
            return apology("enter a valid amount of shares")

        stock_data = lookup(symbol)
        try:
            share_price = stock_data["price"]
        except (TypeError, ValueError):
            return apology("you must enter a valid stock symbol")

        purchase_value = share_price * int(shares)
        if purchase_value > int(balance):
            return apology("sorry, your balance is insuffient")

        date = time.strftime('%Y-%m-%d %H:%M:%S')
        db.execute("INSERT INTO buy (userid, date, symbol, shares, share_price, purchase_value) VALUES (?, ?, ?, ?, ?, ?)",
                   userid, date, symbol, shares, share_price, purchase_value)
        new_cash = balance - purchase_value
        db.execute("UPDATE users SET cash = ? WHERE id = ?", new_cash, userid)
        row_portfolio = db.execute(
            "SELECT * FROM portfolio WHERE userid = ? AND symbol = ?", userid, symbol)

        try:
            if int(row_portfolio["shares"]) >= 0:

                old_shares = row_portfolio["shares"]
                new_shares = old_shares + shares
                average_price = (
                    (row_portfolio["shares"] * row_portfolio["share_average_price"]) + (shares * share_price)) / new_shares
                db.execute("UPDATE portfolio SET shares = ?, share_average_price = ? WHERE userid = ? AND symbol = ?",
                           new_shares, average_price, userid, symbol)
            else:
                db.execute("INSERT INTO portfolio (userid, symbol, shares, share_average_price) VALUES (?, ?, ?, ?)",
                           userid, symbol, shares, share_price)
        except TypeError:
            db.execute("INSERT INTO portfolio (userid, symbol, shares, share_average_price) VALUES (?, ?, ?, ?)",
                       userid, symbol, shares, share_price)
        else:
            return apology("idk what happened bruh")

        return redirect("/")

    return render_template("buy.html", balance_usd=balance_usd, name=name)


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    userid = session["user_id"]

    # row_users = db.execute("SELECT cash FROM users WHERE id = ?", userid)
    row_buy = db.execute(
        "SELECT * FROM buy WHERE userid = ? ORDER BY date", userid)
    row_sell = db.execute(
        "SELECT * FROM sell WHERE userid = ? ORDER BY date", userid)

    return render_template("history.html", row_buy=row_buy, row_sell=row_sell)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?",
                          request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.args.get("symbol"):
        symbol = request.args.get("symbol")
        return return_symbol(symbol)
    if request.method == "POST":
        symbol = request.form.get("symbol")
        return return_symbol(symbol)
    else:
        return render_template("quote.html")
    # return apology("TODO")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        password_confirmation = request.form.get("confirmation")

        if password != password_confirmation:
            return apology("passwords do not match", 400)
        # Ensure username was submitted
        if not username or (len(username) < 1):
            return apology("must provide username", 400)

        # Ensure password was submitted
        elif not password or (len(password) < 1):
            return apology("must provide password", 400)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?",
                          request.form.get("username"))

        # if username exists, refuse registration
        if len(rows) > 0:
            return apology("this username already exists", 400)

        # insert user into db
        hashed_pw = generate_password_hash(password)
        db.execute("INSERT INTO users (username, hash) VALUES (?, ?)",
                   username, hashed_pw)

        # Redirect user to home page
        return redirect("/")

    # no post data, return registration page
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""

    if request.method == "POST":
        userid = session["user_id"]

        symbol = request.form.get("symbol")
        shares_amount = request.form.get("shares")

        iex_data = lookup(symbol)

        if not shares_amount.isnumeric():
            return apology("Please select a valid amount of shares.")
        try:
            int(shares_amount)
        except (ValueError, TypeError):
            return apology("Please select a valid amount of shares.")
        # database queries
        row_users = db.execute("SELECT cash FROM users WHERE id = ?", userid)
        row_portfolio = db.execute(
            "SELECT * FROM portfolio WHERE userid = ? AND symbol = ?", userid, symbol)

        # count the amount of shares we currently have of the stock
        shares_in_portfolio = 0
        for row in row_portfolio:
            if symbol == row["symbol"]:
                shares_in_portfolio += row["shares"]

        # return error if not enough shares in portfolio
        if int(shares_in_portfolio) < int(shares_amount):
            statement_info = "You do not have {} shares of {} ({})".format(
                shares_amount, iex_data["name"], iex_data["symbol"])
            return apology(statement_info)

        # return error if invalid amount of shares is given
        if int(shares_amount) <= 0:
            return apology("Please select a valid amount of shares.")

        # we passed all checks, process sale and update database
        date = time.strftime('%Y-%m-%d %H:%M:%S')
        shares = int(shares_amount)
        share_price = float(iex_data["price"])
        sale_value = int(shares) * float(share_price)
        db.execute("INSERT INTO sell (userid, date, symbol, shares, share_price, sale_value) VALUES (?, ?, ?, ?, ?, ?)",
                   userid, date, symbol, shares, share_price, sale_value)
        new_cash = int(row_users[0]["cash"]) + int(sale_value)
        new_shares = int(row_portfolio[0]["shares"]) - int(shares)
        db.execute("UPDATE users SET cash = ? WHERE id = ?", new_cash, userid)
        db.execute("UPDATE portfolio SET shares = ? WHERE userid = ? AND symbol = ?",
                   new_shares, userid, symbol)

        return redirect("/")

    else:
        userid = session["user_id"]
        row_portfolio = db.execute(
            "SELECT * FROM portfolio WHERE userid = ? AND shares > 0", userid)

    return render_template("sell.html", row_portfolio=row_portfolio)
