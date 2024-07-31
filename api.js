
const API_EndPoint = "https://test.bsdd.buildingsmart.org/api/";
const headers = {
  "Content-Type": "application/json",
  Accept: "application/json",
};

async function searchIfcElements(searchTerm) {
  const payload = {
    DictionaryUri:
      "https://identifier.buildingsmart.org/uri/buildingsmart/ifc/4.3",
    SearchText: searchTerm,
  };
  const response = await axios.get(`${API_EndPoint}SearchInDictionary/v1`, {
    headers,
    params: payload,
  });
  const elements = response.data.dictionary.classes;
  // displayResults(elements);
  return elements
}


async function searchIfcProperties(searchTerm) {
  const payload = {
    DictionaryUri:
      "https://identifier.buildingsmart.org/uri/buildingsmart/ifc/4.3",
    ClassUri: searchTerm,
  };
  const response = await axios.get(`${API_EndPoint}/Class/Properties/v1`, {
    headers,
    params: payload,
  });
  const elements = response.data.classProperties;
  // displayResults(elements);
  return elements;
}

function performSearch(searchTerm) {
   if (searchTerm) {
      searchIfcElements(searchTerm);
   }
}

function displayResults(elements) {
  const resultsDiv = document.getElementById("results");
  resultsDiv.innerHTML = "";
  elements.forEach((el) => {
    const p = document.createElement("p");
    p.textContent = el.name;
    resultsDiv.appendChild(p);
  });
}

function createFormDataState1() {
    
}
