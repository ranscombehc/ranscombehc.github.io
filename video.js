var blurbElement = document.getElementById("mainpara");
var blurbWidth = blurbElement.clientWidth;
var videoUrl = 'http://www.vimeo.com/190882480';
var endpoint = 'https://www.vimeo.com/api/oembed.json';
var callback = 'embedVideo';
var url = endpoint + '?url=' + encodeURIComponent(videoUrl) + '&callback=' + callback + '&width=' + blurbWidth + 'px';
function embedVideo(video) {
document.getElementById('embed').innerHTML = unescape(video.html);
}
function init() {
var js = document.createElement('script');
js.setAttribute('type', 'text/javascript');
js.setAttribute('src', url);
document.getElementsByTagName('head').item(0).appendChild(js);
}
window.onload = init;
