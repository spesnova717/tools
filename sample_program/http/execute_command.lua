ngx.header.content_type = 'text/plain'

-- ここで任意のコマンドを実行
local command = "sleep 5"
local handle = io.popen(command)
local result = handle:read("*a")
handle:close()

ngx.say(result)
