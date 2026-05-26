# 已完成項目報告：PromptProof Agent

## 04 請描述你使用 Agent 或 AI 驅動構建的具體成果

我完成了一個「PromptProof Agent：提示詞品質評估與 Token 預算助手」的可運行 MVP。它解決的痛點是：團隊在提交 AI 任務前，常因需求描述不完整、預期輸出不清、Token 預估不足，造成返工與成本失控。系統採用 5 個輕量 Agent 流程：需求解析、提示詞重寫、評分校驗、Token/成本估算、報告生成。使用者輸入任務描述後，Agent 會自動生成結構化 Prompt、檢查風險與缺漏、產生 0–100 分品質分數、估算單次/每日/每月 Token 消耗，並輸出可截圖的執行日誌。項目目前為前端可運行版本，支援本地離線展示，後續可接 OpenAI/Claude API 轉為真實模型推理。若以 10 人小組、每人每日 20 次任務估算，每次可提前修正需求，預期可降低 30–40% 的無效生成與返工，並用 Token Plan 控制預算。

## 05 使用證明與影響力證明

可提交的證明材料包含：1. 運行主畫面截圖，畫面顯示項目名稱、COMPLETED 狀態、Run ID、Prompt Quality Score、每日與每月 Token 估算；2. 多 Agent 工作流截圖，展示 Intake Agent、Prompt Architect、Risk Checker、Token Planner、Report Agent 五個流程節點；3. Evidence Log 截圖或 JSON 日誌，內容包含 run_id、created_at、agents、quality_score、token_plan 與 estimated_rework_reduction；4. 項目壓縮包或 GitHub 倉庫連結。此項目可作為團隊提交 AI 任務前的品質閘門，讓需求描述先被結構化、預算先被估算、風險先被提示，避免反覆生成與人工修改，對提升 AI 使用效率、控制 Token 成本與標準化內部工作流有直接幫助。

## 截圖建議

請打開 `index.html` 後截圖以下畫面：

1. 上方標題區：顯示 `PromptProof Agent`、`COMPLETED`、Run ID。
2. 評估結果區：顯示品質分數、每日 Token、每月 Token、返工降低預估。
3. 多 Agent 工作流區：顯示 5 個 Agent 節點。
4. Evidence Log 區：顯示 JSON 執行日誌。
