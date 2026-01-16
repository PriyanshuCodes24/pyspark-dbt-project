
# 🚖 Pyspark-DBT-Project 
### Databricks • PySpark • Delta Lake • dbt Cloud

<p align="center">
  <img src="https://img.shields.io/badge/Databricks-FF3621?style=for-the-badge&logo=databricks&logoColor=white"/>
  <img src="https://img.shields.io/badge/Apache%20Spark-E25A1C?style=for-the-badge&logo=apachespark&logoColor=white"/>
  <img src="https://img.shields.io/badge/Delta%20Lake-003B57?style=for-the-badge&logo=delta&logoColor=white"/>
  <img src="https://img.shields.io/badge/dbt-FF694B?style=for-the-badge&logo=dbt&logoColor=white"/>
</p>

---

## 📌 Project Overview

This project demonstrates an **end-to-end modern data engineering pipeline** using **Uber trip data**, built on top of **Databricks**, **PySpark**, **Delta Lake**, and **dbt Cloud**.

The solution follows the **Medallion Architecture (Bronze → Silver → Gold)** and focuses on building **scalable, incremental, and production-ready data pipelines**.

### Key Capabilities
- Incremental data ingestion  
- CDC-based upserts using Delta Lake  
- PySpark-based transformations  
- dbt-powered analytics layer  
- SCD Type-2 history tracking using dbt snapshots  
- Reusable dbt macros & Jinja templates  

---

## 🏗️ Project Architecture
```
Source Data (Uber CSV / Raw Files)
        ↓
Bronze Layer (Delta Tables)
  - Incremental ingestion
  - Raw schema preservation
        ↓
Silver Layer (Delta Tables)
  - Deduplication
  - Data cleansing
  - CDC-based UPSERTs
        ↓
Gold Layer (dbt Models)
  - Business transformations
  - Aggregations
  - SCD Type-2 dimensions
```

---

## 🔧 Tech Stack

| Layer | Technology |
|------|------------|
| Storage | Delta Lake |
| Compute | Databricks |
| Processing | PySpark |
| Transformation | dbt Cloud |
| Modeling | dbt Models & Snapshots |
| Version Control | GitHub |

---

## 📂 Data Layers

### 🥉 Bronze Layer – Raw Ingestion
- Source: Uber datasets (customers, drivers, trips, payments, vehicles, locations)
- Built using **PySpark**
- Incremental ingestion via file-based triggers
- Stored as **Delta tables**
- No transformations applied

---

### 🥈 Silver Layer – Cleaned & Enriched
- Built using **PySpark**
- Includes:
  - Deduplication using window functions
  - Column standardization & cleansing
  - CDC-based `MERGE INTO` upserts
  - Audit columns (`process_timestamp`)
- Stored as **Delta tables**

---

### 🥇 Gold Layer – Analytics Ready
- Built using **dbt Cloud**
- Connected directly to Databricks
- Features:
  - Incremental dbt models
  - dbt macros for reusability
  - Jinja templating for dynamic SQL
  - dbt snapshots for SCD Type-2
- Optimized for BI & analytics consumption

---

## 🔄 Incremental & CDC Strategy

### PySpark (Bronze → Silver)
- Incremental loads using file arrival
- Change detection via `last_updated_timestamp`
- Delta Lake `MERGE` for UPSERT logic

### dbt (Silver → Gold)
- Incremental models using `is_incremental()`
- Snapshot-based historical tracking
- Current vs historical records maintained

---

## 🧬 SCD Type-2 Implementation

- Implemented using **dbt snapshots**
- Automatically managed columns:
  - `dbt_valid_from`
  - `dbt_valid_to`
- Enables full historical analysis
- Business views created on top of snapshots



## 📁 Repository Structure

```
pyspark-dbt-project/
│
├── analyses/
│   ├── Explore.sql
│   │   --> Used to explore source and transformed tables,
│   │       validate data, and analyze lineage in dbt
│
├── macros/
│   ├── generate_schema_name.sql
│   │   --> Custom macro to override the default dbt schema
│   │       naming convention in Databricks
│
├── models/
│   ├── silver/
│   │   --> dbt models built on top of Silver Delta tables
│   │       used for transformations and business logic
│
├── seeds/
│   
├── snapshots/
│   ├── Slowly_Changin_Dimension_Type2.yml
│   │   --> dbt snapshot to track SCD Type-2 changes
│   │       for dimension tables
│   │
│   └── FactTrips.yml
│       --> Snapshot to track historical changes
│           in fact-level trip data
│
├── tests/
│   │   --> dbt tests for data quality and validation
│
├── utils/
│   ├── custom_utils.py
│   │   --> Reusable PySpark transformation utilities
│   │       (deduplication, timestamp handling, upserts)
│
├── .gitignore
│   
│
├── README.md
│  
│
├── bronze_ingestion.ipynb
│   --> PySpark notebook to ingest raw Uber data
│       incrementally into Bronze Delta tables
│
├── dbt_project.yml
│   --> Core dbt project configuration file
│
└── silver_transformations.ipynb
    --> PySpark notebook to clean, deduplicate,
        and UPSERT data from Bronze to Silver layer


```

---

## 🎯 Key Highlights

- End-to-end lakehouse architecture
- Production-grade incremental pipelines
- Clean separation of concerns
- Real-world CDC & SCD Type-2 handling
- Strong Databricks + dbt Cloud integration

---

## 🚀 Future Enhancements

- dbt tests & data quality checks
- Observability & pipeline monitoring
- CI/CD for dbt deployments
- BI integration (Power BI / Tableau / Looker)

---

## 👤 Author

**Priyanshu Kumar Upadhyay**
GitHub: [@PriyanshuCodes24](https://github.com/PriyanshuCodes24)


---

⭐ If you find this project useful, please star the repository!
