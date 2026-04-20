# yuansu02 复现检查

## 主入口
- `index.html`

## Figma MCP 相关内容
- 资产 URL 清单：`figma-asset-urls.txt`
- 资产本地化脚本：`fetch_assets.py`
- 离线固化目标：直接更新 `index.html`（首次自动备份为 `index.backup.html`）

## 对话顺序与逻辑（已包含在主 HTML）
- 首屏 loading 打开：`openOnbReplica364498()`
- 进入对话序列：`runInitialSequence()`
- 第 1 轮提交：`onSubmitRound0(labels)`
- 第 2 轮提交：`onSubmitRound1(labels)`
- 第 3 轮提交：`onSubmitRound2(labels)`
- 首轮到次轮细分映射：`FOLLOWUP`
- 对话完成进入 For You：`openOnbReplica1635()`

## 本地预览
1. 进入 `yuansu02` 目录
2. 执行 `python3 -m http.server 8080`
3. 打开 `http://127.0.0.1:8080/index.html`

## 异地复现建议
1. 先执行 `python3 fetch_assets.py`
2. 再打开 `index.html`

