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

- [公式 | uWSGIでDjangoを使用する方法](https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/uwsgi/)