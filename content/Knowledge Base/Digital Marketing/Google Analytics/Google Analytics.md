---
date: 1970-01-01T00:00:00Z
---

## Basic Principles

### **1. Data Collection**

Google Analytics collects data using a tracking code (usually JavaScript) embedded in each page of your website. This code collects information about:

* **Users**: Who is visiting your site (anonymously), such as location, device, browser.
* **Sessions**: A user's visit, including all interactions within a 30-minute window.
* **Interactions**: Pageviews, clicks, events, transactions, etc.

---

### **2. Users, Sessions, and Hits**

These are the core building blocks:

* **Users**: Unique visitors to your site.
* **Sessions**: A single visit to your site, which can include multiple pageviews or events.
* **Hits**: Any interaction, such as a pageview, event, or e-commerce transaction.

---

### **3. Dimensions and Metrics**

* **Dimensions**: Attributes of your data (e.g., City, Device Type, Page Title).
* **Metrics**: Quantitative measurements (e.g., Sessions, Bounce Rate, Conversion Rate).

Example:

> "City" = New York (dimension)
> "Sessions" = 5,000 (metric)

---

### **4. Goals and Conversions**

Goals track specific actions you want users to take (like completing a form or purchase). These help you measure success.

Types of goals:

* Destination (reaching a specific page)
* Duration (time on site)
* Pages/screens per session
* Events (specific actions like clicks)

---

### **5. Reports**

Google Analytics offers various standard reports:

* **Audience**: Who is visiting
* **Acquisition**: How they got there (e.g., search, social, referral)
* **Behavior**: What they do on your site
* **Conversions**: Whether they completed desired actions

---

### **6. Real-Time Reporting**

See what’s happening on your site **right now**, including current users, pages they’re viewing, and how they got there.

---

### **7. UTM Parameters**

UTM (Urchin Tracking Module) codes are tags added to URLs to track marketing campaigns. They help you analyze which campaigns are most effective.

---

### **8. Segmentation**

Segments allow you to break down data (e.g., mobile users vs desktop users, returning vs new visitors) for deeper insights.

---

### **9. Customization**

You can create:

* **Custom Reports**
* **Dashboards**
* **Custom Dimensions/Metrics**
* **Event Tracking** (for non-pageview actions)

---

### **10. Privacy and Consent**

Under GDPR and similar laws, you must:

* Obtain consent for tracking (cookies, personal data)
* Anonymize IPs if necessary
* Provide users with data transparency

---

## Metrics Definitions in Google Analytics

### 🔢 **1. [[Pageviews]]**

* **Definition**: Total number of times a page was loaded or reloaded.
* **Note**: Multiple views of the same page in a single session are **all counted**.
* **Use case**: Measures raw popularity of a page.

---

### 👤 **2. Unique Pageviews**

* **Definition**: Counts **only one view per session** for each page URL + title combo.
* **Use case**: Helps understand how many **distinct visits** a page received without inflating counts due to reloads or repeat views.

---

### ⏱️ **3. [[Average Time on Page]]**

* **Definition**: The **average time** users spent on a single page (or group of pages).
* **Formula**:

  > (Time on Page for all views – Exits without interaction) ÷ (Total Pageviews – Bounces)
* **Use case**: Indicates **user engagement**. Longer time may suggest deeper interest.

---

### 🚪 **4. [[Bounce Rate]]**

* **Definition**: Percentage of sessions where the user **viewed only one page** and then left without interacting.
* **Formula**:

  > (Single-page sessions ÷ Total sessions starting with that page) × 100
* **Use case**: Measures whether a page keeps users exploring. A **high bounce rate** may indicate poor content or poor targeting (but not always bad!).

---

### 📉 **5. % Exit / [[Page Exit Rate]] **

* **Definition**: How often a page is the **last page** viewed in a session.
* **Formula**:

  > (Number of exits from the page ÷ Pageviews) × 100
* **Use case**: Identifies pages where users commonly leave. High exit rate on a checkout page might be bad; on a "Thank You" page, it's normal.

---

### 🔑 **6. [[Entrances]]**

* **Definition**: The number of times users **entered your site** through a specific page.
* **Use case**: Helps you understand **landing page performance** and which pages are pulling traffic.

---

### 💰 **7. [[Page Value]]**

* **Definition**: A calculated metric showing the **monetary value** a page contributes based on e-commerce and goal completions.
* **Formula**:

  > (Transaction Revenue + Goal Value) ÷ Unique Pageviews of the page
* **Use case**: Helps identify which content **drives revenue or conversions**. High page value = important conversion path.

You're absolutely right — in **Google Analytics 4 (GA4)**, the focus has shifted significantly from sessions and pageviews to **events and engagement**. Here’s a refined and practical explanation of what you just mentioned:

---

## **Events in GA4**

### 🔹 **What Are Events?**

In GA4, **everything is an event**. Unlike Universal Analytics (UA), GA4 doesn't separate different types of hits (pageviews, transactions, etc.). Instead, it treats all user interactions as events.

### 🔹 **Types of Events in GA4**

1. **Automatically Collected Events**
   – Tracked without any configuration (e.g., `first_visit`, `session_start`, `page_view`).

2. **Enhanced Measurement Events**
   – Optional, toggleable events like:

   * `scroll`
   * `click`
   * `video_start`
   * `file_download`

3. **Recommended Events**
   – Google's suggested events for specific use cases (e.g., `purchase`, `sign_up`, `login`).

4. **Custom Events**
   – Events you define yourself, useful when none of the above fits your needs.

### 📦 **Event Structure in GA4**

Each event can include:

* **Event Name** (e.g., `sign_up`)
* **Event Parameters** (e.g., `method: "Google"`)

This makes data more flexible and detailed than Universal Analytics.

---

## **Bounce Rate in GA4 vs Universal Analytics**

### 🔹 **UA Bounce Rate**

* Definition: % of sessions with **only one interaction** (no further engagement).
* Limitation: Treated as a "bad" signal, even when users may have read a full page.

### 🔹 **GA4 Engagement Rate**

* **New Focus**: GA4 prefers **engagement rate**, which is:

  > % of sessions that lasted longer than 10 seconds, had a conversion event, or viewed 2+ pages/screens.

* **Bounce Rate in GA4**: It still exists but is **not shown by default**.

  * It’s simply:

    > `Bounce Rate = 100% - Engagement Rate`

### 🔹 **Why This Matters**

* GA4 provides a **more meaningful measure of engagement**.
* Users can be considered engaged even if they view one page — as long as they stay or interact.

---

### 📚 **Further Reading**

To dive deeper, check:

* [GA4 Events documentation (Google)](https://support.google.com/analytics/answer/9322688)
* [GA4 Engagement & Bounce Rate explained](https://support.google.com/analytics/answer/12195621)