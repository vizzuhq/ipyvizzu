#!/bin/bash
git clone --filter=blob:none --no-checkout --depth 1 https://github.com/vizzuhq/vizzu-lib.git
cd vizzu-lib
git sparse-checkout init --cone
git sparse-checkout set test/integration/test_cases/web_content test/integration/test_data
