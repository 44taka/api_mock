# APIスタブ

PythonのFastAPIでJSONファイルを読み込んでレスポンスするだけのシンプルなAPIスタブ。  
ローカル環境でSPA、アプリなどの開発時の利用を想定。

# Requirement

ローカルPCに以下のインストールが必須。

- Docker
- Docker Compose

# Usage

コンテナ起動。

```bash
docker-compose up -d
```

コンテナ起動後、以下URLにアクセスしてjsonがレスポンスされることを確認。

```
http://localhost:8000/stub/sample
```
