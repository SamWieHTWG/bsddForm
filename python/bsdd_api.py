import csv
import requests
import requests.auth
import json



# API ressources
Resource_Domains = "Domain/v2"
Resource_Classification = "Class/v1"
Resource_Relations = "Class/Relations/v1"
Resource_Classification_Properties = "Class/Properties/v1"
Resource_Prop_Details = "Property/v4"
Resource_Prop_Val_Details = "PropertyValue/v2"

API_EndPoint ='https://test.bsdd.buildingsmart.org/api/'
headers = {'content-type': 'application/json', 'Accept': 'application/json'}

def search_ifc_elements(searchTerm):
    payload = dict()
    payload["DictionaryUri"] = "https://identifier.buildingsmart.org/uri/buildingsmart/ifc/4.3"
    payload["SearchText"] = searchTerm
    res = mResponse = requests.get(API_EndPoint + "/SearchInDictionary/v1", headers=headers, params=payload)
    mResponse = res.json()
    els = mResponse["dictionary"]["classes"]
    return els

def search_ifc_el_properties(uri):
    payload = dict()
    payload["ClassUri"] = uri
    mResponse = requests.get(API_EndPoint + "Class/Properties/v1", headers=headers, params=payload).json()
    props = mResponse["classProperties"]
    json.dump(props, open("props.json", "w"), indent=2)
    return props

if 0:
    #################################

    text = input("Enter search term\n")

    # Frage 2: Welche Baustoffe/Klassen gibt es für Beton in VHF?
    # get classes of IFC
    payload = dict()
    payload["DictionaryUri"] = "https://identifier.buildingsmart.org/uri/buildingsmart/ifc/4.3"
    payload["SearchText"] = text
    res = mResponse = requests.get(API_EndPoint + "/SearchInDictionary/v1", headers=headers, params=payload)
    mResponse = res.json()
    json.dump(mResponse, open("ifc_dict.json", "w"), indent=2)
    els = mResponse["dictionary"]["classes"]
    [print(el["name"]) for el in els]


    text = input("Enter class name\n")

    for el in els:
        if el["name"] == text:
            break


    payload = dict()
    payload["ClassUri"] = el["uri"]
    mResponse = requests.get(API_EndPoint + "Class/Properties/v1", headers=headers, params=payload).json()
    [print(el["name"]) for el in mResponse["classProperties"]]
    props = mResponse["classProperties"]

    stop = 1



