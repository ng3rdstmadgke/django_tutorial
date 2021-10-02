# イメージビルド

```bash
./bin/build.sh
```


# サービス起動

```bash
# 環境変数ファイル作成
cp sample.env .env
vim .env

# サービス起動(開発モード)
./bin/start.sh -m dev

# サービス起動(本番モード)
./bin/start.sh -m prod
```


# デバッグ
```bash
# シェル起動
./bin/shell.sh
```


# 参考

- [公式 | はじめての Django アプリ作成、その 1](https://docs.djangoproject.com/ja/3.2/intro/tutorial01/)
- [公式 | Djangoの認証システムを使用する](https://docs.djangoproject.com/ja/3.2/topics/auth/default/)
- [公式 | クラスベースビュー入門](https://docs.djangoproject.com/ja/3.2/topics/class-based-views/intro/)
- [公式 | uWSGIでDjangoを使用する方法](https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/uwsgi/)
- [Qiita | ちゃんと運用するときのuWSGI設定メモ](https://qiita.com/yasunori/items/64606e63b36b396cf695)
- [Qiita | uWSGIのiniファイルの文法まとめ](https://qiita.com/11ohina017/items/da2ae5b039257752e558)