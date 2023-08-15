
document.addEventListener("DOMContentLoaded", (event) => {
  if (window.location.href.includes("/reference/")) {
    const links = document.links;
    for (let i = 0; i < links.length; i++) {
      if (
        links[i].hostname !== window.location.hostname &&
        links[i].href.includes("https://lib.vizzuhq.com")
      ) {
        links[i].href = links[i].href.replace("latest", "0.8");
      }
    }
  }
});
            