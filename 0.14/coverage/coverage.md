
<style>
article h1, article > a, .md-sidebar--secondary {
    display: none !important;
}
</style>

<iframe
    id="coviframe"
    src="covindex.html"
    frameborder="0"
    scrolling="no"
    onload="resizeIframe();"
    width="100%">
</iframe>

<script>
var coviframe = document.getElementById("coviframe");

function resizeIframe() {
    coviframe.style.height = coviframe.contentWindow.document.documentElement.offsetHeight + 'px';
}

coviframe.contentWindow.document.body.onclick = function() {
    coviframe.contentWindow.location.reload();
}
</script>

