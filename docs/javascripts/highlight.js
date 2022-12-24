document.addEventListener("DOMContentLoaded", (event) => {
  document.querySelectorAll("pre code").forEach((el) => {
    if (window.location.href.includes("/reference/ipyvizzu/")) {
      el.classList.add("language-python");
    }
    hljs.highlightElement(el); // eslint-disable-line no-undef
  });
});
