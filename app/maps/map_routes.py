from flask import Blueprint, render_template, request
from app import matching
from app import cursor
from app import conn
from app.users.auth_routes import email

maps = Blueprint('maps', __name__)

# Map Routes


@maps.route('/map1')
def map1():
    return render_template('map1.html')

# Gets the corrdinates of the user's location , matches users and updates the DB


@maps.route('/map2', methods=['GET', 'POST'])
def map2():
    if request.method == "POST":
        req = request.form
        scoords = req['scoords']
        ecoords = req['ecoords']
        cursor.execute(
            """SELECT * FROM `users`  WHERE `email` LIKE '{}' """.format(email))
        user = cursor.fetchone()
        pooling = 1
        cursor.execute(
            """UPDATE `users` set pooling='{}' WHERE email='{}' """.format(pooling, email))
        cursor.execute(
            """UPDATE `users` set starting_coords='{}' WHERE email='{}' """.format(scoords, email))
        cursor.execute(
            """UPDATE `users` set ending_coords='{}' WHERE email='{}' """.format(ecoords, email))
        conn.commit()
    cursor.execute(
        """SELECT * FROM `users`  WHERE `email` LIKE '{}' """.format(email))
    user = cursor.fetchone()
    cursor.execute("""SELECT * FROM `users` """)
    records = cursor.fetchall()
    u1 = (user[1], user[7])
    u2 = (user[1], user[8])
    d1 = {record[1]: record[7] for record in records}
    d2 = {record[1]: record[8] for record in records}
    # User's match based on compatibility types
    max_user = matching.match(u2, d2)
    cursor.execute(
        """SELECT * FROM `users`  WHERE `name` LIKE '{}' """.format(max_user))
    usr_phn = cursor.fetchone()
    phn = usr_phn[4]
    pooling = 0
    cursor.execute(
        """UPDATE `users` set pooling='{}' WHERE email='{}' """.format(pooling, email))
    return render_template('map2.html', user=max_user, phn=phn)
