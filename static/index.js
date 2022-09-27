var url = new URL(window.location.href)
if (url.searchParams.has("b64")) {
	url = new URL(`https://autoplay.vercel.app/?${atob(url.searchParams.get("b64"))}`)
}
if (!(url.searchParams.has("id"))) {
  alert("No url provided");
} else {	
	var fullurl = `https://www.youtube.com/embed/${url.searchParams.get("id")}?enablejsapi=1`
  let mainframe = document.getElementById("mainframe")
	mainframe.setAttribute("src", fullurl)
}

var tag = document.createElement('script');

tag.src = "https://www.youtube.com/iframe_api";
var firstScriptTag = document.getElementsByTagName('script')[0];
firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);
var player;

function onYouTubeIframeAPIReady() {
  player = new YT.Player('mainframe', {
    events: {
      'onReady': onPlayerReady,
    }
  });
}

function onPlayerReady(event) {
  event.target.playVideo();
}

function stopVideo() {
  player.stopVideo();
}
