#!/bin/bash
git clone --filter=blob:none --no-checkout --depth 1 https://github.com/vizzuhq/vizzu-lib.git
git -C vizzu-lib sparse-checkout init --cone
git -C vizzu-lib sparse-checkout set \
  test/integration/test_cases/web_content \
  test/integration/test_data \
  tools/js2csv
ls -R vizzu-lib