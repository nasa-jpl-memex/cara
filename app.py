
from flask import Flask, request, redirect, url_for, render_template, jsonify
from flask_wtf import Form
from wtforms import StringField, TextField, TextAreaField, DateField, SelectField, RadioField, BooleanField
from wtforms.validators import DataRequired

app = Flask(__name__)


import smtplib
from email.mime.text import MIMEText


def send_mail():
    message = """Test content"""
    
    email = MIMEText(message)
    email['From'] = "mazi@text.com"
    email['To'] = "maziyar_b4@yahoo.com"
    #email['Cc'] = "Thomas.Painter@jpl.nasa.gov,Kathryn.J.Bormann@jpl.nasa.gov"
    email["Subject"] = "Test Subject."
    
    server = smtplib.SMTP("localhost")
    
    try:
        server.sendmail(
            email["From"],
            email["To"].split(','),#+ email["Cc"].split(','),
            email.as_string()
        )
    finally:
        server.quit()


#send_mail()

    
class MyForm(Form):
    first = StringField('First', validators=[DataRequired()])
    last = StringField('Last', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    description = TextAreaField('Description of Use Case', validators=[DataRequired()])
    crawl_type = RadioField(u'Crawl Type', choices=[('exploratory', 'Exploratory'), ('defined', 'Defined'), ('particula_depth', 'Particula Depth')])
    recurring = StringField('Recurring', validators=[DataRequired()])
    seed_ulrs = TextAreaField('Seed Urls', validators=[DataRequired()])
    crawling_config = TextAreaField('Crawling configuration request', validators=[DataRequired()])
    content_type = RadioField('Content Type', choices=[('images', 'Images'), ('videos', 'Videos'), ('multimedia', 'Multimedia (images + videos)'), ('everything', 'Everything')])
    how_much_data = StringField('How much data', validators=[DataRequired()])
    custom_metrics = StringField('Custom Metrics', validators=[DataRequired()])
    extraction = TextAreaField('Extraction', validators=[DataRequired()])
    common_data_repository = BooleanField('Common Data Repository', validators=[DataRequired(False)])
    raw_files = BooleanField('Raw files', validators=[DataRequired(False)])
    nutch_sequence_files = BooleanField('Nutch Sequence Files', validators=[DataRequired(False)])
    custom_schema = BooleanField('Custom Schema', validators=[DataRequired(False)])
    common_crawl_format = BooleanField('Common Crawl Format', validators=[DataRequired(False)])
    warc = BooleanField('WARC', validators=[DataRequired(False)])
    needed_by = DateField('Needed by', validators=[DataRequired(False)])


    
@app.route('/', methods=('GET', 'POST'))
def index():
    message = "Welcome to the DARPA Memex crawl data request CrawlForm provided by NASA JPL. This form enables clients to submit jobs to be processed and delivered by the NASA JPL Team. A member of the Crawl Team will also reach out and ensure that the Crawl job meets your specifications and exceptions. We encourage you to provide as much input into the fields below as possible."
    form = MyForm()
    error = ""
    if form.validate_on_submit():
        first = form.first.data
        last = form.last.data
        email = form.email.data
        description = form.description.data
        crawl_type = form.crawl_type.data
        recurring = form.recurring.data
        seed_ulrs = form.seed_ulrs.data
        crawling_config = form.crawling_config.data
        content_type = form.content_type.data
        how_much_data = form.how_much_data.data
        custom_metrics = form.custom_metrics.data
        extraction = form.extraction.data
        common_data_repository = form.common_data_repository.data
        raw_files = form.raw_files.data
        nutch_sequence_files = form.nutch_sequence_files.data
        custom_schema = form.custom_schema.data
        common_crawl_format = form.common_crawl_format.data
        warc = form.warc.data
        needed_by = form.needed_by.data
        #execfile("script/email.py") 
        return redirect('/success')
    else:
        pass
        #error = "Faild to send request. Please make sure to complete all fields."

    return render_template('index.html', form=form, error=error, message=message, backhome="")


@app.route("/success")
def success():
    backhome = "True"
    message = "Thank you for submitting your crawl data acquisition request to NASA JPL. Someone from the Crawl Team will contact you personally certainly within the next 24 hours. Our Crawl Infrastructure is already working on acquiring your requested data. If you have any issues, please do not hesitate to contact us on memex-crawl@jpl.nasa.gov. Thank you"
    return render_template('index.html', message=message, backhome=backhome)


if __name__ == "__main__":
    app.debug = True
    app.secret_key = 's3cr3t'
    app.run(host="127.0.0.1", port=5000, debug=True)


# Input
# Text area
# Dropdown
# Send button
# lists
#     radio button
#     checkboxes
# Checkbox
