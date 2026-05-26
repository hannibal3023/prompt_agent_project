# PromptProof Agent｜提示詞品質評估與 Token 預算助手

這是一個可直接截圖提交的 AI Agent 小項目 MVP。它用 5 個輕量 Agent 流程完成：需求解析、Prompt 重寫、風險檢查、Token Plan 估算、報告與執行日誌生成。

## 如何運行

1. 解壓縮本資料夾。
2. 直接用瀏覽器打開 `index.html`。
3. 點擊 `載入 Demo` 或自行輸入任務需求。
4. 點擊 `Run Agent`。
5. 截圖以下區塊作為證明：
   - 首頁上方 `COMPLETED` 與 Run ID。
   - `Agent 評估結果` 的分數與 Token Plan。
   - `多 Agent 工作流`。
   - `Evidence Log` 的 JSON 執行日誌。

## 可提交材料

- 運行畫面截圖：`assets/sample_evidence_screenshot.png` 或自行截圖。
- 項目壓縮包：本資料夾 zip。
- 報告文字：`project_report_for_form.md`。
- 執行日誌：網頁中可下載 JSON，或參考 `evidence/demo-run-log.json`。

## 技術說明

本 MVP 使用純 HTML/CSS/JavaScript 製作，無需後端與外部依賴，方便在任何電腦快速打開展示。Agent 行為為可解釋的本地規則流程；若要升級成真實 LLM Agent，可在 `agent.js` 的 `buildOptimizedPrompt()` 和 `estimatePromptScore()` 位置接入 OpenAI/Claude API，保留相同的前端展示與日誌格式。
