# -*- coding: utf-8 -*-
"""lab5 using r kernel.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1bxO1oZ-NZpk5sxq9vzmOuCr-KjNERbAj
"""

# --------------------------------------------------
# Step 1: Importing CSV Files
# --------------------------------------------------
# CSV (Comma-Separated Values) file
# Ensure the file path points to the correct location where the file is stored in your Colab environment.
data_csv <- read.csv("/content/Chocolate Sales.csv", header = TRUE, stringsAsFactors = FALSE)

# Display the first few rows of the CSV data
cat("First few rows of the CSV data:\n")
head(data_csv)

# --------------------------------------------------
# Step 2: Importing Excel Files
# --------------------------------------------------
# Load Excel file using 'readxl'
if (!require(readxl)) install.packages("readxl", dependencies = TRUE)
library(readxl)

# Provide the full path to the Excel file
data_excel <- read_excel("/content/hrdataset.xlsx", sheet = 1)

# Display the first few rows of the Excel data
cat("\nFirst few rows of the Excel data:\n")
head(data_excel)

# --------------------------------------------------
# Step 3: Importing JSON Data
# --------------------------------------------------
# Load JSON file using 'jsonlite'
if (!require(jsonlite)) install.packages("jsonlite", dependencies = TRUE)
library(jsonlite)

# Provide the full path to the JSON file
data_json <- fromJSON("/content/iris.json")

# Inspect the structure of the JSON data
cat("\nJSON Data Structure:\n")
str(data_json)

# --------------------------------------------------
# Step 4: Displaying Summaries (Optional)
# --------------------------------------------------
cat("\nSummary of CSV Data:\n")
summary(data_csv)

cat("\nSummary of Excel Data:\n")
summary(data_excel)

cat("\nJSON Data Structure:\n")
str(data_json)

"""---
title: "Data Import in R"
author: "Aena"
date: "`r Sys.Date()`"
output: html_document
---

# Objective
To demonstrate how to import and load different types of data into R for analysis. This guide covers importing CSV files, Excel files, and JSON data, with example code and detailed explanations.

```{r data-import, message=FALSE, warning=FALSE}
# --------------------------------------------------
# Step 1: Importing CSV Files
# --------------------------------------------------
# Load CSV data using read.csv()
# - header = TRUE indicates that the first row contains column names.
# - stringsAsFactors = FALSE prevents automatic conversion of character data to factors.

data_csv <- read.csv("/content/Chocolate Sales.csv", header = TRUE, stringsAsFactors = FALSE)
# Display the first few rows of the loaded CSV data
head(data_csv)

# --------------------------------------------------
# Step 2: Importing Excel Files
# --------------------------------------------------
# Install and load the 'readxl' package if not already installed
if (!require(readxl)) install.packages("readxl", dependencies = TRUE)
library(readxl)

# Import Excel data using read_excel()
data_excel <- read_excel("/content/hrdataset.xlsx", sheet = 1)
# Display the first few rows of the loaded Excel data
head(data_excel)

# --------------------------------------------------
# Step 3: Importing JSON Data
# --------------------------------------------------
# Install and load the 'jsonlite' package if not already installed
if (!require(jsonlite)) install.packages("jsonlite", dependencies = TRUE)
library(jsonlite)

# Import JSON data using fromJSON()
data_json <- fromJSON("/content/iris.json")
# Display the structure of the imported JSON data
str(data_json)

"""

# task 3 data cleaning and preprocessing on R

# Load required R libraries (Ensure dplyr is installed first)
install.packages("dplyr")  # Install dplyr if not already available
library(dplyr)

# Step 3: Load the uploaded CSV file
file_path <- "/content/Chocolate Sales.csv"  # This will refer to the uploaded file in Colab
data_csv <- read.csv(file_path)

# 1. Handle Missing Values
# Remove rows with missing values to ensure data cleanliness
data_csv <- na.omit(data_csv)

# Convert 'Amount' to numeric after removing the dollar sign ($) for accurate processing
# gsub() function removes the $ symbol from the data
data_csv$Amount <- as.numeric(gsub("\\$", "", data_csv$Amount))

