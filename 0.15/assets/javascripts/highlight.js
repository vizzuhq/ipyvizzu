document.addEventListener("DOMContentLoaded", (event) => {
  document.querySelectorAll("pre code").forEach((el) => {
    if (window.location.href.includes("LICENSE")) {
      return;
    }

    if (window.location.href.includes("/reference/ipyvizzu/")) {
      el.classList.add("language-python");
    }

    hljs.highlightElement(el); // eslint-disable-line no-undef
    if (
      window.location.href.includes("/examples/") ||
      window.location.href.includes("/showcases/") ||
      window.location.href.includes("/reference/") ||
      window.location.href.includes("/environments/")
    ) {
      hljs.lineNumbersBlock(el); // eslint-disable-line no-undef
    }
  });
});
