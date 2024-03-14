from flask.views import MethodView
from wtforms import Form, StringField, SubmitField, FormField
from flask import Flask, render_template, request
from flatmates_bill import flat

app = Flask(__name__)


class HomePage(MethodView):

    def get(self):
        return render_template('index.html')


class BillFormPage(MethodView):

    def get(self):
        bill_form = BillForm()
        return render_template('bill_form_page.html', billform=bill_form)


class ResultsPage(MethodView):

    def post(self):
        billform = BillForm(request.form)
        amount = billform.amount.data
        period = billform.period.data

        bill = flat.Bill(amount=amount, period=period)
        flatemate1 = flat.Flatmate(
            name=billform.flatmate1.data["name_"], days_in_house=billform.flatmate1.data["days_in_house"])
        flatemate2 = flat.Flatmate(
            name=billform.flatmate2.data["name_"], days_in_house=billform.flatmate2.data["days_in_house"])

        result_string = f"{flatemate1.name} pays {flatemate1.pays(bill, [flatemate1,flatemate2])}<br>{flatemate2.name} pays {flatemate2.pays(bill, [flatemate1,flatemate2])}"

        return render_template('results.html', result_string=result_string)


class Flatmate(Form):
    name_ = StringField("Name: ", render_kw={"placeholder": "First Name"})
    days_in_house = StringField("Days in House: ", render_kw={
                                "placeholder": "Amount"})


class BillForm(Form):
    amount = StringField("Bill Amount: ", render_kw={"placeholder": "Amount"})
    period = StringField("Bill Period: ", render_kw={"placeholder": "MM/YYYY"})
    flatmate1 = FormField(Flatmate)
    flatmate2 = FormField(Flatmate)
    button = SubmitField("Calculate")


app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
app.add_url_rule('/bill', view_func=BillFormPage.as_view('bill_form_page'))
app.add_url_rule('/results', view_func=ResultsPage.as_view('results_page'))

app.run(debug=True)