# 2. Filter and Select Data
# Filter rows where the 'Amount' exceeds 5000 (high-value sales)
filtered_data <- data_csv %>% filter(Amount > 5000)

# Select specific columns: 'Sales Person', 'Amount', and 'Country'
# Helps to focus only on the most relevant columns
selected_data <- data_csv %>% select(Sales.Person, Amount, Country)

# 3. Summarize Data
# Group the data by 'Country' and calculate the average sales amount per country
summary_data <- data_csv %>%
  group_by(Country) %>%
  summarize(mean_amount = mean(Amount, na.rm = TRUE))

# Print the summary (Average sales amount per country)
print(summary_data)

# 4. Transform Variables
# Create a new column 'Total Value' by multiplying 'Amount' with 'Boxes Shipped'
# Convert 'Boxes Shipped' to numeric before the multiplication
data_csv <- data_csv %>% mutate(Boxes.Shipped = as.numeric(Boxes.Shipped))
data_csv <- data_csv %>% mutate(Total.Value = Amount * Boxes.Shipped)

# Display the first few rows of the cleaned and transformed data
print(head(data_csv))

# Install necessary packages if not already installed
install.packages("readr")
install.packages("ggplot2")
install.packages("dplyr")

# Load libraries
library(readr)
library(ggplot2)
library(dplyr)

# Set the file path for your uploaded CSV (adjust this path if needed)
file_path <- "/content/Chocolate Sales.csv"  # Path to the already uploaded CSV

# Read the CSV file into a data frame
data <- read_csv(file_path)

# Display the column names to verify "Date" and "Boxes Shipped" exist
colnames(data)

# Preview the first few rows to check the structure of the dataset
head(data)

# Create Bar Plot for Date vs. Boxes Shipped (adjusting for column names if necessary)
if ("Date" %in% colnames(data) && "Boxes Shipped" %in% colnames(data)) {
  ggplot(data, aes(x = Date, y = `Boxes Shipped`)) +
    geom_bar(stat = "identity", fill = "steelblue") +
    theme_minimal() +
    labs(title = "Boxes Shipped Over Time", x = "Date", y = "Boxes Shipped") +
    theme(axis.text.x = element_text(angle = 45, hjust = 1))
} else {
  cat("Error: 'Date' or 'Boxes Shipped' columns not found in the dataset. Please check the column names.")
}

# Install necessary packages (only if missing)
required_packages <- c("caret", "stats", "ggplot2", "dplyr")

install_if_missing <- function(pkg) {
  if (!requireNamespace(pkg, quietly = TRUE)) {
    install.packages(pkg, dependencies = TRUE)
  }
  library(pkg, character.only = TRUE)
}

lapply(required_packages, install_if_missing)

# Load the iris dataset
data_csv <- iris

# Rename columns for clarity
colnames(data_csv) <- c("Feature1", "Feature2", "Feature3", "Feature4", "Category")

# Convert necessary columns to numeric and factor
data_csv$Feature1 <- as.numeric(data_csv$Feature1)
data_csv$Feature2 <- as.numeric(data_csv$Feature2)
data_csv$Category <- as.factor(data_csv$Category)

# Data Preview
print(head(data_csv))

# 1. Linear Regression Analysis
cat("\n📊 **Linear Regression Analysis**\n")
model <- lm(Feature1 ~ Feature2, data = data_csv)
print(summary(model))

# 2. Clustering Analysis (K-Means)
cat("\n🔍 **Clustering Analysis (K-Means)**\n")
clusters <- kmeans(data_csv[, c("Feature1", "Feature2")], centers = 3)
data_csv$Cluster <- as.factor(clusters$cluster)
print(head(data_csv))

# 3. Machine Learning Model (Caret)
cat("\n🤖 **Machine Learning Model (Caret)**\n")
set.seed(123)  # Ensuring Reproducibility
ml_model <- train(Feature2 ~ Feature1,
                  data = data_csv, method = "rf",
                  trControl = trainControl(method = "cv", number = 5))
print(ml_model)