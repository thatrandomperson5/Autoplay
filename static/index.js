//https://stackoverflow.com/questions/247483/http-get-request-in-javascript
function httpGet(theUrl)
{
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", theUrl, false ); // false for synchronous request
    xmlHttp.send( null );
    return xmlHttp.responseText;
}

let url = new URL(window.location.href)
if (!(url.searchParams.has("id"))) {
  alert("No url provided");
} else {
  let input = url.searchParams.get("id");
  // www.youtube.com/embed/${}
  let processed = `https://www.youtube.com/embed/${input}`;
  let mainframe = document.getElementById("mainframe");
  mainframe.setAttribute("src", processed);
  let ytdata = JSON.parse(httpGet(`https://noembed.com/embed?url=https://www.youtube.com/watch?v=${processed}`));
  document.getElementById("title").textContent = `Autoplay - ${ytdata["title"])}`
}
