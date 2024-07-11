fatal: unable to access <link> getaddrinfo() thread failed to start
（https://stackoverflow.com/questions/59911649/fatal-unable-to-access-link-getaddrinfo-thread-failed-to-start）

我遇到了同样的问题，我尝试了几种解决方案，直到我发现问题出在我这里是防火墙。我使用的是“免费防火墙”，我注意到即使授权软件和连接，仍然无法连接到远程存储库。我禁用了它，但问题并没有解决，只有当我卸载它时，问题才得到解决，我才能正常使用 Git。

**禁用Win11或者Win10的防火墙**