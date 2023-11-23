local function execute_command(premature, command)
    if premature then return end

    local handle = io.popen(command)
    local result = handle:read("*a")
    handle:close()

    ngx.log(ngx.NOTICE, "コマンド実行結果: ", result)
end

local command = "echo 'Hello, World!'"
local ok, err = ngx.timer.at(0, execute_command, command)

if not ok then
    ngx.log(ngx.ERR, "タイマー作成に失敗: ", err)
    return ngx.exit(500)
end

ngx.say("コマンド実行スケジュール設定完了")

