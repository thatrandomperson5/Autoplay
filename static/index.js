let url = new URL(window.location.href)
if (!(url.searchParams.has("id"))) {
  alert("No url provided");
} else {
  let input = url.searchParams.get("id");
  // www.youtube.com/embed/${}
  let processed = `https://www.youtube.com/embed/${input}`;
  let mainframe = document.getElementById("mainframe");
  mainframe.setAttribute("src", processed);
  document.getElementById("title").textContent = `Autoplay - ${mainframe.contentDocument.title}`
}
