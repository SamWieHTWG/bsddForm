function createForm(formData) {
     var form = document.createElement("form");
        form.id = "dynamicForm";
        form.method = "post";
        form.action = "#";

        // Iterate over JSON data to create input elements
        for (let i = 0; i < formData["fields"].length; i++) {
          var field = formData["fields"][i];

          var inputDiv = document.createElement("div");

          if( "htmlBefore" in field){
            console.log(field.htmlBefore)
            inputDiv.innerHTML = field.htmlBefore
          }

          var input = document.createElement("input");
          input.type = field["type"];
          if (input.type == "radio") {
            const container = document.getElementById("container");
            for (let j = 0; j < field["options"].length; j++) {
              var opt = field["options"][j];
              var radioButton = document.createElement("input");
              radioButton.type = "radio";
              radioButton.name = field.desc;
              radioButton.value = opt.link;

              // Create a label for the radio button
              const label = document.createElement("label");
              label.appendChild(document.createTextNode("\xa0" + opt.value));

              // Create a link element
              if (opt.link != null) {
                const link = document.createElement("a");
                link.href = opt.link;

                link.textContent = " More info";
                link.target = "_blank"; // Open link in a new tab
                // Append the link to the label
                label.appendChild(link);
              }

              // Append the radio button and label to the container
              inputDiv.appendChild(radioButton);
              inputDiv.appendChild(label);
              inputDiv.appendChild(document.createElement("br"));
            }
            
          }
          else
          {
            input.name = field["desc"];
            input.placeholder = field["desc"];
            inputDiv.appendChild(input)

          }

          input.className = "form-control mb-3"; // Bootstrap class for styling
          form.appendChild(inputDiv); // Append to the form
          form.appendChild(document.createElement("br"));
        }

        // Create a submit button
        var submitButton = document.createElement("button");
        submitButton.type = "submit";
        submitButton.textContent = "Submit";
        submitButton.className = "btn btn-primary";
        form.appendChild(submitButton);

        // Append the form to the container div
        document.querySelector(".container").appendChild(form);
      
}
function createForm_(formData) {
  var form = document.createElement("form");
  form.id = "dynamicForm";
  form.method = "post";
  form.action = "#";

  formData.fields.forEach((field) => {
    var inputDiv = document.createElement("div");
    var input;

    if (field.type === "radio") {
      field.options.forEach((opt) => {
        input = document.createElement("input");
        input.type = "radio";
        input.name = field.desc;
        input.value = opt.value;

        const label = document.createElement("label");
        label.textContent = opt.value;

        inputDiv.appendChild(input);
        inputDiv.appendChild(label);
        inputDiv.appendChild(document.createElement("br"));
      });
    } else {
      input = document.createElement("input");
      input.type = field.type;
      input.name = field.desc;
      input.placeholder = field.desc;
      input.className = "form-control mb-3";
      inputDiv.appendChild(input);
    }
    form.appendChild(inputDiv);
  });

  var submitButton = document.createElement("button");
  submitButton.type = "submit";
  submitButton.textContent = "Submit";
  submitButton.className = "btn btn-primary";
  form.appendChild(submitButton);

  document.querySelector(".container").appendChild(form);
}
