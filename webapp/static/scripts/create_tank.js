const formTitle = document.getElementById("titleform");
const yeastSelect = document.getElementById("yeasts"); 


formTitle.addEventListener("change", (event) => {
    fetch(`/tank/yeast-request-processing`, {
        method: 'POST',
        headers: {
            'Content-Type': 'text/plain;charset=UTF-8'
            },
        body: event.target.value})
        .then((response)=>{
            if (response.ok) {
                let json = response.json()
                .then((json)=>{
                    $('#yeasts').empty();
                    for (let tank_info in json) {
                        let opt = document.createElement("option");
                        opt.innerText=json[tank_info];               
                        yeastSelect.append(opt);        
                      }
                })
               }

        })
});
