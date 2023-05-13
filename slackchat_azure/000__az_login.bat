@REM Azureへのログイン 事前にプロキシを通しておくことを忘れないように set https_proxy=http://...:8080 or env:HTTP_PROXY="http://<proxyのIPアドレス>" env:HTTPS_PROXY="http://<proxyのIPアドレス>"
@REM az config set core.allow_broker=true
@REM az account clear
az login
