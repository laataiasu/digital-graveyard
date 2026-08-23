---
title: "AB Testing and Attribution Models"
date: 2026-08-20
tags: [note]
publish_external: true
---

# AB Testing and Attribution Models

## Tracking Your Campaigns

UTM tracking codes are useful for tracking 6 main campaign marketing parameters including

source
medium
id
name
keywords
content
UTM tracking allows marketers and business owners to see campaign information across marketing channels which is incredibly important for understanding which channels perform best to achieve business results.

Google Analytics Campaign URL Builder(opens in a new tab)

To create a UTM-coded campaign URL, go to the Google Analytics Campaign URL Builder link provided above and enter the following information.

Website URL: enter or paste the URL of the destination page your campaign will drive traffic to from your given ad or email campaign. This is usually your business's website or the specific landing page you’ve assigned for this campaign.
Campaign ID: this is optional, and not useful if you are using software or a promotion method that doesn’t generate campaign IDs.
Campaign source: enter the promotional platform or service you are using for your campaign. Examples include Google, Facebook, YouTube, Tiktok, Newsletter, and LinkedIn.
Campaign medium: this details the marketing medium or methods your campaign is using, such as search, video, emails, SMS text campaign, chatbot, or banners.
You can see a screenshot of a filled-out URL builder below.

Screenshot showing the Google Campaign URL builder
Google Campaign URL Builder

Once the desired fields are filled out, get your generated campaign URL from the “generated URL” field by clicking the copy icon. Now if you paste the link in your web browser, you’ll be directed to the destination page and also see that the entered parameter information is present in the URL slug after the original url link! Add this URL to your ad or promotional campaigns to get going with UTM tracking.

As a tip, you can use the URL shortening tool that is automatically provided by bitly(opens in a new tab) directly in Google Campaign URL Builder. If for any reason you want to use another shortener tool like Tiny URL(opens in a new tab), you would need to log into the account separately. Each is free and will make your link much more concise and easier to share.

Screenshot showing the URL generated from the Campaign URL Builder
URL generated from the Campaign URL Builder

New Terms
UTM Tracking Code - a snippet of code appended onto an existing URL to relay information on where and how users are referred to a destination web page. UTM stands for Urchin Tracking Module and is a URL parameter system created by Urchin, a software company in the early 2000s. Urchin, acquired by Google in 2005, would go on to become what we know today as Google Analytics. UTM codes help attribute data to marketing sources and mediums by detailing the promotional platform and marketing method in the link code.

[[Campaign source]] - the promotional platform or service you are using in a campaign to send traffic

[[Campaign medium]] - the marketing method your campaign is using to reach users

[[Campaign term]] - the keyword or search term your campaign is targeting

[[Campaign content]] - the ad headlines, descriptions, or other assets your campaign is showing to users



## AB Testing for Marketing

* **Purpose**

  * Isolate one variable (ad creative, landing page, form, funnel step, etc.) to find the highest‑performing version.
  * Typical test size: 2–5 versions.

* **Method (Step‑by‑Step)**

  1. Select a single variable to test.
  2. State a hypothesis (e.g., “Creative A will get more clicks than Creative B”).
  3. Define test duration and budget.
  4. Run the experiment to completion without changes.
  5. Evaluate statistical significance (adequate sample size, confidence interval) via tools such as Google Analytics.
  6. Accept or reject the hypothesis; adjust strategy accordingly.

* **Primary Metrics**

  * Choose one metric tied to the campaign goal.
  * Typical conversion events: sales, booked calls, leads, sign‑ups.
  * Example: If sales are the goal, favor the creative with the highest sales conversions and pause the rest.

* **Common Pitfalls**

  * Ending or modifying the test early.
  * Testing too many variables simultaneously.
  * Insufficient sample size or duration (minimum guideline: ≥ 2 weeks & ≥ 100 users).

* **Where to Test / Analyze**

  * Platforms: Google Ads, Facebook Ads, MailChimp, ClickFunnels, etc.
  * Analysis: Google Analytics or built‑in A/B features of the chosen platform.

* **Term**

  * **A/B Testing (split/bucket testing):** Experiment comparing multiple versions of a single variable to identify the one that best drives business goals.

## Attribution Modeling

**Attribution Modeling – Key Concepts for Learning**

---

### **Definition**

* **Attribution Modeling:** Strategy for analyzing customer touchpoints to determine which channels or steps in a funnel get credit for conversions.

---

### **Purpose**

* Understand which parts of the marketing funnel contribute to conversions.
* Optimize campaigns by assigning conversion credit based on touchpoint data.
* Choose an appropriate model based on business size, funnel complexity, and buying cycle.

---

### **Common Attribution Models**

#### **1. First Touch Attribution**

* Credits the **first** touchpoint the user interacts with.
* Best for: Short buying cycles (e.g., fast food, eCommerce).
* Simple to implement.

#### **2. Last Touch Attribution**

* Credits the **last** touchpoint before conversion.
* Best for: Industries with longer sales cycles (e.g., law, solar).
* Straightforward and easy to analyze.

#### **3. Multi-Touch Attribution**

* Distributes credit across **multiple** touchpoints.
* Best for: Longer customer journeys.
* Provides a balanced view of the full path to conversion.

#### **4. Position-Based Modeling**

* Assigns weights across the journey (e.g., 40% to first and last touch, 20% to others).
* Customizable weight distribution.
* Best for: Complex funnels with multiple key interactions.

