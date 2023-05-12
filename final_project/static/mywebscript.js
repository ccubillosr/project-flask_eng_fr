let  translateToFrench =()=>
{
    textToTranslate = document.getElementById("textToTranslate").value;

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() 
    {
        if (this.readyState == 4 && this.status == 200) 
        {
            textTranslated = xhttp.responseText;
            document.getElementById("textTranslated").value = textTranslated;
        }
    };
    xhttp.open("GET", "englishToFrench?textToTranslate"+"="+textToTranslate, true);
    xhttp.send();
    
    
}

let  translateToEnglish = ()=>
{
    textToTranslate = document.getElementById("textToTranslate").value;

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() 
    {
        if (this.readyState == 4 && this.status == 200) {
            textTranslated = xhttp.responseText;
            document.getElementById("textTranslated").value = textTranslated;
        }
    };
    xhttp.open("GET", "frenchToEnglish?textToTranslate"+"="+textToTranslate, true);
    xhttp.send();
    
}
