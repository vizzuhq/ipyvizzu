#!/bin/bash
venv="$1"

#./sparse-clone-vizzu-lib.sh

docsDir=../../docs
examplesDir=${docsDir}/examples
testDir=vizzu-lib/test/integration
testcaseDir=${testDir}/test_cases/web_content
thumbUrl=https://github.com/vizzuhq/vizzu-lib-doc/raw/main/docs/latest/content/examples

staticExamples=$( find ${testcaseDir}/sample_static/ -name "*.mjs" )
animatedExamples=$( find ${testcaseDir}/templates/ -name "*.mjs" )
datafiles="chart_types_eu.mjs infinite_data.mjs music_industry_history_1.mjs tutorial.mjs"

mkdir -p ${docsDir}/data
mkdir -p ${examplesDir}/static
mkdir -p ${examplesDir}/animated

for datafile in $datafiles; do
  echo "Processing $datafile"
  node vizzu-lib/tools/js2csv/js2csv.js "../../test/integration/test_data/${datafile}" ${docsDir}/data/$(basename ${datafile%.mjs}.csv)
done

echo "## Static examples" > ${examplesDir}/examples.md

for example in $staticExamples; do
  echo "<a href=\"examples/static/$(basename ${example%.mjs}.html)\">" >> ${examplesDir}/examples.md
  echo "<img src=\"${thumbUrl}/static/$(basename ${example%.mjs}.png)\"></img>" >> ${examplesDir}/examples.md
  echo "</a>" >> ${examplesDir}/examples.md
  ./mjs2ipynb.sh ${venv} $example ${examplesDir}/static/$(basename ${example%.mjs}.ipynb)
done

echo "## Animated examples" >> ${examplesDir}/examples.md

for example in $animatedExamples; do
  echo "<a href=\"examples/animated/$(basename ${example%.mjs}.html)\">" >> ${examplesDir}/examples.md
  echo "<video autoplay loop src=\"${thumbUrl}/animated/$(basename ${example%.mjs}.mp4)\" type=\"video/mp4\"></video>" >> ${examplesDir}/examples.md
  echo "</a>" >> ${examplesDir}/examples.md
  ./mjs2ipynb.sh ${venv} $example ${examplesDir}/animated/$(basename ${example%.mjs}.ipynb)
done

${venv}/bin/jupytext --update --to ipynb -o ${examplesDir}/examples.ipynb examples.md 
#rm examples.md 
