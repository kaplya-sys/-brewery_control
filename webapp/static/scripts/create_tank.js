const formTitle = document.getElementById("titleform");
const yeastSelect = document.getElementById("yeasts"); 


formTitle.addEventListener("change", function(){
    let select = document.getElementById("title").value;
    fetch(`/tank/yeast-request-processing`, {
        method: 'POST',
        headers: {
            'Content-Type': 'text/plain;charset=UTF-8'
            },
        body: select})
        .then((response)=>{
            if (response.ok) {
                let json = response.json()
                .then((json)=>{
                    $('#yeasts').empty();
                    for (let i in json) {
                        let opt = document.createElement("option");
                        opt.innerText=json[i];               
                        yeastSelect.append(opt);        
                      }
                })
               }

        })
});
