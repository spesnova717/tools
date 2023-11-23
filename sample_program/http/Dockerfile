# OpenRestyのベースイメージを使用
FROM openresty/openresty:latest

# Luaスクリプトをコピー
COPY execute_command_async_ver2.lua /etc/nginx/conf.d/execute_command.lua

# Nginxの設定ファイルをコピー
COPY nginx.conf /usr/local/openresty/nginx/conf/nginx.conf

# 8888ポートを開放
EXPOSE 8888
