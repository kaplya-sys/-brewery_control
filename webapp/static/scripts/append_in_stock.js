const doc = document
const formName = doc.getElementById("type_product0");
const productSelect = doc.getElementById("name_product0");

let counts_forms = 1

formName.addEventListener("change", new_choice(0))


function new_choice(counts_forms){
    // append choices for name_product field
    let next_input = doc.getElementById("type_product" + counts_forms);
    let next_output = doc.getElementById("name_product" + counts_forms);
    next_input.addEventListener("change", (event) => {
        fetch(`/stock/process-request-append`, {
            method: 'POST',
            headers: {
                'Content-Type': 'text/plain;charset=UTF-8'
                },
            body: event.target.value})
            .then((response)=>{
                if (response.ok) {
                    let json = response.json()
                    .then((json)=>{
                        $('#name_product'+ counts_forms).empty();
                        for (let tank_info in json) {
                            let opt = doc.createElement("option");
                            opt.innerText=json[tank_info];      
                            next_output.append(opt);       
                        }
                    })
                }
            })
    });
}


function addFieldType(){
    // add field for type_product form
    let type_field = doc.createElement("select");
    type_field.setAttribute('class', 'form-control')
    type_field.setAttribute('id', 'type_product' + counts_forms)
    type_field.setAttribute('name', 'type_product' + counts_forms)
    let list_types = [["--------", "None"], ["Солод", "malt"], ["Хмель", "hop"], ["Дрожжи", "yeast"]];
    for (i in list_types){
        let newOption = new Option(list_types[i][0], list_types[i][1]);
        type_field.appendChild(newOption)
    }
    doc.getElementById('productform').appendChild(type_field)
}


function addFieldName(){
    // add field for name_product form
    let name_field = doc.createElement("select");
    name_field.setAttribute('class', 'form-control')
    name_field.setAttribute('id', 'name_product' + counts_forms)
    name_field.setAttribute('name', 'name_product' + counts_forms)
    let newOption = new Option('Наименование', 'None')
    name_field.appendChild(newOption)
    doc.getElementById('nameproduct').appendChild(name_field)
}


function addFieldsAmount(){
    // add field for amount_product form
    let amount_product = doc.createElement("input");
    amount_product.setAttribute('class', 'form-control')
    amount_product.setAttribute("type", "text");
    amount_product.setAttribute('id', 'amount_product' + counts_forms);
    amount_product.setAttribute('name', 'amount_product' + counts_forms);
    doc.getElementById('amountproduct').appendChild(amount_product)
}


function addField(){
    // add fields for forms
    addFieldType(counts_forms)
    addFieldName(counts_forms)
    addFieldsAmount()
    new_choice(counts_forms)
    counts_forms++;
}


function add_product(){
    let set_product = {},
        list_type = [],
        list_name = [],
        list_amount = []

    for (let count = 0; count < counts_forms; count++){
        let type = doc.getElementById('type_product' + count).value
        let name = doc.getElementById('name_product' + count).value
        let amound = doc.getElementById('amount_product' + count).value
        list_type.push(type)
        list_name.push(name)
        list_amount.push(amound)
    }
    set_product = {"type_product": list_type, "name_product": list_name, "amount_product": list_amount}
    fetch(`/stock/process-append`,{
        method: 'POST',
        headers: {
            'Content-Type': 'application/json;charset=utf-8'
        },
        body: JSON.stringify(set_product)
    });
}   
