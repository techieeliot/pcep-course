import os
import dedupe as d
import pandas as pd

customers = pd.read_csv("https://raw.githubusercontent.com/dedupeio/dedupe-examples/refs/heads/main/csv_example/csv_example_messy_input.csv", encoding="utf-8")

deduped_customers = d.Dedupe(customers)

print("Starting deduplication process...")
deduped_customers.sample(10).to_csv("deduped_customers_sample.csv", index=False)
print("Deduplication process completed. Sample saved to 'deduped_customers_sample.csv'.", deduped_customers.sample(10))

