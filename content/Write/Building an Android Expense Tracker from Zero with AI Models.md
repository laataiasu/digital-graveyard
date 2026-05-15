---
title: "Building an Android Expense Tracker from Zero with AI Models"
date: 2026-04-05
tags: [android, ai, coding, expense-tracker, gemini]
publish_external: true
---

saya punya zero background android development, nyoba pake AI buat simple expense tracker lumayan sulit juga. 

pake android studio + gemini configure environment nya aja di awal2 aja banyak error terus. tapi kalo udah bener di tengah jalan lumayan ok.


sempet nemu bug

karena opus dan sonnet usage makin dibatasin sm google antigravity, even gemini pro juga jadi semakin gampang lewat batas usage.

akhirnya terpaksa pake gemini flash 3. 


buat debugging si flash 3 ini rada nyeleneh, kaya typical dev, browsing docs pake browser use, udah hampir setengah jam searching tetep ga ketemu2 ngabisin token doang. 

akhirnya cape sendiri 

saya coba codex pake 5.2 medium. 

si codex ini lumayan ok soalnya instead of browsing, dia langsung cari dependency mana yg bikin error, sampe extract jar nya dan dia liat sendiri dalemannya, dan beberapa menit dia bisa fix. 

cuman jujur android dev ini agak ribet pake AI. mungkin suhu android dev punya rekomendasi model atau setup gitukah buat mempermudah?
