#!/bin/bash
input="$1"
output="$2"
mdfile=${output%.ipynb}.md

echo "[mjs2ipynb] Converting from js to md"
node mjs2md.mjs ${input} ${mdfile} 

echo "[mjs2ipynb] Converting from md to ipynb"
jupytext --execute --to notebook ${mdfile}

echo "[mjs2ipynb] Removing md file"
rm ${mdfile}

echo "[mjs2ipynb] Formatting ipynb file"
black ${output}

echo "[mjs2ipynb] Done"
