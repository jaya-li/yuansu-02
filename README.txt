yuansu02 交付包

入口文件：index.html
本地预览命令（在 yuansu02 目录执行）：python3 -m http.server 8080
预览地址：http://127.0.0.1:8080/index.html

离线固化步骤（异地建议先执行）：
1) 先执行：python3 fetch_assets.py
2) 脚本会直接更新 index.html（首次会生成 index.backup.html）
3) 然后打开：http://127.0.0.1:8080/index.html

说明：页面中的设计素材来自 figma.com/api/mcp/asset/* 临时链接。
这些链接可能过期，异地复现需保持网络可访问或后续替换为永久静态资源。
素材 URL 清单见 figma-asset-urls.txt
