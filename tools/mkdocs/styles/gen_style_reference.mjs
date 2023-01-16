import fs from "fs/promises";
import puppeteer from "puppeteer";

function appendContent(obj, level) {
  const tab = "&emsp;";
  let content = "";
  if (level) {
    content += `<div class="collapsible-style-content">`;
  }
  for (const [key, value] of Object.entries(obj)) {
    if (typeof value === "object") {
      content += `<p class="collapsible-style"><button type="button">${tab.repeat(
        level
      )}+&nbsp;${key}</button></p>`;
      content += appendContent(value, level + 1);
    } else {
      content += `<p class="not-collapsible-style">${tab.repeat(
        level
      )}${key}: <code>${value}</code></p>`;
    }
  }
  if (level) {
    content += `</div>`;
  }
  return content;
}

const Vizzu = process.argv[2];

const browserLaunched = puppeteer.launch();

const pageCreated = browserLaunched.then((browser) => {
  return browser.newPage();
});

const getStyleScriptLoaded = fs.readFile(
  "./tools/mkdocs/styles/get_style.mjs",
  { encoding: "utf8" }
);

const pageModified = Promise.all([pageCreated, getStyleScriptLoaded]).then(
  (results) => {
    const page = results[0];
    const getStyleScript = results[1];
    return page.goto(`data:text/html,<script id="style" type="module">
import Vizzu from "${Vizzu}";
${getStyleScript}
</script>`);
  }
);

const selectorLoaded = Promise.all([pageCreated, pageModified]).then(
  (results) => {
    const page = results[0];
    return page.waitForSelector("p");
  }
);

const element = Promise.all([pageCreated, selectorLoaded]).then((results) => {
  const page = results[0];
  return page.$("p");
});

const elementValue = Promise.all([browserLaunched, pageCreated, element]).then(
  (results) => {
    const page = results[1];
    const element = results[2];
    return page.evaluate((el) => el.textContent, element);
  }
);

Promise.all([browserLaunched, elementValue]).then((results) => {
  const browser = results[0];
  browser.close();
});

const setClickEventScriptLoaded = fs.readFile(
  "./tools/mkdocs/styles/set_click_event.mjs",
  { encoding: "utf8" }
);

const setAllScriptLoaded = fs.readFile("./tools/mkdocs/styles/set_all.mjs", {
  encoding: "utf8",
});

Promise.all([elementValue, setClickEventScriptLoaded, setAllScriptLoaded]).then(
  (results) => {
    const elementValue = results[0];
    const setClickEventScript = results[1];
    const setAllScript = results[2];
    let content = "";
    content += `<p id="allbtn-style" class="allbtn-style"><button type="button">+&nbsp;expand all</button></p>`;
    content += appendContent(JSON.parse(elementValue), 0);
    content += `<script>${setClickEventScript}</script>`;
    content += `<script>${setAllScript}</script>`;
    console.log(content);
  }
);
