#!/bin/bash

./sparse-clone-vizzu-lib.sh

docsDir=../../docs
examplesDir=${docsDir}/examples
testDir=vizzu-lib/test/integration
testcaseDir=${testDir}/test_cases/web_content

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

for example in $staticExamples; do
  ./mjs2ipynb.sh $example ${examplesDir}/static/$(basename ${example%.mjs}.ipynb)
done

for example in $animatedExamples; do
  ./mjs2ipynb.sh $example ${examplesDir}/animated/$(basename ${example%.mjs}.ipynb)
done
