local function execute_command(command)
    local handle = io.popen(command)
    local result = handle:read("*a")
    handle:close()
    return result
end

-- local command = "echo 'Hello, World!'"
local command = "sleep 5 ; echo 'END'"

local thread = ngx.thread.spawn(execute_command, command)

-- コマンドの実行を待つ
local ok, result = ngx.thread.wait(thread)
if not ok then
    ngx.log(ngx.ERR, "コマンド実行に失敗しました。")
    return ngx.exit(500)
end

-- 実行結果をレスポンスとして返す
ngx.say("コマンド実行結果: ", result)
