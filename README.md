
---

## NetSuite Ingestion Connector - README

### 📚 Overview

This document provides detailed information about the **NetSuite data source ingestion connector**, including the required credentials, supported data points for ingestion, supported tools and destinations, and any known limitations or considerations.

# NetSuite Data Extraction

## 🔑 Prerequisites

* **Admin Access Required**: To extract data from NetSuite, an account with **admin access** is needed to create the necessary keys and tokens.
* **ODBC Access**: To extract data from NetSuite via **ODBC**, an account with **Web Services Role** access is required. This can be set up by the client with admin access, or JMAN can get admin access to set up the ODBC.

## 1.1 Steps to Create an Account with Admin Access

### 1. Log In to Your NetSuite Account

### 2. Get Your Account ID

* Navigate to **Setup > Company > Company Information**.
* Your **Account ID** is listed under the **Account Information** section.

### 3. Enable Token-Based Authentication

* Go to **Setup > Company > Enable Features > Suite Cloud > Manage Authentication**.
* Enable **Token-Based Authentication**.

### 4. Create a New User:

* Navigate to **Setup > Users/Roles > Manage Users > New**.
* Fill out the user details, including name and email.

### 5. Create a Custom Role with Admin-Level Access:

* Navigate to **Setup > Users/Roles > Manage Roles > New**.
* Enter a name and description for the role, e.g., "Jman Admin".
* Assign the necessary permissions to the role ensuring it has full access to the required features. [NetSuite: SuiteQL Tables & Permissions Reference](https://timdietrich.me/blog/netsuite-suiteql-tables-permissions-reference/)
* Under the **Permissions** tab, add necessary permissions:

  * **Lists**: Full access to all lists.
  * **Setup**: Full access to setup functions.
  * **Transactions**: Access as needed.
  * **Custom Record Types**: Access as needed.

### 6. Assign the Role to the User:

* Go to **Setup > Users/Roles > Manage Users**.

## 1.1.1 Steps to Create Authentication Keys from NetSuite

**\[JMAN can create once Admin access is granted]**

### 1. Create an Integration Record in NetSuite:

* Navigate to **Setup > Integration > Manage Integrations > New**.
* Check **TOKEN-BASED AUTHENTICATION** and "TBA: ISSUETOKEN ENDPOINT", including "User Credentials".
* Uncheck **TBA: AUTHORIZATION FLOW**, **AUTHORIZATION CODE GRANT**, and **OAUTH2**.
* Fill out the required fields to create a new integration. This will give you the **Consumer Key** and **Consumer Secret**.

### 2. Create a Role with Appropriate Permissions: [Reference](https://support.cazoomi.com/hc/en-us/articles/204089345-Manage-NetSuite-Permissions)

* Navigate to **Setup > Users/Roles > Manage Roles > New**.
* Assign the necessary permissions to this role to access the data.

### 3. Assign the Role to a User:

* Navigate to **Setup > Users/Roles > Manage Users**.
* Assign the previously created role to a user.

### 4. Generate Token ID and Token Secret:

* Navigate to **Setup > Users/Roles > Access Tokens > New**.
* Select the **Application Name**, **User**, and **Role**, then generate the **Token ID** and **Token Secret**.

### Necessary Keys for API Integration:

1. **Client ID**
2. **Client Secret**
3. **Account ID**
4. **Access Token**
5. **Access Token Secret**

## 1.1.2 Steps to Get Connection String & ODBC Driver

### 1. Create a Custom Role with Web Services Access

* Navigate to **Setup > Users/Roles > Manage Roles > New**.
* Create the role by entering a name and description, e.g., "Jman Admin".
* Assign the role that has **Web Services Access** alone (refer to the attached screenshot of the role privileges).
* Under the **Permissions** tab, add necessary permissions:

  * **Lists**: Full access to all lists.
  * **Setup**: Full access to setup functions.
  * **Transactions**: Access as needed.
  * **Custom Record Types**: Access as needed.
* **Role ID**: Copy the role ID of the custom role (this will be numeric in the ID section).
  ![image](https://github.com/user-attachments/assets/32823b55-b7fd-431b-8e33-5b481c6e8494)

### 2. Assign the Role to a User:

* Navigate to **Setup > Users/Roles > Manage Users**.
* Assign the previously created role to a user.

### 3. Navigate to Homepage

* Search for **Set Up Suite Analytics Connect** and click on it.
* Download the **ODBC driver** from the **Drivers** section on that page.

### 4. Copy the Below Parameters:

* **Service Host**: `<xxxxx>.connect.api.netsuite.com`
* **Service Port**: `<xxxx>`
* **Service Data Source**: `NetSuite2.com`
* **Account ID**: `<xxx>`
* **Role ID**: `<Role ID of Custom Role>`

### 5. Connection String for ODBC

Update the below with the parameters and include the **Username** and **Password** for the user created with the above role:

> **Note:** The availability of specific data points may depend on the permissions granted to the integration and the NetSuite modules enabled in your account.

### 🧰 Supported Tools

* ✅ **Azure Data Factory (ADF)**
* ✅ **Python (PySpark)**

### 🌍 Supported Destinations

#### Files:

* ✅ **JSON** 📄
* ✅ **CSV** 🧾
* ✅ **Parquet** 📊

#### Lakehouse:

* ✅ **Databricks**: Delta Lake 🛢️
* ✅ **Fabric**: Lakehouse 🌊

#### Data Warehouse / Database:

* ✅ **Snowflake** ❄️
* ✅ **Fabric**: Warehouse 🏭
* ✅ **Azure SQL** 💻

### ⚠️ Limitations

* **Rate Limiting** ⏱️: NetSuite APIs impose **rate limits** that restrict the frequency of data requests. Ensure you are aware of these limits to avoid failures, as excessive requests may result in temporary access restrictions.
* **Data Volume** 📦: Handling **very large datasets** may require batching requests or implementing pagination to manage data ingestion efficiently. Ensure you're prepared to handle large loads without overloading the system.
* **Complex Data Types** 🔄: Complex data types (e.g., nested arrays or objects) may need **pre-processing** before ingestion to ensure compatibility with the destination.
* **Time Zone Handling** ⏰: **Time zone conversions** may not be handled natively, requiring manual adjustments in some cases. Be sure to handle time zone issues based on your business requirements.
* **API Endpoint Changes** 🔄: Any changes in the **NetSuite API endpoints** or schema may require updates to the connector. Ensure you're regularly checking for updates in NetSuite API documentation to stay aligned with any changes.
* **Permissions Management** 🔐: Ensure the appropriate roles and permissions are granted in NetSuite. Incorrect or missing permissions may restrict access to essential data and impede the extraction process.

---
