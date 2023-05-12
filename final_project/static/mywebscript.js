let  translateToFrench =()=>
{
    textToTranslate = document.getElementById("textToTranslate").value;

    let xhttp = new XMLHttpRequest();
    xhttp.open("GET", "englishToFrench?textToTranslate"+"="+textToTranslate, true);
    xhttp.send();
    xhttp.onreadystatechange = function() 
    {
        if (this.readyState == 4 && this.status == 200) 
        {
            document.getElementById("textTranslated").innerHTML = xhttp.responseText;
        }
    };
    
}

let  translateToEnglish = ()=>
{
    textToTranslate = document.getElementById("textToTranslate").value;

    let xhttp = new XMLHttpRequest();
    xhttp.open("GET", "frenchToEnglish?textToTranslate"+"="+textToTranslate, true);
    xhttp.send();
    xhttp.onreadystatechange = function() 
    {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("textTranslated").innerHTML = xhttp.responseText;
        }
    };
}
