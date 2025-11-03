---
title: Git Commit Messages Guideline
date: 2025-07-06T09:03:28+07:00
draft: false
tags:
  - tech
toc: false
publish_external: true
---
A good Git commit message helps you and others understand **what** changed and **why**. Here's a practical guide to writing clear, consist
# Git Commit Messages Guideline

Write your post here in Markdown.

## 📌 Notes
- Change `draft: true` to `false` when you're ready to publish.
- Use standard Hugo front matter fields.
ent, and useful commit messages.

---

### 🔧 Standard Git Commit Message Structure

```
<type>(<scope>): <short summary>

<body>

<footer>
```

---

### ✅ 1. **Types** (What kind of change is this?)

|Type|Description|
|---|---|
|`feat`|A new feature|
|`fix`|A bug fix|
|`docs`|Documentation changes only|
|`style`|Formatting, missing semi-colons, etc.|
|`refactor`|Code change that neither fixes nor adds|
|`test`|Adding or updating tests|
|`chore`|Changes to build process or tooling|
|`perf`|Performance improvement|
|`ci`|Continuous integration changes|

---

### ✅ 2. **Scope** (Optional but recommended)

- Scope is a specific part of the codebase: e.g., `api`, `ui`, `auth`, `login-form`, etc.
    

Example:

```
feat(login-form): add validation for empty fields
```

---

### ✅ 3. **Subject Line** (Short summary)

- Use **imperative mood** (e.g., “fix”, not “fixed” or “fixes”)
    
- **Limit to ~50 characters**
    
- **No period** at the end
    

Example:

```
fix(auth): prevent login with expired token
```

---

### ✅ 4. **Body** (Optional but useful)

- Explain **what** and **why**, not just how
    
- Wrap lines at 72 characters
    
- Use bullet points or paragraphs for clarity
    

Example:

```
- Added a check for expired tokens before login
- This prevents users from being logged in with stale sessions
```

---

### ✅ 5. **Footer** (Optional)

Used for:

- Breaking changes (`BREAKING CHANGE:`)
    
- Related issues (`Closes #123`)
    

Example:

```
BREAKING CHANGE: login endpoint now requires reCAPTCHA
Closes #456
```

---

### 🔁 Examples

```bash
feat(ui): add dark mode toggle
fix(api): handle null user ID in request payload
docs(readme): update installation instructions
style: reformat code with Prettier
chore(deps): bump axios from 0.21 to 0.24
```

---

### 🛠️ Tips

- Make commits small and focused.
    
- Avoid generic messages like “update” or “fix bug”.
    
- Use tools like [`commitlint`](https://commitlint.js.org/) if you want to enforce rules automatically.
    

---