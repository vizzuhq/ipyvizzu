#!/bin/bash
venv="$1"
input="$2"
output="$3"

mdfile=${output%.ipynb}.md

echo "[mjs2ipynb] Converting from js to md"
node mjs2md.mjs ${input} ${mdfile} 

echo "[mjs2ipynb] Converting from md to ipynb"
${venv}/bin/jupytext --to notebook ${mdfile}

echo "[mjs2ipynb] Removing md file"
rm ${mdfile}

echo "[mjs2ipynb] Formatting ipynb file"
${venv}/bin/black ${output}

echo "[mjs2ipynb] Done"
