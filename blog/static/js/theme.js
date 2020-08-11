console.log("its  good working");
let theme = localStorage.getItem('theme');

if(theme == null) 
{
    setTheme("light")
}
else
{
    setTheme(theme)
}

let themeDots = document.getElementsByClassName('theme-dot');

for(var i =0; i<themeDots.length; i++)
{
    themeDots[i].addEventListener('click',function() {
        let mode = this.dataset.mode;
        setTheme(mode)
        console.log("clicked")

    })
}


function setTheme(mode)
{
    if (mode == "light")
    {
        document.getElementById('theme-style').href = 'static/css/light.css'
console.log("its working light")

    }

    if (mode == "blue")
    {
        document.getElementById('theme-style').href = 'static/css/blue.css'
    }
    if (mode == "green")
    {
        document.getElementById('theme-style').href = 'static/css/light.css'
    }

    localStorage.setItem('theme',mode)
}