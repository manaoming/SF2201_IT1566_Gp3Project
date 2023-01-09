from flask import Flask, render_template, request, redirect, url_for, flash
from Forms import CreateUserForm, CreateCustomerForm, DestinationForm, ItineraryForm
import User
import shelve
import Customer
import TravelPlan
app = Flask(__name__)


accommodation_list = {"Destination 1": {  # To use for resolving identifier to name in viewing oage
                '': 'Select',
                '1_1': 'Accommodation 1 for Destination 1',
                '1_2': 'Accommodation 2 for Destination 1'},
                            "Destination 3": {
                '': 'Select',
                '3_1': 'Accommodation 1 for Destination 3',
                '3_2': 'Accommodation 2 for Destination 3'}
                            }
destinations_choices = {"Destination 1": [  # To pass to the booking page as the choices for accommodation for different destination
                ('', 'Select'),
                ('1_1', 'Accommodation 1 for Destination 1'),
                ('1_2', 'Accommodation 2 for Destination 1')],
                            "Destination 3": [
                ('', 'Select'),
                ('3_1', 'Accommodation 1 for Destination 3'),
                ('3_2', 'Accommodation 2 for Destination 3')]
                            }


@app.route('/')
def home():
    return render_template("home.html")


@app.route("/base")
def base():
    return render_template("base.html")


@app.route('/contactUs')
def contact_us():
    return render_template("contactUs.html")


@app.route('/viewplans', methods=["GET", "POST"])
def view_plans():
    plans = shelve.open("plans", "w")
    if "0" not in plans:
        plans["0"] = []
    if request.form:
        print(request.form)
        if "plan_to_edit" in request.form:
            edit_index = int(request.form["plan_to_edit"])
            temp = plans["0"][edit_index]  # this should be an array.
            temp.set_people(request.form["people"])
            temp.set_duration(request.form["duration"])
            plans["0"] = plans["0"][:edit_index] + [temp] + plans["0"][edit_index+1:]

        if "plan_to_del" in request.form:
            del_index = int(request.form["plan_to_del"])
            plans["0"] = plans["0"][:del_index] + plans["0"][del_index+1:]

    plans_list = plans["0"]
    plans.close()
    print("Length of list:", len(plans_list))
    return render_template('wireframe_view.html', plans_list=plans_list, plans_count=len(plans_list), accommodation_list=accommodation_list)


@app.route("/wireframe", methods=["POST", "GET"])
def wireframe():
    destinations = {"Destination 1": "Description for destination", "Destination 2": "Description for destination", "Destination 3": "Description for destination", "Destination 4": "Description for destination", "Destination 5": "Description for destination", "Destination 6": "Description for destination", "Destination 7": "Description for destination"}

    if not request.form:
        return render_template("select_destination.html", destinations=destinations, form=DestinationForm())
    itinerary_form = ItineraryForm(request.form)
    if "destination" in request.form:
        destinations_choices = {"Destination 1": [
                ('', 'Select'),
                ('1_1', 'Accommodation 1 for Destination 1'),
                ('1_2', 'Accommodation 2 for Destination 1')],
                            "Destination 3": [
                ('', 'Select'),
                ('3_1', 'Accommodation 1 for Destination 3'),
                ('3_2', 'Accommodation 2 for Destination 3')]
                            }
        try:
            itinerary_form.accommodation.choices = destinations_choices[request.form["destination"]]
        except KeyError:
            return render_template("base.html")
    if request.method == "POST":
        print(request)
        print(request.form)
        print(itinerary_form.validate())
        for field in itinerary_form:
            print(field.errors)
        if "destination" in request.form and "people" not in request.form and request.form["destination"] in destinations:
            return render_template("wireframe_form.html", form=itinerary_form, dest_form=DestinationForm(request.form), destinations=destinations, destination=request.form['destination'])
        elif "people" in request.form and ItineraryForm(request.form).validate():
            print("Success!!")
            TravelPlan.add_plan(**request.form)
            return redirect('/viewplans')
            return render_template("wireframe.html", destinations=destinations, form=DestinationForm())
        else:
            print("Invalid input")
            return render_template("wireframe_form.html", form=itinerary_form, dest_form=DestinationForm(request.form), destinations=destinations, destination=request.form['destination'])



@app.route("/createUser", methods=["GET", "POST"])
def create_user():
    create_user_form = CreateUserForm(request.form)
    try:
        if request.method == 'POST' and create_user_form.validate():
            users = shelve.open("Users")
            user = User.User(create_user_form.first_name.data, create_user_form.last_name.data, create_user_form.gender.data, create_user_form.membership.data, create_user_form.remarks.data)
            userid = user.get_userid()
            users[userid] = user
            print(users[userid].get_firstname(), users[userid].get_firstname(), "was stored in user.db successfully with user_id ==", users[userid].get_userid())
            users.close()
        return render_template('createUser.html', form=create_user_form)
    except IOError:
        print("Error occurred accessing user database")


@app.route("/createCustomer", methods=["GET", "POST"])
def create_customer():
    create_customer_form = CreateCustomerForm(request.form)
    try:
        if request.method == 'POST' and create_customer_form.validate():
            customers = shelve.open("Customers")
            customer = Customer.Customer(create_customer_form.first_name.data, create_customer_form.last_name.data, create_customer_form.gender.data, create_customer_form.membership.data, create_customer_form.remarks.data, create_customer_form.email.data, create_customer_form.date_joined.data, create_customer_form.address.data)
            customerid = customer.get_userid()
            customers[customerid] = customer
            print(customers[customerid].get_firstname(), customers[customerid].get_lastname(), "was stored in user.db successfully with user_id ==", customers[customerid].get_customerid())
            customers.close()
        return render_template('createCustomer.html', form=create_customer_form)
    except IOError:
        print("Error occurred accessing customer database")


if __name__ == '__main__':
    app.run()
