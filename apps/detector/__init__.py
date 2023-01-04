# 本では以下のコードを書いていたが、循環インポートによってエラーとなった
# そのため、apps/__init__.pyでdbを宣言し初期化をすることで対応することが可能となった
# 以下のインポートの意味合いとしては`flask db migrate`などのコマンドでモデルを認知させるためである

import apps.detector.models