var OSName = "Unknown";
if (window.navigator.userAgent.indexOf("Windows")!= -1) OSName=" Windows";
if (window.navigator.userAgent.indexOf("Linux")!= -1) OSName="Linux"
var osn = document.querySelector("osname")
osn.value = "Windows";

function download(){
    var link = document.createElement("a");

    link.download = "test";
    link.href = "file://files/test.txt";
    link.click();
}