from flask import Flask, render_template, request
from python.bsdd_api import *
import json

app = Flask(__name__)   
app.config['SECRET_KEY'] = 'your_secret_key_here'
app.state =1

useDebug = 0

if not useDebug:
    app.state = 0

def eval_form_state_0(form):
    response = form.ifc_search_term.data
    els = search_ifc_elements(response)
    form.ifc_elements.choices = [(el["uri"],el['name']) for idx, el in enumerate(els)]
    return form

def eval_form_state_1(form):
    response = form.ifc_elements.data
    props = search_ifc_el_properties(response)

    for prop in props:
        stop = 1
        # setattr(SimpleForm, 'dynamic_field', StringField('Dynamic Field', validators=[Optional()]))
    form.ifc_elements.choices = [(el["uri"],el['name']) for idx, el in enumerate(els)]
    return form

def form_submit(form):
    if app.state == 0:
        app.state +=1
        form = eval_form_state_0(form)
    elif app.state == 1:
        app.state +=1
        form = eval_form_state_1(form)
        
    return form


formData  =  {
          "fields": [
            {
              "desc": "IfcSearchTerm",
              "type": "text",
            },
            {
              "desc": "IfcClass",
              "type": "radio",
              "options": [
                { "value": "option1", "link":  'https://www.google.de' },
                { "value": "option2", "link":  'https://www.google.de' },
                { "value": "option3", "link":  'https://www.google.de' },
              ],
            },
          ],
        }

def get_form():
    form = {}
    fields = []
    if app.state == 0:
        fields.append({           
              "desc": "IfcSearchTerm",
              "type": "text",
            })
    elif app.state == 1:
        
        ifc_search_term = request.form.get('IfcSearchTerm')
        input = { "desc": "IfcClass",
              "type": "radio",
              "options" : []}
        input["htmlBefore"] = ""
        input["htmlBefore"] += "<h4>Choose IFC Class</h4>"
        if useDebug:
            els =  json.load(open("class.json", 'r'))
        else:
            els = search_ifc_elements(ifc_search_term)
        for el in els:
            input["options"].append( {"value":el['name'] , "link": el["uri"]})

        fields.append(input)

    elif app.state == 2:
        classVal = request.form.get('IfcClass')
        if useDebug:
            props =  json.load(open("props.json", 'r'))
        else:
            props = search_ifc_el_properties(classVal)
        for prop in props:
            input  ={}
            input["desc"] = prop["name"]
            input["link"] = prop["uri"]
            input["htmlBefore"] = ""
            input["htmlBefore"] += "<h4>"+prop["name"]+"</h4>"
            input["htmlBefore"] += "<p>"+prop["description"]+' <a href="'+prop["uri"] + '" target="_blank">More Information</a>' +"</p>"
            if not "dataType" in prop:
                continue
            dataType = prop["dataType"]
            if dataType == "String":
                input["type"] = "text"         
            elif  dataType == "Real" or dataType == "Integer" or dataType == "Boolean":
                input["type"] = "number"
            else:
                print(dataType)
                continue
            
            fields.append(input)
        stop = 1

    form["fields"] = fields

    return form


@app.route('/submit', methods=['GET', 'POST'])
def submit():
    app.state += 1


    # ifc_class = request.form.getlist('IfcClass')
    
    form = get_form()
    return render_template('form.html', formData = form)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = get_form()
    return render_template('form.html', formData = form)

if __name__ == '__main__':
    app.run(debug=True)
