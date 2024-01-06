from flask import Blueprint, current_app, redirect, render_template, url_for

from hotelpython.models.models import Address, Hotel, db

from .forms import NewHotelForm, NewRoleForm

portal = Blueprint('portal', __name__, template_folder="templates")

HOTEL = "The Lee"  # load from db


@portal.route("/")
def home():
    """Not done yet"""
    elements = {"title": "About Us", "navbrand": HOTEL}
    return render_template("home.html", elements=elements)


@portal.route("/schedule")
def schedule():
    """Not done yet"""
    elements = {"title": "About Us", "navbrand": HOTEL}
    return render_template("schedule.html", elements=elements)


@portal.route("/manage-hotels/", methods=["GET", "POST"])
def manage_hotels():
    """Needs review"""
    # hotel list = db.session.query(Hotel).all
    elements = {"title": "Manage Hotels", "navbrand": HOTEL}
    return render_template("manage_hotels.html", elements=elements)


@portal.route("/create-new-hotel/", methods=["GET", "POST"])
def create_new_hotel():
    """Not done yet"""
    nh_form = NewHotelForm()
    if nh_form.validate_on_submit():
        addr = Address(
            street=nh_form.street.data,
            city=nh_form.city.data,
            state=nh_form.state.data,
            zip=nh_form.zip.data,
        )
        with current_app.app_context():
            db.session.add(addr)
            db.session.flush()  # this synchronizes this session with db
            address_id = addr.id
        hotel = Hotel(
            hotel=nh_form.hotel.data,
            floors=nh_form.floors.data,
            address_id=address_id,
        )
        with current_app.app_context():
            db.session.add(hotel)
            db.session.commit()
            new_hotel = hotel.id
        return redirect(url_for("portal.select_hotel", hotel_id=new_hotel))
    elements = {
        "title": "Portal",
        "navbrand": HOTEL,
    }
    return render_template("create_new_hotel.html", elements=elements, nh_form=nh_form)


@portal.route("/manage-hotels/<int:hotel_id>")
def select_hotel(hotel_id):
    """Not done yet"""
    hotel = db.get_or_404(Hotel, hotel_id)
    elements = {
        "title": "Manage Hotel",
        "navbrand": hotel.hotel,
    }
    return render_template("selected_hotel.html",
                           elements=elements,
                           hotel=hotel)


@portal.route("/manage-roles/", methods=["GET", "POST"])
def manage_roles():
    createForm = NewRoleForm()
    elements = {"title": "Manage Roles", "navbrand": HOTEL}
    return render_template("manage_roles.html", elements=elements)


@portal.route("/manage-employees/")
def manage_employees():
    """Not done yet"""
    employees = []  # db.session.query(Employee).all
    elements = {
        "title": "Manage Employees",
        "navbrand": HOTEL,
        "employees": employees
    }
    return render_template("manage_employees.html", elements=elements)


@portal.route("/manage-rooms/")
def manage_rooms():
    return render_template("manage_rooms.html")


@portal.route("/reservations/")
def manage_reservations():
    return render_template("reservations.html")


@portal.route("reservations/manage/<int:res_id>")
def manage_reservation(res_id):
    return render_template("manage_reservation.html")