#### **5. Data-Driven Modeling**

* Uses **machine learning** and ad data to assign weight based on patterns from converting vs. non-converting paths.
* Requires minimum data volume.
* Best for: Enterprise-level campaigns with rich datasets.

#### **6. Custom Attribution Model**

* Marketer defines the rules and weights manually.
* Fully customizable.
* Best for: Advanced users wanting tailored insights.

---

### **Model Selection Considerations**

* **Business Size:**

  * Small: First or Last Touch
  * Large/Enterprise: Position-Based, Multi-Touch, or Data-Driven

* **Funnel Complexity:**

  * Simple: First/Last Touch
  * Complex: Position-Based, Data-Driven

* **Buying Cycle Duration:**

  * Short: First Touch
  * Long: Last Touch, Multi-Touch

---

### **New Terms Recap**

* **[[Attribution Modeling]]:** Assigns conversion credit to marketing touchpoints.
* **First Touch:** Credit to first interaction.
* **Last Touch:** Credit to last interaction.
* **Multi-Touch:** Credit split among multiple interactions.
* **Position-Based:** Weighted credit (e.g., 40/20/40).
* **[[Data-driven]]:** Algorithm assigns weights based on data.
* **Custom Model:** User-defined credit distribution.

## When To Use A|B Testing

**A/B Testing & Attribution Modeling – Key Learning Points**

---

### **A/B Testing Guidelines**

* Test each component of a digital marketing campaign **individually** to optimize overall performance.
* Perform A/B testing **during and after** campaign launches.
* Treat A/B testing as an **interactive, ongoing process**.

#### **What to A/B Test:**

* **Ad Creatives:** images, videos, memes, GIFs
* **Landing Pages:** visuals, copy, buttons, animations, layout
* **Funnel Flows:** single-step vs multi-step flows (e.g., landing page → form → thank-you page)
* **Keywords:** short-tail vs long-tail
* **Ad Copy:** varying hooks, benefits, or phrasing

---

### **When to Perform A/B Testing**

* Start once the campaign is live.
* Continue **throughout the campaign lifecycle** for ongoing optimization.

---

### **Attribution Model Selection Criteria**

* **Business Goal:** purchases, clicks, impressions, sign-ups, downloads, etc.
* **User Buying Cycle Stage:** awareness, consideration, decision
* **Marketing Channels Used:** email, website, social media, TV, print, billboard, radio, etc.

---

### **Data-Driven vs Custom Attribution Models**

* **Data-Driven:**

  * Use only **after gathering enough sample data**
  * Best for **long-running campaigns** with consistent performance data
* **Custom:**

  * Tailored to **unique business models or structures**
  * Useful when standard models don’t fit business needs

---

### **Edge Cases**

* Some tools or models may not apply in **unusual or extreme scenarios**
* Be flexible in application when standard approaches don't fit

**New Terms – Key Definitions for Learning**

* **[[Ad Creatives]]**

  * Visual content used in ads: **images, videos, memes, GIFs**, etc.
  * Designed to capture attention and drive engagement.

* **[[Landing Pages]]**

  * Web pages users land on after clicking an ad.
  * Elements to test: **images, copy, buttons, animations, videos**, layout, etc.

* **[[Funnel Flows]]**

  * The user journey through your marketing funnel.
  * Examples:

    * **Single-step:** landing page → thank-you page
    * **Multi-step:** landing page → form → thank-you page

* **[[Keywords]]**

  * Search terms targeted in ads or SEO.
  * **Short-tail:** general terms, early in buyer journey
  * **Long-tail:** specific terms, later in buyer journey, higher intent

* **[[Ad Copy]]**

  * Written text in ads.
  * Test variations of how **benefits, solutions, or hooks** are communicated to increase user interest and conversions.

## Glossary

For your reference, here are all the new terms we introduced in this lesson:

[[Urchin Tracking Module|UTM Tracking Code]] - a snippet of code appended onto an existing URL to relay information on where and how users are referred to a destination web page

Campaign source - the promotional platform or service you are using in a campaign to send traffic

Campaign medium - the marketing method your campaign is using to reach users

Campaign term - the keyword or search term your campaign is targeting

Campaign content - the ad headlines, descriptions, or other assets your campaign is showing to users

A/B Testing - an experimentation process of measuring differing versions of a single variable against each other to determine which version performs better

Attribution modeling - a strategy that lets marketers analyze customer touchpoints and assess which touchpoints, or channels, receive credit for a conversion

[[First Touch Attribution]] - assigns a conversion credit to the first touchpoint that a user interacted with before converting

[[Last Touch Attribution]] - assigns a conversion credit to the last touchpoint that a user interacted with before converting

[[Multi Touch Attribution]] - assigns portions of a credit to multiple touchpoints along the user path

[[Position Based Modeling]] - allows the marketer to assign weights to different touchpoints that users interact with along the user path

Data Driven Modeling - allows ad data to assign weights to different touchpoints and touchpoint patterns that arise as users interact with along the user path

Ad Creatives -changing pictures, videos, memes, gifs, etc

Landing Pages - using different images, copy, buttons, animations, videos, etc.

Funnel Flows - having multi-steps or one step; for example a landing page -> form -> thank you page

Keywords - long-tail or short-tail keywords based on how specific the user knows the solution to the problem or how far they are down the consumer buyer journey

Ad Copy - Testing different ways to say the same benefits or solutions with different hooks to entice the user to learn more
