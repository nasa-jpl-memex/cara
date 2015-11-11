import os
from flask import Flask, request, redirect, url_for, render_template, jsonify
from flask_wtf import Form
from wtforms import StringField, TextField, TextAreaField, DateField, SelectField, RadioField, BooleanField
from wtforms.validators import DataRequired

app = Flask(__name__)


import smtplib
from email.mime.text import MIMEText


def send_mail(form):
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
    client_email = "mail -s 'Memex Crawl Request' {0} <<< 'Thank you for submitting your crawl data acquisition request to NASA JPL. Someone from the Crawl Team will contact you personally certainly within the next 24 hours. Our Crawl Infrastructure is already working on acquiring your requested data. If you have any issues, please do not hesitate to contact us on memex-crawl@jpl.nasa.gov. Thank you'".format(email)
    memex_email = "mail -s '[New Crawl Request]' boustani@jpl.nasa.gov <<< 'Request details: \n First Name:{0} \n Last Name:{1} \n Email: {2} \n Description: {3} \n Crawl Type: {4} \n Recurring: {5} \n Seed Urls: {6} \n Crawling Config: {7} \n Content Type: {8} \n How much data: {9} \n Custom Metrics: {10} \n Extraction: {11} \n Common Data Repository: {12} \n Raw Files: {13} \n Nutch Sequence: {14} \n Custom Schema: {15} \n Common Crawl Format: {16} \n WARC: {17} \n Needed by: {18} \n \n Thanks \n Memex Crawl Team'".format(first, last, email, description, crawl_type, recurring, seed_ulrs, crawling_config, content_type, how_much_data, custom_metrics, extraction, common_data_repository, raw_files, nutch_sequence_files, custom_schema, common_crawl_format, warc, needed_by)
    os.system(client_email)
    os.system(memex_email)

    
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
    needed_by = StringField('Needed by', validators=[DataRequired(False)])


    
@app.route('/', methods=('GET', 'POST'))
def index():
    message = "Welcome to the DARPA Memex crawl data request CrawlForm provided by NASA JPL. This form enables clients to submit jobs to be processed and delivered by the NASA JPL Team. A member of the Crawl Team will also reach out and ensure that the Crawl job meets your specifications and exceptions. We encourage you to provide as much input into the fields below as possible."
    form = MyForm()
    error = ""
    if form.validate_on_submit():
        send_mail(form)
        return redirect('/success')
    else:
        pass
    return render_template('index.html', form=form, error=error, message=message, backhome="")


@app.route("/success")
def success():
    backhome = "True"
    message = "Thank you for submitting your crawl data acquisition request to NASA JPL. Someone from the Crawl Team will contact you personally certainly within the next 24 hours. Our Crawl Infrastructure is already working on acquiring your requested data. If you have any issues, please do not hesitate to contact us on memex-crawl@jpl.nasa.gov. Thank you"
    return render_template('index.html', message=message, backhome=backhome)


if __name__ == "__main__":
    app.debug = True
    app.secret_key = 's3cr3t'
    app.run(host="0.0.0.0", port=4000, debug=True)
