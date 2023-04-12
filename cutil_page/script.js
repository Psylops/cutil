var OSName = "Unknown";
if (window.navigator.userAgent.indexOf("Windows")!= -1) OSName=" Windows";
if (window.navigator.userAgent.indexOf("Linux")!= -1) OSName="Linux"
var osn = document.querySelector("osname")
osn.value = "Windows";

function download(){
    alert("it works ig")
}